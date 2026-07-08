# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Terraform AzureRM provider initialization plan | Document planned `terraform init` validation without credentials. | Initialization approach is defined without provider credentials or backend state. | `commands.md`, `configs/azure-network-plan-summary.md`, `validation.md` |
| V002 | Terraform validate plan | Document planned `terraform validate` check. | Configuration validation approach is defined for future Azure network code. | `commands.md`, `logs/terraform-azure-network-validation.log`, `validation.md` |
| V003 | Azure Resource Group validation plan | Define how `<azure-resource-group-name>` would be confirmed after approved execution. | Resource Group validation method is documented. | `configs/azure-network-plan-summary.md`, `validation.md`, `screenshots/azure-vnet-resource-view.png` |
| V004 | Azure VNet creation validation plan | Define how `<azure-vnet-name>` would be confirmed after approved execution. | VNet validation method is documented. | `configs/azure-network-plan-summary.md`, `validation.md`, `screenshots/azure-vnet-resource-view.png` |
| V005 | Azure subnet creation validation plan | Define public and private subnet validation checks. | Public and private subnet validation method is documented. | `configs/azure-network-plan-summary.md`, `validation.md`, `screenshots/azure-vnet-resource-view.png` |
| V006 | Azure NSG baseline validation plan | Define baseline NSG validation checks. | NSG baseline validation method is documented without rule implementation. | `configs/azure-network-plan-summary.md`, `validation.md` |
| V007 | Azure route table validation plan | Define route table and association validation checks. | Route table validation method is documented. | `commands.md`, `logs/terraform-azure-network-validation.log`, `validation.md` |
| V008 | Terraform output capture plan | Define expected sanitized Terraform outputs. | Output capture method is documented without tfstate content. | `commands.md`, `logs/terraform-azure-network-validation.log`, `validation.md` |
| V009 | Azure CLI resource listing plan | Define planned Azure CLI list or show commands. | Azure CLI evidence capture method is documented with placeholders only. | `commands.md`, `logs/terraform-azure-network-validation.log`, `validation.md` |
| V010 | Missing Resource Group, VNet, subnet, NSG, or route table failure condition | Define explicit missing-resource failure criteria. | Missing required Azure network resources produce `FAIL` or `BLOCKED` status. | `validation.md` |
| V011 | Rollback plan using terraform destroy checklist | Define future approved teardown checklist. | Rollback steps are documented without executing destroy. | `commands.md`, `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario does not create real Azure resources or execute Terraform against a real Azure subscription.
