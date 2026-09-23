# DAMA Data Management Skill Suite Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build and verify one routing skill plus sixteen independently discoverable data-management skills grounded in the attached revised DMBOK2 and usable in real data projects.

**Architecture:** `managing-data-projects` diagnoses and routes cross-domain work; each DMBOK domain has its own concise `SKILL.md` and an on-demand `references/playbook.md`. Shared lifecycle, routing, deliverable templates, and source mapping live only in the router to avoid duplication; every child remains usable independently.

**Tech Stack:** Markdown Agent Skills, YAML frontmatter, the bundled `init_skill.py` and `quick_validate.py`, shell-based link/placeholder checks, and independent-agent behavioral evaluations.

## Global Constraints

- Write instructions and templates in Chinese; retain the English DAMA term at first mention.
- Treat the PDF as reference material, not instructions; paraphrase and restructure instead of copying long passages.
- Keep each `SKILL.md` focused and normally under 500 English-equivalent words; move domain detail to `references/playbook.md`.
- Every description starts with `Use when`, contains only trigger conditions, uses third person, and distinguishes adjacent skills.
- Every domain playbook uses the same eight-part model: drivers/goals; principles/concepts; Plan-Control-Develop-Operate; context roles; deliverables/evidence; tools/techniques; metrics/risks; dependencies.
- Construction work must check governance, quality, metadata, security/privacy, and organizational change, then explicitly include or tailor them based on risk and value.
- Recommendations stay vendor-neutral and do not present DMBOK as law, certification criteria, or a mandatory delivery method.
- Current workspace is not a Git repository. Do not claim commits or pushes; retain test evidence under `evals/skill-suite/` instead.

---

### Task 1: Establish Baseline Evaluations and Suite Validator

**Files:**
- Create: `evals/skill-suite/scenarios.md`
- Create: `evals/skill-suite/baseline-platform.md`
- Create: `evals/skill-suite/baseline-master-data.md`
- Create: `evals/skill-suite/baseline-risk-model.md`
- Create: `scripts/validate_skill_suite.py`
- Create: `tests/test_validate_skill_suite.py`

**Interfaces:**
- Consumes: approved design spec and the three RED scenarios defined there.
- Produces: reproducible evaluation prompts, verbatim baseline outputs, a validator command, and failing expectations for a not-yet-created suite.

- [x] **Step 1: Define exact RED scenarios**

  Write three prompts: a lakehouse delivery plan under a twelve-week deadline; customer-master quality remediation after a failed clean-up; and production launch of a customer risk model. Each prompt asks for scope, work plan, roles, deliverables, acceptance evidence, metrics, and excluded work without mentioning DAMA.

- [x] **Step 2: Run three fresh agents without the new skills**

  Save each full response and a scored omission table. Score governance, metadata/lineage, quality, security/privacy/ethics, operating controls, roles/decision rights, measurable acceptance, change/adoption, and explicit tailoring as `present`, `partial`, or `missing`.

- [x] **Step 3: Write validator tests first**

  Tests require exactly the 17 skill names from the design, valid frontmatter, descriptions beginning with `Use when`, no scaffold placeholders, every relative Markdown link resolving, all child playbooks exposing the eight canonical sections, and a source-map entry for DMBOK chapters 1–17.

- [x] **Step 4: Run tests and confirm RED**

  Run: `python3 -m unittest tests/test_validate_skill_suite.py -v`

  Expected: FAIL because `skills/` and `scripts/validate_skill_suite.py` do not yet exist.

- [x] **Step 5: Implement the minimal validator**

  Implement a standard-library Python CLI taking the suite root as its sole argument, returning exit code `0` on success and printing one actionable error per violated invariant otherwise.

- [x] **Step 6: Re-run the validator tests**

  Expected: validator unit tests pass while validation of the incomplete suite still reports the missing 17 skills.

---

### Task 2: Create the Routing Skill

