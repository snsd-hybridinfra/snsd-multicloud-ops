# AWS Security Group Least Privilege Summary

- Scenario: S014-aws-security-group-least-privilege-validation
- Generated: 2026-07-13T10:26:01+09:00
- Overall result: **PASS**
- Scope: local baseline, matrix, Terraform placeholder, and safety checks

| Check ID | Check | Result | Detail |
|---|---|---|---|
| V001 | Least privilege baseline | PASS | Baseline document exists. |
| V002 | Security Group rule matrix | PASS | Rule matrix exists. |
| V003 | Required Security Group placeholders | PASS | All five placeholder groups are documented. |
| V004 | Least privilege statements | PASS | All required inbound, internal, egress, placeholder, and evidence statements exist. |
| V005 | Terraform Security Group placeholder | PASS | The AWS network module contains an aws_security_group resource placeholder. |
| V006 | Terraform state and variables | PASS | No tfstate, real tfvars, or auto tfvars file exists. |
| V007 | AWS credential and account safety | PASS | No credential, key, account ID, access key, UUID, password value, or token value was detected. |
| V008 | Public IP safety | PASS | No real-looking public IP address is present. |
| V009 | Dangerous public inbound rules | PASS | No dangerous port permits inbound 0.0.0.0/0. |
| V010 | Public web exception | PASS | Only HTTP and HTTPS on aws-public-web-sg use public inbound exposure. |
| V011 | Egress justification | PASS | Egress policy and a review-required example are documented. |
| V012 | Remote backend | PASS | No Terraform backend block is configured. |
| V013 | Execution safety boundary | PASS | The validator contains no AWS, Terraform mutation, or network execution command. |

## Safety Boundary

The validator inspected repository files only. It did not authenticate to AWS, query live Security Groups, run AWS CLI, initialize Terraform, create a plan, apply changes, or access cloud resources.
