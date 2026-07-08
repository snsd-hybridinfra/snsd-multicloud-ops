# Commands

Scenario: S004-azure-network-provisioning-validation
Level: L1-foundation
Capability: Azure Network Provisioning Validation
Target: `<target-node>`
Execution timestamp: TODO

Record sanitized output only. Do not include Azure credentials, subscription IDs, tenant IDs, tokens, tfstate, private keys, real public IPs, private IPs, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | Terraform AzureRM provider initialization plan | `terraform init` in the future approved Azure network module path | Confirm initialization plan without committing credentials or backend state. | TODO: record sanitized output after approved execution. |
| V002 | Terraform validate plan | `terraform validate` in the future approved Azure network module path | Confirm Terraform configuration syntax and internal consistency. | TODO: record sanitized output after approved execution. |
| V003 | Azure Resource Group validation plan | `az group show --name <azure-resource-group-name>` | Confirm planned Resource Group lookup method using placeholders. | TODO: record sanitized output after approved execution. |
| V004 | Azure VNet creation validation plan | `az network vnet show --resource-group <azure-resource-group-name> --name <azure-vnet-name>` | Confirm planned VNet lookup method. | TODO: record sanitized output after approved execution. |
| V005 | Azure subnet creation validation plan | `az network vnet subnet list --resource-group <azure-resource-group-name> --vnet-name <azure-vnet-name>` | Confirm planned public and private subnet listing method. | TODO: record sanitized output after approved execution. |
| V006 | Azure NSG baseline validation plan | `az network nsg show --resource-group <azure-resource-group-name> --name <azure-nsg-name>` | Confirm planned NSG baseline lookup method. | TODO: record sanitized output after approved execution. |
| V007 | Azure route table validation plan | `az network route-table show --resource-group <azure-resource-group-name> --name <azure-route-table-name>` | Confirm planned route table lookup method. | TODO: record sanitized output after approved execution. |
| V008 | Terraform output capture plan | `terraform output` | Capture sanitized output names and placeholder values only. | TODO: record sanitized output after approved execution. |
| V009 | Azure CLI resource listing plan | Azure CLI show or list commands for Resource Group, VNet, subnets, NSG, and route table | Cross-check Terraform output against Azure resource listing. | TODO: record sanitized output after approved execution. |
| V010 | Missing Resource Group, VNet, subnet, NSG, or route table failure condition | Review missing-resource validation results. | Confirm missing required resources are marked `FAIL` or `BLOCKED`. | TODO: record decision after execution. |
| V011 | Rollback plan using terraform destroy checklist | `terraform destroy` only after future explicit approval | Confirm rollback checklist exists for approved lab execution. | TODO: record checklist result after approved execution. |

## Planned Supporting Evidence

- `configs/azure-network-plan-summary.md`
- `logs/terraform-azure-network-validation.log`
- `screenshots/azure-vnet-resource-view.png`