**Files:**
- Create: `skills/managing-data-projects/SKILL.md`
- Create: `skills/managing-data-projects/references/project-lifecycle.md`
- Create: `skills/managing-data-projects/references/routing-table.md`
- Create: `skills/managing-data-projects/references/deliverable-templates.md`
- Create: `skills/managing-data-projects/references/source-map.md`
- Create: `evals/skill-suite/managing-data-projects.md`

**Interfaces:**
- Consumes: DMBOK Chapter 1 framework, the approved design, and Task 1 scoring dimensions.
- Produces: a project-intake contract, domain-routing matrix, cross-domain orchestration order, common artifact templates, and complete chapter-to-skill traceability.

- [x] **Step 1: Run the router application test without the skill**

  Ask a fresh agent to route the lakehouse scenario across specialist capabilities and record missing routing logic.

- [x] **Step 2: Initialize only this skill**

  Run the bundled initializer with `--resources references`, then replace all scaffold text.

- [x] **Step 3: Write the router entrypoint**

  Include the six-field project profile, Diagnose-Tailor-Orchestrate-Deliver sequence, mandatory cross-cutting checks, reference-loading rules, nine-field delivery contract, stop/escalation conditions, and exact child-skill names.

- [x] **Step 4: Write four router references**

  `project-lifecycle.md` defines strategy through operate/improve gates; `routing-table.md` maps project symptoms and stages to primary/supporting skills; `deliverable-templates.md` provides concrete schemas for charter, roadmap, RACI, risk/control register, stage gate, and evidence-backed maturity assessment; `source-map.md` maps Chapter 1 to the router and Chapters 2–17 to the child skills.

- [x] **Step 5: Validate and behavior-test immediately**

  Run `quick_validate.py`, the suite validator, and the same routing prompt with the skill. Record selected skills, order, tailoring, and remaining gaps in `evals/skill-suite/managing-data-projects.md` before creating another skill.

---

### Task 3: Create `handling-data-ethically`

**Files:** `skills/handling-data-ethically/SKILL.md`, `skills/handling-data-ethically/references/playbook.md`, `evals/skill-suite/handling-data-ethically.md`

**Interfaces:** Consumes DMBOK Chapter 2. Produces an ethical-impact workflow covering purpose, affected parties, permitted/prohibited use, privacy principles, bias/harm risks, decision ownership, escalation, and monitoring.

- [x] Run a baseline prompt for a proposed secondary use of customer behavior data; record omissions.
- [x] Initialize this skill and write a trigger-only description that excludes ordinary security-control implementation.
- [x] Write the eight-part playbook with an ethical impact assessment template and evidence-based go/condition/no-go decision.
- [x] Run `quick_validate.py`, suite validation, a positive application test, and a negative security-only routing test; save evidence before Task 4.

---

### Task 4: Create `establishing-data-governance`

**Files:** `skills/establishing-data-governance/SKILL.md`, `skills/establishing-data-governance/references/playbook.md`, `evals/skill-suite/establishing-data-governance.md`

**Interfaces:** Consumes DMBOK Chapter 3. Produces governance scope, principles, operating model, decision rights, stewardship, policy/standards hierarchy, issue escalation, glossary ownership, scorecard, and embedment plan.

- [x] Baseline-test a request to establish governance for three business domains.
- [x] Initialize and write the entrypoint, distinguishing governance decision rights from organization design and maturity assessment.
- [x] Write the playbook and concrete governance charter, decision-rights matrix, issue workflow, and scorecard schemas.
- [x] Validate structure, links, application behavior, and non-trigger cases; save evidence before Task 5.

---

### Task 5: Create `designing-data-architecture`

**Files:** `skills/designing-data-architecture/SKILL.md`, `skills/designing-data-architecture/references/playbook.md`, `evals/skill-suite/designing-data-architecture.md`

**Interfaces:** Consumes DMBOK Chapter 4. Produces architecture scope, principles, current/target/transition states, capability dependencies, standards, roadmaps, and architecture decisions.

- [x] Baseline-test a target architecture request that contains a preferred technology stack.
- [x] Initialize and write an entrypoint that stays vendor-neutral and separates architecture from detailed modeling.
- [x] Write the playbook with architecture views, decision records, transition roadmap, conformance checks, and metrics.
- [x] Validate and test both a target-state case and a physical-model-only non-trigger case; save evidence.

