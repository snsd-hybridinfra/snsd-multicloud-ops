# Scope

## Included

- AWS least-privilege Security Group policy and example rule matrix.
- Public web, bastion, private-service, database, and monitoring placeholders.
- Dangerous public inbound checks for SSH, RDP, database, administration, and monitoring ports.
- Public HTTP/HTTPS exception checks limited to the public web placeholder.
- Egress justification checks.
- Existing `aws_security_group` Terraform placeholder validation.
- State, real tfvars, backend, credential, account-ID, secret, and public-IP safety checks.
- Generated log and summary evidence.

## Excluded

- AWS authentication, AWS CLI, live Security Group queries, or cloud API access.
- Terraform init, plan, apply, destroy, state, backend, or real variables.
- Real account IDs, credentials, addresses, corporate ranges, or deployed rule IDs.
- AWS network provisioning, which belongs to S003.
- Terraform provider validation, which belongs to S006.
- SSH key, password, and root-login controls, which belong to S011-S013.
- Azure NSG and OpenStack Security Group validation, which belong to S015-S016.

## Assumptions

- Matrix rows are non-production policy examples, not deployable rules.
- The existing empty AWS Security Group resource remains a safe Terraform placeholder.
