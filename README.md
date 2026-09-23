# DAMA Data-Project Skill Suite

[中文 README](README.zh.md)

This suite turns the knowledge areas in *DAMA-DMBOK Data Management Body of Knowledge, 2nd Edition, Revised Edition* into original workflows for data projects: **one cross-domain router plus 16 independently usable domain skills**. The skills help define scope, ownership, sequencing, deliverables, and acceptance evidence. They do not require every project to implement every knowledge area. The book is source material, not a set of instructions to the agent. The copyrighted source book is not included in this repository or its release package.

## Quick start

The skills/ directory is the single editable source in this repository. Relative symlinks under .agents/skills/ make all 17 skills discoverable to Codex in this project. Invoke a skill explicitly by including $skill-name in your prompt, or describe the task and let Codex choose based on the skill descriptions. For cross-domain work, or when you are unsure which skill to use, start with [Managing Data Projects](skills/managing-data-projects/SKILL.md).

> Use $managing-data-projects to plan a 12-week retail lakehouse project. Select the primary, foundational, and supporting domains; explain scope exclusions, owners, stage gates, and verifiable acceptance evidence.

To use the suite in **another data project**, copy or link the complete skill directories you need from this repository's skills/ into that project's .agents/skills/. Preserve each directory's SKILL.md, references/, and agents/; copying only SKILL.md loses supporting guidance. Install the router alongside the relevant domain skills for cross-domain projects; a focused task may need only one domain skill. If a newly added skill does not appear, restart Codex. See the [official Codex skill documentation](https://learn.chatgpt.com/docs/build-skills) for discovery locations and explicit or implicit invocation.

The prompts below are **examples of requests for a plan or work product**, not preapproved business decisions. Replace the organization, data, deadline, and constraints with your own. When facts are missing, ask the skill to identify questions to resolve instead of inventing thresholds, legal conclusions, or owners.

## All 17 skills

This repository's original materials are licensed under [Apache License 2.0](LICENSE). The license does not grant rights to the copyrighted DMBOK source book.

### 1. [Managing Data Projects · $managing-data-projects](skills/managing-data-projects/SKILL.md)

- Use when: An initiative spans several data-management domains, or the right skills and delivery order are unclear.
- Produces: A project profile, primary/foundational/supporting domain route, tailoring rationale, dependency order, stage gates, and an integrated delivery plan.
- Example: Use $managing-data-projects to create a 12-week roadmap for a new customer-data platform. Explain which governance, quality, metadata, security, operations, and change activities belong in scope, which can wait, and the evidence required at each gate.

### 2. [Handling Data Ethically · $handling-data-ethically](skills/handling-data-ethically/SKILL.md)

- Use when: New collection, sharing, profiling, AI, or secondary use may affect people, fairness, autonomy, or trust, even if the use appears secure or legally permissible.
- Produces: Purpose and alternatives, affected-party mapping, benefit/harm assessment, use boundaries, recourse and stop conditions, and an evidence-based decision recommendation.
- Example: Use $handling-data-ethically to assess using existing customer-behavior data for personalized pricing. Identify affected groups, less intrusive alternatives, fairness risks, and evidence needed before a decision.

### 3. [Establishing Data Governance · $establishing-data-governance](skills/establishing-data-governance/SKILL.md)

- Use when: Teams disagree about definitions, ownership, standards, or exceptions and need clear authority, oversight, and escalation.
- Produces: A governance charter, decision-rights and stewardship matrix, policy/standards hierarchy, issue and exception workflow, and scorecard.
- Example: Use $establishing-data-governance to resolve conflicting definitions of “customer” across three business units. Name the final approver, term-change process, escalation path, and oversight measures.

### 4. [Designing Data Architecture · $designing-data-architecture](skills/designing-data-architecture/SKILL.md)

- Use when: An enterprise, domain, or platform needs current, target, and transition architecture with an evolution roadmap—not merely a single table design.
- Produces: Architecture principles and views, current/target/transition blueprints, decisions and trade-offs, a dependency roadmap, and conformance evidence.
- Example: Use $designing-data-architecture to plan how CRM, POS, and e-commerce data will fit into a target architecture. Compare transition options, system responsibilities, data flows, and phased migration evidence.

### 5. [Modeling Data · $modeling-data](skills/modeling-data/SKILL.md)

