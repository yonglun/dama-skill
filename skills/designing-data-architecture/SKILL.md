---
name: designing-data-architecture
description: Use when an enterprise, domain, platform, program, or project needs current, target, or transition data architecture; capability and data-flow alignment; architecture principles, standards, decisions, conformance, or an evolution roadmap.
---

# 设计数据架构

## 核心原则

数据架构识别企业数据需求并维护满足这些需求的主蓝图。它组织数据、系统、流向、约束和原则，使投资与业务战略对齐；已选技术是约束和候选实现，不是需求本身。

## 适用边界

- 跨系统/业务能力的当前、目标、过渡状态和路线图使用本技能。
- 单一主题的概念/逻辑/物理结构、键、属性和规范化以 `modeling-data` 为主。
- 平台实际备份、恢复、容量和数据库运行以 `operating-data-storage` 为主。
- 具体接口/ETL/流处理契约以 `integrating-data` 为主。

## 工作流

1. 明确业务能力、事件、决策、消费者和当前/长期数据需求；把质量与创新目标分开记录。
2. 读取 [数据架构手册](references/playbook.md)，以运行证据核实现状系统、数据、接口、复制、约束和痛点，不把陈旧图当事实。
3. 定义架构原则和可验证需求：语义、生命周期、共享、互操作、质量、元数据、安全/隐私、地域、服务、成本和可演进性。
4. 产出互相一致的业务/数据、概念、流向、系统/应用、技术部署和治理视图；每个视图只回答明确问题。
5. 比较方案和权衡，记录架构决策及被否决方案；已选技术不适配时呈现差距、补偿或升级决定。
6. 设计目标状态、过渡架构和按能力/数据依赖排序的路线图；同时标记复用、替换、退役与临时状态。
7. 把标准和符合性检查嵌入项目、模型、集成、采购和技术更新；用实际结果维护架构。

## 交付模板

使用 [中文交付包](templates/delivery-pack.zh.md) 或 [English delivery pack](templates/delivery-pack.en.md) 组织输出。叙述性方案和评审记录使用同目录 Word 模板；矩阵、台账和评分卡使用同目录 Excel 模板。模板中的责任、阈值、批准和证据须由实际项目确认。

## 输出契约

输出业务结果与范围；现状证据；原则/需求；视图目录；目标与过渡架构；关键决定和权衡；能力/数据依赖路线图；标准与符合性；风险和例外；指标与验收证据。

## 常见错误

| 错误 | 修正 |
|---|---|
| 架构等于云产品图 | 从能力、数据需求和关系出发，再映射技术 |
| 只有目标图 | 同时提供现状证据、过渡状态和退役路径 |
| 一个巨图回答所有问题 | 为利益相关者和决策拆分一致的视图 |
| 架构师替项目建详细模型 | 提供约束和审查；详细建模交给 `modeling-data` |
