# DAMA Skill Pack Landing Page Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a polished bilingual, offline-capable entry website in `dist/` that explains, demonstrates, and links to the 17-skill DAMA data-project package.

**Architecture:** A semantic `dist/index.html` contains all 17 bilingual skill cards and page copy, `dist/assets/site.css` provides responsive editorial styling, and `dist/assets/site.js` adds client-side filtering, search, language switching, and expandable examples. A locally stored generated hero illustration and restrained typographic skill marks provide the visual identity; the page has no build step or remote runtime dependencies.

**Tech Stack:** HTML5, CSS, vanilla JavaScript, Python 3 standard-library `unittest` for static-content checks, Codex image generation for original artwork, and browser-based verification.

## Global Constraints

- Deliver the website at `dist/index.html` with local assets under `dist/assets/`.
- The site must open directly from disk and make no network requests.
- Include all 17 skills, each with a bilingual use case, expected output, and example prompt.
- Chinese/English switching must preserve active search and filter state.
- Keep the existing v1.0.0 ZIP and skill-package folder unchanged; link to them with relative paths.
- Do not host or publish the page publicly.
- Use warm off-white, ink-blue, and restrained signal-orange colors with original text-free illustrations.
- Meet semantic HTML, keyboard access, visible focus, contrast, responsive-layout, and reduced-motion requirements.
- Do not add a JavaScript framework, build tool, external fonts, analytics, or other runtime dependency.

---

## File map

- Create `dist/index.html`: page structure, 17 full bilingual skill descriptions/examples, install instructions, release metadata, and accessible controls.
- Create `dist/assets/site.css`: design tokens, hero and editorial layout, responsive skill library, focus states, reduced-motion rules, and illustration framing.
- Create `dist/assets/site.js`: data-preserving language toggle, search, group filter, result status, and per-card prompt expansion.
- Create `dist/assets/hero-data-system.png`: generated text-free hero artwork, stored locally.
- Create `tests/test_landing_page.py`: standard-library checks for exactly 17 unique cards, Chinese and English required content for every skill, local asset/download references, and presence of accessible controls.

## Task 1: Build the semantic landing page and content inventory

**Files:**
- Create: `dist/index.html`
- Create: `tests/test_landing_page.py`

**Interfaces:**
- Produces one `<article class="skill-card" data-skill="<slug>" data-group="<group>">` per skill.
- Each card contains paired Chinese and English `.skill-use`, `.skill-output`, and `.skill-example` blocks marked with `data-lang="zh|en"`.
- Search field id: `skill-search`; group filter buttons use `data-filter="all|orchestration|foundations|delivery"`; language buttons use `data-set-lang="zh|en"`.
- Search/filter JavaScript will use `hidden` on complete `.skill-card` elements and announce the current result count in `#results-status`.

- [x] **Step 1: Write static-content tests first.** Added `tests/test_landing_page.py` with a standard-library HTML parser and assertions for 17 unique slugs, bilingual use/output/examples, the 4/9/4 groups, package links, and controls.
- [x] **Step 2: Run the tests to confirm the empty-page failure.** Ran `python3 -m unittest tests/test_landing_page.py -v`; it failed as expected because `dist/index.html` was absent.
- [x] **Step 3: Create `dist/index.html`.** Added the landmarks, translated headings/labels, three groups, search/filter/language controls, all 17 bilingual skill cards, install/download/validation content, and relative release links. Both languages are present in markup.
- [x] **Step 4: Run the tests again.** The initial three inventory/content/control tests passed.

## Task 2: Implement the responsive editorial design system

**Files:**
- Create: `dist/assets/site.css`
- Modify: `dist/index.html`
- Test: `tests/test_landing_page.py`

**Interfaces:**
- `dist/index.html` loads `assets/site.css` and `assets/site.js` with relative URLs.
- Skill-group classes are `.group-orchestration`, `.group-foundations`, and `.group-delivery`.
- Inline SVG icons use `aria-hidden="true"`; informative hero art uses an image alt string per selected language.

