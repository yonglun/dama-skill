# 数据管理领域路由表

## 路由方法

先选择一个直接产生业务结果的 **主技能**，再增加确有风险或依赖的基础/支持技能。一个项目可以有多个主技能，但必须说明边界，避免每个团队都对同一工件负责。

## 按项目场景路由

| 场景或信号 | 主技能 | 常见基础/支持技能 | 关键依赖顺序 |
|---|---|---|---|
| 企业数据战略、跨域路线图、项目组合 | `managing-data-projects` | `assessing-data-management-maturity`, `establishing-data-governance`, `organizing-data-management`, `leading-data-change` | 结果与现状 → 决策权与组织 → 路线图 → 采纳 |
| 治理委员会、所有权、政策、标准、术语争议 | `establishing-data-governance` | `organizing-data-management`, `managing-metadata`, `leading-data-change` | 决策范围 → 角色 → 流程/工件 → 嵌入运营 |
| 当前/目标数据蓝图、能力与迁移路线 | `designing-data-architecture` | `modeling-data`, `securing-data`, `managing-metadata`, `integrating-data` | 原则/需求 → 视图 → 过渡态 → 合规审查 |
| 概念、逻辑或物理数据结构 | `modeling-data` | `designing-data-architecture`, `managing-metadata`, `improving-data-quality` | 业务语义 → 模型层级 → 物理实现 → 模型治理 |
| 数据库、存储、备份、恢复、容量、运行可靠性 | `operating-data-storage` | `securing-data`, `managing-metadata`, `improving-data-quality` | 服务目标 → 物理设计 → 运行控制 → 监控改进 |
| 分类分级、访问、加密、审计、泄露风险 | `securing-data` | `handling-data-ethically`, `establishing-data-governance`, `managing-metadata` | 数据/用途分类 → 控制设计 → 测试 → 持续复核 |
| ETL/ELT、API、流处理、交换、互操作、对账 | `integrating-data` | `designing-data-architecture`, `managing-metadata`, `improving-data-quality`, `securing-data` | 契约 → 映射/设计 → 构建 → 血缘/对账/监控 |
| 合同、邮件、档案、网页等非结构化内容 | `managing-documents-and-content` | `managing-metadata`, `securing-data`, `establishing-data-governance` | 盘点/分类 → 生命周期规则 → 发布/检索 → 保留处置 |
| 客户/产品/供应商黄金记录、代码表、层级 | `managing-reference-and-master-data` | `improving-data-quality`, `establishing-data-governance`, `integrating-data`, `managing-metadata` | 域/权威源 → 身份与规则 → 管理工作流 → 分发对账 |
| 数仓、数据集市、指标、语义层、报表、自助 BI | `delivering-data-warehousing-and-bi` | `modeling-data`, `integrating-data`, `managing-metadata`, `improving-data-quality` | 决策需求 → 模型/语义 → 数据供应 → 验收与采纳 |
| 目录、术语、技术元数据、血缘、影响分析 | `managing-metadata` | `establishing-data-governance`, `designing-data-architecture` | 用例 → 最小元数据 → 采集/治理 → 检索/影响分析 |
| 重复、缺失、无效、不一致、质量记分卡 | `improving-data-quality` | `establishing-data-governance`, `managing-metadata`; 主数据问题再加 `managing-reference-and-master-data` | 定义适用质量 → 基线 → 根因 → 预防/纠正 → 监控 |
| 预测、评分、实验、模型上线与监控 | `delivering-data-science` | `handling-data-ethically`, `securing-data`, `managing-metadata`, `improving-data-quality`, `leading-data-change` | 用途/假设 → 数据与控制 → 实验 → 部署门 → 监控退役 |
| 能力盘点、等级评分、改进优先级 | `assessing-data-management-maturity` | `managing-data-projects`, `organizing-data-management` | 评估目的 → 证据 → 当前/目标差距 → 改进组合 |
| CDO/数据办公室、集中或联邦组织、RACI | `organizing-data-management` | `establishing-data-governance`, `leading-data-change` | 现状参与者 → 模式选择 → 角色互动 → 能力建设 |
| 低采纳、抵触、培训、沟通、文化改变 | `leading-data-change` | 对应主领域技能, `organizing-data-management` | 利益相关者/准备度 → 联盟/愿景 → 参与支持 → 采纳巩固 |
| 新用途、二次使用、偏差、公平、潜在伤害 | `handling-data-ethically` | `securing-data`, `establishing-data-governance`, `delivering-data-science` | 目的与受影响方 → 伤害/权利 → 限制与决策 → 持续观察 |

## 相邻技能边界

- **治理 vs 组织：** 治理定义决策和控制如何运作；组织定义谁以何种结构承担职责。
- **治理 vs 变更：** 治理建立制度；变更让人理解、采用并持续执行制度。
- **架构 vs 建模：** 架构组织企业级能力、系统和数据流；建模定义数据语义和结构。
- **安全 vs 伦理：** 安全判断如何保护数据；伦理判断某种用途是否应当发生以及如何限制伤害。
- **质量 vs 主数据：** 质量适用于任何数据的适用性；主数据管理负责共享核心实体的权威身份、规则和分发。
- **集成 vs 存储：** 集成负责系统间移动与一致；存储运营负责持久化服务的可靠运行。
- **BI vs 数据科学：** BI 主要支持已定义指标和可重复决策；数据科学以假设、统计/机器学习模型和不确定性为核心。

## 最小完备检查

选完技能后，回答：

1. 谁拥有数据与关键决策？
2. 什么数据质量足以支持该用途？
3. 如何追溯含义、来源、转换和影响？
4. 如何保护数据，且该用途是否合宜？
5. 谁运行、监控、处理异常和批准变更？
6. 用户如何采用，何时停止或退役？

任何问题无答案时，增加相应技能或明确记录风险与后续触发条件。
