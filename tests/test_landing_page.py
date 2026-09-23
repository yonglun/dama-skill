from __future__ import annotations

import unittest
from html.parser import HTMLParser
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "dist" / "index.html"

EXPECTED_GROUP_COUNTS = {
    "orchestration": 4,
    "foundations": 9,
    "delivery": 4,
}
REQUIRED_CARD_FIELDS = {"skill-use", "skill-output", "skill-example"}


class LandingPageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.cards: dict[str, dict[str, object]] = {}
        self.groups: dict[str, int] = {name: 0 for name in EXPECTED_GROUP_COUNTS}
        self.ids: set[str] = set()
        self.languages: set[str] = set()
        self.links: set[str] = set()
        self.scripts: list[str] = []
        self.stylesheets: list[str] = []
        self.image_alts: list[str] = []
        self.image_sources: list[str] = []
        self.current_skill: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        classes = set((values.get("class") or "").split())
        element_id = values.get("id")
        if element_id:
            self.ids.add(element_id)

        if tag == "article" and "skill-card" in classes:
            slug = values.get("data-skill")
            group = values.get("data-group")
            if not slug or not group:
                return
            self.current_skill = slug
            self.cards[slug] = {"group": group, "fields": {}}
            if group in self.groups:
                self.groups[group] += 1

        if self.current_skill and classes & REQUIRED_CARD_FIELDS:
            language = values.get("data-lang")
            field = next(iter(classes & REQUIRED_CARD_FIELDS))
            if language:
                card = self.cards[self.current_skill]
                fields = card["fields"]
                assert isinstance(fields, dict)
                fields.setdefault(field, set()).add(language)

        if tag == "button" and values.get("data-set-lang"):
            self.languages.add(values["data-set-lang"] or "")
        if tag == "a" and values.get("href"):
            self.links.add(values["href"] or "")
        if tag == "script" and values.get("src"):
            self.scripts.append(values["src"] or "")
        if tag == "link" and "stylesheet" in (values.get("rel") or "").split():
            self.stylesheets.append(values.get("href") or "")
        if tag == "img":
            self.image_alts.append(values.get("alt") or "")
            if values.get("src"):
                self.image_sources.append(values["src"] or "")
                if self.current_skill and "skill-illustration" in classes:
                    self.cards[self.current_skill]["illustration"] = values["src"]

    def handle_endtag(self, tag: str) -> None:
        if tag == "article" and self.current_skill:
            self.current_skill = None


def parse_page() -> tuple[str, LandingPageParser]:
    source = PAGE.read_text(encoding="utf-8")
    parser = LandingPageParser()
    parser.feed(source)
    parser.close()
    return source, parser


class LandingPageContentTests(unittest.TestCase):
    def test_every_skill_has_bilingual_use_output_and_example(self) -> None:
        _, page = parse_page()

        self.assertEqual(len(page.cards), 17)
        self.assertEqual(page.groups, EXPECTED_GROUP_COUNTS)
        for slug, card in page.cards.items():
            fields = card["fields"]
            self.assertIsInstance(fields, dict, slug)
            for field in REQUIRED_CARD_FIELDS:
                self.assertEqual(fields.get(field), {"zh", "en"}, f"{slug}: {field}")

    def test_page_links_to_release_package_and_bilingual_html_guides(self) -> None:
        _, page = parse_page()
        self.assertIn("dama-data-project-skills-v1.0.0.zip", page.links)
        self.assertIn("site-docs/README.html", page.links)
        self.assertIn("site-docs/README.en.html", page.links)
        self.assertIn("site-docs/VALIDATION.html", page.links)
        self.assertIn("site-docs/skills/managing-data-projects/SKILL.html", page.links)
        self.assertFalse(
            [target for target in page.links if target.split("#", 1)[0].endswith(".md")]
        )
        for target in page.links:
            if target.startswith("#"):
                self.assertIn(target[1:], page.ids, target)
            elif not target.startswith(("mailto:", "http://", "https://")):
                self.assertTrue((ROOT / "dist" / target).exists(), target)

    def test_page_has_discoverable_search_filter_and_language_controls(self) -> None:
        source, page = parse_page()
        self.assertIn("skill-search", page.ids)
        self.assertIn("results-status", page.ids)
        self.assertEqual(page.languages, {"zh", "en"})
        self.assertIn('data-filter="all"', source)
        self.assertIn('data-filter="orchestration"', source)
        self.assertIn('data-filter="foundations"', source)
        self.assertIn('data-filter="delivery"', source)

    def test_referenced_styles_script_and_hero_asset_are_local(self) -> None:
        _, page = parse_page()
        self.assertIn("assets/site.css", page.stylesheets)
        self.assertIn("assets/site.js", page.scripts)
        self.assertIn("assets/hero-notion-workflow.svg", page.image_sources)
        self.assertTrue(all(alt or source.startswith("assets/skills/") for alt, source in zip(page.image_alts, page.image_sources)))
        for source in page.stylesheets + page.scripts + page.image_sources:
            self.assertTrue((ROOT / "dist" / source).is_file(), source)

    def test_every_skill_has_its_own_valid_vector_illustration(self) -> None:
        _, page = parse_page()
        sources = []
        drawings = []
        for slug, card in page.cards.items():
            source = card.get("illustration")
            self.assertEqual(source, f"assets/skills/{slug}.svg")
            asset = ROOT / "dist" / str(source)
            self.assertTrue(asset.is_file(), slug)
            illustration = asset.read_text(encoding="utf-8")
            self.assertIn("<svg", illustration, slug)
            self.assertIn('stroke-linecap="round"', illustration, slug)
            sources.append(source)
            drawings.append(illustration)
        self.assertEqual(len(set(sources)), 17)
        self.assertEqual(len(set(drawings)), 17)

    def test_design_tokens_follow_reference_without_remote_assets(self) -> None:
        stylesheet = (ROOT / "dist" / "assets" / "site.css").read_text(encoding="utf-8")
        self.assertIn("--ink: #171717", stylesheet)
        self.assertIn("--canvas-soft: #fafafa", stylesheet)
        self.assertIn("--gradient-develop-start: #007cf0", stylesheet)
        self.assertIn(".hero::before", stylesheet)
        self.assertIn("border-radius: 100px", stylesheet)

    def test_interaction_controller_exposes_language_filter_and_search_state(self) -> None:
        script = (ROOT / "dist" / "assets" / "site.js").read_text(encoding="utf-8")
        for interface in ("window.DamaSkillSite", "setLanguage", "setGroup", "filterSkills"):
            with self.subTest(interface=interface):
                self.assertIn(interface, script)

    def test_page_uses_no_remote_runtime_assets(self) -> None:
        sources = [
            PAGE.read_text(encoding="utf-8"),
            (ROOT / "dist" / "assets" / "site.css").read_text(encoding="utf-8"),
            (ROOT / "dist" / "assets" / "site.js").read_text(encoding="utf-8"),
        ]
        combined = "\n".join(sources)
        remote_runtime_reference = re.compile(
            r"(?:<script\b[^>]*\bsrc|<link\b[^>]*\bhref)\s*=\s*['\"]https?://"
            r"|@import\b[^;]*https?://|url\(\s*['\"]?https?://"
            r"|fetch\(\s*['\"]https?://",
            re.IGNORECASE,
        )
        self.assertIsNone(remote_runtime_reference.search(combined))


if __name__ == "__main__":
    unittest.main()
