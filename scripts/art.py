"""Draws the README's artwork: the masthead and one title per section.

GitHub shows an SVG as an image, where it cannot load a font, so every letter
here is an outline traced from Archivo (SIL Open Font License), the typeface
fortunexbt.com is set in.

    uv run --with fonttools --with brotli scripts/art.py path/to/archivo.woff2

The font is assets/archivo.woff2 in fortunexbt/fortunexbt-landing.
"""
import sys
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ART = Path(__file__).resolve().parent.parent / "art"
INK = {"light": "#000000", "dark": "#f4f4f2"}
TITLES = {
    "start-here": "Start here",
    "agent-controls": "Agent controls",
    "local-first-tools": "Local-first tools",
    "labs-and-benches": "Labs and benches",
    "data-up-close": "Data up close",
    "games": "Games",
    "measured": "Things I measured",
    "upstream": "Upstream and smaller",
}
# The masthead is Pit Viper's Original in front view, the same drawing as the
# one on fortunexbt.com. PIT and VIPER are the brand's fang lettering, used
# with their permission.
LENS = "M6 50Q600 26 1194 50L1178 360Q1176 378 1160 386L862 528Q836 540 822 514L704 304C690 258 652 234 600 234C548 234 510 258 496 304L378 514Q364 540 338 528L40 386Q24 378 22 360Z"
FRAME = "M0 44Q600 18 1200 44V60Q600 36 0 60ZM432 20Q600 10 768 20Q774 20 774 27V58Q774 64 768 64H432Q426 64 426 58V27Q426 20 432 20ZM0 40 72 36V62L36 66 32 150Q31 161 21 163L6 167ZM1200 40 1194 167 1179 163Q1169 161 1168 150L1164 66 1128 62V36Z"
NOSE = "M486 312C502 250 546 222 600 222C654 222 698 250 714 312L724 346 700 346C694 282 654 250 600 250C546 250 506 282 500 346L476 346Z"
PIT = "M5.3,27.2s.9-15.2,1.6-20.1c1.6-.3,2.4-.4,4-.7-1.4,1.6-2.4,2.4-3.8,4.1,0,.7,0,1-.1,1.7,2.8-2.6,6.1-6.4,8.9-9.1C5.7,3.8,3.9,5.2,3.9,5.2c-1.3,7.9.8,23,.8,23,.2-.3.3-.7.5-1ZM27.6,2.7s-4,0-10.2.5c-.7.7-2.1,2.1-2.8,2.8,2.1-.4,5.2-.6,7.2-.9,0,1.8-.1,3.6-.1,3.6.7.4,1,.6,1.7,1,0,0,0-2.7.1-4.8.8-.1,1.6-.2,2.4-.3.6-.7,1.1-1.2,1.7-1.9ZM17.1,9.7c.1-1.2.3-3.1.3-3.2-.1-.1-1.7.1-1.7.2-.1.1-.4,4-.4,4.1.1,0,1.1-.6,1.8-1.1Z"
VIPER = "M53.5,10.1h0c.2-.2.4-.4.5-.6.2-.2.3-.4.5-.5l.2-.2h-.3c-1.8-.3-2.6-.3-4.4-.5h-.2s0,1.5,0,1.5h.1c1.4.2,1.9.2,3.3.4h0ZM54.6,8h0c0-.3,0-.6,0-.8,0-.2,0-.4,0-.6h0c0,0,0-.1,0-.1-1.8-.2-2.6-.3-4.5-.5h-.1s0,1.5,0,1.5h.1c1.9.2,2.6.3,4.5.5h.1ZM60.4,28.3v-.4c.1-1.2.7-12.1-.8-19.2.2,0,.3,0,.4,0,.1,0,.3,0,.5.1h0s0,0,0,0c0,0-.2-3.5-.2-3.6-.1-.2-.8-.4-1.1-.4,0,0-.9-.2-1.4-.2-4.7-.7-8.1-1.1-8.1-1.1h-.1s0,1.5,0,1.5h.1c3.4.4,6.6.8,9.5,1.2,0,.3,0,.7,0,.9-1.6-.3-2.5-.4-4.1-.6h-.1s0,.1,0,.1c0,.7.1,1.6.1,2.1,0,.6,0,1.1.1,1.8h0c0,0,0,0,0,0,.4.2.7.4,1.1.6h.2c0,.1-.2-3.2-.2-3.2.3,0,.8.2,1,.2,1.2,4.7,1.5,10.7,1.7,14.4.1,2.1.2,3.6.4,4.2l.7,1.2ZM42.9,10.3l-.3-4.7h0c-.2-.1-1.5-.1-1.5,0,0,0,0,.2,0,1.9,0,.5,0,1.1.1,1.6h0c0,0,0,0,0,0,.5.4.8.7,1.4,1.1h.2ZM44.5,10.3l.2-.2c.2-.2.4-.4.6-.6.2-.2.4-.4.6-.6h0s0,0,0,0c0-.4,0-.6,0-.8,0-.2,0-.3,0-.7h.1c1.3,0,1.9.1,3.2.2h.1s-.1-4-.1-4h0c-.8-.1-4-.4-10.9-.5h-.1s.4,3.5.4,3.5c-.6-.5-1.1-1.1-1.7-1.6-.6-.6-1.5-1.5-2.3-2.1h0s0,0,0,0c-.8,0-1.4-.1-2-.1s-.2,0-.3,0h-.3s.3.2.3.2c1.6,1.3,3.7,3.1,5.5,4.7.8.7,1.6,1.4,2.4,2l.2.2-.3-5.1c2.7,0,5.3.2,8,.4v.8c-1.3-.1-2.1-.1-3.5-.2h-.1s.4,4.7.4,4.7Z"
SPATTER = [(389, 36, 4), (58, 151, 1.4), (439, 20, 3.2), (258, 25, 2.6), (84, 26, 2.6), (71, 107, 1.8), (757, 110, 1.4), (693, 78, 1.8), (56, 158, 2.2), (503, 103, 3.2), (370, 150, 1.8), (124, 108, 1.8), (447, 104, 1.4), (677, 116, 2.6), (816, 84, 2.2), (559, 169, 2.2), (360, 147, 4), (936, 24, 2.2), (630, 161, 4), (539, 115, 1.4), (142, 82, 5), (410, 171, 2.6), (47, 125, 5), (670, 146, 5), (376, 130, 3.2), (596, 147, 1.4), (1008, 172, 2.6), (836, 21, 4), (842, 121, 4), (986, 59, 2.6), (1064, 70, 2.6), (427, 115, 2.6), (71, 142, 1.8), (886, 78, 5), (596, 39, 2.6), (659, 162, 5), (517, 105, 4), (498, 72, 2.6), (1149, 36, 1.8), (182, 123, 1.4), (582, 111, 2.2), (338, 35, 3.2), (443, 107, 1.8), (829, 99, 3.2), (786, 137, 2.6), (1079, 144, 5), (817, 106, 2.6), (479, 28, 4), (481, 43, 1.8), (529, 29, 3.2), (63, 10, 1.8), (644, 173, 3.2), (31, 160, 3.2), (451, 119, 2.2), (723, 92, 1.4), (1019, 181, 2.6), (576, 64, 1.8), (123, 69, 2.2), (574, 129, 3.2), (28, 174, 3.2), (434, 129, 1.4), (910, 61, 4), (1036, 130, 2.2), (622, 166, 2.2), (926, 102, 5), (603, 119, 3.2), (974, 179, 5), (234, 51, 2.6), (888, 49, 3.2), (591, 136, 1.4), (948, 91, 1.8), (831, 175, 2.6), (970, 134, 2.2), (1146, 73, 1.8), (123, 91, 2.2), (245, 117, 3.2), (1009, 92, 4), (413, 121, 5), (793, 166, 5), (854, 44, 1.8), (521, 119, 1.4), (961, 177, 2.6), (556, 138, 1.4), (870, 39, 1.8), (33, 112, 2.6), (968, 35, 5), (715, 92, 2.2), (187, 104, 1.4), (17, 177, 4), (123, 139, 1.8), (521, 160, 5), (1049, 15, 1.8), (352, 51, 3.2), (391, 104, 5), (157, 167, 2.2), (1077, 124, 5), (1085, 82, 3.2), (157, 36, 3.2), (22, 86, 1.8), (730, 143, 1.8), (207, 91, 4), (144, 21, 4), (622, 106, 5), (932, 162, 1.4), (298, 58, 5), (117, 88, 1.4), (912, 167, 2.6), (391, 177, 3.2), (615, 129, 2.6), (610, 149, 3.2), (1130, 130, 2.2), (1107, 164, 1.8), (1008, 34, 1.4), (471, 64, 4), (289, 23, 4), (363, 31, 5), (185, 133, 4), (439, 54, 1.8), (1161, 48, 1.4), (478, 94, 4), (999, 38, 2.6), (1193, 79, 2.6), (235, 65, 4), (439, 68, 2.6), (529, 13, 2.2), (621, 61, 1.4), (135, 168, 1.8), (1166, 28, 2.2), (326, 166, 1.8), (325, 32, 2.6), (1020, 126, 2.2), (487, 102, 3.2), (685, 130, 1.4), (335, 148, 1.8), (510, 22, 1.4), (761, 148, 1.4), (730, 48, 2.2), (1035, 88, 2.2), (1193, 82, 2.2), (746, 17, 4), (286, 29, 1.8), (314, 41, 2.2), (754, 101, 1.8), (348, 96, 1.8), (325, 148, 2.2), (44, 13, 3.2), (661, 43, 2.6), (295, 87, 4), (983, 84, 2.6), (655, 163, 3.2)]


