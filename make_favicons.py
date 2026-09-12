#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "pillow>=10.2",
#     "fonttools>=4.49",
# ]
#
# [tool.uv]
# exclude-newer = "2026-09-12T00:00:00Z"
# ///
"""Generate the favicon set: a Charter "A" reversed out of the site amber.

    uv run make_favicons.py

Writes into _assets/. Run it again only to change the design -- the output is
committed, so a normal build never needs this script or its dependencies.

The PNGs are rendered with Charter at 16x and downsampled, which is how an
icon pipeline gets clean edges at 16px. The SVG carries the letter as an
outline extracted from the same font, so it does not depend on Charter being
installed wherever the page is viewed.
"""

from __future__ import annotations

import pathlib

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

CREAM = (255, 255, 248)
AMBER = (164, 111, 13)
CREAM_HEX = "#fffff8"
AMBER_HEX = "#a46f0d"

CHARTER = "/System/Library/Fonts/Supplemental/Charter.ttc"
LETTER = "A"
ASSETS = pathlib.Path(__file__).parent / "_assets"

BOX = 32          # design grid
RADIUS = 6 / BOX  # corner radius as a fraction of the box
GLYPH = 0.60      # cap height as a fraction of the box
SUPERSAMPLE = 16


def render(px: int, *, rounded: bool = True) -> Image.Image:
    """The icon at an arbitrary size, supersampled then downsampled."""
    big = px * SUPERSAMPLE
    im = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)

    if rounded:
        d.rounded_rectangle([0, 0, big - 1, big - 1],
                            radius=int(big * RADIUS), fill=AMBER)
    else:
        # Full bleed: iOS applies its own mask to apple-touch-icon, and a
        # rounded source would leave pale corners inside it.
        d.rectangle([0, 0, big - 1, big - 1], fill=AMBER)

    font = ImageFont.truetype(CHARTER, int(big * GLYPH * 1.30))
    box = d.textbbox((0, 0), LETTER, font=font)
    d.text(((big - (box[2] - box[0])) / 2 - box[0],
            (big - (box[3] - box[1])) / 2 - box[1]),
           LETTER, font=font, fill=CREAM)

    return im.resize((px, px), Image.LANCZOS)


def letter_svg_path() -> str:
    """The letter as an SVG path, scaled and centred in the design grid."""
    font = TTFont(CHARTER, fontNumber=0)
    glyph_name = font.getBestCmap()[ord(LETTER)]
    glyph_set = font.getGlyphSet()

    pen = SVGPathPen(glyph_set)
    glyph_set[glyph_name].draw(pen)
    path = pen.getCommands()

    bounds = font["glyf"][glyph_name]
    x_min, y_min = bounds.xMin, bounds.yMin
    x_max, y_max = bounds.xMax, bounds.yMax
    w, h = x_max - x_min, y_max - y_min

    scale = (BOX * GLYPH) / h
    # Font coordinates are y-up, SVG is y-down, hence the negative y scale.
    tx = (BOX - scale * w) / 2 - scale * x_min
    ty = (BOX - scale * h) / 2 + scale * y_max

    return (f'<g transform="translate({tx:.3f} {ty:.3f}) '
            f'scale({scale:.5f} {-scale:.5f})">'
            f'<path d="{path}" fill="{CREAM_HEX}"/></g>')


def main() -> None:
    ASSETS.mkdir(exist_ok=True)

    # Tab and bookmark icons.
    for size in (16, 32):
        render(size).save(ASSETS / f"favicon-{size}x{size}.png")
        print(f"  favicon-{size}x{size}.png")

    # Multi-resolution .ico for browsers that still ask for it.
    render(48).save(ASSETS / "favicon.ico",
                    sizes=[(16, 16), (32, 32), (48, 48)])
    print("  favicon.ico (16/32/48)")

    # iOS home screen: full bleed, no rounding, no alpha.
    apple = Image.new("RGB", (180, 180), AMBER)
    apple.paste(render(180, rounded=False).convert("RGB"), (0, 0))
    apple.save(ASSETS / "apple-touch-icon.png")
    print("  apple-touch-icon.png (180, full bleed)")

    for size in (192, 512):
        render(size).save(ASSETS / f"android-chrome-{size}x{size}.png")
        print(f"  android-chrome-{size}x{size}.png")

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {BOX} {BOX}">'
        f'<rect width="{BOX}" height="{BOX}" rx="{BOX * RADIUS:.0f}" '
        f'fill="{AMBER_HEX}"/>'
        f"{letter_svg_path()}"
        f"</svg>\n"
    )
    (ASSETS / "favicon.svg").write_text(svg)
    print(f"  favicon.svg ({len(svg)} bytes, letter as an outline)")


if __name__ == "__main__":
    main()
