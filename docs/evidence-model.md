# Evidence Model

## Current Truth State

S002 and S005 have `READY` sanitized evidence packages. S002 is based on
authorized operator-executed lab validation. S005 combines operator-executed
deployment/data-plane evidence with Codex-executed forced-command read-only
corroboration. Other packages remain unchanged.
Repository/document lint results are not scenario evidence. Static examples,
synthetic output, sample terminal text, and provenance-uncertain material
cannot be promoted without an observed execution and provenance record.

Operator-supplied runtime results may support validation when their command
context is identifiable, pass criteria are satisfied, corroborating
control-plane/data-plane observations agree, contradictions are resolved, and
sensitive values are removed. The evidence must state whether Codex only
normalized the supplied result or also executed a separately authorized
restricted live check.

Evidence proves that a scenario was executed and validated. It must be reproducible, reviewable, and mapped to validation criteria.

Screenshots alone are not enough. Every evidence item must be linked to a scenario and explain what it proves.

## Evidence Directory Rule

Each scenario must have a matching evidence directory using the same level and scenario directory name.

Example:

```text
scenarios/L1-foundation/S001-control-plane-toolchain-validation/
evidence/L1-foundation/S001-control-plane-toolchain-validation/
```

## Required Evidence Files

Every evidence directory must include:

- `commands.md`
- `validation.md`
- `logs/.gitkeep`
- `screenshots/.gitkeep`
- `configs/.gitkeep`

## Evidence File Purpose

`commands.md` records:

- commands executed
- execution timestamp
- target host or environment
- expected purpose of each command

`validation.md` records:

- validation criteria
- expected result
- actual result
- a Validation Result Status
- evidence reference

`logs/` stores applicable text logs, including:

- tool execution logs
- Terraform logs
- Ansible logs
- Kubernetes command output
- Prometheus or Grafana related logs where applicable

`screenshots/` stores applicable screenshots, including:

- console screenshots
- Grafana dashboard screenshots
- Prometheus target screenshots
- cloud resource screenshots where applicable

`configs/` stores sanitized configuration snapshots only. Do not include secrets, credentials, private keys, or account-specific sensitive data.

## Evidence Naming Rule

Use clear kebab-case filenames.

Examples:

- `terraform-plan-output.md`
- `ansible-playbook-result.md`
- `kubectl-get-pods.md`
- `prometheus-targets.md`
- `grafana-dashboard-screenshot.png`
- `db-replication-status.md`
- `security-policy-validation.md`

## Evidence Readiness Status

`docs/evidence-status-matrix.md` tracks whether the required evidence set is
complete enough for review:

- `NOT_READY`: required evidence has not been collected.
- `PARTIAL`: some required evidence exists, but gaps remain.
- `READY`: all required evidence exists and is ready for review.
- `REVIEWED`: a reviewer has checked the complete evidence set.

## Validation Result Status

Individual `validation.md` checks record the outcome of execution:

- `NOT_RUN`: the validation has not been executed.
- `PASS`: the expected result was observed.
- `FAIL`: the expected result was not observed.
- `BLOCKED`: a dependency or access issue prevented execution.
- `INCONCLUSIVE`: execution occurred, but the evidence cannot support a result.

Evidence Readiness Status and Validation Result Status are related but distinct:
readiness describes the completeness of the evidence package, while result
status describes the outcome of a validation check.

## Validation Table Template

Use this table in `validation.md`:

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|

## Evidence Quality Rule

Evidence must be:

- specific
- timestamped when possible
- sanitized
- scenario-mapped
- repeatable
- minimal but sufficient

## Zero Trust Capability and Maturity Evidence

Zero Trust assessment records must identify the capability ID, authoritative
source table, bounded environment, evaluator, validation authority, evidence
date, evidence level, exceptions, and gaps.

- Source authority: the local `제로트러스트 가이드라인 2.0` PDF defines
  terminology and maturity characteristics.
- Evidence authority uses exactly: `USER_EXECUTED_RUNTIME`,
  `CODEX_EXECUTED_LOCAL`, `CODEX_EXECUTED_LIVE_RUNTIME`, `DESIGN_ONLY`,
  `CONFIGURATION_ONLY`, or `MISSING`.
- `DESIGN` evidence supports alignment only.
- `CONFIGURATION` evidence supports bounded implementation but not behavior.
- `RUNTIME` evidence supports only the observed paths and time window.
- `CONTINUOUS` evidence requires repeated or continuously collected coverage
  with review rules.

Scenario `VALIDATED` status does not automatically validate every mapped Zero
Trust capability and never assigns a maturity level by itself.

## Prohibited Evidence

Do not commit:

- real credentials
- private keys
- cloud account IDs
- subscription IDs
- tenant IDs
- real public IPs unless intentionally sanitized
- Terraform state files
- kubeconfig files
- `.env` files
- binary archives
- unexplained screenshots

Non-executed or provenance-uncertain material must be removed from the active
scenario evidence path or placed under `quarantine/non-authoritative-evidence/`.
Quarantined material is historical context only and must never support a PASS,
READY, IMPLEMENTED, PARTIAL, or VALIDATED claim.

## Evidence Review Checklist

- [ ] Does the evidence map to a scenario?
- [ ] Does the evidence map to validation criteria?
- [ ] Is the result clearly `PASS` or `FAIL` when execution is complete?
- [ ] Are commands recorded?
- [ ] Are sensitive values removed?
- [ ] Are screenshots explained?
- [ ] Can another reviewer understand the result?