- Use when: Business requirements must become conceptual, logical, or physical models with explicit entities, grain, keys, relationships, and rules.
- Produces: Models and term definitions, conceptual-to-logical-to-physical traceability, reviews, versions, and controlled changes.
- Example: Use $modeling-data to design a logical model for orders, refunds, and customers. Specify order-line grain, primary and foreign keys, historical states, and questions requiring business confirmation.

### 6. [Operating Data Storage · $operating-data-storage](skills/operating-data-storage/SKILL.md)

- Use when: A database, lakehouse, or file store needs production readiness, capacity, performance, backup/recovery, change control, or operational handoff.
- Produces: Service targets, capacity and cost estimates, RTO/RPO, recovery exercises, monitoring, runbooks, and Go/No-Go evidence.
- Example: Use $operating-data-storage to assess a new analytical database before production. Define recovery drills, capacity and performance tests, on-call handoff, and release blockers.

### 7. [Securing Data · $securing-data](skills/securing-data/SKILL.md)

- Use when: Data needs classification, access control, encryption/masking, export limits, auditability, cloud or vendor safeguards, and control tests.
- Produces: Classification, a subject-by-data-by-action access matrix, selected controls, negative tests, exceptions, and residual-risk evidence.
- Example: Use $securing-data to design least-privilege and masking controls for a cloud platform containing customer contact details. Specify access ordinary analysts must be denied, revocation tests, and audit evidence.

### 8. [Integrating Data · $integrating-data](skills/integrating-data/SKILL.md)

- Use when: Data must move or interoperate between systems through batch, CDC, streams, APIs, or sharing, with mappings, replay, reconciliation, and interface ownership.
- Produces: Integration-pattern decisions, versioned interface contracts, source-to-target mappings, failure isolation/retry/replay, lineage, reconciliation, and SLAs.
- Example: Use $integrating-data to design a customer-change CDC pipeline from CRM to billing. Cover out-of-order and duplicate events, idempotent replay, schema changes, and business reconciliation.

### 9. [Managing Documents and Content · $managing-documents-and-content](skills/managing-documents-and-content/SKILL.md)

- Use when: Contracts, email, records, or media need lifecycle governance for classification, versions, search, publication, retention, and disposition; not for editing a single document.
- Produces: Content inventory and taxonomy, controlled vocabulary, lifecycle and access rules, hold/disposition workflows, search, and audit evidence.
- Example: Use $managing-documents-and-content to govern customer contracts and correspondence spread across repositories. Design classification, versioning, search, retention, and legal-hold interfaces, marking decisions that require legal approval.

### 10. [Managing Reference and Master Data · $managing-reference-and-master-data](skills/managing-reference-and-master-data/SKILL.md)

- Use when: Shared customer/product identities or controlled code sets such as countries and statuses conflict across systems and need authority and ongoing distribution.
- Produces: Source/consumer/authority matrices, global IDs and crosswalks, golden-record and survivorship rules, match/merge/split tests, reference-code versions, and stewardship workflows.
- Example: Use $managing-reference-and-master-data to address duplicate customers across three CRMs. Define false-merge safeguards, reversible splits, golden-record rules, country-code versions, and consumer acknowledgments.

### 11. [Delivering Data Warehousing and BI · $delivering-data-warehousing-and-bi](skills/delivering-data-warehousing-and-bi/SKILL.md)

- Use when: Delivering a warehouse, mart, metric, report, or dashboard, especially with disputed definitions, historical comparisons, business acceptance, or self-service analytics.
- Produces: Decision-to-metric traceability, metric contracts, fact grain and conformed dimensions, history policy, load reconciliation, BI release/support/adoption evidence.
- Example: Use $delivering-data-warehousing-and-bi to deliver an executive sales dashboard. Resolve revenue definitions and refund attribution before specifying certified metrics, year-over-year history, and acceptance tests.

### 12. [Managing Metadata · $managing-metadata](skills/managing-metadata/SKILL.md)

- Use when: Data assets, business terms, fields, ownership, operational status, or lineage must be discoverable and maintained for provenance and change-impact analysis.
- Produces: A minimum metadata product, catalog/glossary, design versus actual-run lineage, impact analysis, and coverage/freshness measures. Governance retains final authority over disputed terms.
- Example: Use $managing-metadata to build a searchable catalog and field-level lineage for three critical reports. Require a trace from report to source run and a downstream-impact test for a changed source field.

