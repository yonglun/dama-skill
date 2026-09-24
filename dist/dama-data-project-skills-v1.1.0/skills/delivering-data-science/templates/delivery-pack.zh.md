# 数据科学交付包

Skill: `delivering-data-science`

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

### 业务假设与决策边界 (`hypothesis`)

定义拟验证的假设、基线方案、成功判据和禁止自动化的决定。

> 填写项目证据、结论与责任人。


### 数据特征与标签 (`data_features`)

固定预测时点、数据用途、特征可用性、标签延迟和泄漏检查。

> 填写项目证据、结论与责任人。


### 实验与评估协议 (`evaluation`)

规定时间切分、独立测试、分群误差、成本和对照指标。

> 填写项目证据、结论与责任人。


### 可复现证据 (`reproducibility`)

记录数据版本、代码、环境、随机性和评估工件。

> 填写项目证据、结论与责任人。


### 模型卡与限制 (`model_card`)

说明目标用途、表现、已知失败模式、受影响方和人工兜底。

> 填写项目证据、结论与责任人。


### 生产服务与灰度 (`production`)

定义影子或灰度门、人工流程、可观测性和发布批准。

> 填写项目证据、结论与责任人。


### 监控重训与变更 (`monitoring`)

设定漂移、效果、偏差与再训练触发和独立复核。

> 填写项目证据、结论与责任人。


### 回滚与退役 (`rollback`)

写明停止阈值、回退、数据保留和退役责任。

> 填写项目证据、结论与责任人。


## 工作台账

### 数据特征 (`features`)

记录特征来源、时点和用途约束。

| 特征 (`feature`) | 定义 (`definition`) | 来源 (`source`) | 规则 (`rule`) | 负责人 (`owner`) | 证据 (`evidence`) |
| --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |   |

### 验证监控 (`validation`)

跟踪独立验证、漂移和停用动作。

| 指标 (`metric`) | 验证 (`validation`) | 漂移阈值 (`drift_threshold`) | 测试结果 (`test_result`) | 负责人 (`owner`) | 证据 (`evidence`) | 复核日期 (`review_date`) |
| --- | --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |   |   |
