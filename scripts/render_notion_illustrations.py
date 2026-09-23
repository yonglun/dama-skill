"""Create original, Notion-inspired line illustrations for the offline site.

The 17 small scenes share a hand-drawn stroke vocabulary, but each depicts a
different data-management task. No external assets or font downloads are used.
"""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "dist" / "assets"
SKILLS = ASSETS / "skills"
INK = "#171717"
BLUE = "#cbdcfb"
PINK = "#f8d7dc"
YELLOW = "#fbe7a7"
MINT = "#ccece1"
LAVENDER = "#e2d9f7"
PAPER = "#fffefc"


def path(d: str, fill: str = "none", width: float = 3, stroke: str = INK) -> str:
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"/>'


def rect(x: int, y: int, width: int, height: int, fill: str = "white", radius: int = 5) -> str:
    return f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" fill="{fill}"/>'


def circle(x: int, y: int, radius: int, fill: str = "white", width: float = 3) -> str:
    return f'<circle cx="{x}" cy="{y}" r="{radius}" fill="{fill}" stroke-width="{width}"/>'


def ellipse(x: int, y: int, rx: int, ry: int, fill: str = "white") -> str:
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill}"/>'


def check(x: int, y: int, size: int = 18) -> str:
    return path(f"M{x} {y + size // 2} l{size // 3} {size // 3} l{size} -{size}", width=3.3)


def person(x: int, y: int, shirt: str = BLUE, pose: str = "point", scale: float = 1) -> str:
    """A small expressive figure; x/y locate the head, not a shared template box."""
    arms = {
        "point": path("M16 39 Q36 31 54 15 M-14 41 Q-28 55 -18 78"),
        "work": path("M15 42 Q36 58 56 50 M-15 43 Q-31 58 -11 68"),
        "carry": path("M16 40 Q30 58 14 69 M-14 42 Q-28 54 -18 72"),
        "wave": path("M15 38 Q33 12 35 -12 M-14 42 Q-30 57 -18 74"),
        "open": path("M15 41 Q44 46 67 31 M-15 42 Q-32 51 -26 69"),
    }[pose]
    legs = (
        path("M-8 92 Q-18 114 -23 144 M9 92 Q20 113 28 142")
        if pose != "open" else
        path("M-8 92 Q-31 117 -27 142 M9 92 Q29 113 41 136")
    )
    return (
        f'<g transform="translate({x} {y}) scale({scale})">'
        + circle(0, 0, 18, "white")
        + path("M-18 -4 Q-15 -22 0 -21 Q15 -21 18 -6 M-18 -4 Q-8 -11 0 -12", width=3.2)
        + circle(-6, 1, 1.3, INK, 0) + circle(7, 1, 1.3, INK, 0)
        + path("M-3 10 Q1 13 6 10", width=1.7)
        + path("M-17 35 Q-11 23 0 25 Q13 24 17 37 L12 92 Q-1 98 -14 91 Z", shirt)
        + arms + legs
        + path("M-32 145 q10 4 19 0 M19 144 q10 5 20 -1", width=3.4)
        + "</g>"
    )


def page(body: str, background: str = PAPER) -> str:
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 300" '
        'width="480" height="300" stroke="#171717" stroke-width="3" '
        'stroke-linecap="round" stroke-linejoin="round" role="img" aria-hidden="true">'
        + f'<rect width="480" height="300" fill="{background}" stroke="none"/>'
        + body + "</svg>\n"
    )


