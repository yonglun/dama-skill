# Bilingual Deliverable Templates Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship self-contained Chinese and English Markdown, Word, and Excel deliverable templates for all 17 DAMA data-project skills, with a new versioned distribution and discoverable website links.

**Architecture:** A versioned catalog defines shared field identifiers, translations, and domain work products. A build command generates two Markdown packs, two Word reports, and two Excel workbooks per skill in that skill's `templates/` folder; each skill then remains portable on its own. A separate release command packages the complete source suite as v1.1.0, and the existing documentation renderer mirrors the new Markdown while linking to downloadable Office files.

**Tech Stack:** Python 3 with bundled `python-docx` 1.2.0 for Word, bundled Node.js with `@oai/artifact-tool` for Excel, Python standard-library `unittest`, and installed Pandoc. Use the executables returned by `load_workspace_dependencies`; system Python does not include `python-docx`.

**Implementation note:** The illustrative `openpyxl` authoring code in Task 3 is superseded by `scripts/build_template_workbooks.mjs`, which uses `@oai/artifact-tool` to create XLSX files. `openpyxl` remains read-only in tests. The builder normalizes OOXML relationship IDs so the 102 generated files are byte-reproducible.

## Global Constraints

- Preserve the existing v1.0.0 source directory, ZIP, checksum, and site-doc pages; publish new content as v1.1.0.
- Keep `skills/` the editable skill source; a copied single-skill directory must contain all its linked templates.
- Every skill gets `delivery-pack.zh.md`, `delivery-pack.en.md`, `report.zh.docx`, `report.en.docx`, `register.zh.xlsx`, and `register.en.xlsx` under its own `templates/` directory. These are six *purpose-specific* files, not three copies of one artifact.
- Chinese and English must have the same stable field IDs, sections, controls, and acceptance requirements; natural wording may differ.
- Never fabricate real project facts, approval, legal thresholds, or evidence. The source book and extracted material under `dmbok/` and `tmp/` never enter a release.
- All generated Office files must be macro-free and have no external data connections.
- Do not edit the generated template files by hand; change the catalog or generator and rebuild.

## File map

| Path | Responsibility |
|---|---|
| `templates/catalog.json` | Versioned shared field labels and 17 bilingual domain specifications |
| `scripts/build_deliverable_templates.py` | Catalog validation and generation of Markdown, DOCX, XLSX |
| `tests/test_deliverable_templates.py` | Catalog parity, format integrity, field and domain coverage, reproducibility |
| `skills/*/templates/` | Six self-contained distributable files per skill |
| `skills/*/SKILL.md` | Short relative links and selection guidance for templates |
| `README.md`, `README.zh.md` | English and Chinese installation and template usage |
| `scripts/build_release.py` | Deterministic v1.1.0 package, manifest and checksums |
| `tests/test_release.py` | ZIP membership, hash integrity, exclusions and single-skill portability |
| `scripts/render_site_docs.py`, `tests/test_site_docs.py` | New v1.1.0 HTML mirrors and Office download links |
| `dist/index.html`, `tests/test_landing_page.py` | Current release download and template discovery |

---

### Task 1: Catalog schema and validation

**Files:**
- Create: `templates/catalog.json`
- Create: `scripts/build_deliverable_templates.py`
- Create: `tests/test_deliverable_templates.py`

**Interfaces:**
- Produces: `load_catalog(path: Path) -> dict`, raising `ValueError` on missing skills, languages, duplicate IDs, empty sections, or Excel columns.
- Consumes: `EXPECTED_SKILLS` from `scripts/validate_skill_suite.py`.

- [ ] **Step 1: Write failing catalog tests.** Add `unittest` cases that load the catalog, assert its skill keys equal `EXPECTED_SKILLS`, and reject a copied catalog with one deleted English field label or repeated field ID. Test with `load_catalog` imported from `scripts.build_deliverable_templates`.

```python
from copy import deepcopy
from pathlib import Path
import unittest
from scripts.build_deliverable_templates import load_catalog, validate_catalog
from scripts.validate_skill_suite import EXPECTED_SKILLS

CATALOG = Path(__file__).resolve().parents[1] / "templates/catalog.json"

class CatalogTests(unittest.TestCase):
    def test_all_skills_and_languages_are_present(self):
        catalog = load_catalog(CATALOG)
        self.assertEqual(set(catalog["skills"]), set(EXPECTED_SKILLS))
        self.assertEqual(validate_catalog(catalog), [])

    def test_missing_translation_is_rejected(self):
        catalog = deepcopy(load_catalog(CATALOG))
        del catalog["skills"]["managing-data-projects"]["sections"][0]["en"]
        self.assertIn("missing en", " ".join(validate_catalog(catalog)))
```

