# 数据模型交付包

Skill: `modeling-data`

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

### 业务用例与范围 (`use_cases`)

说明模型支持的业务过程、决定和消费者。

> 填写项目证据、结论与责任人。


### 模型层级与方案 (`model_level`)

选择概念、逻辑或物理层级及关系、维度或其他适用模式。

> 填写项目证据、结论与责任人。


### 需求与术语 (`requirements`)

列出受控定义、术语冲突和业务规则的批准状态。

> 填写项目证据、结论与责任人。


### 粒度键与关系 (`grain_keys`)

固定实体或事实粒度、键、基数、可选性及时态规则。

> 填写项目证据、结论与责任人。


### 模型与来源追溯 (`traceability`)

追踪概念到逻辑到物理，以及源到目标的映射和偏差。

> 填写项目证据、结论与责任人。


### 评审与批准 (`review`)

记录需求、设计和物理可行性评审中的问题与决定。

> 填写项目证据、结论与责任人。


### 版本与变更 (`change_control`)

对破坏性变更记录影响、迁移、兼容和回退。

> 填写项目证据、结论与责任人。


### 质量与验收证据 (`acceptance_evidence`)

用场景、数据剖析和实现逆向核对模型正确性。

> 填写项目证据、结论与责任人。


## 工作台账

### 数据字典 (`dictionary`)

维护实体字段键和精确定义。

| 实体或事实 (`entity`) | 属性 (`attribute`) | 定义 (`definition`) | 键 (`key`) | 来源 (`source`) | 负责人 (`owner`) | 版本 (`version`) |
| --- | --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |   |   |

### 模型映射 (`mappings`)

追踪源字段到目标字段及转换规则。

| 源字段 (`source_field`) | 目标字段 (`target_field`) | 转换规则 (`transformation`) | 规则 (`rule`) | 负责人 (`owner`) | 测试 (`test`) | 证据 (`evidence`) |
| --- | --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |   |   |
