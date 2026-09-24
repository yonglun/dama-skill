---
name: managing-reference-and-master-data
description: Use when shared business entities or controlled code sets must be made authoritative across systems; when resolving customer, product, supplier, location, employee, account, hierarchy, or reference-code conflicts; or when defining identity resolution, golden-record, match/merge/split, survivorship, stewardship, publication, reconciliation, and system-of-record controls.
---

# 参考数据与主数据管理

## 核心原则

主数据描述被多个流程反复引用的业务实体，参考数据约束这些实体及交易使用的允许值、分类和层级。目标不是制造一张“最干净的表”，而是持续提供完整、一致、当前、可追溯且经业务授权的共享数据。

黄金记录是当前获批的最佳业务表示，不是永远正确的唯一真相。任何匹配、合并、拆分、属性裁决、层级或代码变化都必须保留来源、理由、规则版本、批准和可逆路径。

## 适用边界

- 跨系统实体身份、交叉引用、黄金记录、匹配/合并/拆分、属性生存规则、层级与共享发布使用本技能。
- 国家码、状态码、计量单位、分类、风险等级等受控值集的 owner、版本、生效期、映射和分发使用本技能。
- 通用完整性、准确性、及时性规则与根因整改由 `improving-data-quality` 主导；本技能负责共享实体和代码的权威裁决及持续运营。
- 接口、CDC、批流编排、重试和传输对账由 `integrating-data` 主导；本技能给出发布内容、权威来源、版本和业务对账要求。
- 业务术语、技术元数据和跨域血缘由 `managing-metadata` 主导；本技能维护实体、属性、代码、层级和来源的专门元数据。
- 单系统内一次性去重、字段修复或报表清洗，且不改变共享身份/代码权威时，不应由本技能主导。

## 工作流

1. 明确业务结果、主数据域/参考数据集、法人/地域/用途、消费者、风险和不纳入范围；任命数据 owner 与管家。
2. 阅读[参考数据与主数据项目手册](references/playbook.md)，盘点来源、消费者、业务键、源标识、实际质量、层级、代码、变更者和现有权威。
3. 为实体和代码建立语义模型、全局标识/交叉引用、系统责任和字段级权威矩阵；区分 system of record、system of entry 与 system of reference。
4. 定义标准化、候选生成、匹配特征/阈值、自动与人工裁决区、合并/拆分、生存规则和反向链接；用已标注正反例测试，优先控制误合并。
5. 建立管家队列、职责分离、争议、SLA 和升级；高影响合并、身份/层级争议及政策例外由业务 owner 决定。
6. 对参考数据实施提议、影响分析、批准、版本、生效/失效、映射、发布、弃用和紧急变更控制；禁止静默覆盖历史含义。
7. 选择 registry、consolidation、coexistence 或 transaction hub 等模式；按写入权威和业务能力选择，不由产品名称反推架构。
8. 灰度发布并按对象数、标识映射、属性/代码版本、层级、拒绝/例外和消费者确认对账；监控合并质量、漂移、队列与采用。

## 交付模板

使用 [中文交付包](templates/delivery-pack.zh.md) 或 [English delivery pack](templates/delivery-pack.en.md) 组织输出。叙述性方案和评审记录使用同目录 Word 模板；矩阵、台账和评分卡使用同目录 Excel 模板。模板中的责任、阈值、批准和证据须由实际项目确认。

## 输出契约

输出业务范围与域章程；角色/决策权；来源—消费者—权威矩阵；实体/参考模型；全局 ID 与交叉引用；黄金记录/生存规则；匹配、合并、拆分测试与回滚；层级治理；参考数据变更控制；管家工作流；发布契约、分发/回执/对账；质量与运行指标；阶段门、风险、例外和验收证据。

## 常见错误

| 错误 | 修正 |
|---|---|
| 把主数据项目当一次性清洗 | 建立持续裁决、发布、监控和源头防控 |
| 把“黄金”理解为无来源的绝对真相 | 保存源值、权威规则、置信度、时间和批准 |
| 只按姓名或单字段自动合并 | 使用多特征、负证据、已标注测试和人工裁决区 |
| 合并后删除来源身份 | 保留交叉引用、谱系和可逆拆分证据 |
| 参考表直接覆盖 | 版本化并定义生效/失效、替换和消费者迁移 |
| 所有字段都由一个系统权威 | 按域、属性、时间和用途声明权威 |
| 发布成功即消费者一致 | 用回执和业务对账验证映射、版本及拒绝项 |
