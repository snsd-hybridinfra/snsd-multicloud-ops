# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Terraform CLI availability validation plan | `commands.md`; `logs/terraform-provider-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Terraform fmt validation plan | `commands.md`; `logs/terraform-provider-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Terraform init plan for AWS provider | `commands.md`; `configs/terraform-provider-structure-summary.md`; `validation.md` | command plan, provider summary, validation record | yes |
| Terraform init plan for AzureRM provider | `commands.md`; `configs/terraform-provider-structure-summary.md`; `validation.md` | command plan, provider summary, validation record | yes |
| Terraform init plan for OpenStack provider | `commands.md`; `configs/terraform-provider-structure-summary.md`; `validation.md` | command plan, provider summary, validation record | yes |
| Terraform validate plan for each provider environment | `commands.md`; `logs/terraform-provider-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Provider version pinning check | `configs/terraform-provider-structure-summary.md`; `validation.md` | provider summary, validation record | yes |
| Provider credential hardcoding check | `configs/terraform-provider-structure-summary.md`; `validation.md` | provider summary, validation record | yes |
| tfstate exclusion check | `configs/gitignore-tfstate-check.md`; `validation.md` | gitignore policy evidence, validation record | yes |
| Missing provider, invalid provider version, or credential exposure failure condition | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real Terraform provider output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
