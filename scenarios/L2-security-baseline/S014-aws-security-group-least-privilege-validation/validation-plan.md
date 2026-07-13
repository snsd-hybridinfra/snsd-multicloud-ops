# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Least privilege baseline | Test the policy path. | Document exists. | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V002 | Security Group rule matrix | Test the matrix path. | Matrix exists. | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V003 | Required Security Group placeholders | Search for five groups. | Every group exists. | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V004 | Least privilege statements | Search policy rules and placeholders. | Every statement exists. | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V005 | Terraform Security Group placeholder | Check module and resource type. | `aws_security_group` exists. | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V006 | Terraform state and variables | Scan Terraform filenames. | No forbidden artifact exists. | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V007 | AWS credential and account safety | Scan baseline, matrix, and AWS Terraform files. | No forbidden content exists. | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V008 | Public IP safety | Classify numeric addresses. | Only private examples and `0.0.0.0/0` policy values exist. | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V009 | Dangerous public inbound rules | Parse inbound matrix rows and dangerous ports. | No dangerous port uses `0.0.0.0/0`. | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V010 | Public web exception | Parse public inbound rows. | Only ports 80/443 on public web use public exposure. | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V011 | Egress justification | Check baseline and matrix. | Egress is documented and review-required. | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V012 | Remote backend | Search Terraform files. | No backend block exists. | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |
| V013 | Execution safety boundary | Scan validator source. | No AWS, Terraform mutation, or network command exists. | `logs/aws-security-group-least-privilege-validation.log`, `configs/aws-security-group-least-privilege-summary.md` |

## Review Notes

All checks are required and any failure produces a non-zero exit.