### 13. [Improving Data Quality · $improving-data-quality](skills/improving-data-quality/SKILL.md)

- Use when: Defects recur and the business needs fit-for-purpose rules, a measured baseline, root-cause analysis, prevention, and ongoing monitoring.
- Produces: Versioned quality rules, profiling and baselines, business-impact priorities, root-cause remediation, issue closure, scorecards, and trends.
- Example: Use $improving-data-quality to address customer addresses that became invalid again after a cleanup. Separate existing-record repair from new-error prevention and define delivery-specific rules, root-cause evidence, and recurrence measures.

### 14. [Delivering Data Science · $delivering-data-science](skills/delivering-data-science/SKILL.md)

- Use when: Testing a data hypothesis or building/deploying a predictive or statistical model, including experiment validity, reproducibility, production monitoring, and retirement. Use the BI skill for ordinary dashboards.
- Produces: Hypotheses, data/feature/label cards, experiment and independent-validation protocols, model cards, shadow/canary gates, drift monitoring, and rollback criteria.
- Example: Use $delivering-data-science to design the launch of a customer-risk model. Fix the prediction time, temporal split, and independent test; define group error, human fallback, and stop conditions.

### 15. [Assessing Data-Management Maturity · $assessing-data-management-maturity](skills/assessing-data-management-maturity/SKILL.md)

- Use when: An organization needs an evidence-based current and target capability assessment, gap analysis, and improvement priorities.
- Produces: Assessment scope and rubric, evidence-strength rules, current/target matrix, uncertainty statements, prioritized improvements, and reassessment cadence.
- Example: Use $assessing-data-management-maturity to assess governance, quality, and metadata across three business units. State sampling and evidence strength; do not claim a verified enterprise-wide score without operational evidence.

### 16. [Organizing Data Management · $organizing-data-management](skills/organizing-data-management/SKILL.md)

- Use when: Designing central/local responsibilities, operating models, roles, committees, shared services, RACI, funding, or coordination.
- Produces: Comparison of centralized, decentralized, network, hybrid, and federated models; an operating model, role charters, activity-level RACI, resource gaps, and a pilot roadmap.
- Example: Use $organizing-data-management to compare centralized and federated data offices for a multi-region company. Define central and local roles, decision interfaces, RACI, staffing capacity, and pilot gates.

### 17. [Leading Data Change · $leading-data-change](skills/leading-data-change/SKILL.md)

- Use when: A new catalog, governance process, standard, or stewardship practice exists but is underused, bypassed, or not sustained, and real working behavior must change.
- Produces: Change case and target behaviors, stakeholder readiness, guiding coalition, communication/training, obstacle log, short-term wins, and an adoption funnel.
- Example: Use $leading-data-change to improve a catalog's 12% active-use rate three months after launch. Address middle-manager participation, hands-on support, feedback closure, and sustained-use metrics.

## Combining skills

The router **selects, sequences, tailors, and consolidates**; domain skills supply their specialist methods and work products. A build project should at least check governance, quality, metadata, security/privacy, ethical use, and organizational adoption. Checking an area does not authorize implementing it. Do not load all 17 skills merely because a prompt contains a broad data term.

- Lakehouse/BI: Start with $managing-data-projects; warehousing/BI and integration are often primary, with architecture, quality, metadata, security, storage operations, and change added as risks warrant.
- Customer-master remediation: Make master/reference data primary; use quality for recurring field defects, integration for cross-system distribution, and governance for disputed authority.
- Risk-model launch: Make data science primary and independently check ethical use, security, quality, metadata, and human adoption. A dashboard or a security pass is not model-release approval.

## Sources, validation, and boundaries

- [DMBOK Chapter 1–17 source map](skills/managing-data-projects/references/source-map.md); [cross-domain routing table](skills/managing-data-projects/references/routing-table.md); [completion audit and behavior evaluations](evals/skill-suite/completion-audit.md).
- In this repository, run python3 scripts/validate_skill_suite.py skills and python3 -m unittest tests/test_validate_skill_suite.py to verify structure, links, and validator tests.
- The skills neither reproduce the book nor constitute official DAMA forms, legal advice, certification rules, or a vendor-specific implementation. Authorized owners must confirm current laws, actual data, thresholds, and permissions for each real project.