- [ ] **Step 2: Confirm RED.** Run the bundled Python with `-m unittest tests/test_deliverable_templates.py -v`. Expect import failure because the builder does not exist.
- [ ] **Step 3: Create the catalog skeleton and validator.** Use JSON with top-level `schema_version: 1`, `common_fields`, and `skills`. The required common field IDs are `artifact_id`, `project`, `skill`, `version`, `date`, `status`, `author`, `owner`, `approver`, `purpose`, `business_outcome`, `scope`, `source_inputs`, `assumptions`, `decisions`, `rationale`, `risks`, `exceptions`, `open_items`, `due_date`, `acceptance_criteria`, `evidence_location`, `reviewer_decision`, and `next_gate`. Each common field has `id`, `zh`, and `en`. Each skill has bilingual `title`, `report_title`, `register_title`, nonempty `sections` (each `id`, `zh`, `en`, and bilingual `instruction`), and `sheets` (each `id`, bilingual `name`, bilingual `purpose`, and nonempty bilingual `columns`; each column has `id`, `zh`, `en`, and bilingual `instruction`). Guidance tells the user what evidence or decision belongs in a field without supplying fictional project facts. Shared field IDs must be unique. The validator checks exactly 17 skills and never silently supplies a translation. Implement these exact interface names:

```python
import json
from pathlib import Path
from scripts.validate_skill_suite import EXPECTED_SKILLS

def load_catalog(path: Path) -> dict:
    catalog = json.loads(path.read_text(encoding="utf-8"))
    errors = validate_catalog(catalog)
    if errors:
        raise ValueError("; ".join(errors))
    return catalog

def validate_catalog(catalog: dict) -> list[str]:
    errors = []
    if catalog.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    fields = catalog.get("common_fields", [])
    if not fields:
        errors.append("common_fields: empty")
    required = {"artifact_id", "project", "skill", "version", "date", "status", "author", "owner", "approver", "purpose", "business_outcome", "scope", "source_inputs", "assumptions", "decisions", "rationale", "risks", "exceptions", "open_items", "due_date", "acceptance_criteria", "evidence_location", "reviewer_decision", "next_gate"}
    if {field.get("id") for field in fields} != required:
        errors.append("common_fields: wrong field ids")
    if len([field.get("id") for field in fields]) != len({field.get("id") for field in fields}):
        errors.append("common_fields: duplicate id")
    for field in fields:
        for lang in ("zh", "en"):
            if not field.get(lang):
                errors.append(f"common_fields.{field.get('id')}: missing {lang}")
    if set(catalog.get("skills", {})) != set(EXPECTED_SKILLS):
        errors.append("skill set does not match EXPECTED_SKILLS")
    for slug, spec in catalog.get("skills", {}).items():
        for key in ("title", "report_title", "register_title"):
            for lang in ("zh", "en"):
                if not spec.get(key, {}).get(lang):
                    errors.append(f"{slug}.{key}: missing {lang}")
        for group in ("sections", "sheets"):
            rows = spec.get(group, [])
            if not rows:
                errors.append(f"{slug}.{group}: empty")
            ids = [row.get("id") for row in rows]
            if len(ids) != len(set(ids)):
                errors.append(f"{slug}.{group}: duplicate id")
            for row in rows:
                labels = row if group == "sections" else row.get("name", {})
                for lang in ("zh", "en"):
                    if not labels.get(lang):
                        errors.append(f"{slug}.{group}.{row.get('id')}: missing {lang}")
                    guidance = row.get("instruction", {}) if group == "sections" else row.get("purpose", {})
                    if not guidance.get(lang):
                        errors.append(f"{slug}.{group}.{row.get('id')}: missing {lang} guidance")
                if group == "sheets":
                    columns = row.get("columns", [])
                    if not columns:
                        errors.append(f"{slug}.sheets.{row.get('id')}: empty columns")
                    if len([column.get("id") for column in columns]) != len({column.get("id") for column in columns}):
                        errors.append(f"{slug}.sheets.{row.get('id')}: duplicate column id")
                    for lang in ("zh", "en"):
                        if len(row.get("name", {}).get(lang, "")) > 31:
                            errors.append(f"{slug}.sheets.{row.get('id')}: {lang} name exceeds Excel limit")
                    for column in columns:
                        for lang in ("zh", "en"):
                            if not column.get(lang):
                                errors.append(f"{slug}.sheets.{row.get('id')}.{column.get('id')}: missing {lang}")
                            if not column.get("instruction", {}).get(lang):
                                errors.append(f"{slug}.sheets.{row.get('id')}.{column.get('id')}: missing {lang} guidance")
    return errors
```

