# Failure Condition

## Critical Failure Conditions

- A required module or environment file is missing.
- A required OpenStack network resource type is missing.
- A real tfvars, auto tfvars, or tfstate file is present.
- A `clouds.yaml` or openrc file is present.
- A backend block, account assignment, credential, private key, token, UUID-like identity value, or secret is detected.
- Example CIDRs, external network placeholder, or non-production marker differ from the approved set.
- The validator attempts OpenStack authentication, cloud API access, provider initialization, or state-producing Terraform execution.

## Non-Critical Warnings

- Terraform is unavailable for formatting checks.
- Terraform validation is skipped because initialization and provider download are prohibited.

Critical failures produce a non-zero exit. Warnings remain documented without weakening the safety boundary.