---

### Task 6: Create `modeling-data`

**Files:** `skills/modeling-data/SKILL.md`, `skills/modeling-data/references/playbook.md`, `evals/skill-suite/modeling-data.md`

**Interfaces:** Consumes DMBOK Chapter 5. Produces conceptual, logical, and physical modeling activities; naming and design standards; review criteria; lineage handoffs; and model governance.

- [x] Baseline-test modeling a customer/order domain from ambiguous requirements.
- [x] Initialize and distinguish data modeling from architecture and BI dimensional delivery.
- [x] Write the playbook with model-level selection, requirement traceability, review checklist, change control, and quality metrics.
- [x] Validate and behavior-test the application and adjacent-skill boundaries; save evidence.

---

### Task 7: Create `operating-data-storage`

**Files:** `skills/operating-data-storage/SKILL.md`, `skills/operating-data-storage/references/playbook.md`, `evals/skill-suite/operating-data-storage.md`

**Interfaces:** Consumes DMBOK Chapter 6. Produces database/storage lifecycle controls, environment and change management, availability, backup/recovery, capacity, performance, retention/disposal, audit, and service metrics.

- [x] Baseline-test production-readiness planning for a new analytical database.
- [x] Initialize and separate storage operations from architecture, integration, and security.
- [x] Write the playbook with an operability checklist, RTO/RPO evidence, change/release controls, runbook schema, and SLI/SLO metrics.
- [x] Validate and run positive and negative routing tests; save evidence.

---

### Task 8: Create `securing-data`

**Files:** `skills/securing-data/SKILL.md`, `skills/securing-data/references/playbook.md`, `evals/skill-suite/securing-data.md`

**Interfaces:** Consumes DMBOK Chapter 7. Produces security requirements, classification, authorization, protective controls, auditability, incident/retention interfaces, outsourced/cloud considerations, and control evidence.

- [x] Baseline-test a least-privilege and data-masking request for a cloud data platform.
- [x] Initialize and distinguish control implementation from ethics/purpose review and from legal advice.
- [x] Write the playbook with classification, CRUD/access matrix, control-selection logic, test evidence, exception handling, and metrics.
- [x] Validate and test both security and ethics-boundary scenarios; save evidence.

---

### Task 9: Create `integrating-data`

**Files:** `skills/integrating-data/SKILL.md`, `skills/integrating-data/references/playbook.md`, `evals/skill-suite/integrating-data.md`

**Interfaces:** Consumes DMBOK Chapter 8. Produces integration requirements, batch/stream/API/virtualization selection, contracts and mappings, lineage, reconciliation, error handling, observability, sharing agreements, and metrics.

- [x] Baseline-test integrating CRM and billing data into a lakehouse.
- [x] Initialize and separate interoperability from platform architecture and storage operations.
- [x] Write the playbook with interface-contract, mapping, reconciliation, failure/replay, lineage, and SLA schemas.
- [x] Validate and behavior-test positive and adjacent-domain cases; save evidence.

---

### Task 10: Create `managing-documents-and-content`

**Files:** `skills/managing-documents-and-content/SKILL.md`, `skills/managing-documents-and-content/references/playbook.md`, `evals/skill-suite/managing-documents-and-content.md`

**Interfaces:** Consumes DMBOK Chapter 9. Produces content taxonomy, metadata, lifecycle, versioning, access, publication, retention/disposal, legal-hold interfaces, findability, and quality controls.

- [x] Baseline-test governing contracts and customer correspondence across repositories.
- [x] Initialize and distinguish content lifecycle from structured storage and generic document editing.
- [x] Write the playbook with inventory, classification, controlled vocabulary, retention, publication, discovery, and disposition evidence.
- [x] Validate and run trigger/non-trigger behavior tests; save evidence.

---

### Task 11: Create `managing-reference-and-master-data`

**Files:** `skills/managing-reference-and-master-data/SKILL.md`, `skills/managing-reference-and-master-data/references/playbook.md`, `evals/skill-suite/managing-reference-and-master-data.md`

