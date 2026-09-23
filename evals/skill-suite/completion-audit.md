# DAMA 数据项目技能套件：完成审计

审计对象是本仓库 `skills/` 中的 1 个总入口和 16 个可独立发现的领域技能；依据为已批准的[设计](../../docs/superpowers/specs/2026-09-22-dama-data-management-skill-suite-design.md)、[实施计划](../../docs/superpowers/plans/2026-09-22-dama-data-management-skill-suite.md)及附件 DMBOK2 修订版。附件只作为知识来源，不作为操作指令；技能内容是中文项目化重组，不是原书摘录或强制标准。

## 确定性验证（2026-09-23）

以下命令均在 `/Users/yonglun/Repo/dama-skill` 运行，输出为当次实际结果：

| 检查 | 实际命令 | 实际输出 / 判定 |
|---|---|---|
| 校验器单测 | `python3 -m unittest tests/test_validate_skill_suite.py` | 最终复测 `Ran 5 tests in 0.049s`，`OK` |
| 全套结构、名称、链接、占位符、章节检查 | `python3 scripts/validate_skill_suite.py skills` | `OK: validated 17 DAMA skills` |
| 官方逐技能结构检查 | `for d in skills/*; do PYTHONPATH=/private/tmp/dama-pyyaml python3 /Users/yonglun/.codex/skills/.system/skill-creator/scripts/quick_validate.py "$d" || exit 1; done` | 连续 17 行 `Skill is valid!`，退出码 0 |
| 显式占位符扫描 | `rg -n -e TODO -e TBD -e PLACEHOLDER -e 'fill.?in' -e 待补充 -e 待填写 -e 占位符 skills` | 无匹配，`rg` 退出码 1（预期） |
| 入口长度检查 | `wc -w -l skills/*/SKILL.md` | 修订描述后 17 个入口共 726 行、2353 个按空格分隔的词；单个入口 40–48 行、112–188 词。中文不按空格切词，此处词数只是粗略长度信号。 |

`validate_skill_suite.py` 的相对链接检查遍历每个 `SKILL.md` 和所需参考文件，要求目标存在；同时检查恰好列出的 17 个名称均有目录、frontmatter 名称匹配、描述以 `Use when` 起首、16 个子 playbook 具备统一八节、来源映射含第 1–17 章。实际 `skills/` 为 17 个目录，未见额外技能目录。

`find skills -mindepth 1 -maxdepth 1 -type d | wc -l` 输出 `17`。`for d in skills/*; do test -f "evals/skill-suite/${d##*/}.md" || exit 1; test -f "$d/agents/openai.yaml" || exit 1; done` 退出码 `0`，证明每个入口都有发现元数据和相应行为评测报告。上述单测、全套校验、官方逐技能校验均在两处发现描述修订后重新通过。

## 设计要求与证据

