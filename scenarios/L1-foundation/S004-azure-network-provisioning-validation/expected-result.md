# Expected Result

## Success Conditions

- Azure baseline network validation is fully documented.
- Terraform initialization and validate plans are defined without credentials or backend state.
- Resource Group, VNet, subnet, NSG, route table, public IP placeholder, and management entry point placeholder validation methods are mapped to evidence.
- Terraform output capture is planned without exposing tfstate content.
- Azure CLI resource listing is planned with sanitized placeholders only.
- Rollback using a future `terraform destroy` checklist is defined.

## Required Evidence

- `commands.md`
- `validation.md`
- `configs/azure-network-plan-summary.md`
- `logs/terraform-azure-network-validation.log`
- `screenshots/azure-vnet-resource-view.png`

## Completion Criteria

The scenario can move from `PLANNED` to `VALIDATED` only after approved, sanitized evidence confirms the Azure baseline network validation checks. Real Azure execution is not part of this skeleton.
