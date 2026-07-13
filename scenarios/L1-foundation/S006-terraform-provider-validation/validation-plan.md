# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Provider directory | Test the provider-validation path. | Directory exists. | `logs/terraform-provider-validation.log`, `configs/terraform-provider-baseline-summary.md` |
| V002 | Required files | Test `versions.tf`, `providers.tf`, and `README.md`. | All required files exist. | `logs/terraform-provider-validation.log`, `configs/terraform-provider-baseline-summary.md` |
| V003 | Terraform version constraint | Search `versions.tf` for `required_version`. | An explicit constraint exists. | `logs/terraform-provider-validation.log`, `configs/terraform-provider-baseline-summary.md` |
| V004 | Required providers block | Search `versions.tf` for `required_providers`. | The block exists. | `logs/terraform-provider-validation.log`, `configs/terraform-provider-baseline-summary.md` |
| V005 | AWS provider source | Verify the AWS source. | `hashicorp/aws` is declared. | `logs/terraform-provider-validation.log`, `configs/terraform-provider-baseline-summary.md` |
| V006 | AzureRM provider source | Verify the AzureRM source. | `hashicorp/azurerm` is declared. | `logs/terraform-provider-validation.log`, `configs/terraform-provider-baseline-summary.md` |
| V007 | OpenStack provider source | Verify the OpenStack source. | `terraform-provider-openstack/openstack` is declared. | `logs/terraform-provider-validation.log`, `configs/terraform-provider-baseline-summary.md` |
| V008 | Provider version constraints | Inspect all three required-provider entries. | Every provider has a version constraint. | `logs/terraform-provider-validation.log`, `configs/terraform-provider-baseline-summary.md` |
| V009 | Provider blocks | Inspect `providers.tf`. | Non-authenticating blocks exist for all providers. | `logs/terraform-provider-validation.log`, `configs/terraform-provider-baseline-summary.md` |
| V010 | Generated Terraform artifacts | Scan for real tfvars, state, auto tfvars, and `.terraform`. | No forbidden artifact exists. | `logs/terraform-provider-validation.log`, `configs/terraform-provider-baseline-summary.md` |
| V011 | Remote backend | Search provider files for backend blocks. | No backend block exists. | `logs/terraform-provider-validation.log`, `configs/terraform-provider-baseline-summary.md` |
| V012 | Credential and account content | Scan provider files for credentials, private keys, access keys, UUIDs, and account assignments. | No forbidden content is detected. | `logs/terraform-provider-validation.log`, `configs/terraform-provider-baseline-summary.md` |
| V013 | Safety boundary documentation | Check the provider README for required boundary statements. | Authentication, backend, and execution boundaries are documented. | `logs/terraform-provider-validation.log`, `configs/terraform-provider-baseline-summary.md` |
| V014 | Terraform formatting | Run `terraform fmt -check` only when Terraform exists. | Formatting passes or absence is recorded as a warning. | `logs/terraform-provider-validation.log`, `configs/terraform-provider-baseline-summary.md` |
| V015 | Terraform provider validation boundary | Record the initialization and authentication boundary. | Runtime validation is skipped. | `logs/terraform-provider-validation.log`, `configs/terraform-provider-baseline-summary.md` |

## Review Notes

V001-V013 are required checks. V014-V015 are informational readiness checks and do not trigger a non-zero exit.
