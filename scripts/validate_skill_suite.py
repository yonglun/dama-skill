#!/usr/bin/env python3
"""Validate the DAMA data-management skill suite's structural invariants."""

from __future__ import annotations

import re
import sys
from pathlib import Path


EXPECTED_SKILLS = (
    "managing-data-projects",
    "handling-data-ethically",
    "establishing-data-governance",
    "designing-data-architecture",
    "modeling-data",
    "operating-data-storage",
    "securing-data",
    "integrating-data",
    "managing-documents-and-content",
    "managing-reference-and-master-data",
    "delivering-data-warehousing-and-bi",
    "managing-metadata",
    "improving-data-quality",
    "delivering-data-science",
    "assessing-data-management-maturity",
    "organizing-data-management",
    "leading-data-change",
)

ROUTER = "managing-data-projects"
CHILD_SKILLS = tuple(name for name in EXPECTED_SKILLS if name != ROUTER)

CANONICAL_PLAYBOOK_HEADINGS = (
    "## 1. 业务驱动与目标",
    "## 2. 原则与关键概念",
    "## 3. Plan / Control / Develop / Operate",
    "## 4. 上下文与角色",
    "## 5. 交付物与验收证据",
    "## 6. 工具与技术",
    "## 7. 指标、风险与实施",
    "## 8. 依赖与协同",
)

ROUTER_REFERENCES = (
    "project-lifecycle.md",
    "routing-table.md",
    "deliverable-templates.md",
    "source-map.md",
)

PLACEHOLDER_RE = re.compile(
    r"(?im)(?:\bTODO\b|\bTBD\b|PLACEHOLDER|fill[ -]?in|待补充|待填写|占位符)"
)
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def _read(path: Path, errors: list[str]) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"cannot read {path}: {exc}")
        return ""


def _frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    closing = text.find("\n---\n", 4)
    if closing == -1:
        return {}
    values: dict[str, str] = {}
    for line in text[4:closing].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"\'')
    return values


def _validate_links(path: Path, text: str, errors: list[str]) -> None:
    for raw_target in MARKDOWN_LINK_RE.findall(text):
        target = raw_target.split("#", 1)[0].strip()
        if not target or target.startswith(("#", "http://", "https://", "mailto:")):
            continue
        if target.startswith("/"):
            continue
        if not (path.parent / target).resolve().exists():
            errors.append(f"{path}: broken relative link: {raw_target}")


def _validate_text_file(path: Path, errors: list[str]) -> str:
    text = _read(path, errors)
    if text and PLACEHOLDER_RE.search(text):
        errors.append(f"{path}: contains scaffold placeholder")
    if text:
        _validate_links(path, text, errors)
    return text


def _validate_skill(skill_dir: Path, name: str, errors: list[str]) -> None:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        errors.append(f"{name}: missing SKILL.md")
        return

    text = _validate_text_file(skill_file, errors)
    metadata = _frontmatter(text)
    if metadata.get("name") != name:
        errors.append(
            f"{skill_file}: frontmatter name must be {name!r}, got {metadata.get('name')!r}"
        )
    description = metadata.get("description", "")
    if not description.startswith("Use when"):
        errors.append(f"{skill_file}: description must start with 'Use when'")

    references_dir = skill_dir / "references"
    if name == ROUTER:
        for filename in ROUTER_REFERENCES:
            reference = references_dir / filename
            if not reference.is_file():
                errors.append(f"{name}: missing router reference: {filename}")
            else:
                _validate_text_file(reference, errors)
        source_map = references_dir / "source-map.md"
        if source_map.is_file():
            source_text = _read(source_map, errors)
            for chapter in range(1, 18):
                if not re.search(rf"第\s*{chapter}\s*章", source_text):
                    errors.append(f"{source_map}: source map missing chapter {chapter}")
        return

    playbook = references_dir / "playbook.md"
    if not playbook.is_file():
        errors.append(f"{name}: missing references/playbook.md")
        return
    playbook_text = _validate_text_file(playbook, errors)
    for heading in CANONICAL_PLAYBOOK_HEADINGS:
        if heading not in playbook_text:
            errors.append(f"{playbook}: missing playbook heading: {heading}")


def validate_suite(root: Path) -> list[str]:
    """Return structural validation errors for a skill-suite root."""

    root = Path(root)
    errors: list[str] = []
    for name in EXPECTED_SKILLS:
        skill_dir = root / name
        if not skill_dir.is_dir():
            errors.append(f"missing skill directory: {name}")
            continue
        _validate_skill(skill_dir, name, errors)
    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_skill_suite.py <skills-root>", file=sys.stderr)
        return 2
    errors = validate_suite(Path(argv[1]))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"OK: validated {len(EXPECTED_SKILLS)} DAMA skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