- [ ] **Step 4: Add all 17 valid skill specs.** Start with `managing-data-projects` sections: `business_outcome`, `scope`, `assumptions`, `domain_route`, `dependencies`, `decision_rights`, `risks_controls`, `acceptance_evidence`, `next_gate`. Its workbook sheets are `work_packages` (`domain`, `goal`, `owner`, `dependency`, `deliverable`, `acceptance_evidence`), `risks` (`event`, `impact`, `control`, `owner`, `threshold`, `escalation`), and `gates` (`stage`, `exit_criteria`, `evidence`, `decision`, `approver`, `date`). Give every field a professional Chinese and English label. Populate the other 16 specs using their output contracts and the explicit domain ID map in Task 2; do not insert generic temporary domain content.
- [ ] **Step 5: Confirm GREEN and commit.** Run bundled Python `-m unittest tests/test_deliverable_templates.py -v`; expect the catalog tests to pass. Commit catalog, validator and tests with message `Add bilingual deliverable template catalog`.

### Task 2: Domain-complete bilingual content

**Files:**
- Modify: `templates/catalog.json`
- Test: `tests/test_deliverable_templates.py`

**Interfaces:**
- Consumes: Task 1 catalog schema.
- Produces: exactly 17 complete domain specs keyed by the names in `EXPECTED_SKILLS`.

- [ ] **Step 1: Add one test that checks domain-specific tokens.** For each skill below, assert its `sections` contain the listed IDs and at least one sheet contains each listed column ID. This catches generic templates that omit the skill's actual output contract.

```python
REQUIRED = {
    "handling-data-ethically": ({"purpose", "affected_parties", "harms", "recourse", "stop_conditions"}, {"affected_party", "harm", "control"}),
    "establishing-data-governance": ({"charter", "decision_rights", "policy", "exceptions", "scorecard"}, {"decision", "accountable", "escalation"}),
    "designing-data-architecture": ({"current_state", "target_state", "transition", "tradeoffs", "conformance"}, {"capability", "dependency", "owner"}),
    "modeling-data": ({"use_cases", "model_level", "grain_keys", "traceability", "review"}, {"entity", "attribute", "definition", "key"}),
    "operating-data-storage": ({"service_scope", "slo", "recovery", "runbook", "go_no_go"}, {"rto", "rpo", "test_result"}),
    "securing-data": ({"classification", "threats", "access_design", "control_tests", "residual_risk"}, {"subject", "data", "action", "decision"}),
    "integrating-data": ({"interface_contract", "mapping", "replay", "schema_evolution", "reconciliation"}, {"source_field", "target_field", "transformation"}),
    "managing-documents-and-content": ({"content_scope", "taxonomy", "retention", "legal_hold", "disposition"}, {"content_type", "retention_rule", "disposition"}),
    "managing-reference-and-master-data": ({"authority", "global_identity", "survivorship", "merge_split", "distribution"}, {"source_id", "global_id", "match_rule"}),
    "delivering-data-warehousing-and-bi": ({"decisions", "metric_contract", "fact_grain", "history", "business_acceptance"}, {"metric", "definition", "source", "test"}),
    "managing-metadata": ({"metadata_product", "glossary", "lineage", "freshness", "impact_analysis"}, {"term", "owner", "source", "consumer"}),
    "improving-data-quality": ({"purpose", "rules", "baseline", "root_cause", "prevention", "scorecard"}, {"rule", "denominator", "threshold", "owner"}),
    "delivering-data-science": ({"hypothesis", "data_features", "evaluation", "model_card", "monitoring", "rollback"}, {"feature", "source", "validation", "drift_threshold"}),
    "assessing-data-management-maturity": ({"scope", "rubric", "evidence", "current_target", "roadmap"}, {"criterion", "evidence_strength", "current", "target"}),
    "organizing-data-management": ({"model_options", "selected_model", "role_charter", "raci", "pilot"}, {"activity", "accountable", "responsible"}),
    "leading-data-change": ({"case_for_change", "stakeholders", "communications", "adoption", "reinforcement"}, {"stakeholder", "action", "adoption_metric"}),
}
```

- [ ] **Step 2: Confirm RED.** Run `/Users/yonglun/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -m unittest tests/test_deliverable_templates.py -v`; expect missing-domain failures.
- [ ] **Step 3: Populate each domain row with the required IDs, translations and guidance.** Use the approved [design](../specs/2026-09-24-bilingual-deliverable-templates-design.md) table for report/register names, and each `skills/<slug>/SKILL.md` `## 输出契约` for the full content. For each listed ID above, supply a Chinese label, English label, and short bilingual instruction specifying the decision, evidence or rule to record; add `decisions`, `risks_exceptions`, and `acceptance_evidence` sections when not already covered. Workbook columns include `owner`, `status`, `evidence`, and `review_date` in addition to the domain columns unless redundant, with bilingual instructions for each column. The domain-specific IDs in the test code above are the minimum required content, not sample data.
- [ ] **Step 4: Confirm GREEN and commit.** Run `/Users/yonglun/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 -m unittest tests/test_deliverable_templates.py -v` and `python3 scripts/validate_skill_suite.py skills`; expect all tests to pass and `OK: validated 17 DAMA skills`. Commit the stronger domain-coverage tests and any catalog corrections with message `Verify domain-specific template coverage`.

