# Execution Plan

## Preparation

1. Review S001 for Terraform CLI and Azure CLI readiness.
2. Confirm this scenario is documentation and evidence planning only.
3. Confirm no Azure credentials, subscription IDs, tenant IDs, tfstate, private keys, or account-specific files are present or required.
4. Confirm the S004 evidence directory exists.

## Execution Steps

1. Define the Terraform AzureRM provider initialization validation plan.
2. Define the Terraform validate command plan.
3. Define the Azure Resource Group validation plan.
4. Define the Azure VNet validation plan.
5. Define the Azure public and private subnet validation plan.
6. Define the Azure NSG baseline validation plan.
7. Define the Azure route table validation plan.
8. Define the Terraform output capture plan.
9. Define the Azure CLI resource listing plan.
10. Define failure conditions for missing Resource Group, VNet, subnet, NSG, or route table.
11. Define the rollback checklist using `terraform destroy` for future approved execution.

## Evidence Capture

1. Record planned commands and placeholders in `commands.md`.
2. Record validation checks and TODO results in `validation.md`.
3. Map future plan evidence to `configs/azure-network-plan-summary.md`.
4. Map future Terraform and Azure CLI logs to `logs/terraform-azure-network-validation.log`.
5. Map future console evidence to `screenshots/azure-vnet-resource-view.png` only after binary evidence is approved and sanitized.
