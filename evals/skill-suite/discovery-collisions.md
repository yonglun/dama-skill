# 技能发现碰撞评测：七组相邻领域

## 方法与判定标准

独立阅读全部 17 个 `skills/*/SKILL.md` 的 frontmatter `description`，再读取[总入口路由表](../../skills/managing-data-projects/references/routing-table.md)及下列相邻技能正文的「适用边界」。对每个输入先作**描述层候选判断**，再按路由表确定**实际主技能**、必要支持技能和明确不应作为主技能的邻居。这里的「不触发」指场景没有独立工作包时不加载该技能，不禁止后续因新风险补充。此项是情境化发现/路由静态测试，不是对 Codex 搜索排序算法的运行时测量。

判定规则：主技能必须直接交付情境所求结果；支持技能只处理具名依赖或独立风险；若两个描述都可能被搜索命中，正文及路由表仍须给出唯一可解释主责。14 个情境覆盖要求的六组正反方向，加测治理/元数据。

| 编号与测试输入 | 描述层候选 → 实际判定 | 可选支持；明确不作为主技能 | 证据与结果 |
|---|---|---|---|
| G1：三个事业部争议“客户”的正式定义，需决定最终批准人、争议升级和例外规则。 | 治理、组织、元数据 → `establishing-data-governance` | 元数据负责发布获批定义；若角色结构需重设再加组织。组织、元数据不主导裁决。 | [治理描述及边界](../../skills/establishing-data-governance/SKILL.md)触发“shared decision rights / business terminology governance”；[路由表](../../skills/managing-data-projects/references/routing-table.md)把“术语争议”归治理，组织处理谁以何种结构履责。通过。 |
| O1：集团要比较集中、联邦和混合数据办公室模式，并设计编制、预算、岗位章程和跨区 RACI；尚无具体术语争议。 | 组织、治理 → `organizing-data-management` | 治理可确认决策权限；治理不主导组织结构设计。 | [组织描述及边界](../../skills/organizing-data-management/SKILL.md)列出 operating models、staffed/funded、RACI；[路由表](../../skills/managing-data-projects/references/routing-table.md)把 CDO、数据办公室、模式和 RACI 归组织。通过。 |
| A1：三套平台整合，要核实当前系统/数据流，确定目标与过渡蓝图、架构原则和迁移路线。 | 架构、建模 → `designing-data-architecture` | 建模仅细化选定主题结构；建模不主导跨系统蓝图。 | [架构描述及边界](../../skills/designing-data-architecture/SKILL.md)覆盖 current/target/transition architecture 与 roadmap；[路由表](../../skills/managing-data-projects/references/routing-table.md)把蓝图和路线归架构。通过。 |
| M1：订单业务过程要定义实体关系、事实粒度、键、属性，以及概念—逻辑—物理模型映射。 | 建模、架构 → `modeling-data` | 架构可给标准/约束；架构不主导局部实体设计。 | [建模描述及边界](../../skills/modeling-data/SKILL.md)明确 entities、grain、keys、conceptual/logical/physical models；[路由表](../../skills/managing-data-projects/references/routing-table.md)把具体结构归建模。通过。 |
| S1：已获批用途的敏感数据集需要细分导出权限、加密、脱敏、访问审计和控制测试。 | 安全 → `securing-data` | 若发现新用途/人群伤害再加伦理；本输入不让伦理主导既定用途的控制实现。 | [安全描述及边界](../../skills/securing-data/SKILL.md)列明 access、encryption、auditability；[路由表](../../skills/managing-data-projects/references/routing-table.md)区分“如何保护”和“是否应当使用”。通过。 |
| E1：已加密且法律上可能允许的消费画像将用于差异化定价；要评估不公平影响、可选择性与申诉。 | 伦理、安全 → `handling-data-ethically` | 安全落实获批用途限制；安全不代替用途可接受性结论。 | [伦理描述及边界](../../skills/handling-data-ethically/SKILL.md)明确 legally permitted but may still cause harm；[路由表](../../skills/managing-data-projects/references/routing-table.md)把新用途、画像、公平交给伦理。通过。 |
| Q1：地址字段缺失与格式错误反复影响配送；需定义用途阈值、质量规则、根因整改和趋势监控，不重建客户身份。 | 质量 → `improving-data-quality` | 主数据无独立共享身份/权威工作，不加载；它不主导字段质量闭环。 | [质量描述及边界](../../skills/improving-data-quality/SKILL.md)覆盖 recurring errors、rules、root cause、monitoring；[路由表](../../skills/managing-data-projects/references/routing-table.md)只在主数据问题时追加 MDM。通过。 |
| R1：三套 CRM 中同一客户有不同 ID；需确立黄金记录、匹配/合并/拆分、生存规则、跨系统分发与回执。 | 主数据、质量 → `managing-reference-and-master-data` | 质量评估错误与控制；质量不主导权威身份和持续分发。 | [主数据描述及边界](../../skills/managing-reference-and-master-data/SKILL.md)明确 identity resolution、golden record、match/merge/split、survivorship；[路由表](../../skills/managing-data-projects/references/routing-table.md)把客户黄金记录归主数据。通过。 |
| I1：订单 CDC 管道迟到、乱序和重跑造成重复；需版本化契约、幂等重放、死信和源目标对账。 | 集成、存储 → `integrating-data` | 若源数据库服务不稳才加存储；存储不主导跨系统管道语义。 | [集成描述及边界](../../skills/integrating-data/SKILL.md)明确 CDC、contracts、replay、reconciliation；[路由表](../../skills/managing-data-projects/references/routing-table.md)将系统间移动/一致归集成。通过。 |
| T1：数据湖备份作业成功但从未恢复；需要 RTO/RPO 演练、容量、值班和生产运行移交，不建设新接口。 | 存储 → `operating-data-storage` | 安全可检查备份保护；集成无独立数据移动契约，不加载、不主导恢复。 | [存储描述及边界](../../skills/operating-data-storage/SKILL.md)明确 backup/recovery、capacity、operational handoff；[路由表](../../skills/managing-data-projects/references/routing-table.md)把运行可靠性归存储。通过。 |
| B1：整合两套新增销售来源，发布已定义收入指标的同比仪表盘和自助 BI 数据集；不做预测、实验或训练。 | BI；“new data sources for ... insight”也可能命中数据科学 → `delivering-data-warehousing-and-bi` | 集成处理来源接入；数据科学无模型/假设工作，不加载、不主导描述性洞察。 | [BI 描述及边界](../../skills/delivering-data-warehousing-and-bi/SKILL.md)覆盖指标、历史比较、dashboard、自助 BI；[数据科学边界](../../skills/delivering-data-science/SKILL.md)将标准报表交 BI；[路由表](../../skills/managing-data-projects/references/routing-table.md)以“已定义指标/可重复决策”判 BI。路由通过；描述层有 P2 歧义。 |
| D1：违约预测模型需定义标签时点、时间切分、校准、分群误差、独立测试、灰度上线和漂移监控。 | 数据科学、BI → `delivering-data-science` | 伦理审查受影响客户，BI 可展示获批模型结果；BI 不主导模型有效性。 | [数据科学描述及边界](../../skills/delivering-data-science/SKILL.md)明确 prediction、model evaluation、monitoring；[路由表](../../skills/managing-data-projects/references/routing-table.md)以假设/模型/不确定性判数据科学。通过。 |
| V1：两个事业部争议业务词“净收入”的正式定义与例外；要指定裁决人和批准政策，暂不建设目录。 | 治理；“reconciling conflicting definitions”也可能命中元数据 → `establishing-data-governance` | 元数据可登记并传播获批版本；元数据不拥有最终政策/定义裁决。 | [治理描述](../../skills/establishing-data-governance/SKILL.md)含 terminology governance；[元数据描述及边界](../../skills/managing-metadata/SKILL.md)含 conflicting definitions 但正文明确治理决定政策/争议；[路由表](../../skills/managing-data-projects/references/routing-table.md)把术语争议归治理。路由通过；描述层有 P2 歧义。 |
| X1：净收入定义已批准；现在需将术语、表字段、报表和血缘登记目录，监测同步、新鲜度、版本与下游影响。 | 元数据、治理 → `managing-metadata` | 治理仅处理新争议或所有权变更；不主导目录采集/维护。 | [元数据描述及边界](../../skills/managing-metadata/SKILL.md)明确 catalog、lineage、downstream change impact；[路由表](../../skills/managing-data-projects/references/routing-table.md)把目录/术语/血缘/影响分析归元数据。通过。 |