### Task 3: Generate self-contained Markdown, Word, and Excel files

**Files:**
- Modify: `scripts/build_deliverable_templates.py`
- Modify: `tests/test_deliverable_templates.py`
- Create: `skills/<each-of-17>/templates/` generated outputs

**Interfaces:**
- Consumes: `load_catalog(path: Path) -> dict`.
- Produces: `build_all(catalog_path: Path, skills_root: Path) -> list[Path]`, six files per skill; `build_deliverable_templates.py --check` exits nonzero if generated bytes differ from committed outputs.

- [ ] **Step 1: Add a failing generation test.** Generate into a temporary directory containing the 17 skill folders, assert 102 output files, parse DOCX with `docx.Document`, parse XLSX with `openpyxl.load_workbook`, and assert the Chinese and English heading IDs/sheet IDs are equal per skill. Assert `.docx` has paragraphs and `.xlsx` has a header row, filter, frozen header, and no external links.
- [ ] **Step 2: Confirm RED.** Run bundled Python `-m unittest tests/test_deliverable_templates.py -v`; expect `build_all` import failure.
- [ ] **Step 3: Implement renderers using catalog data.** `render_markdown` writes the common envelope, domain sections, Markdown tables for every workbook sheet, and same-language Office links. `render_docx` creates a separately structured narrative report; `render_xlsx` creates an Instructions sheet plus each declared register sheet. Add this code to the builder after the validator, with the imports shown. Adjust styling only after inspecting the first generated files.

```python
from datetime import datetime
from io import BytesIO
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
from docx import Document
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

FIXED_TIME = datetime(2026, 9, 24)

def render_markdown(slug: str, spec: dict, common_fields: list[dict], lang: str) -> str:
    lines = [f"# {spec['title'][lang]}", "", f"Skill: `{slug}`", ""]
    lines += [f"[Word](report.{lang}.docx) · [Excel](register.{lang}.xlsx)", ""]
    lines.append("## " + ("基本信息" if lang == "zh" else "Record details"))
    lines += [f"- **{field[lang]}** (`{field['id']}`): " for field in common_fields]
    for section in spec["sections"]:
        lines += ["", f"## {section[lang]} (`{section['id']}`)", "", section["instruction"][lang], "", "—"]
    for sheet in spec["sheets"]:
        columns = sheet["columns"]
        lines += ["", f"## {sheet['name'][lang]} (`{sheet['id']}`)", "", sheet["purpose"][lang], ""]
        lines += ["| " + " | ".join(col[lang] for col in columns) + " |"]
        lines += ["| " + " | ".join("---" for _ in columns) + " |"]
        lines += ["| " + " | ".join("" for _ in columns) + " |"]
    return "\n".join(lines) + "\n"

def render_docx(slug: str, spec: dict, common_fields: list[dict], lang: str, path: Path) -> None:
    document = Document()
    document.core_properties.title = spec["report_title"][lang]
    document.core_properties.created = FIXED_TIME
    document.core_properties.modified = FIXED_TIME
    document.add_heading(spec["report_title"][lang], 0)
    document.add_paragraph(f"Skill: {slug}")
    metadata = document.add_table(rows=0, cols=2)
    metadata.style = "Light Shading Accent 1"
    for field in common_fields:
        cells = metadata.add_row().cells
        cells[0].text = f"{field[lang]} ({field['id']})"
        cells[1].text = " "
    for section in spec["sections"]:
        document.add_heading(f"{section[lang]} ({section['id']})", level=1)
        document.add_paragraph(section["instruction"][lang])
        document.add_paragraph(" ")
    document.save(path)
    normalize_ooxml(path)

def render_xlsx(slug: str, spec: dict, common_fields: list[dict], lang: str, path: Path) -> None:
    workbook = Workbook()
    workbook.properties.created = FIXED_TIME
    workbook.properties.modified = FIXED_TIME
    guide = workbook.active
    guide.title = "说明" if lang == "zh" else "Instructions"
    guide.append([spec["register_title"][lang], slug])
    for field in common_fields:
        guide.append([f"{field[lang]} ({field['id']})", ""])
    for sheet in spec["sheets"]:
        guide.append([sheet["id"], f"{sheet['name'][lang]} — {sheet['purpose'][lang]}"])
        for column in sheet["columns"]:
            guide.append([column["id"], column["instruction"][lang]])
    guide.column_dimensions["A"].width = 34
    guide.column_dimensions["B"].width = 55
    for sheet in spec["sheets"]:
        worksheet = workbook.create_sheet(sheet["name"][lang][:31])
        worksheet.append([col[lang] for col in sheet["columns"]])
        worksheet.freeze_panes = "A2"
        last_col = get_column_letter(len(sheet["columns"]))
        worksheet.auto_filter.ref = f"A1:{last_col}26"
        worksheet.print_title_rows = "1:1"
        worksheet.page_setup.orientation = "landscape"
        for index, column in enumerate(sheet["columns"], 1):
            cell = worksheet.cell(1, index)
            cell.font = Font(bold=True, color="FFFFFF")
            cell.fill = PatternFill("solid", fgColor="171717")
            cell.alignment = Alignment(wrap_text=True)
            worksheet.column_dimensions[get_column_letter(index)].width = min(38, max(18, len(column[lang]) + 8))
        for row in worksheet.iter_rows(min_row=2, max_row=26, min_col=1, max_col=len(sheet["columns"])):
            for cell in row:
                cell.alignment = Alignment(vertical="top", wrap_text=True)
    workbook.save(path)
    normalize_ooxml(path)

def normalize_ooxml(path: Path) -> None:
    with ZipFile(path) as source:
        entries = [(name, source.read(name)) for name in sorted(source.namelist())]
    buffer = BytesIO()
    with ZipFile(buffer, "w") as target:
        for name, contents in entries:
            info = ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            target.writestr(info, contents)
    path.write_bytes(buffer.getvalue())

def build_all(catalog_path: Path, skills_root: Path) -> list[Path]:
    catalog = load_catalog(catalog_path)
    outputs = []
    for slug, spec in sorted(catalog["skills"].items()):
        skill_dir = skills_root / slug
        if not skill_dir.is_dir():
            raise ValueError(f"missing skill directory: {slug}")
        output_dir = skill_dir / "templates"
        output_dir.mkdir(exist_ok=True)
        for lang in ("zh", "en"):
            markdown = output_dir / f"delivery-pack.{lang}.md"
            report = output_dir / f"report.{lang}.docx"
            register = output_dir / f"register.{lang}.xlsx"
            markdown.write_text(render_markdown(slug, spec, catalog["common_fields"], lang), encoding="utf-8", newline="\n")
            render_docx(slug, spec, catalog["common_fields"], lang, report)
            render_xlsx(slug, spec, catalog["common_fields"], lang, register)
            outputs.extend((markdown, report, register))
    return outputs
```
- [ ] **Step 4: Add CLI and generated-file check.** `--check` generates into `tempfile.TemporaryDirectory()` and compares each expected file to `skills_root/<slug>/templates/<name>` byte-for-byte. Normal mode writes only six known names per skill and leaves unrelated user files untouched. Reject missing skill directories. Append:

