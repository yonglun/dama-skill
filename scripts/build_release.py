#!/usr/bin/env python3
"""Build a deterministic, source-book-free v1.1.0 DAMA skill release."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import shutil
import tempfile
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

from scripts.validate_skill_suite import EXPECTED_SKILLS, TEMPLATE_FILES, validate_suite


ROOT = Path(__file__).resolve().parents[1]
PACKAGE_NAME = "dama-data-project-skills-v1.1.0"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _copy_file(source: Path, destination: Path) -> None:
    if source.is_symlink() or not source.is_file():
        raise ValueError(f"release source is not a regular file: {source}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)


def _copy_guide(source: Path, destination: Path, old_link: str, new_link: str) -> None:
    if source.is_symlink() or not source.is_file():
        raise ValueError(f"release guide is not a regular file: {source}")
    content = source.read_text(encoding="utf-8")
    if old_link not in content:
        raise ValueError(f"release guide link not found: {old_link}")
    content = content.replace(old_link, new_link)
    content = content.replace(
        "](evals/skill-suite/completion-audit.md)",
        "](https://github.com/yonglun/dama-skill/blob/main/evals/skill-suite/completion-audit.md)",
    )
    destination.write_text(content, encoding="utf-8", newline="\n")


def build_release(output_root: Path, release_date: str = "2026-09-24") -> Path:
    output_root = Path(output_root)
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
        _copy_file(ROOT / "LICENSE", draft / "LICENSE")
        _copy_guide(ROOT / "README.zh.md", draft / "README.md", "[English README](README.md)", "[English README](README.en.md)")
        _copy_guide(ROOT / "README.md", draft / "README.en.md", "[中文 README](README.zh.md)", "[中文 README](README.md)")
        for slug in EXPECTED_SKILLS:
            source = ROOT / "skills" / slug
            target = draft / "skills" / slug
            _copy_file(source / "SKILL.md", target / "SKILL.md")
            for dirname, pattern in (("references", "*.md"), ("agents", "*.yaml")):
                for item in sorted((source / dirname).glob(pattern)):
                    _copy_file(item, target / dirname / item.name)
            for filename in TEMPLATE_FILES:
                _copy_file(source / "templates" / filename, target / "templates" / filename)

        manifest = {
            "name": "dama-data-project-skills", "version": "1.1.0",
            "release_date": release_date, "skill_count": len(EXPECTED_SKILLS),
            "template_file_count": len(EXPECTED_SKILLS) * len(TEMPLATE_FILES),
            "skills": sorted(EXPECTED_SKILLS),
            "excluded": ["DMBOK source book", "dmbok/", "tmp/"],
        }
        (draft / "MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (draft / "VALIDATION.md").write_text(
            "# Release validation / 发布验证\n\n"
            "The release builder checked all 17 skill directories and all 102 required template files. "
            "The copyrighted source book is excluded.\n\n"
            "构建器检查了全部 17 个技能目录与 102 个必需模板文件；有版权的原书未打包。\n",
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
        with ZipFile(draft_zip) as zipped:
            if zipped.testzip() is not None:
                raise ValueError("ZIP member failed CRC test")
        draft.rename(package)
        shutil.copyfile(draft_zip, archive)
        checksum.write_text(f"{digest(archive)}  {archive.name}\n", encoding="utf-8")
    return package


if __name__ == "__main__":
    print(build_release(ROOT / "dist"))
