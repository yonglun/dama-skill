# DAMA Skill Documentation HTML Mirror Design

## Goal

Make every Markdown document in the v1.0.0 release readable as a page in the same offline website, without changing or replacing the original Markdown distribution.

## Approved direction

Generate one static HTML mirror for each of the 40 `.md` files under `dist/dama-data-project-skills-v1.0.0/`. Store the mirrors under `dist/site-docs/` with the same relative directory structure and `.html` extensions. Keep the original Markdown files and `dama-data-project-skills-v1.0.0.zip` unchanged.

The landing page's links to the Chinese README, English README, validation summary, and router skill should open their HTML mirrors. Markdown links inside rendered pages should navigate to corresponding HTML mirrors when a target is another packaged Markdown document. Each document page should use the landing page's existing local stylesheet and palette, offer a path back to the landing page, and link to its original Markdown source.

## Technical approach

- Use a small Python 3 standard-library build script at `scripts/render_site_docs.py` and the installed Pandoc executable to convert Markdown to an HTML fragment. Pandoc is a build-time requirement only; generated pages run from disk and make no network requests.
- Preserve fenced code blocks, tables, headings, lists, and inline links through Pandoc's GitHub-Flavored Markdown reader.
- Wrap each fragment in a semantic HTML document shell with the shared local CSS, title, language metadata, breadcrumbs, home navigation, and source-Markdown download link.
- Rewrite local `.md` links to the matching mirrored `.html` file, preserving anchors. Fail generation on a broken local Markdown target rather than emitting a misleading link.
- Keep all output under `dist/site-docs/`; do not edit the versioned package folder, ZIP, README source, or individual skill content.

## Acceptance criteria

- Exactly 40 packaged `.md` sources each have one HTML mirror, with matching relative path and `.html` suffix.
- The four Markdown links on the landing page now point to styled HTML mirrors.
- Every local Markdown link in generated pages resolves to a generated HTML mirror; non-Markdown links remain local or external as authored.
- Every mirror links to the shared local stylesheet, the home page, and its original Markdown source.
- Tables, code fences, headings, and readable line lengths are retained in rendered pages.
- The website remains offline-capable and the v1.0.0 source folder and ZIP checksum are unchanged.

## Out of scope

- Editing or repackaging any Markdown source.
- Publishing or hosting the site.
- Adding a JavaScript or network-based Markdown renderer to the visitor experience.

## Self-review

- The mirror path is unambiguous: package-relative `path/name.md` maps to `dist/site-docs/path/name.html`.
- Conversion is a build-time operation, so Pandoc does not become a runtime dependency.
- Source downloads remain available and generated links stay inside the mirror tree.