def scenes() -> dict[str, str]:
    scene: dict[str, str] = {}
    ground = path("M54 262 Q242 267 426 260", width=2)

    scene["managing-data-projects"] = (
        ellipse(310, 213, 124, 48, BLUE) + ground
        + person(103, 103, PINK, "point")
        + path("M166 165 Q220 132 274 157 T385 142", width=2.5)
        + rect(194, 106, 62, 76) + rect(275, 117, 62, 76, YELLOW)
        + rect(356, 88, 62, 76, MINT)
        + check(205, 141, 13) + check(287, 152, 13) + check(368, 122, 13)
        + circle(221, 94, 4, PINK) + circle(307, 104, 4, BLUE)
    )
    scene["assessing-data-management-maturity"] = (
        ellipse(282, 231, 153, 30, LAVENDER) + ground
        + path("M170 245 H216 V209 H268 V168 H322 V124 H383 V82 H422 V245 Z", BLUE)
        + person(116, 106, YELLOW, "carry")
        + rect(94, 153, 52, 56) + path("M107 170 h23 M107 181 h23 M107 192 h14", width=2)
        + path("M378 82 v-33 l34 10 -34 11", PINK)
        + circle(327, 114, 6, PINK)
    )
    scene["organizing-data-management"] = (
        ellipse(239, 233, 153, 25, MINT) + ground
        + person(95, 113, BLUE, "point", .82)
        + person(386, 112, PINK, "carry", .82)
        + ellipse(240, 185, 100, 33, YELLOW)
        + path("M210 211 l-18 44 M271 211 l20 44", width=3.4)
        + circle(240, 66, 22, LAVENDER)
        + path("M240 89 v27 M240 116 h-69 v20 M240 116 h70 v20")
        + circle(171, 145, 13, BLUE) + circle(310, 145, 13, PINK)
    )
    scene["leading-data-change"] = (
        ellipse(282, 239, 148, 25, YELLOW) + ground
        + person(113, 99, MINT, "open")
        + path("M232 46 q4 -7 12 0 h106 q8 0 8 8 v169 q0 7 -9 7 H237 q-7 0 -7 -8 Z", BLUE)
        + path("M263 60 v154 h81 V60", width=2)
        + circle(331, 145, 5, YELLOW)
        + path("M370 129 q32 1 39 28 q-7 29 -39 30", width=2.2)
        + check(375, 148, 15)
    )
    scene["handling-data-ethically"] = (
        ellipse(239, 243, 166, 21, PINK) + ground
        + person(91, 122, BLUE, "point", .75)
        + person(399, 122, MINT, "carry", .75)
        + path("M240 77 v145 M149 114 Q239 103 331 114 M174 116 l-23 63 m23 -63 l21 63 M307 116 l-20 63 m20 -63 l23 63", width=3)
        + path("M122 180 Q173 222 223 180 Z", YELLOW)
        + path("M259 180 Q308 222 357 180 Z", LAVENDER)
        + path("M228 79 C211 61 209 47 223 44 q13 -2 17 8 q9 -13 22 -8 q19 15 -22 42 Z", PINK)
    )
    scene["establishing-data-governance"] = (
        ellipse(264, 242, 149, 24, BLUE) + ground
        + person(100, 105, LAVENDER, "point", .8)
        + rect(197, 111, 159, 102, YELLOW, 12)
        + path("M197 139 h159 M217 159 h82 M217 177 h118", width=2.5)
        + circle(322, 82, 28, MINT) + check(308, 82, 12)
        + path("M322 111 v40", width=2)
        + circle(220, 229, 7, PINK) + circle(332, 229, 7, PINK)
    )
    scene["designing-data-architecture"] = (
        ellipse(280, 246, 140, 25, MINT) + ground
        + person(95, 100, YELLOW, "work")
        + rect(194, 176, 68, 63, BLUE) + rect(266, 132, 68, 107, PINK)
        + rect(338, 83, 68, 156, LAVENDER)
        + path("M210 195 h36 M281 153 h37 M354 103 h36 M228 176 v-28 h73 v-16 M301 132 v-27 h70 v-22", width=2.5)
        + path("M180 242 q94 9 247 1", width=2)
    )
    scene["modeling-data"] = (
        ellipse(230, 241, 170, 22, LAVENDER) + ground
        + person(84, 108, MINT, "point", .78)
        + rect(174, 55, 90, 65, YELLOW) + rect(323, 81, 90, 65, BLUE)
        + rect(243, 184, 90, 65, PINK)
        + path("M264 87 Q302 83 323 111 M219 120 Q228 158 273 184 M367 146 Q363 176 333 210", width=2.5)
        + circle(287, 91, 5, MINT) + circle(226, 151, 5, BLUE)
        + path("M189 76 h49 M189 93 h33 M338 101 h49 M258 205 h49", width=2)
    )
    scene["securing-data"] = (
        ellipse(272, 239, 151, 26, PINK) + ground
        + person(95, 100, BLUE, "carry", .9)
        + path("M286 53 l92 32 v65 q0 63 -92 94 q-92 -31 -92 -94 V85 Z", MINT)
        + path("M255 144 v-21 q0 -31 31 -31 q30 0 30 31 v21", width=3.5)
        + rect(244, 143, 84, 63, YELLOW, 8)
        + circle(286, 170, 8, INK, 0)
        + path("M286 178 v12", width=4)
        + path("M393 84 q19 7 23 25", width=2)
    )
    scene["managing-documents-and-content"] = (
        ellipse(273, 239, 158, 25, YELLOW) + ground
        + person(97, 106, PINK, "point", .88)
        + rect(192, 80, 190, 158, BLUE)
        + path("M208 119 h158 M208 168 h158 M208 209 h158", width=2.4)
        + rect(225, 93, 59, 16, "white", 2)
        + rect(225, 139, 59, 16, "white", 2)
        + rect(225, 180, 59, 16, "white", 2)
        + path("M318 146 h24 M318 189 h24", width=2.5)
        + path("M391 76 q21 3 25 22", width=2)
    )
    scene["managing-reference-and-master-data"] = (
        ellipse(240, 246, 167, 21, MINT) + ground
        + person(75, 129, YELLOW, "point", .72)
        + rect(164, 87, 68, 94, BLUE) + rect(248, 87, 68, 94, PINK)
        + path("M198 181 q40 42 78 43 M282 181 q-39 43 -78 43", width=2.5)
        + rect(193, 174, 94, 77, YELLOW, 10)
        + circle(240, 198, 13, "white") + path("M219 235 q2 -22 21 -22 q19 0 21 22", width=2.3)
        + path("M181 110 h33 M265 110 h33", width=2)
        + circle(383, 181, 13, LAVENDER)
    )
    scene["managing-metadata"] = (
        ellipse(260, 238, 160, 23, LAVENDER) + ground
        + person(100, 109, BLUE, "work", .8)
        + rect(190, 65, 164, 153, YELLOW, 10)
        + path("M210 94 h107 M210 114 h85 M211 156 h109 M211 179 h72", width=2.3)
        + path("M349 91 q26 4 29 30 q0 26 -25 32 q-27 -4 -28 -31 q2 -26 24 -31 Z", PINK)
        + path("M371 147 l39 45", width=6)
        + circle(250, 154, 5, BLUE) + circle(282, 178, 5, MINT)
    )
    scene["improving-data-quality"] = (
        ellipse(254, 239, 164, 23, BLUE) + ground
        + person(92, 107, PINK, "work", .85)
        + rect(190, 59, 175, 178, "white", 9)
        + path("M213 101 h128 M213 147 h128 M213 193 h128", width=2)
        + circle(228, 90, 10, YELLOW) + circle(228, 136, 10, YELLOW)
        + circle(228, 182, 10, MINT)
        + check(218, 88, 10) + check(218, 134, 10) + check(218, 180, 10)
        + path("M365 101 l25 -25 M364 196 l27 24", width=2)
    )
    scene["integrating-data"] = (
        ellipse(236, 241, 170, 26, MINT) + ground
        + person(71, 114, BLUE, "point", .7)
        + person(417, 113, PINK, "carry", .7)
        + rect(145, 102, 75, 101, YELLOW, 11)
        + rect(262, 102, 75, 101, LAVENDER, 11)
        + path("M220 139 q28 -26 42 0 M220 167 q26 25 42 0", width=4)
        + path("M169 126 v30 M194 126 v30 M285 153 v28 M310 153 v28", width=3)
        + circle(241, 153, 5, INK, 0)
    )
    scene["operating-data-storage"] = (
        ellipse(252, 245, 170, 21, PINK) + ground
        + person(95, 103, YELLOW, "carry", .88)
        + rect(193, 56, 184, 176, BLUE, 10)
        + path("M208 110 h154 M208 166 h154", width=2.5)
        + "".join(circle(x, y, 6, MINT) for x, y in ((226, 81), (226, 136), (226, 191)))
        + path("M247 82 h98 M247 136 h98 M247 191 h98", width=2.5)
        + path("M336 233 v26 h48", width=2.2)
        + circle(389, 258, 5, YELLOW)
    )
    scene["delivering-data-warehousing-and-bi"] = (
        ellipse(268, 242, 161, 21, YELLOW) + ground
        + person(88, 108, MINT, "point", .8)
        + rect(177, 60, 226, 167, "white", 9)
        + path("M195 194 h186 M212 190 v-51 h28 v51 M259 190 v-81 h28 v81 M306 190 v-38 h28 v38 M353 190 v-104 h28 v104", BLUE)
        + path("M203 122 q47 -29 92 -12 t88 -42", width=3)
        + circle(382, 70, 6, PINK)
    )
    scene["delivering-data-science"] = (
        ellipse(262, 239, 161, 24, LAVENDER) + ground
        + person(94, 104, BLUE, "work", .8)
        + rect(179, 57, 229, 171, "white", 10)
        + path("M206 195 V82 M206 195 H383", width=2.5)
        + "".join(circle(x, y, 6, PINK) for x, y in ((228, 171), (249, 158), (268, 169), (286, 132), (313, 125), (335, 103), (356, 94)))
        + path("M222 178 Q292 142 369 83", width=3.4)
        + path("M396 63 q14 -14 26 0 l-10 26 h-27 Z", YELLOW)
    )
    return scene