- [x] **Step 1: Add a static asset-reference assertion.** Added local stylesheet, script, and hero-image assertions. The test first failed because stylesheet/script references were not yet present.
- [x] **Step 2: Add the CSS and semantic asset references.** Added the local stylesheet and deferred script, warm paper/ink/orange tokens, editorial hero, skill library, example callouts, release panel, 1024/760/380px responsive rules, focus states, and reduced-motion handling. Each skill has a small typographic mark rather than a hand-drawn pictorial SVG.
- [x] **Step 3: Run the static test.** `python3 -m unittest tests/test_landing_page.py -v` passed after the CSS and local script reference were added.

## Task 3: Generate and integrate original hero artwork

**Files:**
- Create: `dist/assets/hero-data-system.png`
- Modify: `dist/index.html`
- Modify: `dist/assets/site.css`
- Test: `tests/test_landing_page.py`

**Interfaces:**
- The hero image is a local asset with a CSS `object-fit: cover` treatment and no text baked into the image.
- The image includes bilingual alt text in markup and does not carry essential copy.

- [x] **Step 1: Add an image asset assertion.** Added checks for the hero asset, local file, and nonempty alternative text. The artwork was generated first per the visual-asset workflow, then linked and checked.
- [x] **Step 2: Generate the art.** Generated one original 1536×1024 editorial illustration of a connected data ecosystem; saved a project copy at `dist/assets/hero-data-system.png`.
- [x] **Step 3: Integrate and test the asset.** Added localized alt text, desktop containment/mobile crop positioning, and confirmed the image file and local references through the static tests.

## Task 4: Add interactive discovery and language switching

**Files:**
- Create: `dist/assets/site.js`
- Modify: `dist/index.html`
- Modify: `tests/test_landing_page.py`

**Interfaces:**
- Initial exported function: `window.DamaSkillSite` with `setLanguage(language)`, `setGroup(group)`, and `filterSkills()` methods for browser-test access.
- State shape: `{ language: "zh" | "en", group: "all" | "orchestration" | "foundations" | "delivery", query: string }`.
- Search matches both language versions of the skill name, use case, output, and example, regardless of selected display language.

- [x] **Step 1: Write interaction tests.** Added checks for `window.DamaSkillSite`, `setLanguage`, `setGroup`, and `filterSkills`; they failed against the initial non-interactive script stub.
- [x] **Step 2: Implement the interaction state.** `site.js` now switches all `data-lang` copy and accessible labels, searches both languages, filters groups/cards, announces result counts, provides Ctrl/Command+K and Escape shortcuts, and toggles keyboard-operable examples while preserving search/filter state.
- [x] **Step 3: Run static tests.** `python3 -m unittest tests/test_landing_page.py -v` passed all six static tests, and `node --check dist/assets/site.js` passed.

## Task 5: Verify the actual browser experience and local release links

**Files:**
- Modify: `dist/index.html`, `dist/assets/site.css`, or `dist/assets/site.js` only for verified defects.
- Test: `tests/test_landing_page.py`

**Interfaces:**
- Verification uses the existing installed browser through the computer-use/browser testing tools; no site server or public deployment is added.
- Acceptance checks cover desktop and narrow viewport, Chinese and English, one text query, each group filter, a combined search/filter, prompt disclosure, console errors, and relative ZIP/README asset resolution.

- [x] **Step 1: Run all static tests.** `python3 -m unittest tests/test_landing_page.py -v` passed six tests; JavaScript syntax check passed.
- [ ] **Step 2: Open the page locally in a browser.** Blocked: browser-use security policy refused the `file://` URL. Do not try an alternate browser surface or workaround.
- [ ] **Step 3: Test interactions.** Blocked with the local browser preview; the planned search, language, filter, and keyboard flows were not runtime-verified.
- [ ] **Step 4: Check layouts and errors.** Blocked with the local browser preview; no rendered screenshot or browser console inspection was available.
- [x] **Step 5: Report the handoff.** Link the static entry page, note that it is offline-capable and not publicly hosted, and disclose the browser-preview limitation.

---

## Self-review

- The content inventory, three groups, search, filters, bilingual state, download/install area, responsive design, no-network requirement, and public-hosting exclusion each map to Tasks 1–5.
- Test code is limited to Python's standard library. Static content and syntax checks passed; rendered UI behavior still needs human/local browser verification because the local-file URL was blocked by policy.
- All selector names and `window.DamaSkillSite` method names are defined here and remain consistent across tasks.
- The release ZIP and versioned package are read-only inputs; all website deliverables stay under `dist/` and tests under `tests/`.
