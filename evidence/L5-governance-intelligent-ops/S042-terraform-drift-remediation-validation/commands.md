# Commands

Scenario: S042-terraform-drift-remediation-validation
Level: L5-governance-intelligent-ops
Capability: Terraform Drift Remediation Validation

Record approved commands or manual actions used during validation. Do not include real Terraform output yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Command Records

| Check ID | Purpose | Planned Command Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Reference prior drift detection evidence. | Review S041 `validation.md` and sanitized drift summary | S041 evidence directory | `configs/terraform-drift-remediation-summary.md` |
| V002 | Review plan before remediation. | `terraform plan` placeholder; do not run against real accounts | `<terraform-env>` | `logs/terraform-drift-remediation-validation.log`, `screenshots/terraform-plan-before-remediation.png` |
| V003 | Record remediation decision point. | Review `<remediation-plan>` and approval placeholder | `<drifted-resource>` | `configs/terraform-remediation-decision-model.md` |
| V004 | Document apply placeholder behavior. | `terraform apply <remediation-plan>` placeholder only; do not execute | `<terraform-env>` | `logs/terraform-drift-remediation-validation.log` |
| V005 | Map AWS remediation placeholder. | Review AWS Security Group drift remediation placeholder | AWS placeholder resource | `configs/terraform-remediation-target-mapping.md` |
| V006 | Map Azure remediation placeholder. | Review Azure NSG drift remediation placeholder | Azure placeholder resource | `configs/terraform-remediation-target-mapping.md` |
| V007 | Map OpenStack remediation placeholder. | Review OpenStack Security Group drift remediation placeholder | OpenStack placeholder resource | `configs/terraform-remediation-target-mapping.md` |
| V008 | Reference security rule remediation boundary. | Review security rule drift placeholder and S037 boundary | Security rule placeholder | `configs/terraform-drift-remediation-summary.md` |
| V009 | Compare tag or label remediation placeholders. | Compare `<expected-state>`, `<actual-state>`, and `<remediation-plan>` | `<resource-name>` | `configs/terraform-remediation-target-mapping.md` |
| V010 | Review post-remediation plan placeholder. | `terraform plan` placeholder after remediation; do not run against real accounts | `<terraform-env>` | `screenshots/terraform-plan-after-remediation.png` |
| V011 | Apply remediation judgment state. | Classify result as `REMEDIATION_READY`, `REMEDIATION_APPLIED`, `REMEDIATION_BLOCKED`, `REMEDIATION_FAILED`, or `OUT_OF_SCOPE` | `<drifted-resource>` | `configs/terraform-remediation-decision-model.md`, `screenshots/terraform-remediation-judgment.png` |
| V012 | Capture remediation evidence set. | Record commands, sanitized outputs, screenshots, and reviewer notes | S042 evidence directory | `validation.md`, `logs/terraform-drift-remediation-validation.log` |

## Remediation Decision Placeholder

```text
Terraform environment: <terraform-env>
Provider: <provider>
Resource: <resource-name>
Drifted resource: <drifted-resource>
Expected state: <expected-state>
Actual state: <actual-state>
Remediation plan: <remediation-plan>
Decision: TODO (REMEDIATION_READY | REMEDIATION_APPLIED | REMEDIATION_BLOCKED | REMEDIATION_FAILED | OUT_OF_SCOPE)
Manual approval placeholder: TODO
Reviewer: TODO
Timestamp: TODO
```

## Output Placeholder

```text
TODO: Paste sanitized Terraform remediation summaries or manual validation notes here after execution approval.
TODO: Do not paste real credentials, backend configuration, tfstate content, account IDs, subscription IDs, tenant IDs, kubeconfig content, private keys, public IPs, or account-specific values.
```