def hero() -> str:
    """A transparent, original working-together scene for the hero mesh backdrop."""
    illustration = (
        ellipse(465, 612, 340, 61, "#ffffff")
        + path("M107 609 Q454 628 813 607", width=3.5)
        + person(176, 304, BLUE, "point", 1.48)
        + person(730, 323, PINK, "work", 1.32)
        + rect(328, 215, 292, 300, "white", 18)
        + path("M328 262 h292 M357 291 h122 M356 316 h84", width=3.4)
        + rect(357, 352, 67, 92, MINT, 5)
        + rect(443, 331, 67, 113, YELLOW, 5)
        + rect(529, 302, 67, 142, BLUE, 5)
        + path("M352 468 h247", width=3)
        + path("M399 544 q47 -30 97 -8 t111 -20", width=3)
        + circle(399, 544, 11, PINK) + circle(607, 516, 11, LAVENDER)
        + rect(598, 110, 108, 86, LAVENDER, 12)
        + check(622, 146, 23)
        + rect(233, 126, 101, 90, YELLOW, 12)
        + path("M256 156 h52 M256 176 h35", width=3)
        + path("M335 172 Q388 124 436 172", width=3)
        + path("M704 165 Q765 151 790 213", width=3)
        + circle(776, 227, 8, MINT)
    )
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 680" '
        'width="900" height="680" stroke="#171717" stroke-width="3" '
        'stroke-linecap="round" stroke-linejoin="round" role="img" aria-hidden="true">'
        + illustration + "</svg>\n"
    )


def main() -> None:
    SKILLS.mkdir(parents=True, exist_ok=True)
    for slug, illustration in scenes().items():
        (SKILLS / f"{slug}.svg").write_text(page(illustration), encoding="utf-8")
    (ASSETS / "hero-notion-workflow.svg").write_text(hero(), encoding="utf-8")


if __name__ == "__main__":
    main()
