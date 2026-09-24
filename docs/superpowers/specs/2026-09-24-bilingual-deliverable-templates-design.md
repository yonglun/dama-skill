# Bilingual Deliverable Templates for the DAMA Skill Suite

## Goal and scope

Give each of the 17 skills a self-contained, editable set of Chinese and English deliverable templates. A user who copies one complete skill directory into another project must be able to find and use its templates without installing the other 16 skills. Templates guide project work; they do not assert that a real project's owners, thresholds, approvals, or evidence already exist.

The existing [router templates](../../../skills/managing-data-projects/references/deliverable-templates.md) and the 17 skills' output contracts are the content baseline. The new templates retain their evidence-based, risk-aware approach while making the format and field names consistent across domains.

## Chosen approach

Use a common deliverable envelope plus domain-specific sections. Every skill receives a Chinese and an English Markdown delivery-pack template. Provide editable Word templates for narrative work products and Excel templates for matrices, inventories, registers, scorecards, or test records. Do not force each individual artifact into all three formats. A skill may have both Word and Excel files when its output contract includes both kinds of work.

The alternatives were (1) a three-format copy of every artifact, which creates many awkward and redundant files, and (2) only a generic suite-wide form, which omits domain-specific guidance. The chosen approach preserves both usability and completeness.

## Common contract

All formats use the same concepts and stable identifiers for: artifact title/type; project and skill; version, date, status, author, owner and approver; purpose, business outcome and scope; source inputs and assumptions; domain analysis or design; decisions and rationale; risks, exceptions and unresolved items with owners and due dates; acceptance criteria, evidence location and reviewer decision; next action or stage gate. Domain-specific templates can reorder or omit inapplicable fields but must explain significant omissions. Blank fields remain blank or explicitly marked as unresolved; examples must be labeled as examples, not project facts.

Chinese and English versions are separate files with equivalent sections, fields, examples, sheet structure, and field identifiers. English is not required to be a literal translation when a clearer professional term exists. Neither language version may silently add or remove a decision, control, or acceptance requirement.

## Artifact set and location

Each skill stores its distributable files under `skills/<skill-name>/templates/`. Files use explicit `.zh` and `.en` language suffixes. At minimum, each skill has `delivery-pack.zh.md` and `delivery-pack.en.md`. Its Word and Excel files are selected from the work-product types in the table below; they are not empty re-exports of the Markdown pack.

| Skill | Word narrative template | Excel structured template |
|---|---|---|
| managing-data-projects | Integrated project plan and gate decision | Work-package, dependency, risk and evidence registers |
| handling-data-ethically | Ethical-use impact and decision record | Affected-party, harm, control and review register |
| establishing-data-governance | Governance charter and policy decision | Decision-rights, stewardship and exception register |
| designing-data-architecture | Architecture views and decision record | Capability, interface and transition inventory |
| modeling-data | Model specification and review record | Entity, attribute, key and mapping dictionary |
| operating-data-storage | Operations readiness and runbook | Capacity, recovery-test and handoff checklist |
| securing-data | Data-security assessment and control design | Classification, access and control-test matrix |
| integrating-data | Versioned interface contract | Source-target mapping, failure and reconciliation register |
| managing-documents-and-content | Content lifecycle and retention design | Content inventory, classification and disposition register |
| managing-reference-and-master-data | Domain authority and survivorship decision | Crosswalk, matching, merge/split and code-set register |
| delivering-data-warehousing-and-bi | Metric and analytical-product specification | Metric, source, reconciliation and UAT register |
| managing-metadata | Metadata product and stewardship specification | Glossary, lineage, coverage and freshness register |
| improving-data-quality | Quality improvement and root-cause plan | Rule, baseline, issue and scorecard register |
| delivering-data-science | Experiment plan and model card | Data, feature, validation and monitoring register |
| assessing-data-management-maturity | Evidence-based assessment report | Criteria, evidence-strength and gap matrix |
| organizing-data-management | Operating-model and role charter | RACI, staffing and pilot-measure register |
| leading-data-change | Change and adoption plan | Stakeholder, activity, obstacle and adoption register |

The exact sheets and sections follow each skill's output contract. A table row describes a coherent workbook or document, not a requirement to compress every domain deliverable into one page. The Markdown pack indexes the corresponding Office files and explains which is appropriate for a given task.

## Production and distribution

Maintain a versioned template catalog in the repository as the source of shared field definitions, bilingual labels, domain sections, and Office file assignments. Generate the distributable Markdown, `.docx`, and `.xlsx` files into each skill's `templates/` directory from that catalog. Generated Office files contain no macros or external connections. The build must be repeatable and must flag missing translations or mismatched field identifiers rather than publishing partial files.

Add relative links from each `SKILL.md` to its templates and short usage guidance in both READMEs. Keep the single-skill copy workflow intact. Include the new files in a new versioned package under `dist/`, with an updated manifest and checksums; do not silently replace the v1.0.0 archive. Update the landing page's current download and documentation links to the new package. Markdown templates receive styled HTML mirrors on the site; Word and Excel templates remain downloadable files.

## Verification

- Validate all 17 skill directories, template links, bilingual pairs, field identifiers, Office ZIP structure, and absence of copyrighted source-book material.
- Verify that each skill's output-contract topics appear in its delivery pack and that narrative and structured Office templates cover their declared purpose.
- Open or render representative Word and Excel templates from multiple domains and both languages; inspect page layout, worksheet names, column widths, wrapping, print settings, and editable fields. Repair layout problems before release.
- Rebuild the package and site twice to confirm deterministic contents and checksums, then run the existing skill, website, and documentation checks.
- Confirm that a copied single-skill directory contains every linked template, and that the release ZIP, manifest, landing-page download, and HTML documentation refer to the same version.

## Out of scope

Populating templates with a real organization's data, deciding actual approval authorities or legal thresholds, embedding macros, and reproducing DMBOK text or official DAMA forms are not part of this work.
