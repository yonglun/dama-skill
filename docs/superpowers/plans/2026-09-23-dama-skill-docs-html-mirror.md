# DAMA Skill Documentation HTML Mirror Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate consistent, offline HTML pages for all 40 Markdown documents in the v1.0.0 skill package.

**Architecture:** A build-time Python script calls Pandoc to render package Markdown into a mirrored `dist/site-docs/` tree. It rewrites local Markdown links to HTML mirrors and wraps each fragment in a common semantic page shell using the landing page's stylesheet. The source Markdown and ZIP remain untouched.

**Tech Stack:** Python 3 standard library, installed Pandoc, HTML5, existing CSS, Python `unittest`.

## Global Constraints

- Keep the original `dist/dama-data-project-skills-v1.0.0/` files and versioned ZIP unchanged.
- Write generated pages only under `dist/site-docs/` and update the landing page's four Markdown links to HTML.
- Use the existing local `dist/assets/site.css`; do not add runtime network requests or JavaScript.
- Generate one `.html` page for each of the 40 packaged `.md` source files, preserving their relative paths.
- Keep an explicit link from each HTML page to the corresponding raw `.md` source.
- Local Markdown links in generated content must resolve to mirrored HTML pages and preserve fragment identifiers.
- Run verification after each implementation slice; the inline execution mode was selected by the user.

---

## File Map

- Create `scripts/render_site_docs.py`: enumerate Markdown sources, call Pandoc, rewrite Markdown links, and emit pages under `dist/site-docs/`.
- Create `tests/test_site_docs.py`: verify source/output coverage, page shell, local links, Markdown rendering structures, and landing-page destinations.
- Modify `dist/assets/site.css`: add documentation-shell and Markdown-content typography using existing design tokens.
- Modify `dist/index.html`: point the four documentation links to `site-docs/*.html` mirrors.
- Create 40 generated `.html` files under `dist/site-docs/` by running the generator.

## Task 1: Specify mirror behavior in tests

**Files:**
- Create: `tests/test_site_docs.py`
- Test: `dist/dama-data-project-skills-v1.0.0/` and `dist/site-docs/`

**Interfaces:**
- Source root: `dist/dama-data-project-skills-v1.0.0/`.
- Mirror root: `dist/site-docs/`.
- Mapping: source-relative `name.md` maps to mirror-relative `name.html`.

- [x] Add standard-library tests asserting exactly 40 Markdown sources and one mirrored HTML page per source.
- [x] Assert every generated page has a stylesheet, home link, and raw-source link that resolve locally.
- [x] Parse generated anchor links and assert there are no unresolved local `.md` links or broken local mirror targets.
- [x] Assert representative pages retain headings, tables, fenced code, and frontmatter-derived titles without showing raw YAML delimiters.
- [x] Assert the landing page links to `site-docs/README.html`, `site-docs/README.en.html`, `site-docs/VALIDATION.html`, and `site-docs/skills/managing-data-projects/SKILL.html`.
- [x] Run `python3 -m unittest tests.test_site_docs -v` before implementation; it failed because mirrors and HTML landing destinations were absent.

## Task 2: Generate static HTML mirrors

**Files:**
- Create: `scripts/render_site_docs.py`
- Create: `dist/site-docs/**/*.html`
- Test: `tests/test_site_docs.py`

**Interfaces:**
- CLI: `python3 scripts/render_site_docs.py`.
- Pandoc call: `pandoc --from=gfm --to=html5 --wrap=none` with Markdown supplied on stdin.
- Input mapping: each sorted `*.md` below the release root.
- Output mapping: corresponding relative `.html` path below `dist/site-docs/`.
- Each page shell includes `.docs-page`, `.docs-header`, `.docs-main`, `.docs-content`, a local stylesheet URL, a local home URL, and a raw source URL.

- [x] Implement deterministic discovery of all packaged Markdown sources and fail if the release contains zero Markdown files or Pandoc is unavailable.
- [x] Convert each document to an HTML fragment with Pandoc; derive the browser title from the first Markdown heading or filename.
- [x] Rewrite local `.md` href targets relative to the mirrored directory, normalize paths, and preserve any `#fragment`; fail if the source target is missing.
- [x] Wrap fragments in valid HTML5 with `lang="zh-CN"` for Chinese docs and `lang="en"` for `README.en.md`.
- [x] Add a raw Markdown source link pointing back to the unchanged release tree; compute all navigation and stylesheet links as relative paths.
- [x] Run `python3 scripts/render_site_docs.py`, then `python3 -m unittest tests.test_site_docs -v`; all six mirror tests passed.

## Task 3: Match the landing page design and route visitors to HTML

**Files:**
- Modify: `dist/assets/site.css`
- Modify: `dist/index.html`
- Test: `tests/test_site_docs.py`, `tests/test_landing_page.py`

**Interfaces:**
- All generated documents use existing design tokens (`--paper`, `--paper-bright`, `--ink`, `--ink-soft`, `--signal`, `--line`).
- Landing links target the four existing mirrors; original Markdown remains linked from each mirror as a download/source option.

- [x] Add responsive document layout styles: centered readable column, clear heading hierarchy, styled tables/code, accessible links, and mobile horizontal table scrolling.
- [x] Change the four landing-page `.md` hrefs to their HTML mirror destinations without changing visible bilingual labels.
- [x] Re-run `python3 scripts/render_site_docs.py` to ensure generated pages continue to reference the shared CSS.
- [x] Run `python3 -m unittest discover -s tests -v` (17 tests passed), `node --check dist/assets/site.js`, and the ZIP sidecar checksum verification (all passed).

## Task 4: Browser verification and handoff

**Files:**
- Verify: landing page and representative root, skill, and reference-document mirrors.

- [x] Browser preview remains unavailable: the prior approved local-file preview was refused by security policy; no alternate surface or workaround was attempted.
- [ ] Inspect a README, a skill page, and a reference page at desktop and mobile widths; blocked by the local-browser policy.
- [x] Report the exact static checks and disclose that rendered layout and runtime browser behavior could not be inspected.

## Self-review

- All 40 Markdown files are covered by recursive source enumeration; path mirroring is one-to-one and generated output is separate from the release source.
- Pandoc is only used during generation, so visitors have no conversion dependency.
- The plan includes tests before the converter, then content generation, design integration, and final verification in order.
