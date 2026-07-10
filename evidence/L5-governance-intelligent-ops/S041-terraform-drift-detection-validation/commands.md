# Commands

Scenario: S041-terraform-drift-detection-validation
Level: L5-governance-intelligent-ops
Capability: Terraform Drift Detection Validation

Record approved commands or manual actions used during validation. Do not include real Terraform output yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Command Records

| Check ID | Purpose | Planned Command Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Review Terraform working directory placeholder. | `Get-ChildItem <terraform-env>` or approved equivalent | `<terraform-env>` | `configs/terraform-drift-detection-summary.md` |
| V002 | Validate Terraform init placeholder flow without real backend credentials. | `terraform init -backend=false` or approved placeholder | `<terraform-env>` | `logs/terraform-drift-detection-validation.log` |
| V003 | Validate Terraform configuration placeholder flow. | `terraform validate` or approved placeholder | `<terraform-env>` | `logs/terraform-drift-detection-validation.log` |
| V004 | Review plan-based drift detection behavior. | `terraform plan -refresh-only` or approved placeholder | `<terraform-env>` | `screenshots/terraform-plan-no-drift.png`, `screenshots/terraform-plan-drift-detected.png` |
| V005 | Map AWS drift placeholder. | Review `<provider>` and `<drifted-resource>` mapping | AWS placeholder resource | `configs/terraform-drift-target-mapping.md` |
| V006 | Map Azure drift placeholder. | Review `<provider>` and `<drifted-resource>` mapping | Azure placeholder resource | `configs/terraform-drift-target-mapping.md` |
| V007 | Map OpenStack drift placeholder. | Review `<provider>` and `<drifted-resource>` mapping | OpenStack placeholder resource | `configs/terraform-drift-target-mapping.md` |
| V008 | Reference security rule drift detection boundary. | Compare expected and actual rule placeholders | Security rule placeholder | `configs/terraform-drift-detection-summary.md` |
| V009 | Compare tag or label drift placeholders. | Compare `<expected-state>` and `<actual-state>` | `<resource-name>` | `configs/terraform-drift-target-mapping.md` |
| V010 | Apply drift judgment state. | Classify result as `NO_DRIFT`, `DRIFT_DETECTED`, `INCONCLUSIVE`, or `OUT_OF_SCOPE` | `<drifted-resource>` | `configs/terraform-drift-judgment-model.md` |
| V011 | Capture drift evidence set. | Record commands, sanitized outputs, screenshots, and reviewer notes | S041 evidence directory | `validation.md`, `logs/terraform-drift-detection-validation.log` |

## Drift Judgment Placeholder

```text
Terraform environment: <terraform-env>
Provider: <provider>
Resource: <resource-name>
Drifted resource: <drifted-resource>
Expected state: <expected-state>
Actual state: <actual-state>
Judgment: TODO (NO_DRIFT | DRIFT_DETECTED | INCONCLUSIVE | OUT_OF_SCOPE)
Reviewer: TODO
Timestamp: TODO
```

## Output Placeholder

```text
TODO: Paste sanitized Terraform command summaries or manual validation notes here after execution.
TODO: Do not paste real credentials, backend configuration, tfstate content, account IDs, subscription IDs, tenant IDs, kubeconfig content, or private keys.
```
