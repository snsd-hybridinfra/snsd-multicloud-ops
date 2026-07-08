# Failure Condition

## Failure Conditions

- Terraform AzureRM provider initialization validation cannot be planned safely.
- Terraform validate evidence cannot be defined.
- Resource Group, VNet, subnet, NSG, route table, public IP placeholder, or management entry point validation criteria are missing.
- Terraform output capture would require committing tfstate or sensitive values.
- Azure CLI resource listing would expose subscription IDs, tenant IDs, credentials, real public IPs, or other sensitive values.
- Rollback through `terraform destroy` is not documented for future approved execution.
- Real Azure resources, credentials, subscription IDs, tenant IDs, tfstate, private keys, or account-specific files are added.

## Evidence of Failure

Record failed or blocked checks in `validation.md`, with supporting TODO references to `commands.md`, `configs/azure-network-plan-summary.md`, or `logs/terraform-azure-network-validation.log`.

## Follow-Up Requirement

Create a follow-up task to clarify the Azure network plan, sanitize evidence expectations, or define a safe future lab execution path before implementation proceeds.
