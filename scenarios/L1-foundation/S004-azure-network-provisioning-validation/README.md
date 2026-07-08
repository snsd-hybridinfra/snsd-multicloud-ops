# S004-azure-network-provisioning-validation

| Field | Value |
|---|---|
| Scenario ID | S004 |
| Scenario Name | Azure Network Provisioning Validation |
| Level | L1 Foundation Validation |
| Category | Foundation |
| Primary Domain | Azure baseline network readiness |
| Related Components | Resource Group, Virtual Network, public subnet, private subnet, Network Security Group baseline, route table placeholder, public IP placeholder, optional bastion or management entry point, Terraform outputs |
| Validation Type | Infrastructure Validation |
| Evidence Directory | evidence/L1-foundation/S004-azure-network-provisioning-validation/ |
| Status | PLANNED |

## Objective Summary

Define and validate the Azure baseline network provisioning scenario for the SNSD Multi-Cloud Ops project.

## Scope Summary

This scenario defines how Azure network provisioning will be validated later. It does not create real Azure resources, configure provider credentials, store subscription or tenant IDs, or generate Terraform state.

## Related Components

- `<azure-resource-group-name>` placeholder
- `<azure-vnet-name>` placeholder
- `<azure-public-subnet-name>` placeholder
- `<azure-private-subnet-name>` placeholder
- `<azure-nsg-name>` placeholder
- `<azure-route-table-name>` placeholder
- `<azure-public-ip-name>` placeholder
- `<azure-management-entry-point>` placeholder

## Validation Summary

Validation checks cover Terraform AzureRM initialization planning, Terraform validation planning, Azure resource validation planning, Terraform output capture planning, Azure CLI listing planning, missing-resource failure conditions, and rollback through a `terraform destroy` checklist.

## Evidence Output Summary

Evidence must be recorded under `evidence/L1-foundation/S004-azure-network-provisioning-validation/`, with command plans in `commands.md` and validation results in `validation.md`.
