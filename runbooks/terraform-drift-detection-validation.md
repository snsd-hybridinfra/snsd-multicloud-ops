# Terraform Drift Detection Validation

> SAMPLE / NON-PRODUCTION — static evidence model only.

## Purpose

S041 validates that a sanitized Terraform plan can distinguish declared state from an observed-infrastructure placeholder without running Terraform or reading state. Drift means the declared configuration for `<terraform-environment>` and `<terraform-module-placeholder>` differs from the observed value represented in approved lab evidence.

## Workflow

1. Identify `<cloud-provider-placeholder>` and `<terraform-resource-address-placeholder>`.
2. Record `<expected-value-placeholder>` as declared state and `<observed-value-placeholder>` as the observed-state placeholder.
3. Review sanitized `terraform plan -detailed-exitcode` evidence: `0` means no changes, `1` means plan error, and `2` means changes are present.
4. Classify create, update, replace, delete, security exposure, tag, route, provider, or backend mismatch signals.
5. Record `<drift-change-id-placeholder>`, `<drift-severity-placeholder>`, and `<evidence-path>`.
6. Escalate security/public exposure drift and route remediation to S042.

An unauthorized manual change is a drift candidate, not proof of malicious activity. Severity is Critical for public/security exposure, High for destructive replacement, Medium for material configuration change, and Low for tag-only drift, subject to review.

## Evidence Model

Evidence contains sanitized text/JSON, classification, manifest, and final judgment only. Static validation differs from real plan execution: the validator reads repository files and never contacts providers or remote state.

## Out of Scope

- `terraform apply`, `terraform destroy`, `terraform import`, `terraform state rm`, `terraform state mv`, and `terraform force-unlock`
- Real cloud drift remediation or cloud API mutation
- Production backend access, tfstate inspection, or credentialed provider execution
- Real Terraform plan execution; remediation is owned by S042