```python
def main() -> int:
    import argparse
    import tempfile
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    catalog = root / "templates/catalog.json"
    skills_root = root / "skills"
    if not args.check:
        print(f"Generated {len(build_all(catalog, skills_root))} template files")
        return 0
    with tempfile.TemporaryDirectory() as temporary:
        temporary_root = Path(temporary)
        for slug in EXPECTED_SKILLS:
            (temporary_root / slug).mkdir()
        generated = build_all(catalog, temporary_root)
        changed = [
            path.relative_to(temporary_root)
            for path in generated
            if not (skills_root / path.relative_to(temporary_root)).is_file()
            or path.read_bytes() != (skills_root / path.relative_to(temporary_root)).read_bytes()
        ]
    if changed:
        print("Out-of-date templates: " + ", ".join(map(str, changed)))
        return 1
    print("OK: 102 generated template files match catalog")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```
- [ ] **Step 5: Confirm GREEN, inspect and commit.** Run bundled Python `-m scripts.build_deliverable_templates`, then `-m scripts.build_deliverable_templates --check`, then bundled Python `-m unittest tests/test_deliverable_templates.py -v`. Open one Chinese and one English report and workbook using read-only parsers; check that all 17 output directories have six files. Commit generator, tests, and generated templates with message `Add bilingual Markdown and Office templates`.

### Task 4: Make templates discoverable and validate portable skills

**Files:**
- Modify: `skills/*/SKILL.md`
- Modify: `README.md`, `README.zh.md`
- Modify: `scripts/validate_skill_suite.py`
- Modify: `tests/test_validate_skill_suite.py`

**Interfaces:**
- Consumes: six generated files per skill from Task 3.
- Produces: every skill links to both Markdown packs and explains Office format selection.