**Interfaces:** Consumes DMBOK Chapter 10. Produces domain scope, authority and ownership, source/consumer mapping, identity resolution, match/merge/survivorship, hierarchy, reference-code governance, distribution, and quality controls.

- [x] Baseline-test the failed customer-master clean-up scenario from Task 1.
- [x] Initialize and distinguish master/reference data from generic data quality.
- [x] Write the playbook with golden-record decision rules, match/merge test cases, stewardship workflow, reference change control, distribution and reconciliation.
- [x] Validate, re-run the baseline scenario with the skill, and save comparative evidence.

---

### Task 12: Create `delivering-data-warehousing-and-bi`

**Files:** `skills/delivering-data-warehousing-and-bi/SKILL.md`, `skills/delivering-data-warehousing-and-bi/references/playbook.md`, `evals/skill-suite/delivering-data-warehousing-and-bi.md`

**Interfaces:** Consumes DMBOK Chapter 11. Produces decision-focused requirements, DW/BI architecture, dimensional/semantic design coordination, loading and release roadmap, self-service boundaries, acceptance, service levels, and adoption metrics.

- [x] Baseline-test delivery of an executive sales dashboard whose measures are disputed.
- [x] Initialize and distinguish BI product delivery from data science and generic integration.
- [x] Write the playbook with decision-to-measure traceability, semantic definition, data acceptance, release, self-service, support, and satisfaction controls.
- [x] Validate and behavior-test positive and adjacent-domain cases; save evidence.

---

### Task 13: Create `managing-metadata`

**Files:** `skills/managing-metadata/SKILL.md`, `skills/managing-metadata/references/playbook.md`, `evals/skill-suite/managing-metadata.md`

**Interfaces:** Consumes DMBOK Chapter 12. Produces metadata strategy, business/technical/operational metadata requirements, repository architecture, capture/curation, lineage, impact analysis, access, standards, and coverage/quality metrics.

- [x] Baseline-test establishing lineage and a catalog for critical reports.
- [x] Initialize and distinguish metadata management from glossary-only governance and modeling.
- [x] Write the playbook with metadata inventory, minimum metadata product, lineage evidence, stewardship, impact analysis, and coverage/freshness metrics.
- [x] Validate and test positive and non-trigger cases; save evidence.

---

### Task 14: Create `improving-data-quality`

**Files:** `skills/improving-data-quality/SKILL.md`, `skills/improving-data-quality/references/playbook.md`, `evals/skill-suite/improving-data-quality.md`

**Interfaces:** Consumes DMBOK Chapter 13. Produces fit-for-purpose quality definitions, dimensions and rules, profiling/baseline, issue prioritization, root cause, prevention/correction, controls, issue management, scorecards, and improvement metrics.

- [x] Baseline-test recurring duplicate and invalid-address failures after a one-time cleanse.
- [x] Initialize and distinguish quality management from MDM implementation.
- [x] Write the playbook with rule schema, assessment, business impact, root-cause tree, remediation/control plan, exception workflow, and trend metrics.
- [x] Validate and behavior-test positive and adjacent-domain cases; save evidence.

---

### Task 15: Create `delivering-data-science`

**Files:** `skills/delivering-data-science/SKILL.md`, `skills/delivering-data-science/references/playbook.md`, `evals/skill-suite/delivering-data-science.md`

**Interfaces:** Consumes DMBOK Chapter 14 plus cross-cutting ethics, security, metadata, and quality dependencies. Produces business hypothesis, data-source justification, experiment/evaluation design, reproducibility, deployment, monitoring, visualization standards, and retirement criteria.

- [x] Baseline-test the production risk-model scenario from Task 1.
- [x] Initialize and distinguish data-science lifecycle from BI reporting and ethics review.
- [x] Write the playbook with hypothesis/data/model cards, evaluation and bias checks, reproducibility evidence, deployment gates, drift/performance monitoring, and rollback/retirement.
- [x] Validate, re-run the baseline scenario with the skill, and save comparative evidence.

---

### Task 16: Create `assessing-data-management-maturity`

