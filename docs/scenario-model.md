# Scenario Model

Scenario-based validation is the main repository method. Each scenario is a controlled test of one operational capability and must produce reviewable evidence.

## Scenario Format

Each scenario should include:

- `id`: stable scenario ID
- `title`: short descriptive name
- `level`: one of the five validation levels
- `objective`: behavior being validated
- `scope`: allowed systems and files
- `prerequisites`: required setup
- `steps`: validation procedure
- `evidence`: required artifacts
- `pass_criteria`: measurable pass conditions

## Core Scenario Set

### L1 Foundation

- `L1-S01`: Repository structure validation
- `L1-S02`: Scope lock review
- `L1-S03`: Excluded scope review
- `L1-S04`: Naming convention validation
- `L1-S05`: Evidence model validation
- `L1-S06`: ADR workflow readiness
- `L1-S07`: Scenario template readiness
- `L1-S08`: Directory ownership mapping
- `L1-S09`: Git ignore safety validation
- `L1-S10`: Codex workflow validation

### L2 Security Baseline

- `L2-S01`: Identity baseline review
- `L2-S02`: Access policy baseline review
- `L2-S03`: Network segmentation baseline review
- `L2-S04`: Firewall policy baseline review
- `L2-S05`: Kubernetes security baseline review
- `L2-S06`: Secret-handling control review
- `L2-S07`: Host hardening baseline review
- `L2-S08`: Logging baseline review
- `L2-S09`: Vulnerability management baseline review
- `L2-S10`: Compliance control mapping review

### L3 Service Operations

- `L3-S01`: Service deployment procedure validation
- `L3-S02`: Namespace operation validation
- `L3-S03`: Workload operation validation
- `L3-S04`: Ingress operation validation
- `L3-S05`: Traffic routing validation
- `L3-S06`: Observability dashboard validation
- `L3-S07`: Metrics exporter validation
- `L3-S08`: Configuration change validation
- `L3-S09`: Runbook execution validation
- `L3-S10`: Operational handoff validation

### L4 Failure Recovery

- `L4-S01`: Failure injection procedure validation
- `L4-S02`: Service restart recovery validation
- `L4-S03`: Network path failure validation
- `L4-S04`: Firewall policy rollback validation
- `L4-S05`: Kubernetes workload recovery validation
- `L4-S06`: Configuration restore validation
- `L4-S07`: Backup evidence validation
- `L4-S08`: Recovery time objective review
- `L4-S09`: Recovery point objective review
- `L4-S10`: Incident runbook validation

### L5 Governance Intelligent Ops

- `L5-S01`: Cost tagging policy validation
- `L5-S02`: Cost anomaly review
- `L5-S03`: Governance policy validation
- `L5-S04`: Compliance reporting validation
- `L5-S05`: Security dataset readiness
- `L5-S06`: ML security script review
- `L5-S07`: Model artifact governance review
- `L5-S08`: Intelligent alert triage validation
- `L5-S09`: Executive report evidence validation
- `L5-S10`: Continuous improvement review

## Status Values

Use `planned`, `ready`, `running`, `passed`, `partial`, `failed`, or `retired`.
