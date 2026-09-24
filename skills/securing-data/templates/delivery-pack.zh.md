# 数据安全交付包

Skill: `securing-data`

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

### 安全范围与责任 (`scope`)

说明数据资产、处理链、供应商和共同责任边界。

> 填写项目证据、结论与责任人。


### 数据与风险分类 (`classification`)

按用途、敏感性和损害程度确定分类及处理要求。

> 填写项目证据、结论与责任人。


### 威胁与暴露 (`threats`)

记录威胁路径、暴露面、既有控制和剩余风险。

> 填写项目证据、结论与责任人。


### 身份与访问设计 (`access_design`)

按主体、数据和操作定义最小权限、撤销及拒绝路径。

> 填写项目证据、结论与责任人。


### 控制与负向测试 (`control_tests`)

覆盖加密、脱敏、非生产数据、导出、审计和越权测试。

> 填写项目证据、结论与责任人。


### 监控事件与响应 (`incident`)

规定日志、告警、事件分级、升级和复盘证据。

> 填写项目证据、结论与责任人。


### 例外与残余风险 (`residual_risk`)

说明例外批准、补偿控制、到期与复审。

> 填写项目证据、结论与责任人。


### 阶段门与验收 (`acceptance_evidence`)

列出控制测试、角色批准和运营移交的证据。

> 填写项目证据、结论与责任人。


## 工作台账

### 访问矩阵 (`access`)

记录主体数据操作和允许或拒绝决定。

| 主体 (`subject`) | 数据范围 (`data`) | 操作 (`action`) | 决定 (`decision`) | 负责人 (`owner`) | 批准人 (`approver`) | 证据 (`evidence`) |
| --- | --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |   |   |

### 控制测试 (`control_tests`)

跟踪控制有效性与剩余例外。

| 控制措施 (`control`) | 测试 (`test`) | 测试结果 (`test_result`) | 例外 (`exception`) | 负责人 (`owner`) | 证据 (`evidence`) | 复核日期 (`review_date`) |
| --- | --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |   |   |
