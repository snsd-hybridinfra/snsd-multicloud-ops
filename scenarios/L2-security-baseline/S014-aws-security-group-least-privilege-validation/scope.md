# Scope

## Included

- AWS service node ingress policy validation plan.
- AWS service node egress policy review plan.
- Bastion-to-AWS SSH access rule validation plan.
- HTTP and HTTPS service exposure rule placeholder validation.
- AWS App Node to On-Prem DB access rule placeholder validation.
- Monitoring scrape access rule placeholder validation.
- Denial of unrestricted SSH access.
- Denial of unrestricted DB access.
- Security Group rule evidence collection plan.
- Terraform plan or AWS CLI rule capture plan using placeholders.

## Excluded

- Real AWS Terraform resource implementation.
- Real AWS Security Group creation or modification.
- AWS credentials, account IDs, access keys, tfstate, private keys, or account-specific values.
- Real public IP addresses or production CIDR values.
- Azure NSG validation, which is handled in S015.
- OpenStack Security Group validation, which is handled in S016.
- Runtime firewall enforcement outside AWS Security Group rule review.

## Placeholder Rules

Use placeholders such as `<aws-security-group-id>`, `<aws-app-node>`, `<bastion-cidr>`, `<monitoring-cidr>`, and `<onprem-db-cidr>`.
