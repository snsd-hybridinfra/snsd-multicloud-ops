# Validation

Scenario: S014-aws-security-group-least-privilege-validation

Level: L2-security-baseline

Date: 2026-07-13

Overall status: PASS

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Least privilege baseline | File exists. | Baseline exists. | PASS | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V002 | Security Group rule matrix | File exists. | Rule matrix exists. | PASS | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V003 | Required Security Group placeholders | Five groups exist. | All groups are documented. | PASS | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V004 | Least privilege statements | All statements exist. | All required statements are documented. | PASS | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V005 | Terraform Security Group placeholder | Resource exists. | Existing `aws_security_group` placeholder was found. | PASS | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V006 | Terraform state and variables | No unsafe artifact exists. | No state or real tfvars was detected. | PASS | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V007 | AWS credential and account safety | No forbidden content exists. | No credential, key, ID, or token was detected. | PASS | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V008 | Public IP safety | No real public IP exists. | Only private examples and policy `0.0.0.0/0` values exist. | PASS | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V009 | Dangerous public inbound rules | No dangerous port is public. | No dangerous public inbound row was detected. | PASS | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V010 | Public web exception | Only public web 80/443 is public. | Exception is correctly limited. | PASS | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V011 | Egress justification | Egress is documented. | Policy and review-required row exist. | PASS | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V012 | Remote backend | No backend exists. | No backend block was detected. | PASS | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V013 | Execution safety boundary | No AWS or Terraform mutation exists. | No prohibited command was detected. | PASS | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |

## Generated Result

All thirteen policy, matrix, Terraform, sensitive-content, dangerous-inbound, public-web, egress, backend, and execution-boundary checks passed. No AWS authentication, CLI, Security Group query, Terraform init/plan/apply, state creation, or resource modification occurred.
