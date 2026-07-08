# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Terraform CLI availability validation plan | Document planned `terraform version` check. | Terraform CLI availability can be validated without credentials. | `commands.md`, `logs/terraform-provider-validation.log`, `validation.md` |
| V002 | Terraform fmt validation plan | Document planned `terraform fmt -check -recursive` check. | Formatting validation approach is documented. | `commands.md`, `logs/terraform-provider-validation.log`, `validation.md` |
| V003 | Terraform init plan for AWS provider | Define safe AWS provider initialization planning. | AWS provider role is documented without credentials. | `commands.md`, `configs/terraform-provider-structure-summary.md`, `validation.md` |
| V004 | Terraform init plan for AzureRM provider | Define safe AzureRM provider initialization planning. | AzureRM provider role is documented without credentials. | `commands.md`, `configs/terraform-provider-structure-summary.md`, `validation.md` |
| V005 | Terraform init plan for OpenStack provider | Define safe OpenStack provider initialization planning. | OpenStack provider role is documented without credentials. | `commands.md`, `configs/terraform-provider-structure-summary.md`, `validation.md` |
| V006 | Terraform validate plan for each provider environment | Define validation checks for AWS, AzureRM, and OpenStack environment boundaries. | Provider environments have separate validation plans. | `commands.md`, `logs/terraform-provider-validation.log`, `validation.md` |
| V007 | Provider version pinning check | Review required provider constraints. | Provider versions are pinned or constrained intentionally. | `configs/terraform-provider-structure-summary.md`, `validation.md` |
| V008 | Provider credential hardcoding check | Review provider structure for hardcoded secrets or account-specific values. | No credentials, keys, tokens, account IDs, subscription IDs, tenant IDs, or passwords are hardcoded. | `configs/terraform-provider-structure-summary.md`, `validation.md` |
| V009 | tfstate exclusion check | Review `.gitignore` and repository state policy. | Terraform state files and `.terraform/` directories are excluded from commit. | `configs/gitignore-tfstate-check.md`, `validation.md` |
| V010 | Missing provider, invalid provider version, or credential exposure failure condition | Define explicit failure criteria. | Missing provider, invalid version policy, or credential exposure produces `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. AWS, AzureRM, and OpenStack provider roles must remain separated in future Terraform structure and validation evidence.