class Face:
    def __init__(self, source, weight, width):
        font = instantiateVariableFont(TTFont(source), {"wght": weight, "wdth": width})
        self.glyphs = font.getGlyphSet()
        self.cmap = font.getBestCmap()
        self.advance = {name: adv for name, (adv, _) in font["hmtx"].metrics.items()}
        self.upm = font["head"].unitsPerEm

    def width(self, text, size, tracking=0.0):
        return sum(self.advance[self.cmap[ord(c)]] for c in text) * size / self.upm + tracking * size * len(text)

    def path(self, text, size, x, baseline, tracking=0.0, anchor="start"):
        if anchor == "middle":
            x -= self.width(text, size, tracking) / 2
        scale = size / self.upm
        pen = SVGPathPen(self.glyphs, ntos=lambda v: f"{v:.1f}".rstrip("0").rstrip("."))
        for char in text:
            name = self.cmap[ord(char)]
            self.glyphs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, x, baseline)))
            x += self.advance[name] * scale + tracking * size
        return pen.getCommands()


PLACE = "translate(108 42) rotate(-4 492 220) scale(.82)"
# The letters seen through the lens: tinted dark on a light page, warm on a dark one.
THROUGH = {"#000000": ("#2a0a02", ".8"), "#f4f4f2": ("#fff1c7", ".9")}
NOSE_FILL = {"#000000": "#1c1c1e", "#f4f4f2": "#3a3a3e"}


