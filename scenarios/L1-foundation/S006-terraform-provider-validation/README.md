# S006-terraform-provider-validation

| Field | Value |
|---|---|
| Scenario ID | S006 |
| Scenario Name | Terraform Provider Validation |
| Level | L1 Foundation Validation |
| Category | Foundation |
| Primary Domain | Repository-side Terraform provider declarations |
| Related Components | AWS, AzureRM, and OpenStack provider baselines; local safety validator |
| Validation Type | Infrastructure Validation |
| Evidence Directory | evidence/L1-foundation/S006-terraform-provider-validation/ |
| Status | VALIDATED |

## Objective Summary

Validate that AWS, AzureRM, and OpenStack Terraform providers are declared with explicit sources and version constraints without credentials, backend state, initialization, or cloud authentication.

## Scope Summary

S006 checks required provider files, Terraform and provider constraints, provider blocks, unsafe generated artifacts, backend configuration, credential-like content, account assignments, and documented safety boundaries.

## Related Components

- `terraform/envs/provider-validation/`
- `tools/validate-terraform-provider-baseline.ps1`

## Validation Summary

Required repository checks determine success. Terraform formatting is optional when the CLI exists. Runtime provider validation is skipped because S006 prohibits initialization, provider download, credential access, and external authentication.

## Evidence Output Summary

- `logs/terraform-provider-validation.log`
- `configs/terraform-provider-baseline-summary.md`
- `commands.md`
- `validation.md`
