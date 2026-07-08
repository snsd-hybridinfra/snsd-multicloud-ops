# Commands

Scenario: S006-terraform-provider-validation
Level: L1-foundation
Capability: Terraform Provider Validation
Target: `<target-node>`
Execution timestamp: TODO

Record sanitized output only. Do not include AWS credentials, Azure credentials, OpenStack credentials, tokens, tfstate, private keys, account IDs, subscription IDs, tenant IDs, project IDs, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | Terraform CLI availability validation plan | `terraform version` | Confirm Terraform CLI version can be captured safely. | TODO: record sanitized output after approved execution. |
| V002 | Terraform fmt validation plan | `terraform fmt -check -recursive` | Confirm Terraform formatting check plan. | TODO: record sanitized output after approved execution. |
| V003 | Terraform init plan for AWS provider | `terraform init` in future approved AWS provider validation path | Confirm AWS provider initialization plan without credentials. | TODO: record sanitized output after approved execution. |
| V004 | Terraform init plan for AzureRM provider | `terraform init` in future approved AzureRM provider validation path | Confirm AzureRM provider initialization plan without credentials. | TODO: record sanitized output after approved execution. |
| V005 | Terraform init plan for OpenStack provider | `terraform init` in future approved OpenStack provider validation path | Confirm OpenStack provider initialization plan without credentials. | TODO: record sanitized output after approved execution. |
| V006 | Terraform validate plan for each provider environment | `terraform validate` in each future approved provider validation path | Confirm validation plan for AWS, AzureRM, and OpenStack environment boundaries. | TODO: record sanitized output after approved execution. |
| V007 | Provider version pinning check | Review required provider constraints in Terraform provider structure. | Confirm provider versions are pinned or constrained intentionally. | TODO: record sanitized result after review. |
| V008 | Provider credential hardcoding check | Review provider files for hardcoded credential patterns. | Confirm no credentials or account-specific values are hardcoded. | TODO: record sanitized result after review. |
| V009 | tfstate exclusion check | Review `.gitignore` and Terraform state exclusion policy. | Confirm tfstate and `.terraform/` paths are excluded. | TODO: record sanitized result after review. |
| V010 | Missing provider, invalid provider version, or credential exposure failure condition | Review failed provider validation findings. | Confirm failure criteria produce `FAIL` or `BLOCKED` status. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/terraform-provider-structure-summary.md`
- `logs/terraform-provider-validation.log`
- `configs/gitignore-tfstate-check.md`