- [ ] **Step 1: Add failing suite tests.** In the validator tests, remove `templates/delivery-pack.en.md` from a temporary skill directory and assert a missing-template error. Add a test that checks all 17 `SKILL.md` files link to `templates/delivery-pack.zh.md` and `templates/delivery-pack.en.md`.
- [ ] **Step 2: Confirm RED.** Run `python3 -m unittest tests/test_validate_skill_suite.py -v`; expect the new cases to fail.
- [ ] **Step 3: Extend the validator.** For each of `delivery-pack.zh.md`, `delivery-pack.en.md`, `report.zh.docx`, `report.en.docx`, `register.zh.xlsx`, `register.en.xlsx`, check `skill_dir / "templates" / filename` is a file. Reuse `_validate_links` for both Markdown packs. Do not scan legitimate blank form fields as scaffold errors; instead require nonempty headings, the skill name, and links to the two Office files. Add this constant and function, then call it once inside the router branch before its early `return` and once at the end of the non-router branch:

```python
TEMPLATE_FILES = (
    "delivery-pack.zh.md", "delivery-pack.en.md",
    "report.zh.docx", "report.en.docx",
    "register.zh.xlsx", "register.en.xlsx",
)

def _validate_templates(skill_dir: Path, name: str, errors: list[str]) -> None:
    template_dir = skill_dir / "templates"
    for filename in TEMPLATE_FILES:
        path = template_dir / filename
        if not path.is_file():
            errors.append(f"{name}: missing template: {filename}")
            continue
        if path.suffix == ".md":
            body = _read(path, errors)
            _validate_links(path, body, errors)
            lang = "zh" if ".zh." in filename else "en"
            if not body.startswith("# ") or name not in body:
                errors.append(f"{path}: missing heading or skill id")
            if f"report.{lang}.docx" not in body or f"register.{lang}.xlsx" not in body:
                errors.append(f"{path}: missing Office links")
```
- [ ] **Step 4: Update all 17 skill files.** Add this same short section after each output contract, with the skill's relative paths; keep domain methods unchanged:

```markdown
## 交付模板

使用 [中文交付包](templates/delivery-pack.zh.md) 或 [English delivery pack](templates/delivery-pack.en.md) 组织输出。叙述性方案和评审记录使用同目录 Word 模板；矩阵、台账和评分卡使用同目录 Excel 模板。模板中的责任、阈值、批准和证据须由实际项目确认。
```

- [ ] **Step 5: Update both READMEs.** Add a concise `Templates` / `交付模板` section after Quick start explaining the six files, language suffixes, Word versus Excel selection, single-skill portability, blank fields, and source/release relationship. Link to the router's two Markdown packs as examples. Do not reprint 17 skill tables.
- [ ] **Step 6: Confirm GREEN and commit.** Run suite validator and unit tests; verify relative links with `rg -n 'delivery-pack' skills/*/SKILL.md`. Commit with message `Link deliverable templates from skills and guides`.

### Task 5: Build an immutable v1.1.0 release

**Files:**
- Create: `scripts/build_release.py`
- Create: `tests/test_release.py`
- Create: `dist/dama-data-project-skills-v1.1.0/`, `dist/dama-data-project-skills-v1.1.0.zip`, `dist/dama-data-project-skills-v1.1.0.zip.sha256`

**Interfaces:**
- Consumes: source `skills/`, README files, `LICENSE`, and verified templates.
- Produces: `build_release(output_root: Path, release_date: str = "2026-09-24") -> Path` returning the package directory; no mutation of v1.0.0.

- [ ] **Step 1: Write failing release tests.** Build into `TemporaryDirectory()`. Assert the ZIP includes 17 `SKILL.md`, 102 template files, Apache license and both guides; excludes `dmbok/`, `tmp/`, `.DS_Store`, symlinks and secret-like files; passes `zipfile.ZipFile.testzip()`. Build into two independent temporary roots and compare ZIP SHA-256 digests.
- [ ] **Step 2: Confirm RED.** Run bundled Python `-m unittest tests/test_release.py -v`; expect import failure.
- [ ] **Step 3: Implement release builder.** Copy only `skills/<expected-slug>/{SKILL.md,references,agents,templates}`, `LICENSE`, and the two README sources into a new `dama-data-project-skills-v1.1.0/` folder. Keep package guide naming compatible with v1.0.0: source `README.zh.md` becomes package `README.md`; source `README.md` becomes package `README.en.md`. Write `MANIFEST.json` with `version: 1.1.0`, 17 skill names, 102 template file count, and exclusions; write `VALIDATION.md` with checks actually performed by the builder; write `SHA256SUMS` for all package files except itself. Create ZIP entries in lexical order with fixed timestamps and normalized permissions. Write the adjacent `.zip.sha256` in the same format as v1.0.0. Refuse to overwrite an existing target directory or ZIP, so a failed experiment cannot destroy a previous release.

