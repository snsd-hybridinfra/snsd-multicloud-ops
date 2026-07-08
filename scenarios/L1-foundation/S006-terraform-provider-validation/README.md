# S006-terraform-provider-validation

| Field | Value |
|---|---|
| Scenario ID | S006 |
| Scenario Name | Terraform Provider Validation |
| Level | L1 Foundation Validation |
| Category | Foundation |
| Primary Domain | Terraform provider structure readiness |
| Related Components | AWS provider, AzureRM provider, OpenStack provider, provider version pinning, environment separation, Terraform init, Terraform validate, Terraform fmt, credential exclusion, tfstate exclusion |
| Validation Type | Infrastructure Validation |
| Evidence Directory | evidence/L1-foundation/S006-terraform-provider-validation/ |
| Status | PLANNED |

## Objective Summary

Define and validate the Terraform provider structure required for AWS, Azure, and OpenStack provisioning in the SNSD Multi-Cloud Ops project.

## Scope Summary

This scenario validates provider structure and safety policy only. It does not create provider credentials, execute real cloud authentication, create tfstate, or implement real Terraform provider resources.

## Related Components

- AWS provider placeholder
- AzureRM provider placeholder
- OpenStack provider placeholder
- Provider version pinning strategy
- Environment-specific provider separation
- `.gitignore` tfstate exclusion policy

## Validation Summary

Validation checks cover Terraform CLI availability, `terraform fmt`, provider initialization planning for AWS, AzureRM, and OpenStack, provider-specific validation planning, provider version pinning, hardcoded credential detection, tfstate exclusion, and failure conditions.

## Evidence Output Summary

Evidence must be recorded under `evidence/L1-foundation/S006-terraform-provider-validation/`, with command plans in `commands.md` and validation results in `validation.md`.