## 结果与修订建议

- 14/14 情境在读取路由表与正文边界后可解释地选中主技能，未发现 P0/P1 级主责冲突；对应的反方向情境也未把邻居误选为主技能。
- 12/14 情境的 frontmatter 触发描述足以清晰辨认主责；B1、V1 会产生合理的双候选。**P2 建议**：将 `delivering-data-science` 描述中的“combine new data sources for prediction or insight”收窄到“for hypothesis testing, prediction, or model-based insight”，避免把新增来源的描述性看板吸入数据科学。保留其实际探索/实验场景触发。
- **P2 建议**：将 `managing-metadata` 描述中的“reconciling conflicting definitions”具体为“recording and propagating approved definitions and surfacing conflicts for authoritative resolution”；最终术语争议裁决仍由 `establishing-data-governance`，元数据处理登记、差异证据与传播。
- 以上两项为发现文案的精度改进，不是运行时失败结论。本轮没有修改技能；若采纳文案修订，应针对 B1、V1 复测并重跑套件校验。

## 修订后复测

主任务采纳上述两处 P2 文案建议后，我重新读取四个相邻技能的 frontmatter，沿用同一测试输入复判；上表保留的是**修订前**发现记录，不回写历史结果。

| 情境 | 修订后的描述层判定 | 实际主技能与邻居排除 | 结论 |
|---|---|---|---|
| B1：新增销售来源，交付已定义收入指标的同比仪表盘与自助数据集，无预测/实验/训练。 | [BI 描述](../../skills/delivering-data-warehousing-and-bi/SKILL.md)直接命中 dashboard、historical comparisons、self-service BI；[数据科学描述](../../skills/delivering-data-science/SKILL.md)现在把新增来源限定于 hypothesis testing、prediction 或 model-based insight，本输入均无。描述层不再双候选。 | `delivering-data-warehousing-and-bi`；数据科学不触发，集成可支持来源接入。 | 原 B1 P2 关闭。 |
| V1：两个事业部争议“净收入”正式定义及例外，要求裁决人与政策批准，暂不建设目录。 | [治理描述](../../skills/establishing-data-governance/SKILL.md)直接命中 shared decision rights、policy/standards control、business terminology governance；[元数据描述](../../skills/managing-metadata/SKILL.md)只说记录/传播**已批准**定义或将冲突暴露给有权裁决者，不再声称负责调和或最终裁决。若需记录争议，元数据仍可成为支持候选，但不是同等主责候选。 | `establishing-data-governance`；元数据只在有目录/传播工作包时支持，不主导裁决。 | 原 V1 P2 主责歧义关闭；支持技能可选属于预期双候选，不是误触发。 |
| D1：违约预测模型，含标签时点、校准、独立测试和漂移监控。 | 修订后[数据科学描述](../../skills/delivering-data-science/SKILL.md)仍直接命中 prediction、model evaluation、production monitoring。 | `delivering-data-science`；BI 只在交付报告/可视化产品时支持，不主导模型。 | 正向触发未受损。 |
| X1：定义已批准，需将术语、字段、报表血缘入目录并维护版本/新鲜度。 | 修订后[元数据描述](../../skills/managing-metadata/SKILL.md)仍直接命中 catalog、approved definitions、lineage、downstream impact。 | `managing-metadata`；治理只处理新争议或权属决定。 | 正向触发未受损。 |

复测是基于描述与路由文本的独立情境判定，未测量实际检索排名；四项预期路由均保持正确，两处 P2 文案风险在本测试范围内关闭。主任务仍需执行最终静态校验。
