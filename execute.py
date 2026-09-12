#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "nbclient>=0.9",
#     "nbformat>=5.9",
#     "ipykernel>=6.29",
#     "anndata>=0.10",
#     "numpy>=1.26",
#     "scipy>=1.11",
#     "pandas>=2.1",
#     "matplotlib>=3.8",
# ]
#
# [tool.uv]
# exclude-newer = "2026-09-12T00:00:00Z"
# ///
"""Execute the code cells in a post and cache their outputs.

    uv run execute.py                      # every post with code cells
    uv run execute.py ten_min_to_adata     # just one

Outputs land in `posts/_outputs/<slug>.json`, keyed by a hash of each cell's
source, and that file is committed. `build.py` only reads the cache, so the
normal build and CI never execute anything -- which is the point: posts that
touch real data can't run in CI anyway.

Add the packages a post needs to the dependency block above. Editing a cell
changes its hash, so re-run this to refresh it.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).parent
POSTS = ROOT / "posts"
CACHE = POSTS / "_outputs"

# Kept in sync with build.py.
RE_CODE_CELL = re.compile(
    r"^```\{code-cell\}[ \t]*(?P<lang>[\w-]*)\n(?P<opts>(?::[\w-]+:.*\n)*)"
    r"(?P<src>.*?)\n```[ \t]*$",
    re.S | re.M,
)


def cell_key(source: str) -> str:
    return hashlib.sha256(source.encode()).hexdigest()[:16]


def execute(path: Path) -> None:
    slug = path.stem
    sources = [m.group("src") for m in RE_CODE_CELL.finditer(path.read_text())]
    if not sources:
        return

    print(f"{slug}: executing {len(sources)} cells")
    nb = nbformat.v4.new_notebook(
        cells=[nbformat.v4.new_code_cell(s) for s in sources],
        metadata={
            "kernelspec": {
                "name": "python3",
                "language": "python",
                "display_name": "Python 3",
            }
        },
    )

    client = NotebookClient(
        nb,
        timeout=600,
        kernel_name="python3",
        allow_errors=True,
        resources={"metadata": {"path": str(ROOT)}},
    )
    client.execute()

    cache: dict[str, list[dict]] = {}
    failed = 0
    for source, cell in zip(sources, nb.cells):
        outputs = [dict(o) for o in cell.get("outputs", [])]
        if any(o.get("output_type") == "error" for o in outputs):
            failed += 1
            print(f"  ! cell errored: {source.splitlines()[0][:60]}")
        cache[cell_key(source)] = outputs

    CACHE.mkdir(parents=True, exist_ok=True)
    out = CACHE / f"{slug}.json"
    out.write_text(json.dumps(cache, indent=1, sort_keys=True) + "\n")
    print(f"  wrote {out.relative_to(ROOT)}"
          + (f" ({failed} cell(s) errored)" if failed else ""))


if __name__ == "__main__":
    wanted = sys.argv[1:]
    paths = (
        [POSTS / f"{w.removesuffix('.md')}.md" for w in wanted]
        if wanted
        else sorted(POSTS.glob("*.md"))
    )
    for path in paths:
        if not path.exists():
            sys.exit(f"no such post: {path}")
        execute(path)
