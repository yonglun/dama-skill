---
name: managing-data-projects
description: Use when a data initiative spans multiple data-management domains, when the correct DAMA knowledge areas or delivery order are unclear, or when a cross-domain project plan, readiness assessment, roadmap, stage gate, or governance coverage check is needed.
---

# 管理数据项目

## 核心原则

从业务结果和风险出发编排数据管理能力。DMBOK 是知识框架，不是必须全量执行的瀑布流程；每个纳入或裁剪决定都要有价值、风险、依赖或成熟度依据。

## 工作流

1. 建立最小项目画像：业务结果与价值假设、项目类型与阶段、数据范围与消费者、监管/伦理/安全约束、当前能力与责任人、已有工件与决策期限。缺少会改变方案的信息时，只询问最关键的问题。
2. 把能力分成三层：
   - **主知识域**：直接产生项目核心结果；
   - **基础与监督域**：治理、质量、元数据、安全/隐私/伦理；
   - **支持域**：组织、变更、架构、运营或成熟度等依赖。
3. 读取 [路由表](references/routing-table.md)，选择最少但完整的领域技能；说明选择顺序和未选择理由。
4. 建设或整改项目读取 [项目生命周期](references/project-lifecycle.md)，把工作映射到 Plan / Control / Develop / Operate 和阶段门。
5. 加载所选领域技能。不要用本入口替代领域方法；涉及多个领域时合并重复角色、工件和控制。
6. 使用 [交付模板](references/deliverable-templates.md)形成可审阅结果。需要核对 DMBOK 覆盖或出处时读取 [来源映射](references/source-map.md)。

## 必需的跨域检查

任何建设型项目都检查治理责任、数据质量、元数据/血缘、安全与隐私、伦理用途和组织采纳。检查不代表全部实施；若裁剪，记录理由、风险所有者和重新纳入的触发条件。

## 输出契约

除纯问答外，输出依次包含：业务结果与范围；假设/约束/未决问题；所选知识域及理由；活动与依赖顺序；角色和决策权；交付物与验收证据；指标/风险/控制/升级；裁剪项与理由；下一阶段门及证据。

## 边界

- 法律、监管或行业标准要求必须核对适用地区和当前权威来源。
- DMBOK 不背书厂商；按能力、约束和证据选择工具。
- 诊断不授权扩大实施范围或外部变更。重大新增范围先征得用户确认。
- 不用无证据的单一分数表示成熟度，也不长篇复制原书。

## 常见错误

| 错误 | 修正 |
|---|---|
| 按 DAMA Wheel 罗列全部领域 | 只选能改变结果或风险的领域，并说明裁剪 |
| 先选平台再找问题 | 先定义业务结果、数据消费者和验收证据 |
| 把治理当审批会议 | 明确决策权、所有权、标准、问题闭环和指标 |
| 把上线当结束 | 加入运行责任、服务目标、监控、变更与退役 |
