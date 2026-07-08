# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Terraform AzureRM provider initialization plan | `commands.md`; `configs/azure-network-plan-summary.md`; `validation.md` | command plan, plan summary, validation record | yes |
| Terraform validate plan | `commands.md`; `logs/terraform-azure-network-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Azure Resource Group validation plan | `configs/azure-network-plan-summary.md`; `validation.md`; `screenshots/azure-vnet-resource-view.png` | plan summary, validation record, screenshot reference | yes |
| Azure VNet creation validation plan | `configs/azure-network-plan-summary.md`; `validation.md`; `screenshots/azure-vnet-resource-view.png` | plan summary, validation record, screenshot reference | yes |
| Azure subnet creation validation plan | `configs/azure-network-plan-summary.md`; `validation.md`; `screenshots/azure-vnet-resource-view.png` | plan summary, validation record, screenshot reference | yes |
| Azure NSG baseline validation plan | `configs/azure-network-plan-summary.md`; `validation.md` | plan summary, validation record | yes |
| Azure route table validation plan | `commands.md`; `logs/terraform-azure-network-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Terraform output capture plan | `commands.md`; `logs/terraform-azure-network-validation.log`; `validation.md` | command plan, output capture log, validation record | yes |
| Azure CLI resource listing plan | `commands.md`; `logs/terraform-azure-network-validation.log`; `validation.md` | command plan, Azure CLI listing log, validation record | yes |
| Missing Resource Group, VNet, subnet, NSG, or route table failure condition | `validation.md` | failure criteria and status record | yes |
| Rollback plan using terraform destroy checklist | `commands.md`; `validation.md` | rollback checklist and validation record | yes |

## Evidence Notes

No real Terraform or Azure output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
