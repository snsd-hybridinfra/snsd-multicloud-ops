# Scope

## Included

- Azure service node inbound security rule validation plan.
- Azure service node outbound security rule review plan.
- Bastion-to-Azure SSH access rule validation plan.
- HTTP and HTTPS service exposure rule placeholder validation.
- Azure App Node to On-Prem DB access rule placeholder validation.
- Monitoring scrape access rule placeholder validation.
- Denial of unrestricted SSH access.
- Denial of unrestricted DB access.
- NSG rule evidence collection plan.
- Terraform plan or Azure CLI NSG rule capture plan using placeholders.

## Excluded

- Real Azure Terraform resource implementation.
- Real Azure NSG creation or modification.
- Azure credentials, subscription IDs, tenant IDs, tfstate, private keys, or account-specific values.
- Real public IP addresses or production CIDR values.
- AWS Security Group validation, which is handled in S014.
- OpenStack Security Group validation, which is handled in S016.
- Runtime firewall enforcement outside Azure NSG rule review.

## Placeholder Rules

Use placeholders such as `<azure-nsg-name>`, `<azure-app-node>`, `<bastion-cidr>`, `<monitoring-cidr>`, and `<onprem-db-cidr>`.
