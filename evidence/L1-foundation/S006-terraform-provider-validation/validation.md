# Validation

Scenario: S006-terraform-provider-validation
Level: L1-foundation
Capability: Terraform Provider Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real Terraform provider command output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Terraform CLI availability validation plan | Terraform CLI availability can be validated without credentials. | TODO | NOT_RUN | `commands.md`; `logs/terraform-provider-validation.log` |
| V002 | Terraform fmt validation plan | Formatting validation approach is documented. | TODO | NOT_RUN | `commands.md`; `logs/terraform-provider-validation.log` |
| V003 | Terraform init plan for AWS provider | AWS provider role is documented without credentials. | TODO | NOT_RUN | `commands.md`; `configs/terraform-provider-structure-summary.md` |
| V004 | Terraform init plan for AzureRM provider | AzureRM provider role is documented without credentials. | TODO | NOT_RUN | `commands.md`; `configs/terraform-provider-structure-summary.md` |
| V005 | Terraform init plan for OpenStack provider | OpenStack provider role is documented without credentials. | TODO | NOT_RUN | `commands.md`; `configs/terraform-provider-structure-summary.md` |
| V006 | Terraform validate plan for each provider environment | Provider environments have separate validation plans. | TODO | NOT_RUN | `commands.md`; `logs/terraform-provider-validation.log` |
| V007 | Provider version pinning check | Provider versions are pinned or constrained intentionally. | TODO | NOT_RUN | `configs/terraform-provider-structure-summary.md` |
| V008 | Provider credential hardcoding check | No credentials, keys, tokens, account IDs, subscription IDs, tenant IDs, or passwords are hardcoded. | TODO | NOT_RUN | `configs/terraform-provider-structure-summary.md` |
| V009 | tfstate exclusion check | Terraform state files and `.terraform/` directories are excluded from commit. | TODO | NOT_RUN | `configs/gitignore-tfstate-check.md` |
| V010 | Missing provider, invalid provider version, or credential exposure failure condition | Missing provider, invalid version policy, or credential exposure produces `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- Terraform provider structure summary is captured: NOT_READY
- Terraform provider validation log is captured: NOT_READY
- tfstate exclusion check is captured: NOT_READY

## Notes

This scenario does not include real Terraform provider credentials, AWS credentials, Azure credentials, OpenStack credentials, tfstate, private keys, or account-specific files.
