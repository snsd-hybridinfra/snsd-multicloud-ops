# Terraform Drift Remediation Validation

> SAMPLE / NON-PRODUCTION — static remediation evidence only.

## Purpose and S041 Relationship

S042 validates decisions made after S041 identifies `<drift-detection-id-placeholder>` for `<terraform-environment>`, `<terraform-module-placeholder>`, `<cloud-provider-placeholder>`, and `<terraform-resource-address-placeholder>`. It does not execute remediation.

## Decision Model

- Option A — `REVERT_TO_TERRAFORM`: propose returning `<observed-value-placeholder>` to `<expected-value-placeholder>`.
- Option B — `CODIFY_APPROVED_CHANGE`: propose updating declared code to an approved `<remediated-value-placeholder>`.
- Option C — `INVESTIGATE_ONLY` or `REJECT_CHANGE`: stop for manual investigation.
- A documented exception may use `ACCEPT_DOCUMENTED_EXCEPTION`.

Medium, High, and Critical drift requires `<approval-id-placeholder>` and risk review. Every plan requires `<remediation-change-id-placeholder>`, a prior `<rollback-change-id-placeholder>`, post-remediation no-drift evidence, and `<evidence-path>`.

Static validation checks documentation and sanitized samples. It differs from real Terraform remediation because no plan, apply, provider, state, or cloud operation is run.

## Out of Scope

- `terraform apply`, `terraform destroy`, `terraform import`, `terraform state rm`, `terraform state mv`, and `terraform force-unlock`
- Real or automatic remediation and cloud API mutation
- Production backend access, tfstate inspection, or credentialed provider execution
