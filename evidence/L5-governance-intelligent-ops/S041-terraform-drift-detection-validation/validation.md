# Validation

Scenario: S041-terraform-drift-detection-validation
Level: L5-governance-intelligent-ops
Capability: Terraform Drift Detection Validation

| Field | Value |
| --- | --- |
| Result | PARTIAL |
| Reviewer | TBD |
| Date | TBD |
| Follow-up | Collect sanitized Terraform drift detection evidence after execution approval. |

No real Terraform output has been collected yet. This file defines the validation skeleton and TODO evidence expectations.

## Validation Checks

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Terraform working directory validation plan | `<terraform-env>` is identified and contains only placeholder-safe references. | TODO | PARTIAL | `commands.md`, `configs/terraform-drift-detection-summary.md` |
| V002 | Terraform init placeholder validation plan | Init flow is documented without real backend credentials or generated tfstate. | TODO | PARTIAL | `commands.md`, `logs/terraform-drift-detection-validation.log` |
| V003 | Terraform validate placeholder validation plan | Validate flow is documented for the placeholder Terraform environment. | TODO | PARTIAL | `commands.md`, `logs/terraform-drift-detection-validation.log` |
| V004 | Terraform plan drift detection validation plan | Plan output review can distinguish no-drift and drift-detected cases. | TODO | PARTIAL | `commands.md`, `screenshots/terraform-plan-no-drift.png`, `screenshots/terraform-plan-drift-detected.png` |
| V005 | AWS drift placeholder validation plan | AWS Security Group drift placeholder is mapped without real account values. | TODO | PARTIAL | `configs/terraform-drift-target-mapping.md` |
| V006 | Azure drift placeholder validation plan | Azure NSG drift placeholder is mapped without subscription or tenant values. | TODO | PARTIAL | `configs/terraform-drift-target-mapping.md` |
| V007 | OpenStack drift placeholder validation plan | OpenStack Security Group drift placeholder is mapped without clouds.yaml or openrc content. | TODO | PARTIAL | `configs/terraform-drift-target-mapping.md` |
| V008 | Security rule drift detection reference plan | Security drift is detected here and response remains assigned to S037 or S042 as applicable. | TODO | PARTIAL | `configs/terraform-drift-detection-summary.md` |
| V009 | Tag or label drift detection plan | `<expected-state>` and `<actual-state>` placeholders can be compared. | TODO | PARTIAL | `configs/terraform-drift-target-mapping.md` |
| V010 | Drift judgment state validation plan | Result is classified as `NO_DRIFT`, `DRIFT_DETECTED`, `INCONCLUSIVE`, or `OUT_OF_SCOPE`. | TODO | PARTIAL | `configs/terraform-drift-judgment-model.md` |
| V011 | Drift evidence capture plan | Commands, validation notes, sanitized logs, summaries, and screenshots are mapped. | TODO | PARTIAL | `commands.md`, `logs/terraform-drift-detection-validation.log` |
| V012 | Failure condition review | Missing baseline, missing plan output, undetected manual change, ambiguous result, real credentials, committed tfstate, or missing evidence produces `FAIL` or `BLOCKED`. | TODO | PARTIAL | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs captured: NOT_READY
- Terraform drift detection summary: NOT_READY
- Terraform drift judgment model: NOT_READY
- Terraform drift target mapping: NOT_READY
- Terraform drift detection log: NOT_READY
- Terraform plan screenshots captured: NOT_READY

## Drift Judgment States

- `NO_DRIFT`: Terraform planned state and actual state match.
- `DRIFT_DETECTED`: Terraform plan or manual comparison indicates a difference between expected and actual state.
- `INCONCLUSIVE`: Evidence is insufficient or ambiguous.
- `OUT_OF_SCOPE`: The finding belongs to remediation, policy-as-code, Kubernetes manifest policy, security misconfiguration response, or cost guardrail validation.

## Boundary Notes

This scenario validates detection only. It does not perform automated remediation, run real Terraform against cloud accounts, create Terraform modules, create tfstate, or introduce Terraform Cloud, Spacelift, Atlantis, GitOps, or any new governance tooling.