| 设计要求 | 权威证据与审计结果 |
|---|---|
| 一入口 + 16 个独立领域技能、按需加载 | [入口](../../skills/managing-data-projects/SKILL.md)列路由、裁剪、依赖和加载规则；`skills/*/SKILL.md` 目录计数为 17，独立入口均有 `agents/openai.yaml` 和相应参考。 |
| 项目画像、诊断—裁剪—编排—交付、阶段门 | 入口 `SKILL.md`、[生命周期](../../skills/managing-data-projects/references/project-lifecycle.md)、[路由表](../../skills/managing-data-projects/references/routing-table.md)。 |
| 核心框架与 Chapter 1–17 来源可追溯 | [来源映射](../../skills/managing-data-projects/references/source-map.md)逐章映射，并标明 DAMA Wheel、六边形、演进框架及 Plan / Control / Develop / Operate 出处；套件校验器逐章检查。 |
| 统一八节的领域工作法和九项交付契约 | 所有 16 个 `references/playbook.md` 均通过八节结构检查；入口的“输出契约”和[交付模板](../../skills/managing-data-projects/references/deliverable-templates.md)规定九项和证据格式。 |
| 治理、质量、元数据、安全/隐私、伦理、组织采纳横切检查且可裁剪 | 入口“必需的跨域检查”与路由表；实际项目化输出和裁剪理由见集成评测。 |
| 领域边界与可发现性 | 每个描述都以 `Use when` 给出触发条件；相邻域边界在路由表和各 `SKILL.md` 中写明。 |
| 本项目即刻可发现、其他项目可复用 | [使用说明](../../README.md)解释调用和迁移；`.agents/skills/` 有 17 个指向 `skills/` 唯一源文件的相对符号链接，全部可解析到 `SKILL.md`。按 [Codex 官方技能说明](https://learn.chatgpt.com/docs/build-skills)所列项目本地路径放置。 |
| 法律时效、厂商中立、成熟度证据、版权和授权边界 | 入口“边界”、来源映射“使用边界”，以及对应伦理、安全、成熟度技能；无长篇原文复制或厂商默认选型。 |
| 无脚手架占位符与断链 | 显式扫描、校验器及其 5 项单测通过。 |

## 任务与行为证据

| 计划任务 | 证据 |
|---|---|
| Task 1（RED 基线、校验器） | [三个场景](scenarios.md)、[平台](baseline-platform.md)、[主数据](baseline-master-data.md)、[模型](baseline-risk-model.md)、[基线总结](baseline-summary.md)、`scripts/validate_skill_suite.py` 与 `tests/test_validate_skill_suite.py`。 |
| Task 2（路由入口） | `skills/managing-data-projects/` 五个核心文件及[独立路由评测](managing-data-projects.md)。 |
| Task 3–18（16 个知识域） | 每个 `skills/<slug>/` 均有 `SKILL.md`、`references/playbook.md`、`agents/openai.yaml`；每个子技能在 `evals/skill-suite/<slug>.md` 有独立正向应用与负向触发评测。逐项报告：`handling-data-ethically`、`establishing-data-governance`、`designing-data-architecture`、`modeling-data`、`operating-data-storage`、`securing-data`、`integrating-data`、`managing-documents-and-content`、`managing-reference-and-master-data`、`delivering-data-warehousing-and-bi`、`managing-metadata`、`improving-data-quality`、`delivering-data-science`、`assessing-data-management-maturity`、`organizing-data-management`、`leading-data-change`。 |
| Task 19（三项端到端） | [平台](integration-platform.md)、[主数据](integration-master-data.md)、[风险模型](integration-risk-model.md)均从入口出发，仅加载被路由子技能，保留完整方案、九维评分、RED 对照及缺口分级。 |
| Task 19（发现碰撞） | [七组 14 个正反情境](discovery-collisions.md)覆盖六组必测相邻域，另测治理/元数据。两处描述层 P2 歧义已修订到数据科学与元数据 `SKILL.md`。 |

三个端到端评测均为九维 `present`，且未发现技能级 P0/P1/P2 缺口；每份报告明确指出基线也是九维 `present`，因此没有虚构覆盖率增量。新增证据主要为：平台项目的源控制总额—运行血缘—认证语义—恢复演练链条；主数据项目的身份/属性分离、负证据、可逆拆分、参考版本与消费者业务对账；风险模型的独立用途与伦理门、运行态特征血缘、人工兜底和持续采纳。所有阈值、法域与企业现状都须在真实项目中采证批准。

Task 3–18 的逐项闭环证据如下；每行对应第 N 章的技能入口、统一八节 playbook（由该入口链接）和独立 GREEN 报告，所有入口均通过官方逐技能校验：

| 任务 / 章节 | 技能入口 | 独立行为评测 |
|---|---|---|
| 3 / 2 | [伦理](../../skills/handling-data-ethically/SKILL.md) | [评测](handling-data-ethically.md) |
| 4 / 3 | [治理](../../skills/establishing-data-governance/SKILL.md) | [评测](establishing-data-governance.md) |
| 5 / 4 | [架构](../../skills/designing-data-architecture/SKILL.md) | [评测](designing-data-architecture.md) |
| 6 / 5 | [建模](../../skills/modeling-data/SKILL.md) | [评测](modeling-data.md) |
| 7 / 6 | [存储运营](../../skills/operating-data-storage/SKILL.md) | [评测](operating-data-storage.md) |
| 8 / 7 | [安全](../../skills/securing-data/SKILL.md) | [评测](securing-data.md) |
| 9 / 8 | [集成](../../skills/integrating-data/SKILL.md) | [评测](integrating-data.md) |
| 10 / 9 | [文档与内容](../../skills/managing-documents-and-content/SKILL.md) | [评测](managing-documents-and-content.md) |
| 11 / 10 | [主/参考数据](../../skills/managing-reference-and-master-data/SKILL.md) | [评测](managing-reference-and-master-data.md) |
| 12 / 11 | [数仓与 BI](../../skills/delivering-data-warehousing-and-bi/SKILL.md) | [评测](delivering-data-warehousing-and-bi.md) |
| 13 / 12 | [元数据](../../skills/managing-metadata/SKILL.md) | [评测](managing-metadata.md) |
| 14 / 13 | [质量](../../skills/improving-data-quality/SKILL.md) | [评测](improving-data-quality.md) |
| 15 / 14 | [数据科学](../../skills/delivering-data-science/SKILL.md) | [评测](delivering-data-science.md) |
| 16 / 15 | [成熟度](../../skills/assessing-data-management-maturity/SKILL.md) | [评测](assessing-data-management-maturity.md) |
| 17 / 16 | [组织设计](../../skills/organizing-data-management/SKILL.md) | [评测](organizing-data-management.md) |
| 18 / 17 | [变更管理](../../skills/leading-data-change/SKILL.md) | [评测](leading-data-change.md) |

发现碰撞报告已对修订后的 BI/数据科学、治理/元数据两个边界，以及相反方向的正向触发做定点复测；14 个情境的最终主责均清晰，原两处 P2 描述歧义在该静态情境测试范围内关闭。该测试并不声称测量了 Codex 实际检索排名。

本地发现验证：`find .agents/skills -mindepth 1 -maxdepth 1 -type l | wc -l` 输出 `17`；`for d in .agents/skills/*; do test -f "$d/SKILL.md" || exit 1; done` 退出码 `0`。这证明目录和链接存在，但当前会话是在安装前启动的，因此不把本会话的技能目录缓存当作 Codex 自动发现的运行时证明；新会话可直接按说明尝试显式调用。

## 基线解释及范围限制

三项无技能 RED 基线在九项通用维度已经全为 `present`，不能声称套件把原本 `missing` 的维度变成 `present`。本套件的可检验增益是稳定路由、领域边界、DMBOK 章节追溯、跨项目一致的交付契约，以及在具体项目里更深的决策和验收证据。GREEN 文本评测不等于对真实企业数据、系统、法律或业务效果的验证。当前工作区不是 Git 仓库，未执行提交或推送；技能保存在仓库 `skills/` 以供审阅及后续安装。