def masthead(display, ink):
    colours = ("#000", "#000", "#fff", "#000", "#ff4fa3")
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{colours[i % 5] if i % 3 != 2 else "#fff"}"/>' for i, (x, y, r) in enumerate(SPATTER))
    word = display.path("fortunexbt", 352, 600, 520, tracking=-0.012, anchor="middle")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 36 1200 504" role="img" aria-label="fortunexbt">
<defs>
<linearGradient id="g" x1="0" y1=".42" x2="1" y2=".58"><stop offset="0" stop-color="#d9e83c"/><stop offset=".1" stop-color="#ffd21f"/><stop offset=".3" stop-color="#ff8414"/><stop offset=".5" stop-color="#e4201f"/><stop offset=".7" stop-color="#ff8414"/><stop offset=".9" stop-color="#ffd21f"/><stop offset="1" stop-color="#d9e83c"/></linearGradient>
<clipPath id="c"><path d="{LENS}"/></clipPath>
<clipPath id="p"><path transform="{PLACE}" d="{LENS}"/></clipPath>
<clipPath id="f"><path d="{FRAME}"/></clipPath>
</defs>
<path d="{word}" fill="{ink}"/>
<g transform="{PLACE}">
<g clip-path="url(#c)">
<rect width="1200" height="548" fill="url(#g)"/>
<g fill="#fff"><path d="M-420 548-150 0H-30L-300 548Z" opacity=".3"/><path d="M-250 548 20 0H48L-222 548Z" opacity=".2"/>
<animateTransform attributeName="transform" type="translate" values="0 0;1750 0;1750 0" keyTimes="0;.22;1" dur="9s" begin="1s" repeatCount="indefinite" calcMode="spline" keySplines=".4 0 .2 1;0 0 1 1"/></g>
<g fill="#fff"><path transform="translate(8 46) scale(8.2)" d="{PIT}"/><path transform="translate(694.6 46) scale(8.2)" d="{VIPER}"/></g>
</g>
<path d="{NOSE}" fill="{NOSE_FILL[ink]}"/>
<path d="{FRAME}" fill="#3dd6c0"/>
<g clip-path="url(#f)">{dots}</g>
</g>
<path d="{word}" fill="{THROUGH[ink][0]}" opacity="{THROUGH[ink][1]}" clip-path="url(#p)"/>
</svg>
"""


def title(display, text, ink):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 156" role="img" aria-label="{text}">
<rect y="20" width="1200" height="4" fill="{ink}"/>
<path d="{display.path(text, 112, 0, 122, tracking=-0.012)}" fill="{ink}"/>
</svg>
"""


def main(source):
    display = Face(source, 750, 62)
    ART.mkdir(exist_ok=True)
    for scheme, ink in INK.items():
        (ART / f"masthead-{scheme}.svg").write_text(masthead(display, ink))
        for slug, text in TITLES.items():
            (ART / f"{slug}-{scheme}.svg").write_text(title(display, text, ink))


if __name__ == "__main__":
    main(sys.argv[1])
