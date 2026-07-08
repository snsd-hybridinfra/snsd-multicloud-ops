# Scope

## Included

- OpenStack service VM ingress rule validation plan.
- OpenStack service VM egress rule review plan.
- Bastion-to-OpenStack SSH access rule validation plan.
- HTTP and HTTPS service exposure rule placeholder validation.
- OpenStack App VM to On-Prem DB access rule placeholder validation.
- Monitoring scrape access rule placeholder validation.
- Denial of unrestricted SSH access.
- Denial of unrestricted DB access.
- Security Group rule evidence collection plan.
- Terraform plan or OpenStack CLI security group rule capture plan using placeholders.

## Excluded

- Real OpenStack Terraform resource implementation.
- Real OpenStack Security Group creation or modification.
- OpenStack credentials, openrc files, clouds.yaml, tfstate, private keys, or account-specific values.
- Real public IP addresses or production CIDR values.
- AWS Security Group validation, which is handled in S014.
- Azure NSG validation, which is handled in S015.
- Runtime firewall enforcement outside OpenStack Security Group rule review.

## Placeholder Rules

Use placeholders such as `<openstack-security-group-id>`, `<openstack-app-node>`, `<bastion-cidr>`, `<monitoring-cidr>`, and `<onprem-db-cidr>`.
