# Scope

## Included

- Terraform AzureRM provider initialization plan.
- Terraform validate plan.
- Azure Resource Group validation plan.
- Azure Virtual Network creation validation plan.
- Azure public and private subnet validation plan.
- Azure Network Security Group baseline validation plan.
- Azure route table validation plan.
- Public IP placeholder validation plan.
- Optional Bastion or management entry point placeholder validation plan.
- Terraform output capture plan.
- Azure CLI resource listing plan.
- Failure condition for missing Resource Group, VNet, subnet, NSG, or route table.
- Rollback plan using a `terraform destroy` checklist.

## Excluded

- Real Azure Terraform resource implementation.
- Terraform provider credentials or backend configuration.
- Azure credentials, subscription IDs, tenant IDs, private keys, tfstate files, or account-specific files.
- Real Azure resource creation, modification, or deletion.
- Terraform plan, apply, or destroy execution against a real subscription.
- Ansible, Kubernetes, monitoring, ML, backup, or other unrelated logic.

## Assumptions

- Azure identifiers are represented only with placeholders such as `<azure-vnet-name>` and `<azure-resource-group-name>`.
- Any future Azure CLI output must be sanitized before commit.
- This scenario remains in planning status until an approved lab execution path exists.
