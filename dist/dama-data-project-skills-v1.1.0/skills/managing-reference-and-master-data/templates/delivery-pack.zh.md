# 主数据与参考数据交付包

Skill: `managing-reference-and-master-data`

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

### 数据域章程 (`domain_charter`)

界定共享实体或代码集、业务用途、所有者和消费者。

> 填写项目证据、结论与责任人。


### 来源与权威 (`authority`)

按属性或事件明确权威来源、裁决权和分发关系。

> 填写项目证据、结论与责任人。


### 全局身份与交叉引用 (`global_identity`)

定义全局 ID、源标识映射、生成与废止规则。

> 填写项目证据、结论与责任人。


### 黄金记录与生存规则 (`survivorship`)

写出来源优先、时效、冲突、人工裁决与可追溯规则。

> 填写项目证据、结论与责任人。


### 匹配合并与拆分 (`merge_split`)

覆盖误合并防护、拆分回退、版本和独立测试。

> 填写项目证据、结论与责任人。


### 层级与参考代码 (`hierarchies`)

规定层级变更、代码集版本、生效与向后兼容。

> 填写项目证据、结论与责任人。


### 发布与回执 (`distribution`)

说明发布契约、消费方回执、对账和纠错。

> 填写项目证据、结论与责任人。


### 质量与运行验收 (`acceptance_evidence`)

列出管家工作流、质量指标、例外和阶段门证据。

> 填写项目证据、结论与责任人。


## 工作台账

### 身份交叉引用 (`crosswalk`)

记录本地身份与受控全局身份。

| 来源 (`source`) | 源标识 (`source_id`) | 全局标识 (`global_id`) | 匹配规则 (`match_rule`) | 负责人 (`owner`) | 状态 (`status`) | 证据 (`evidence`) |
| --- | --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |   |   |

### 匹配裁决 (`decisions`)

追踪合并拆分及误判恢复证据。

| 源标识 (`source_id`) | 全局标识 (`global_id`) | 决定 (`decision`) | 依据 (`rationale`) | 批准人 (`approver`) | 测试 (`test`) | 证据 (`evidence`) |
| --- | --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |   |   |
