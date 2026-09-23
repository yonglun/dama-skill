# Release validation / 发布验证

Version: `1.0.0`  
Release date: `2026-09-23`

## Source-suite evidence

This release packages the 17 skill directories from the audited source suite. The source completion audit records these checks on 2026-09-23:

- 17/17 skills passed the official `quick_validate.py` structure check.
- `python3 scripts/validate_skill_suite.py skills` passed the suite-specific structure, naming, chapter coverage, and relative-link checks.
- `python3 -m unittest tests/test_validate_skill_suite.py` passed all 5 tests.
- All 17 skills have individual behavior-evaluation reports; three cross-domain integration evaluations and 14 discovery-boundary cases were also completed.
- The integration evaluations reported no skill-level P0/P1/P2 gaps. They do not establish legal, operational, or business correctness for a recipient's specific project.

The detailed evidence and limitations are in the source repository at `evals/skill-suite/completion-audit.md`. The source audit notes that the baseline already covered its nine general dimensions; this release makes no claim of a measured coverage increase.

## Release-package checks

Before distribution, verify that:

- The package contains exactly the 17 skill directories listed in `MANIFEST.json`.
- Each directory retains its complete `SKILL.md`, `references/`, and `agents/` content.
- The archive passes `unzip -t`, and all package-local Markdown links resolve.
- The package includes the Apache License 2.0 text in `LICENSE`.
- The original DMBOK PDF is not included.

SHA-256 checksums are provided in `SHA256SUMS` and alongside the ZIP archive. To verify the ZIP checksum on macOS or Linux, run:

```sh
shasum -a 256 -c dama-data-project-skills-v1.0.0.zip.sha256
```

## 源套件验证证据

本版本打包自已完成审计的 17 个技能目录。源仓库的完成审计记录了 2026-09-23 的以下检查：

- 17/17 个技能通过官方 `quick_validate.py` 结构检查。
- `python3 scripts/validate_skill_suite.py skills` 通过套件结构、命名、章节覆盖和相对链接检查。
- `python3 -m unittest tests/test_validate_skill_suite.py` 的 5 项测试全部通过。
- 17 个技能各有独立行为评测报告；另完成 3 项跨域集成评测和 14 个发现边界情境。
- 集成评测未发现技能级 P0/P1/P2 缺口。这不代表接收方具体项目的法律、运营或业务正确性已经得到验证。

详细证据与限制见源仓库 `evals/skill-suite/completion-audit.md`。源审计说明基线在九项通用维度上本已全部覆盖，因此本版本不声称测得覆盖率提升。

## 发布包检查

分发前需确认：

- 包内恰好包含 `MANIFEST.json` 列出的 17 个技能目录。
- 每个目录均保留完整的 `SKILL.md`、`references/` 和 `agents/` 内容。
- 压缩包通过 `unzip -t`，且包内 Markdown 链接均可解析。
- 发布包包含 `LICENSE` 中的 Apache License 2.0 正文。
- 未包含原始 DMBOK PDF。

SHA-256 校验值见 `SHA256SUMS` 和 ZIP 旁的校验文件。在 macOS 或 Linux 上可运行：

```sh
shasum -a 256 -c dama-data-project-skills-v1.0.0.zip.sha256
```
