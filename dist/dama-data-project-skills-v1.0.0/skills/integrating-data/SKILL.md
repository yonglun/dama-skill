---
name: integrating-data
description: Use when data must move or interoperate across stores, applications, or organizations; when selecting batch, CDC, stream, API, service, or virtualization patterns; or defining contracts, mappings, orchestration, reconciliation, replay, lineage, sharing agreements, and integration SLAs.
---

# 数据集成与互操作

## 核心原则

数据集成在数据存储、应用和组织之间移动、转换或联合数据；互操作使系统以共同语义通信。目标是按消费者需要的格式和时间提供数据，同时用共享模型、接口和可运行契约降低点对点复杂度。

## 适用边界

- 跨系统批处理、CDC、事件流、API/服务、迁移、发布/订阅、虚拟化和数据共享使用本技能。
- 企业平台、系统责任、目标/过渡蓝图由 `designing-data-architecture` 主导。
- 实体粒度、键和业务结构冲突由 `modeling-data` 主导；本技能实现获批语义。
- 数据库容量、备份恢复和实例运行由 `operating-data-storage` 主导。
- 主数据身份解析、黄金记录和持续合并/拆分运营由 `managing-reference-and-master-data` 主导。

## 工作流

1. 明确消费者、用途、对象/粒度、来源/目标、延迟、新鲜度、完整性、容量、保留、安全和共享限制；分别暴露不同源水位。
2. 阅读[数据集成项目手册](references/playbook.md)，发现/剖析实际源与目标，确认键、代码、删除、更正、顺序和源能力；记录未知项和 owner。
3. 按业务时限、耦合、事务、一致性、量级、源负载、历史/重放、成本和运行能力选择批、CDC、事件、同步 API、异步消息或虚拟化；不把“实时”当默认优越方案。
4. 定义版本化接口/数据产品契约、源目标映射、代码/时区/空值规则、字段级血缘、共享协议和 schema 演进。
5. 设计编排、状态、水位、依赖、幂等、顺序、迟到、删除、重试、隔离/死信、受控重放、原子发布和降级。
6. 用记录级、分组级和总量级对账及质量门验证全量/增量、故障、重跑、坏 schema、源迟到和消费者兼容。
7. 发布并监控可用性、量级、速度、延迟、成本、复杂度、使用和错误积压；业务 owner 批准映射/转换变化。

## 输出契约

输出范围/需求；发现与源能力；模式选择和权衡；接口/数据产品契约；映射/血缘；编排与状态；错误/重试/隔离/重放；对账/质量；schema 演进；共享协议；SLA/监控；角色、阶段门、风险和验收证据。

## 常见错误

| 错误 | 修正 |
|---|---|
| 所有数据都要实时 | 由业务响应时限、源能力、成本和故障耦合决定 |
| 作业成功即数据正确 | 同源控制清单做记录、分组和总量对账后原子发布 |
| 重试等于可靠 | 区分瞬时与确定性错误，定义幂等、隔离、重放和副作用控制 |
| 字段名相同即语义相同 | 由业务 owner 批准定义、粒度、代码和转换 |
| 虚拟化等于无运行代价 | 显式承接源可用性、性能、权限和 schema 变化 |
