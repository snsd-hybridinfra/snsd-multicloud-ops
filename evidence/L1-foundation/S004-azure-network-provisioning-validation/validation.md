# Validation

Scenario: S004-azure-network-provisioning-validation
Level: L1-foundation
Capability: Azure Network Provisioning Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real Terraform or Azure command output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Terraform AzureRM provider initialization plan | Initialization approach is defined without credentials or backend state. | TODO | NOT_RUN | `commands.md`; `configs/azure-network-plan-summary.md` |
| V002 | Terraform validate plan | Terraform validation approach is defined for future Azure network code. | TODO | NOT_RUN | `commands.md`; `logs/terraform-azure-network-validation.log` |
| V003 | Azure Resource Group validation plan | Resource Group validation method is documented with `<azure-resource-group-name>` placeholder. | TODO | NOT_RUN | `configs/azure-network-plan-summary.md`; `screenshots/azure-vnet-resource-view.png` |
| V004 | Azure VNet creation validation plan | VNet validation method is documented with `<azure-vnet-name>` placeholder. | TODO | NOT_RUN | `configs/azure-network-plan-summary.md`; `screenshots/azure-vnet-resource-view.png` |
| V005 | Azure subnet creation validation plan | Public and private subnet validation method is documented. | TODO | NOT_RUN | `configs/azure-network-plan-summary.md`; `screenshots/azure-vnet-resource-view.png` |
| V006 | Azure NSG baseline validation plan | NSG baseline validation method is documented. | TODO | NOT_RUN | `configs/azure-network-plan-summary.md` |
| V007 | Azure route table validation plan | Route table validation method is documented. | TODO | NOT_RUN | `commands.md`; `logs/terraform-azure-network-validation.log` |
| V008 | Terraform output capture plan | Terraform output capture is planned without tfstate content. | TODO | NOT_RUN | `commands.md`; `logs/terraform-azure-network-validation.log` |
| V009 | Azure CLI resource listing plan | Azure CLI resource listing is planned with sanitized placeholders. | TODO | NOT_RUN | `commands.md`; `logs/terraform-azure-network-validation.log` |
| V010 | Missing Resource Group, VNet, subnet, NSG, or route table failure condition | Missing required Azure network resources produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |
| V011 | Rollback plan using terraform destroy checklist | Future approved teardown checklist is documented without execution. | TODO | NOT_RUN | `commands.md`; `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- Azure network plan summary is captured: NOT_READY
- Terraform and Azure CLI validation log is captured: NOT_READY
- Azure VNet resource screenshot is captured: NOT_READY

## Notes

This scenario does not include real Azure resource creation, Terraform provider credentials, subscription IDs, tenant IDs, tfstate, private keys, or account-specific files.
