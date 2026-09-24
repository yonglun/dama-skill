# Master and Reference Data Pack

Skill: `managing-reference-and-master-data`

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

### Domain charter (`domain_charter`)

Define the shared entity or code set, business use, owner, and consumers.

> Enter project evidence, conclusion, and owner.


### Sources and authority (`authority`)

Assign authoritative sources, adjudication rights, and distribution by attribute or event.

> Enter project evidence, conclusion, and owner.


### Global identity and crosswalk (`global_identity`)

Define global IDs, local-ID crosswalks, creation, and retirement rules.

> Enter project evidence, conclusion, and owner.


### Golden record and survivorship (`survivorship`)

Specify source precedence, recency, conflicts, human adjudication, and traceability.

> Enter project evidence, conclusion, and owner.


### Match merge and split (`merge_split`)

Cover false-merge safeguards, reversible splits, versions, and independent tests.

> Enter project evidence, conclusion, and owner.


### Hierarchies and reference codes (`hierarchies`)

Set hierarchy changes, code-set versions, effective dates, and backward compatibility.

> Enter project evidence, conclusion, and owner.


### Distribution and acknowledgment (`distribution`)

Define publication contracts, consumer acknowledgments, reconciliation, and correction.

> Enter project evidence, conclusion, and owner.


### Quality and operating acceptance (`acceptance_evidence`)

List stewardship workflow, quality measures, exceptions, and gate evidence.

> Enter project evidence, conclusion, and owner.


## Working registers

### Identity Crosswalk (`crosswalk`)

Record local identities against governed global identities.

| Source (`source`) | Source ID (`source_id`) | Global ID (`global_id`) | Match rule (`match_rule`) | Owner (`owner`) | Status (`status`) | Evidence (`evidence`) |
| --- | --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |   |   |

### Match Decisions (`decisions`)

Track merge/split decisions and false-match recovery evidence.

| Source ID (`source_id`) | Global ID (`global_id`) | Decision (`decision`) | Rationale (`rationale`) | Approver (`approver`) | Test (`test`) | Evidence (`evidence`) |
| --- | --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |   |   |