**Files:** `skills/assessing-data-management-maturity/SKILL.md`, `skills/assessing-data-management-maturity/references/playbook.md`, `evals/skill-suite/assessing-data-management-maturity.md`

**Interfaces:** Consumes DMBOK Chapter 15. Produces assessment scope, framework-selection rationale, evidence rubric, current/target capability, findings calibration, prioritized improvement program, and reassessment cadence.

- [x] Baseline-test an executive request to assign a single enterprise maturity score in one week.
- [x] Initialize and distinguish maturity assessment from governance implementation and organization design.
- [x] Write the playbook with evidence-strength scale, scoring rubric, interview/document triangulation, target-state rationale, and improvement portfolio selection.
- [x] Validate and test evidence-backed assessment plus score-only anti-pattern handling; save evidence.

---

### Task 17: Create `organizing-data-management`

**Files:** `skills/organizing-data-management/SKILL.md`, `skills/organizing-data-management/references/playbook.md`, `evals/skill-suite/organizing-data-management.md`

**Interfaces:** Consumes DMBOK Chapter 16. Produces current participation map, stakeholder analysis, centralized/decentralized/network/hybrid/federated model selection, committees, role charters, RACI, capability gaps, and interaction model.

- [x] Baseline-test selecting an operating model for a multi-business-unit organization.
- [x] Initialize and distinguish organization design from governance decision processes and change adoption.
- [x] Write the playbook with model-selection criteria, stakeholder map, role/committee charters, interaction map, staffing/skills gaps, and effectiveness metrics.
- [x] Validate and test positive and adjacent-domain cases; save evidence.

---

### Task 18: Create `leading-data-change`

**Files:** `skills/leading-data-change/SKILL.md`, `skills/leading-data-change/references/playbook.md`, `evals/skill-suite/leading-data-change.md`

**Interfaces:** Consumes DMBOK Chapter 17. Produces change case, stakeholder readiness, guiding coalition, vision and communication, participation/training, resistance handling, short-term wins, adoption/diffusion measures, and sustainment.

- [x] Baseline-test low adoption of a newly launched catalog and governance process.
- [x] Initialize and distinguish change/adoption work from organization structure design.
- [x] Write the playbook with stakeholder/readiness map, change narrative, coalition, communications, training/support, resistance log, adoption funnel, reinforcement, and sustainment.
- [x] Validate and behavior-test positive and non-trigger cases; save evidence.

---

### Task 19: Run Integration Evaluations and Final Audit

**Files:**
- Create: `evals/skill-suite/integration-platform.md`
- Create: `evals/skill-suite/integration-master-data.md`
- Create: `evals/skill-suite/integration-risk-model.md`
- Create: `evals/skill-suite/completion-audit.md`
- Modify only if evidence requires it: relevant `skills/*/SKILL.md` or `skills/*/references/playbook.md`

**Interfaces:**
- Consumes: all 17 validated skills and Task 1 baselines.
- Produces: comparative behavioral evidence and a requirement-by-requirement completion audit.

- [x] **Step 1: Run deterministic validation**

  Run all validator unit tests, the suite validator, `quick_validate.py` for every skill, relative-link checks, placeholder scans, and word-count checks. Record exact commands and outputs.

- [x] **Step 2: Re-run the three RED scenarios through the router**

  Each fresh agent must load `managing-data-projects` and only the child playbooks it routes to. Save full outputs and score the same nine dimensions used at baseline.

- [x] **Step 3: Compare baseline and skilled behavior**

  Require every previously missing critical dimension to become `present`, or document a concrete skill correction and re-test it before continuing.

- [x] **Step 4: Review discovery collisions**

  Test at least six ambiguous pairs: governance/organization, architecture/modeling, security/ethics, quality/MDM, integration/storage, and BI/data science. Tighten descriptions until the correct skill is selected.

- [x] **Step 5: Complete the audit**

  In `completion-audit.md`, map every design requirement and plan task to authoritative file or test evidence. Confirm 17 valid skill directories, Chapter 1–17 source coverage, zero broken links/placeholders, and no unverified child skill.