```python
from __future__ import annotations
from hashlib import sha256
import json
from pathlib import Path
import shutil
import tempfile
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED
from scripts.validate_skill_suite import EXPECTED_SKILLS, validate_suite

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_NAME = "dama-data-project-skills-v1.1.0"
TEMPLATE_NAMES = (
    "delivery-pack.zh.md", "delivery-pack.en.md",
    "report.zh.docx", "report.en.docx",
    "register.zh.xlsx", "register.en.xlsx",
)

def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()

def build_release(output_root: Path, release_date: str = "2026-09-24") -> Path:
    output_root.mkdir(parents=True, exist_ok=True)
    package = output_root / PACKAGE_NAME
    archive = output_root / f"{PACKAGE_NAME}.zip"
    checksum = output_root / f"{PACKAGE_NAME}.zip.sha256"
    if any(path.exists() for path in (package, archive, checksum)):
        raise FileExistsError("v1.1.0 release already exists")
    errors = validate_suite(ROOT / "skills")
    if errors:
        raise ValueError("; ".join(errors))
    with tempfile.TemporaryDirectory(dir=output_root) as temporary:
        staging = Path(temporary)
        draft = staging / PACKAGE_NAME
        draft.mkdir()
        shutil.copyfile(ROOT / "LICENSE", draft / "LICENSE")
        shutil.copyfile(ROOT / "README.zh.md", draft / "README.md")
        shutil.copyfile(ROOT / "README.md", draft / "README.en.md")
        for slug in EXPECTED_SKILLS:
            source = ROOT / "skills" / slug
            target = draft / "skills" / slug
            target.mkdir(parents=True)
            shutil.copyfile(source / "SKILL.md", target / "SKILL.md")
            for dirname in ("references", "agents"):
                for item in sorted((source / dirname).glob("*.md" if dirname == "references" else "*.yaml")):
                    destination = target / dirname
                    destination.mkdir(exist_ok=True)
                    shutil.copyfile(item, destination / item.name)
            destination = target / "templates"
            destination.mkdir()
            for filename in TEMPLATE_NAMES:
                shutil.copyfile(source / "templates" / filename, destination / filename)
        manifest = {
            "name": "dama-data-project-skills", "version": "1.1.0",
            "release_date": release_date, "skill_count": len(EXPECTED_SKILLS),
            "template_file_count": len(EXPECTED_SKILLS) * len(TEMPLATE_NAMES),
            "skills": sorted(EXPECTED_SKILLS),
            "excluded": ["DMBOK source book", "dmbok/", "tmp/"],
        }
        (draft / "MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (draft / "VALIDATION.md").write_text(
            "# Release validation / 发布验证\n\n"
            "The builder checked all 17 skills and 102 template files. "
            "The source book is excluded. / 构建器检查了 17 个技能与 102 个模板文件；原书未打包。\n",
            encoding="utf-8",
        )
        files = sorted(path for path in draft.rglob("*") if path.is_file())
        (draft / "SHA256SUMS").write_text(
            "".join(f"{digest(path)}  {path.relative_to(draft).as_posix()}\n" for path in files),
            encoding="utf-8",
        )
        draft_zip = staging / archive.name
        with ZipFile(draft_zip, "w") as zipped:
            for path in sorted(item for item in draft.rglob("*") if item.is_file()):
                info = ZipInfo(f"{PACKAGE_NAME}/{path.relative_to(draft).as_posix()}", (1980, 1, 1, 0, 0, 0))
                info.compress_type = ZIP_DEFLATED
                info.external_attr = 0o644 << 16
                zipped.writestr(info, path.read_bytes())
        if ZipFile(draft_zip).testzip() is not None:
            raise ValueError("ZIP member failed CRC test")
        draft.rename(package)
        shutil.copyfile(draft_zip, archive)
        checksum.write_text(f"{digest(archive)}  {archive.name}\n", encoding="utf-8")
    return package
```
- [ ] **Step 4: Confirm GREEN.** Run release tests and `unzip -t` on the generated test ZIP. After tests pass, run `python3 -c 'from pathlib import Path; from scripts.build_release import build_release; print(build_release(Path("dist")))'` once. Compare the v1.0.0 ZIP SHA-256 before and after; expect unchanged. Commit release builder, tests and new v1.1.0 artifacts with message `Package template-enabled v1.1.0 release`.

### Task 6: Mirror the new docs and update the landing page

**Files:**
- Modify: `scripts/render_site_docs.py`
- Modify: `tests/test_site_docs.py`, `tests/test_landing_page.py`
- Modify: `dist/index.html`
- Create: `dist/site-docs/v1.1.0/` generated HTML pages

**Interfaces:**
- Consumes: v1.1.0 package from Task 5.
- Produces: v1.1.0 Markdown mirrors and downloadable Office links while old `dist/site-docs/` pages remain available.

