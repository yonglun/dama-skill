# Landing-Page Template Links Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Simplify the landing-page release links and give every skill card a language-aware link to its own HTML deliverable pack.

**Architecture:** Keep one anchor per destination, storing English and Chinese URLs in `data-href-en` and `data-href-zh`. Extend the existing `setLanguage` function to synchronize `href` alongside existing bilingual text. Render 17 ordinary anchors directly in the static HTML so destinations remain discoverable.

**Tech Stack:** Static HTML/CSS/vanilla JavaScript, Python `unittest`, local browser preview.

## Global Constraints

- English remains the default language.
- Reuse the existing `dist/site-docs/v1.1.0/skills/<slug>/templates/delivery-pack.{en,zh}.html` pages; they already link to Word and Excel templates.
- Do not change the v1.1.0 archive, checksum, template files, or documentation mirrors. Do not publish automatically.
- Preserve search, filters, disclosures, keyboard operation, and responsive layout.

## File map

- `dist/index.html`: release-area guide anchor and 17 card template anchors.
- `dist/assets/site.js`: language-aware `href` synchronization.
- `dist/assets/site.css`: one small card-action rule following the current visual style.
- `tests/test_landing_page.py`: structural and target-existence assertions.
- `docs/superpowers/specs/2026-09-24-landing-page-template-links-design.md`: approved specification (read-only).

## Task 1: One language-aware release guide

**Files:** Modify `tests/test_landing_page.py`, `dist/index.html`, `dist/assets/site.js`.

**Interfaces:** `setLanguage(language: 'en' | 'zh')` updates each anchor with both `data-href-en` and `data-href-zh`; existing `window.DamaSkillSite` API remains unchanged.

- [ ] **Step 1: Write failing tests.** In `LandingPageParser.__init__`, add `self.release_links: list[dict[str, str | None]] = []`; in `handle_starttag`, when `tag == "a"` and `"release-guide" in classes`, append `values`. Remove the old `VALIDATION.html` assertion. Add this test:

```python
def test_release_area_has_one_language_aware_guide(self) -> None:
    source, page = parse_page()
    self.assertEqual(len(page.release_links), 1)
    link = page.release_links[0]
    self.assertEqual(link["href"], "site-docs/v1.1.0/README.en.html")
    self.assertEqual(link["data-href-en"], "site-docs/v1.1.0/README.en.html")
    self.assertEqual(link["data-href-zh"], "site-docs/v1.1.0/README.html")
    for removed in ("Explore a deliverable template", "View validation summary", "ZIP SHA-256 checksum"):
        self.assertNotIn(removed, source)
    self.assertNotIn("site-docs/v1.1.0/VALIDATION.html", page.links)
    self.assertNotIn("dama-data-project-skills-v1.1.0.zip.sha256", page.links)
    script = (ROOT / "dist/assets/site.js").read_text(encoding="utf-8")
    self.assertIn("a[data-href-zh][data-href-en]", script)
```

- [ ] **Step 2: Run red test.** `python3 -m unittest discover -s tests -p 'test_landing_page.py' -q` should fail on old release links.
- [ ] **Step 3: Implement.** Replace all five anchors inside `.release-links` with:

```html
<a class="release-guide" href="site-docs/v1.1.0/README.en.html" data-href-en="site-docs/v1.1.0/README.en.html" data-href-zh="site-docs/v1.1.0/README.html"><span data-lang="zh" hidden>阅读中文使用指南</span><span data-lang="en">Read the English guide</span><span aria-hidden="true">↗</span></a>
```

Immediately after the existing `document.querySelectorAll('[data-lang]')` loop in `setLanguage`, add:

```js
document.querySelectorAll('a[data-href-zh][data-href-en]').forEach((element) => {
  element.href = element.dataset[language === 'zh' ? 'hrefZh' : 'hrefEn'];
});
```

- [ ] **Step 4: Run green test.** `python3 -m unittest discover -s tests -p 'test_landing_page.py' -q` should pass.
- [ ] **Step 5: Commit.** Stage only the three task files, inspect `git diff --cached --check` and the staged diff, then commit `feat: switch release guide with site language`.

## Task 2: One deliverable-pack link per skill card

**Files:** Modify `tests/test_landing_page.py`, `dist/index.html`, `dist/assets/site.css`.

