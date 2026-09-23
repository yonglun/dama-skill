from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import unittest


ROOT = Path(__file__).resolve().parents[1]
PACKAGE_ROOT = ROOT / "dist" / "dama-data-project-skills-v1.0.0"
DOCS_ROOT = ROOT / "dist" / "site-docs"
LANDING_PAGE = ROOT / "dist" / "index.html"


class PageInspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[tuple[str, set[str]]] = []
        self.stylesheets: list[str] = []
        self.ids: set[str] = set()
        self.tags: set[str] = set()
        self.title_parts: list[str] = []
        self.in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        self.tags.add(tag)
        if values.get("id"):
            self.ids.add(values["id"] or "")
        if tag == "a" and values.get("href"):
            self.links.append((values["href"] or "", set((values.get("class") or "").split())))
        if tag == "link" and "stylesheet" in (values.get("rel") or "").split():
            self.stylesheets.append(values.get("href") or "")
        if tag == "title":
            self.in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)


def inspect(path: Path) -> tuple[str, PageInspector]:
    source = path.read_text(encoding="utf-8")
    page = PageInspector()
    page.feed(source)
    page.close()
    return source, page


class DocumentationMirrorTests(unittest.TestCase):
    def test_every_packaged_markdown_file_has_a_mirrored_html_page(self) -> None:
        sources = sorted(PACKAGE_ROOT.rglob("*.md"))
        self.assertEqual(len(sources), 40)
        self.assertTrue(DOCS_ROOT.is_dir(), "run scripts/render_site_docs.py")
        pages = sorted(DOCS_ROOT.rglob("*.html"))
        self.assertEqual(len(pages), len(sources))

        expected = {
            source.relative_to(PACKAGE_ROOT).with_suffix(".html")
            for source in sources
        }
        actual = {page.relative_to(DOCS_ROOT) for page in pages}
        self.assertEqual(actual, expected)

    def test_each_document_has_shared_styles_home_and_raw_source_links(self) -> None:
        for source in sorted(PACKAGE_ROOT.rglob("*.md")):
            relative = source.relative_to(PACKAGE_ROOT)
            page_path = DOCS_ROOT / relative.with_suffix(".html")
            with self.subTest(page=relative.as_posix()):
                self.assertTrue(page_path.is_file(), f"missing {page_path}")
                _, page = inspect(page_path)
                targets = [(href, classes) for href, classes in page.links]
                self.assertTrue(any("docs-home" in classes for _, classes in targets))
                raw_links = [href for href, classes in targets if "source-markdown" in classes]
                self.assertEqual(len(raw_links), 1)
                raw_path = (page_path.parent / unquote(urlsplit(raw_links[0]).path)).resolve()
                self.assertEqual(raw_path, source.resolve())
                self.assertEqual(len(page.stylesheets), 1)
                stylesheet = (page_path.parent / page.stylesheets[0]).resolve()
                self.assertEqual(stylesheet, (ROOT / "dist/assets/site.css").resolve())

    def test_generated_markdown_links_point_to_existing_html_mirrors(self) -> None:
        for page_path in sorted(DOCS_ROOT.rglob("*.html")):
            source, page = inspect(page_path)
            with self.subTest(page=page_path.relative_to(DOCS_ROOT).as_posix()):
                for href, classes in page.links:
                    parsed = urlsplit(href)
                    if parsed.scheme or parsed.netloc or not parsed.path:
                        continue
                    if "source-markdown" in classes:
                        self.assertTrue(parsed.path.endswith(".md"), href)
                        continue
                    self.assertFalse(parsed.path.endswith(".md"), href)
                    target = (page_path.parent / unquote(parsed.path)).resolve()
                    self.assertTrue(target.is_file(), f"{href} from {page_path}")
                    if parsed.fragment and target.suffix == ".html":
                        _, target_page = inspect(target)
                        self.assertIn(unquote(parsed.fragment), target_page.ids, href)

    def test_markdown_structures_are_rendered_and_yaml_frontmatter_is_hidden(self) -> None:
        routing_page = DOCS_ROOT / "skills/managing-data-projects/references/routing-table.html"
        _, routing = inspect(routing_page)
        self.assertIn("table", routing.tags)
        self.assertIn("h2", routing.tags)

        playbook_page = DOCS_ROOT / "skills/assessing-data-management-maturity/references/playbook.html"
        _, playbook = inspect(playbook_page)
        self.assertIn("pre", playbook.tags)
        self.assertIn("table", playbook.tags)

        skill_page = DOCS_ROOT / "skills/managing-data-projects/SKILL.html"
        skill_source, skill = inspect(skill_page)
        self.assertIn("h1", skill.tags)
        self.assertIn("managing-data-projects", skill_source)
        self.assertNotIn("<hr", skill_source)
        self.assertNotIn(">name:", skill_source)

    def test_landing_page_links_to_styled_document_mirrors(self) -> None:
        _, page = inspect(LANDING_PAGE)
        hrefs = {href for href, _ in page.links}
        expected = {
            "site-docs/README.html",
            "site-docs/README.en.html",
            "site-docs/VALIDATION.html",
            "site-docs/skills/managing-data-projects/SKILL.html",
        }
        self.assertTrue(expected.issubset(hrefs), expected - hrefs)
        for href in expected:
            self.assertTrue((ROOT / "dist" / href).is_file(), href)

    def test_shared_stylesheet_covers_document_layout_and_narrow_tables(self) -> None:
        stylesheet = (ROOT / "dist/assets/site.css").read_text(encoding="utf-8")
        for selector in (".docs-header", ".docs-main", ".docs-content", ".markdown-body table"):
            with self.subTest(selector=selector):
                self.assertIn(selector, stylesheet)
        self.assertRegex(stylesheet, r"\.markdown-body table[^{}]*\{[^}]*overflow-x:\s*auto")
        self.assertIn("@media (max-width: 760px)", stylesheet)


if __name__ == "__main__":
    unittest.main()