- [ ] **Step 1: Write failing site tests.** Point `PACKAGE_ROOT` in tests at the v1.1.0 directory and `DOCS_ROOT` at `dist/site-docs/v1.1.0`; compare the number of HTML pages dynamically with packaged Markdown count rather than the old constant 40. Assert a template page links to its `report.zh.docx` and `register.zh.xlsx` under the v1.1.0 package. Assert landing-page download targets v1.1.0 and both language guide links target its mirrors.
- [ ] **Step 2: Confirm RED.** Run `python3 -m unittest tests/test_site_docs.py tests/test_landing_page.py -v`; expect the new-version checks to fail.
- [ ] **Step 3: Parameterize the renderer.** Set `PACKAGE_ROOT = DIST_ROOT / "dama-data-project-skills-v1.1.0"` and `DOCS_ROOT = DIST_ROOT / "site-docs/v1.1.0"`; update `relative_url`, `rewrite_local_href`, guide links, version labels, and language detection so `*.en.md` uses `lang="en"` and `*.zh.md` uses `lang="zh-CN"`. Keep local non-Markdown hrefs as downloadable package paths. The path calculation must account for `v1.1.0` being one level deeper than the old mirror; replace the corresponding constants/function with:

```python
VERSION = "1.1.0"
PACKAGE_ROOT = DIST_ROOT / f"dama-data-project-skills-v{VERSION}"
DOCS_REL = PurePosixPath("site-docs") / f"v{VERSION}"
DOCS_ROOT = DIST_ROOT / DOCS_REL

def relative_url(target: PurePosixPath, current_output: PurePosixPath) -> str:
    if target.parts[:2] == DOCS_REL.parts:
        target_from_mirror = PurePosixPath(*target.parts[2:])
    else:
        target_from_mirror = PurePosixPath("../..") / target
    relative = posixpath.relpath(
        target_from_mirror.as_posix(), start=current_output.parent.as_posix()
    )
    return quote(relative, safe="/-._~")
```

Use `DOCS_REL / PurePosixPath(source_target).with_suffix(".html")` for Markdown links, `DOCS_REL / "README.html"` and `DOCS_REL / "README.en.html"` for guide links, and `language = "en" if relative_source.name.endswith(".en.md") else "zh-CN"`. Replace hard-coded `1.0.0` labels in the page shell with `VERSION`. Remove the outdated footer phrase “独立制作 · 项目化重组” from newly generated docs.
- [ ] **Step 4: Update landing links.** Change only current-release ZIP, checksum, guide, validation and router links, plus displayed version labels, from v1.0.0 to v1.1.0. Add a small bilingual template-discovery link in the Install section to the router's new `delivery-pack.en.html` and `delivery-pack.zh.html` mirrors. Preserve the GitHub Star invitation and existing default English behavior.
- [ ] **Step 5: Generate, verify and commit.** Run `python3 scripts/render_site_docs.py`, then the site tests, landing tests, and a read-only check that all new HTML local hrefs resolve. Review representative English/Chinese template pages at desktop and narrow widths if browser policy allows; if blocked, report the limitation and use HTML/CSS structure checks. Commit with message `Publish v1.1.0 template documentation`.

### Task 7: Final quality gate and handoff

**Files:**
- No source edits unless a check exposes a defect.

**Interfaces:**
- Consumes: Tasks 1–6.
- Produces: verified release evidence and clean Git state.

- [ ] **Step 1: Run complete checks.** Execute `python3 scripts/validate_skill_suite.py skills`; bundled Python `-m unittest discover -s tests -v`; bundled Python `-m scripts.build_deliverable_templates --check`; `unzip -t dist/dama-data-project-skills-v1.1.0.zip`; and `shasum -a 256 -c dist/dama-data-project-skills-v1.1.0.zip.sha256`. Run `python3 scripts/render_site_docs.py` twice and compare the sorted SHA-256 list of `dist/site-docs/v1.1.0/*.html` recursively before and after; expect identical output and zero failures.
- [ ] **Step 2: Inspect Office quality.** Use the document and spreadsheet rendering workflows to visually review a Chinese and English report and workbook from the router, one control-heavy domain, and one analytical domain. Confirm editing, print layout, fonts, wrapping, worksheet labels and blank-field affordances; fix any issues and rerun checks.
- [ ] **Step 3: Verify content and source exclusions.** Inspect a representative copied skill directory, `MANIFEST.json`, ZIP listing, README links, and website download. Search the ZIP listing for `dmbok`, `tmp`, `.pdf`, and `.DS_Store`; expect none. Check `git diff --check` and `git status --short`.
- [ ] **Step 4: Report release path, checksums, test results and any browser-visual limitation.** Push or publish only if the user explicitly asks or the current task's authorization still clearly includes updating the existing public repository.
