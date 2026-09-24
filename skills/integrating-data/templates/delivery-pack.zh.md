# 数据集成交付包

Skill: `integrating-data`

[Word 报告](report.zh.docx) · [Excel 台账](register.zh.xlsx)

## 基本信息

| ID | 字段 | 填写内容 |
| --- | --- | --- |
| `artifact_id` | 工件编号 | |
| `project` | 项目 | |
| `skill` | 适用技能 | |
| `version` | 版本 | |
| `date` | 日期 | |
| `status` | 状态 | |
| `author` | 编写人 | |
| `owner` | 负责人 | |
| `approver` | 批准人 | |
| `purpose` | 目的 | |
| `business_outcome` | 业务结果 | |
| `scope` | 范围与排除项 | |
| `source_inputs` | 输入与来源 | |
| `assumptions` | 假设与约束 | |
| `decisions` | 决定 | |
| `rationale` | 决定依据 | |
| `risks` | 风险 | |
| `exceptions` | 例外 | |
| `open_items` | 未决项 | |
| `due_date` | 期限 | |
| `acceptance_criteria` | 验收标准 | |
| `evidence_location` | 证据位置 | |
| `reviewer_decision` | 评审决定 | |
| `next_gate` | 下一阶段门 | |

## 专题分析与决策

### 范围与业务要求 (`scope`)

说明数据来源、消费者、延迟、完整性与失败容忍度。

> 填写项目证据、结论与责任人。


### 来源能力与模式选择 (`source_capability`)

比较批量、CDC、流、API 或共享方式与约束。

> 填写项目证据、结论与责任人。


### 版本化接口契约 (`interface_contract`)

定义所有者、模式、语义、SLA、版本和变更通知。

> 填写项目证据、结论与责任人。


### 映射与血缘 (`mapping`)

记录字段级转换、质量规则、目标语义和来源追溯。

> 填写项目证据、结论与责任人。


### 错误隔离与重放 (`replay`)

规定幂等、顺序、重试、死信、重放与人工恢复。

> 填写项目证据、结论与责任人。


### 模式演进 (`schema_evolution`)

定义兼容窗口、破坏性变更批准和消费者迁移。

> 填写项目证据、结论与责任人。


### 对账与质量 (`reconciliation`)

核对记录、业务总量、拒收、延迟和异常关闭。

> 填写项目证据、结论与责任人。


### 监控与验收 (`operations`)

明确告警、运行负责人、阶段门和消费者验收证据。

> 填写项目证据、结论与责任人。


## 工作台账

### 源目标映射 (`mappings`)

维护字段语义、转换和测试。

| 源字段 (`source_field`) | 目标字段 (`target_field`) | 转换规则 (`transformation`) | 规则 (`rule`) | 负责人 (`owner`) | 测试 (`test`) | 版本 (`version`) |
| --- | --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |   |   |

### 对账异常 (`reconciliation`)

记录对账差异、隔离与恢复证据。

| 来源 (`source`) | 目标 (`target`) | 规则 (`rule`) | 测试结果 (`test_result`) | 影响 (`impact`) | 负责人 (`owner`) | 证据 (`evidence`) | 状态 (`status`) |
| --- | --- | --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |   |   |   |