**Interfaces:** Each card has exactly one `a.skill-template-link` with `data-href-en`, `data-href-zh`, and initial English `href`. The Task 1 language updater supplies runtime switching.

- [ ] **Step 1: Write failing tests.** In `LandingPageParser.handle_starttag`, when `tag == "a"`, `self.current_skill` is set, and `"skill-template-link" in classes`, append `values` to `self.cards[self.current_skill].setdefault("template_links", [])`. Add this test to `LandingPageContentTests`:

```python
def test_every_skill_links_to_its_bilingual_delivery_pack(self) -> None:
    source, page = parse_page()
    self.assertEqual(len(page.cards), 17)
    for slug, card in page.cards.items():
        links = card.get("template_links", [])
        self.assertEqual(len(links), 1, slug)
        link = links[0]
        prefix = f"site-docs/v1.1.0/skills/{slug}/templates/delivery-pack"
        self.assertEqual(link["href"], f"{prefix}.en.html")
        self.assertEqual(link["data-href-en"], f"{prefix}.en.html")
        self.assertEqual(link["data-href-zh"], f"{prefix}.zh.html")
        for language in ("en", "zh"):
            self.assertTrue((ROOT / "dist" / f"{prefix}.{language}.html").is_file())
    self.assertEqual(source.count(">Deliverable template<"), 17)
    self.assertEqual(source.count(">交付物模板<"), 17)
```

- [ ] **Step 2: Run red test.** `python3 -m unittest discover -s tests -p 'test_landing_page.py' -q` should fail because card links are absent.
- [ ] **Step 3: Implement.** In each `article.skill-card`, insert one anchor after its `div.example-panel`. The first card uses:

```html
<a class="skill-template-link" href="site-docs/v1.1.0/skills/managing-data-projects/templates/delivery-pack.en.html" data-href-en="site-docs/v1.1.0/skills/managing-data-projects/templates/delivery-pack.en.html" data-href-zh="site-docs/v1.1.0/skills/managing-data-projects/templates/delivery-pack.zh.html"><span data-lang="zh" hidden>交付物模板</span><span data-lang="en">Deliverable template</span><span aria-hidden="true">↗</span></a>
```

For the remaining cards, use each exact `data-skill` slug in the three URL attributes: `assessing-data-management-maturity`, `organizing-data-management`, `leading-data-change`, `handling-data-ethically`, `establishing-data-governance`, `designing-data-architecture`, `modeling-data`, `securing-data`, `managing-documents-and-content`, `managing-reference-and-master-data`, `managing-metadata`, `improving-data-quality`, `integrating-data`, `operating-data-storage`, `delivering-data-warehousing-and-bi`, `delivering-data-science`.

Add a focused CSS rule next to `.example-panel`:

```css
.skill-template-link { display: flex; justify-content: space-between; gap: 1rem; align-items: center; min-height: 2.7rem; margin-top: .65rem; padding-top: .65rem; border-top: 1px solid var(--hairline); color: var(--ink); font-size: .78rem; font-weight: 500; }
.skill-template-link:hover { text-decoration: underline; text-underline-offset: 3px; }
```

- [ ] **Step 4: Run green tests.** `python3 -m unittest discover -s tests -p 'test_landing_page.py' -q` should pass. Then run all tests with the bundled Python and artifact-tool runtime used by this repository:

```bash
DAMA_NODE=/Users/yonglun/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node DAMA_ARTIFACT_TOOL_MODULE=/Users/yonglun/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs /Users/yonglun/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -m unittest discover -s tests -q
```

Expected: all tests pass.
- [ ] **Step 5: Browser check.** Serve `dist/` locally. At desktop and narrow viewport, verify English default; switching to Chinese updates release guide and sampled cards in all three groups; click links and confirm corresponding pages load; verify search, filter, disclosure, keyboard focus, and no console errors.
- [ ] **Step 6: Commit.** Inspect staged diff and `git diff --cached --check`, then commit `feat: link every skill to its bilingual deliverable pack`.

## Self-review checklist

- [ ] All three requested footer changes map to Task 1; all 17 skill links map to Task 2.
- [ ] No placeholders or divergent interface names remain.
- [ ] No archive, checksum, or generated documentation pages change.
