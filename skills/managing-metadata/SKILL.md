---
name: managing-metadata
description: Use when data assets, business terms, technical schemas, operational runs, ownership, lineage, or usage must be discovered and kept current across systems; when building a catalog or metadata repository, recording and propagating approved definitions or surfacing conflicts for authoritative resolution, proving report provenance, or assessing downstream change impact.
---

# 元数据管理

## 核心原则

元数据解释数据的含义、位置、结构、来源、运行状态、责任和使用限制。将其作为持续维护的产品：既从工具中采集实际实现，也由有权人员策展业务语义，并公开差异、证据、版本和新鲜度。

## 适用边界

- 跨系统目录、业务词汇表、资产/字段登记、生产与消费依赖、端到端血缘、影响分析、元数据质量和服务使用本技能。
- 单个模型内命名两个字段或局部实体结构由 `modeling-data` 处理；只有需要跨系统登记、复用或影响分析时本技能主导。
- 数据治理决定政策、owner 任命和争议裁决；本技能实现元数据的采集、维护、交付和证据。
- 指标的业务计算、仓库装载与 BI 产品由 `delivering-data-warehousing-and-bi` 主导；本技能保持指标/报表的定义、版本和血缘可发现。
- 数据质量团队判定业务数据是否适用；本技能管理关于数据质量的规则/结果元数据及元数据自身的质量。

## 工作流

1. 明确消费任务：查找数据、理解指标、证明来源、审计或变更影响；限定资产/字段/报表范围、粒度和成功标准。
2. 阅读[元数据项目手册](references/playbook.md)，盘点生产者/消费者、业务/技术/运行元数据源、现有目录、接口、版本与访问限制。
3. 定义最小元模型、稳定资产标识、关系、owner、必填字段、来源、更新时间和质量规则；选择集中、分布或混合架构。
4. 以连接器/扫描/API 采集技术和运行事实；用有审批的人工策展补充业务定义、未可解析转换与语境。
5. 分别保存设计态和实际实现态血缘；逐边记录来源、转换、代码/作业版本、证据、观测时间、可信度和缺口，持续对齐差异。
6. 用上下游图遍历做变更影响分析；暴露未解析、过期和低置信边，要求关键变更前由受影响 owner 确认。
7. 发布搜索、术语、血缘、质量、访问与 API 服务；监控覆盖、完整性、准确性、新鲜度、使用、反馈和修复队列。

## 交付模板

使用 [中文交付包](templates/delivery-pack.zh.md) 或 [English delivery pack](templates/delivery-pack.en.md) 组织输出。叙述性方案和评审记录使用同目录 Word 模板；矩阵、台账和评分卡使用同目录 Excel 模板。模板中的责任、阈值、批准和证据须由实际项目确认。

## 输出契约

输出元数据策略与范围；用户任务和需求；源/消费者清单；元模型和最小元数据产品；集中/分布/混合架构；采集/策展/冲突流程；业务词汇表；设计态与实现态字段级血缘及证据；影响分析与变更门；权限/敏感元数据控制；质量/新鲜度/覆盖/采用指标；角色、阶段门和验收证据。

## 常见错误

| 错误 | 修正 |
|---|---|
| 目录只有表名 | 关联业务含义、owner、字段、来源、运行、质量和消费 |
| 设计文档当作生产事实 | 标注设计态与实现态，采集运行版本并记录差异 |
| 自动解析到哪里就宣称全链路 | 逐边标证据、覆盖、可信度和未知段 |
| 血缘图漂亮即能做影响分析 | 对真实变更做上下游遍历和漏报复核 |
| 所有元数据向所有人公开 | 控制敏感资产存在性、字段、SQL、访问与审计 |
| 一次扫描后不维护 | 设同步频率、漂移告警、策展队列与责任人 |
