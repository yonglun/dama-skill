# DAMA Skill Pack Landing Page Design

## Goal

Create a polished, bilingual entry website that helps data-project teams understand, discover, and download the 17-skill DAMA data-project package. The primary audience is a colleague encountering the package for the first time.

## Approved direction

Build a standalone static website in `dist/` that can be opened locally without a build step or network dependency. Keep the existing `dama-data-project-skills-v1.0.0.zip` as the downloadable release. Do not publish the page to a public host or alter the skill contents.

Use a modern editorial visual system: warm off-white canvas, ink-blue typography, restrained signal-orange accents, carefully spaced typography, and original abstract data-management illustrations with a coherent line-and-form language. The site should feel like a considered knowledge product, not a generic SaaS dashboard.

## Information architecture

1. **Hero:** explain the purpose of the suite in one short bilingual message, show the 17-skill scope, link to the package download, and introduce the system through an original hero illustration.
2. **How it works:** communicate the router-to-domain-skill model and the distinction between project planning and specialist playbooks.
3. **Skill library:** list all 17 skills in three practical groups—project orchestration, foundational capabilities, and delivery/operations. Each skill entry presents its name, when to use it, expected output, and one actionable example prompt.
4. **Find a skill:** provide client-side text search and group filters; every skill remains visible without JavaScript and filtering must not obscure the underlying copy.
5. **Use and trust:** give a concise install path (`.agents/skills/`), package version, validation summary, source/authority boundary, and a second download link.
6. **Language:** support Chinese and English from the same page, with a visible language toggle and equivalent descriptions/examples in both languages.

## Content source

Use the released bilingual READMEs and packaged skill metadata as the source of truth for all skill names, triggers, outputs, and examples. Do not invent additional capabilities or imply that the suite is DAMA-approved. Preserve the boundary that DMBOK is source material and not agent instructions; the source PDF is not distributed in the release bundle.

## Technical approach

- Deliver `dist/index.html` and local assets under `dist/assets/`.
- Use plain HTML, CSS, and small dependency-free JavaScript; no build pipeline, framework, remote fonts, analytics, or external runtime requests.
- Keep skill content in structured page data so the 17 entries remain consistent across language, filters, and search.
- Prefer semantic HTML, keyboard-accessible controls, visible focus, adequate contrast, responsive layouts, and reduced-motion support.
- Link to the relative versioned ZIP and bilingual release documentation so the complete site can be moved together with the release directory.

## Visual assets

Generate an original, text-free hero illustration around the idea of a data project becoming a connected, governed system. Use a consistent family of simple, custom vector motifs for skill groups and individual skills so the library remains legible and fast to load. Illustrations must reinforce information hierarchy and must not contain embedded words or pseudo-text.

## Acceptance criteria

- The site opens directly from `dist/index.html` without a server or network access.
- All 17 skills are discoverable, and each has a use case, expected output, and bilingual example prompt.
- Search and group filters work with keyboard and pointer input; selecting a skill can reveal its full example without navigating away.
- Chinese/English switching preserves the current filter/search state and changes all page copy, not only the navigation.
- The download action resolves to `dist/dama-data-project-skills-v1.0.0.zip` when served locally or hosted with the `dist/` tree intact.
- Layout remains readable at mobile, tablet, and desktop widths; decorative images have suitable alternative-text treatment.
- Browser verification reports no uncaught console errors or broken local links.
- The website stays outside the versioned skill bundle unless a later release explicitly includes it.

## Out of scope

- Hosting, domain setup, deployment automation, or public release.
- Editing skills, changing README content, or creating a new skill-package version.
- User accounts, backend search, usage analytics, or installation automation.

## Self-review

- No placeholder content is required; examples come from the existing bilingual README content.
- The 17-skill count and existing v1.0.0 ZIP are consistent with the release manifest.
- Offline use is compatible with local assets and dependency-free JavaScript.
- The download route assumes the site and ZIP remain under the same `dist/` tree, as specified.
