# Landing-page guide and deliverable-template links

## Goal

Make the release area concise and let visitors reach the deliverable template for the skill they are viewing, in the currently selected language.

## Current state

The `dist/index.html` release area has five links: one generic template example, separate Chinese and English guides, a validation summary, and a ZIP checksum. The 17 skill cards have prompt examples but no template links. Each skill already has Chinese and English delivery-pack HTML pages under `dist/site-docs/v1.1.0/skills/<slug>/templates/`; those pages link to the corresponding Word report and Excel register.

## Design decision

Use one language-aware link in each skill card and one language-aware guide link in the release area. This keeps card actions compact while preserving access to Markdown, Word, and Excel templates through each delivery-pack page. Separate per-language links would add visual clutter; three direct format links per card would duplicate navigation already available on the delivery-pack page.

## Behavior and layout

- Remove the generic `Explore a deliverable template`, `View validation summary`, and `ZIP SHA-256 checksum` links from the release area. Do not remove the underlying files.
- Replace the two guide links with one visible guide link. In English it reads `Read the English guide` and points to `site-docs/v1.1.0/README.en.html`; in Chinese it reads `阅读中文使用指南` and points to `site-docs/v1.1.0/README.html`.
- Add one `Deliverable template` / `交付物模板` link to each of the 17 skill cards, below the prompt example action. It opens that card's own `delivery-pack.en.html` or `delivery-pack.zh.html` according to the selected language.
- Keep the existing default of English. Switching languages changes labels and destinations immediately, including after search or category filtering. Links remain ordinary keyboard-accessible anchors. The current visual style and responsive card layout remain intact.
- Use a small shared language-switching mechanism for anchor destinations; avoid duplicating two visible links per card.

## Scope

Change only the landing-page markup, its interaction script and targeted styling, plus landing-page tests. Do not rebuild or alter the v1.1.0 archive, checksum, template content, or HTML documentation mirrors. Do not publish automatically.

## Acceptance checks

1. The release area contains only one guide link from the five existing release links; the removed labels and links are absent there.
2. All 17 cards link to their own English and Chinese HTML delivery packs, and every target exists.
3. Default English and switched Chinese labels and `href` values are correct in a real browser; switching back restores English.
4. Search, filters, disclosure buttons, keyboard navigation, and mobile layout still work.
5. Landing-page and site-documentation tests pass; no unrelated files change.
