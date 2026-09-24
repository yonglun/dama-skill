# 数据存储运营交付包

Skill: `operating-data-storage`

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

### 服务范围与依赖 (`service_scope`)

说明持久化服务、环境、消费者和上游下游依赖。

> 填写项目证据、结论与责任人。


### 配置与容量基线 (`configuration`)

记录版本、配置、容量预测、成本和性能测量。

> 填写项目证据、结论与责任人。


### 服务目标 (`slo`)

明确可用性、性能、RTO 和 RPO 的批准值与测点。

> 填写项目证据、结论与责任人。


### 备份与恢复 (`recovery`)

记录备份频率、恢复演练、数据完整性和失败动作。

> 填写项目证据、结论与责任人。


### 变更与发布 (`release_control`)

规定环境隔离、发布门、兼容、回滚和配置漂移检查。

> 填写项目证据、结论与责任人。


### 监控值班与移交 (`runbook`)

列出告警、事件、值班、升级和运营日历。

> 填写项目证据、结论与责任人。


### 上线决定 (`go_no_go`)

汇总测试证据、阻断项、例外和具名上线批准。

> 填写项目证据、结论与责任人。


## 工作台账

### 服务目标 (`targets`)

记录服务目标、责任和实测结果。

| 服务 (`service`) | RTO (`rto`) | RPO (`rpo`) | 阈值 (`threshold`) | 负责人 (`owner`) | 证据 (`evidence`) | 复核日期 (`review_date`) |
| --- | --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |   |   |

### 恢复演练 (`recovery_tests`)

记录恢复场景、结果和纠正动作。

| 服务 (`service`) | 测试 (`test`) | 测试结果 (`test_result`) | 影响 (`impact`) | 负责人 (`owner`) | 证据 (`evidence`) | 期限 (`due_date`) |
| --- | --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |   |   |
