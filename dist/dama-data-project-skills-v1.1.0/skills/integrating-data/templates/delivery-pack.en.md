# Data Integration Delivery Pack

Skill: `integrating-data`

[Word report](report.en.docx) · [Excel register](register.en.xlsx)

## Record details

| ID | Field | Project value |
| --- | --- | --- |
| `artifact_id` | Artifact ID | |
| `project` | Project | |
| `skill` | Skill | |
| `version` | Version | |
| `date` | Date | |
| `status` | Status | |
| `author` | Author | |
| `owner` | Owner | |
| `approver` | Approver | |
| `purpose` | Purpose | |
| `business_outcome` | Business outcome | |
| `scope` | Scope and exclusions | |
| `source_inputs` | Inputs and sources | |
| `assumptions` | Assumptions and constraints | |
| `decisions` | Decisions | |
| `rationale` | Rationale | |
| `risks` | Risks | |
| `exceptions` | Exceptions | |
| `open_items` | Open items | |
| `due_date` | Due date | |
| `acceptance_criteria` | Acceptance criteria | |
| `evidence_location` | Evidence location | |
| `reviewer_decision` | Reviewer decision | |
| `next_gate` | Next stage gate | |

## Domain analysis and decisions

### Scope and business requirements (`scope`)

Define sources, consumers, latency, completeness, and failure tolerance.

> Enter project evidence, conclusion, and owner.


### Source capability and pattern choice (`source_capability`)

Compare batch, CDC, streaming, API, or sharing against constraints.

> Enter project evidence, conclusion, and owner.


### Versioned interface contract (`interface_contract`)

Define owner, schema, semantics, SLA, version, and change notice.

> Enter project evidence, conclusion, and owner.


### Mapping and lineage (`mapping`)

Record field transformations, quality rules, target meaning, and provenance.

> Enter project evidence, conclusion, and owner.


### Failure isolation and replay (`replay`)

Set idempotency, ordering, retry, dead letter, replay, and manual recovery.

> Enter project evidence, conclusion, and owner.


### Schema evolution (`schema_evolution`)

Define compatibility window, breaking-change approval, and consumer migration.

> Enter project evidence, conclusion, and owner.


### Reconciliation and quality (`reconciliation`)

Reconcile records, business totals, rejects, latency, and exception closure.

> Enter project evidence, conclusion, and owner.


### Operations and acceptance (`operations`)

Define alerts, operations owner, stage gates, and consumer acceptance evidence.

> Enter project evidence, conclusion, and owner.


## Working registers

### Source Target Mapping (`mappings`)

Maintain field meaning, transformations, and tests.

| Source field (`source_field`) | Target field (`target_field`) | Transformation (`transformation`) | Rule (`rule`) | Owner (`owner`) | Test (`test`) | Version (`version`) |
| --- | --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |   |   |

### Reconciliation (`reconciliation`)

Record reconciliation differences, isolation, and recovery evidence.

| Source (`source`) | Target state (`target`) | Rule (`rule`) | Test result (`test_result`) | Impact (`impact`) | Owner (`owner`) | Evidence (`evidence`) | Status (`status`) |
| --- | --- | --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |   |   |   |
