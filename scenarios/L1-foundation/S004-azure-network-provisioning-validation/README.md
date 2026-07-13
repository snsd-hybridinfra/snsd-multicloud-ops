# S004-azure-network-provisioning-validation

| Field | Value |
|---|---|
| Scenario ID | S004 |
| Scenario Name | Azure Network Provisioning Validation |
| Level | L1 Foundation Validation |
| Category | Foundation |
| Primary Domain | Repository-side Azure network definitions |
| Related Components | Azure network Terraform module, validation environment, local safety validator |
| Validation Type | Infrastructure Validation |
| Evidence Directory | evidence/L1-foundation/S004-azure-network-provisioning-validation/ |
| Status | VALIDATED |

## Objective Summary

Validate that Azure network provisioning is represented by reviewable Terraform definitions without authenticating to Azure or creating resources.

## Scope Summary

S004 checks required files, Azure resource block types, safe example values, absence of state and real variable files, absence of backend and identity configuration, and absence of credential-like content.

## Related Components

- `terraform/modules/azure-network/`
- `terraform/envs/azure-network-validation/`
- `tools/validate-azure-network-provisioning.ps1`

## Validation Summary

Required repository checks determine success. Terraform formatting is optional when the CLI exists. Provider-dependent validation is skipped because S004 prohibits initialization, authentication, and Azure API access.

## Evidence Output Summary

- `logs/azure-network-provisioning-validation.log`
- `configs/azure-network-provisioning-summary.md`
- `commands.md`
- `validation.md`
