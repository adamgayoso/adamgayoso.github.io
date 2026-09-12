#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "jinja2>=3.1",
#     "markdown-it-py[linkify]>=3.0",
#     "mdit-py-plugins>=0.4",
#     "beautifulsoup4>=4.12",
#     "pygments>=2.17",
#     "pyyaml>=6.0",
# ]
#
# [tool.uv]
# exclude-newer = "2026-09-12T00:00:00Z"
# ///
"""Build adamgayoso.com.

    uv run build.py            # build into _build/
    uv run build.py --serve    # build, then serve on :8000
    uv run build.py --execute  # re-run notebook code cells and refresh the cache

Content lives in `index.md` and `posts/*.md`. Posts with `{code-cell}` blocks
(jupytext md:myst) have their outputs read from `posts/_outputs/<slug>.json`,
which is committed, so a normal build -- and CI -- never executes anything.
Pass --execute to regenerate that cache; see execute.py for the dependencies
that needs.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

import yaml
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markdown_it import MarkdownIt
from mdit_py_plugins.deflist import deflist_plugin
from mdit_py_plugins.dollarmath import dollarmath_plugin
from mdit_py_plugins.footnote import footnote_plugin
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name

ROOT = Path(__file__).parent
BUILD = ROOT / "_build"
POSTS = ROOT / "posts"
CACHE = POSTS / "_outputs"
BASE_URL = "https://adamgayoso.com"

# Directories copied verbatim into the build. `_assets` holds the favicons that
# site.webmanifest points at, so the paths have to stay put.
STATIC_TREES = ["_assets", "_static", "static"]


# --------------------------------------------------------------------------- #
# markdown
# --------------------------------------------------------------------------- #


def make_markdown() -> MarkdownIt:
    md = (
        MarkdownIt("commonmark", {"html": True, "linkify": True, "typographer": True})
        .enable(["table", "strikethrough", "linkify", "smartquotes", "replacements"])
        .use(dollarmath_plugin, double_inline=True)
        .use(footnote_plugin)
        .use(deflist_plugin)
    )

    # Hand math to KaTeX as \( \) / \[ \] rather than rendering it here.
    md.add_render_rule(
        "math_inline",
        lambda self, tokens, i, opts, env: f"\\({tokens[i].content}\\)",
    )
    md.add_render_rule(
        "math_inline_double",
        lambda self, tokens, i, opts, env: f"\\[{tokens[i].content}\\]",
    )
    md.add_render_rule(
        "math_block",
        lambda self, tokens, i, opts, env: (
            f'<div class="math-block">\\[{tokens[i].content}\\]</div>'
        ),
    )

    # Figures: ![alt](src "fullwidth") and ![alt](src "marginnote") opt into the
    # two Tufte figure widths. Any other title is kept as a caption.
    def image(self, tokens, i, opts, env):
        tok = tokens[i]
        src = tok.attrGet("src") or ""
        alt = tok.content or ""
        title = tok.attrGet("title") or ""
        cls = {"fullwidth": "fullwidth", "marginnote": "margin-figure"}.get(title, "")
        caption = "" if title in ("fullwidth", "marginnote", "") else title
        inner = f'<img src="{src}" alt="{alt}" loading="lazy">'
        if caption:
            inner += f"<figcaption>{caption}</figcaption>"
        return f'<figure class="{cls}">{inner}</figure>'

    md.add_render_rule("image", image)

    # External links open in place but are marked so CSS can flag them.
    def link_open(self, tokens, i, opts, env):
        tok = tokens[i]
        href = tok.attrGet("href") or ""
        if href.startswith(("http://", "https://")) and BASE_URL not in href:
            tok.attrSet("class", "external")
        return self.renderToken(tokens, i, opts, env)

    md.add_render_rule("link_open", link_open)
    return md


MD = make_markdown()

# MyST directives left over from the Sphinx build, rewritten before parsing.
RE_ARTICLE_INFO = re.compile(r"^```\{article-info\}\n.*?\n```\n", re.S | re.M)
RE_ADMONITION = re.compile(
    r"^```\{admonition\}[ \t]*(?P<title>.*?)\n(?P<body>.*?)\n```[ \t]*$",
    re.S | re.M,
)


def strip_myst_directives(text: str) -> str:
    """Drop `{article-info}` (the date comes from front matter now) and turn
    `{admonition}` into an <aside>."""
    text = RE_ARTICLE_INFO.sub("", text)

    def admonition(m: re.Match) -> str:
        title = m.group("title").strip()
        body = MD.render(dedent_block(m.group("body")))
        head = f"<p class='aside-title'>{title}</p>" if title else ""
        return f'<aside class="note">{head}{body}</aside>'

    return RE_ADMONITION.sub(admonition, text)


def dedent_block(text: str) -> str:
    lines = [ln for ln in text.splitlines()]
    indents = [len(ln) - len(ln.lstrip()) for ln in lines if ln.strip()]
    cut = min(indents) if indents else 0
    return "\n".join(ln[cut:] if len(ln) >= cut else ln for ln in lines)


def footnotes_to_sidenotes(html: str) -> str:
    """Move markdown footnotes into Tufte sidenotes.

    Write ordinary `[^1]` footnotes; they land in the right margin, numbered,
    and collapse to a click-to-expand note on narrow screens. Pure CSS, no JS.
    """
    soup = BeautifulSoup(html, "html.parser")
    section = soup.find("section", class_="footnotes")
    if section is None:
        return html

    for sep in soup.find_all("hr", class_="footnotes-sep"):
        sep.decompose()

    bodies: dict[str, str] = {}
    for li in section.find_all("li", class_="footnote-item"):
        fid = li.get("id", "")
        for back in li.find_all("a", class_="footnote-backref"):
            back.decompose()
        inner = "".join(str(c) for c in li.children).strip()
        # Unwrap the single <p> markdown-it wraps each footnote body in.
        frag = BeautifulSoup(inner, "html.parser")
        if len(frag.find_all("p", recursive=False)) == 1:
            p = frag.find("p")
            inner = "".join(str(c) for c in p.children).strip()
        bodies[fid] = inner

    for n, ref in enumerate(soup.find_all("sup", class_="footnote-ref"), start=1):
        link = ref.find("a")
        target = (link.get("href", "") if link else "").lstrip("#")
        body = bodies.get(target)
        if body is None:
            continue
        sid = f"sn-{target}"
        ref.replace_with(
            BeautifulSoup(
                f'<label for="{sid}" class="margin-toggle sidenote-number"></label>'
                f'<input type="checkbox" id="{sid}" class="margin-toggle">'
                f'<span class="sidenote">{body}</span>',
                "html.parser",
            )
        )

    section.decompose()
    return str(soup)


def render_markdown(text: str) -> str:
    return footnotes_to_sidenotes(MD.render(strip_myst_directives(text)))


# --------------------------------------------------------------------------- #
# code cells
# --------------------------------------------------------------------------- #

RE_CODE_CELL = re.compile(
    r"^```\{code-cell\}[ \t]*(?P<lang>[\w-]*)\n(?P<opts>(?::[\w-]+:.*\n)*)"
    r"(?P<src>.*?)\n```[ \t]*$",
    re.S | re.M,
)


@dataclass
class Cell:
    kind: str  # "markdown" | "code"
    source: str


def split_cells(text: str) -> list[Cell]:
    """Split jupytext md:myst source into markdown and code cells."""
    cells: list[Cell] = []
    pos = 0
    for m in RE_CODE_CELL.finditer(text):
        if before := text[pos : m.start()].strip("\n"):
            cells.append(Cell("markdown", before))
        cells.append(Cell("code", m.group("src")))
        pos = m.end()
    if tail := text[pos:].strip("\n"):
        cells.append(Cell("markdown", tail))
    return cells


def render_code(source: str) -> str:
    lexer = get_lexer_by_name("python")
    formatter = HtmlFormatter(nowrap=False, cssclass="highlight")
    return highlight(source, lexer, formatter)


def render_outputs(outputs: list[dict]) -> str:
    """Render cached nbformat outputs. Richest representation wins."""
    parts: list[str] = []
    for out in outputs:
        data = out.get("data", {})
        if "image/png" in data:
            parts.append(
                f'<img class="cell-image" alt="" '
                f'src="data:image/png;base64,{data["image/png"]}">'
            )
        elif "text/html" in data:
            parts.append(f'<div class="cell-html">{join(data["text/html"])}</div>')
        elif "text/plain" in data:
            parts.append(f"<pre class='cell-text'>{esc(join(data['text/plain']))}</pre>")
        elif out.get("output_type") == "stream":
            cls = "cell-stderr" if out.get("name") == "stderr" else "cell-text"
            parts.append(f"<pre class='{cls}'>{esc(join(out.get('text', '')))}</pre>")
        elif out.get("output_type") == "error":
            tb = esc(strip_ansi("\n".join(out.get("traceback", []))))
            parts.append(f"<pre class='cell-stderr'>{tb}</pre>")
    return "".join(parts)


def join(v) -> str:
    return "".join(v) if isinstance(v, list) else str(v)


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def strip_ansi(s: str) -> str:
    return re.sub(r"\x1b\[[0-9;]*m", "", s)


def cell_key(source: str) -> str:
    return hashlib.sha256(source.encode()).hexdigest()[:16]


def render_notebook_post(text: str, slug: str) -> tuple[str, bool]:
    """Render a post containing code cells. Returns (html, outputs_missing)."""
    cache_path = CACHE / f"{slug}.json"
    cached: dict[str, list[dict]] = {}
    if cache_path.exists():
        cached = json.loads(cache_path.read_text())

    missing = False
    parts: list[str] = []
    for cell in split_cells(text):
        if cell.kind == "markdown":
            parts.append(render_markdown(cell.source))
            continue
        key = cell_key(cell.source)
        outputs = cached.get(key)
        if outputs is None:
            missing = True
        block = f'<div class="cell"><div class="cell-input">{render_code(cell.source)}</div>'
        if outputs:
            block += f'<div class="cell-output">{render_outputs(outputs)}</div>'
        parts.append(block + "</div>")
    return "".join(parts), missing


# --------------------------------------------------------------------------- #
# content
# --------------------------------------------------------------------------- #

RE_FRONT_MATTER = re.compile(r"^---\n(.*?)\n---\n", re.S)


@dataclass
class Page:
    slug: str
    url: str
    meta: dict = field(default_factory=dict)
    body: str = ""

    @property
    def title(self) -> str:
        return self.meta.get("title", self.slug)

    @property
    def date(self) -> date | None:
        d = self.meta.get("date")
        return d if isinstance(d, date) else None

    @property
    def date_display(self) -> str:
        return self.date.strftime("%B %-d, %Y") if self.date else ""


def load(path: Path) -> tuple[dict, str]:
    raw = path.read_text()
    if m := RE_FRONT_MATTER.match(raw):
        meta = yaml.safe_load(m.group(1)) or {}
        return meta, raw[m.end() :]
    return {}, raw


def load_posts() -> list[Page]:
    pages: list[Page] = []
    for path in sorted(POSTS.glob("*.md")):
        meta, text = load(path)
        if meta.get("draft"):
            continue
        slug = path.stem
        page = Page(slug=slug, url=f"/posts/{slug}/", meta=meta)
        if RE_CODE_CELL.search(text):
            page.body, missing = render_notebook_post(text, slug)
            if missing:
                print(f"  ! {slug}: some cell outputs are not cached "
                      f"(run: uv run execute.py {slug})")
        else:
            page.body = render_markdown(text)
        pages.append(page)
    return sorted(pages, key=lambda p: p.date or date.min, reverse=True)


# --------------------------------------------------------------------------- #
# build
# --------------------------------------------------------------------------- #


def write(url: str, html: str) -> None:
    """Write to a directory URL, matching the old dirhtml output."""
    out = BUILD / url.strip("/") / "index.html" if url != "/" else BUILD / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print(f"  {url:34s} -> {out.relative_to(ROOT)}")


def build() -> None:
    if BUILD.exists():
        shutil.rmtree(BUILD)
    BUILD.mkdir(parents=True)

    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.globals["base_url"] = BASE_URL

    posts = load_posts()
    print(f"building {len(posts) + 2} pages")

    home_meta, home_text = load(ROOT / "index.md")
    write(
        "/",
        env.get_template("home.html").render(
            meta=home_meta, body=render_markdown(home_text), posts=posts
        ),
    )

    write("/blog/", env.get_template("blog.html").render(posts=posts))

    post_tpl = env.get_template("post.html")
    for post in posts:
        write(post.url, post_tpl.render(page=post))

    # Pygments stylesheets, generated so they always match the installed
    # version. Two themes, because one set of token colours can't carry both
    # the cream and the dark background.
    css_dir = BUILD / "static" / "css"
    css_dir.mkdir(parents=True, exist_ok=True)
    light = HtmlFormatter(style="friendly", cssclass="highlight").get_style_defs(
        ".highlight"
    )
    dark = HtmlFormatter(style="gruvbox-dark", cssclass="highlight").get_style_defs(
        ".highlight"
    )
    (css_dir / "pygments.css").write_text(
        f"{light}\n\n@media (prefers-color-scheme: dark) {{\n{dark}\n}}\n"
    )

    for tree in STATIC_TREES:
        src = ROOT / tree
        if src.is_dir():
            shutil.copytree(src, BUILD / tree, dirs_exist_ok=True)

    for extra in ("CNAME", "robots.txt"):
        if (ROOT / extra).exists():
            shutil.copy(ROOT / extra, BUILD / extra)

    # Browsers ask for /favicon.ico regardless of the <link> tags.
    if (ROOT / "_assets" / "favicon.ico").exists():
        shutil.copy(ROOT / "_assets" / "favicon.ico", BUILD / "favicon.ico")

    print(f"done -> {BUILD.relative_to(ROOT)}")


def serve(port: int = 8000) -> None:
    import functools
    from http.server import HTTPServer, SimpleHTTPRequestHandler

    handler = functools.partial(SimpleHTTPRequestHandler, directory=str(BUILD))
    print(f"serving {BUILD.relative_to(ROOT)} at http://localhost:{port}")
    HTTPServer(("", port), handler).serve_forever()


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--serve", action="store_true", help="serve after building")
    ap.add_argument("--port", type=int, default=8000)
    args = ap.parse_args()

    build()
    if args.serve:
        serve(args.port)
