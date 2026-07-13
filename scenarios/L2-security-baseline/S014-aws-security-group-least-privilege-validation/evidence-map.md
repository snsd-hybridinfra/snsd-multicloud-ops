# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| V001 Least privilege baseline | `logs/aws-security-group-least-privilege-validation.log`; `configs/aws-security-group-least-privilege-summary.md` | generated log and summary | yes |
| V002 Security Group rule matrix | `logs/aws-security-group-least-privilege-validation.log`; `configs/aws-security-group-least-privilege-summary.md` | generated log and summary | yes |
| V003 Required Security Group placeholders | `logs/aws-security-group-least-privilege-validation.log`; `configs/aws-security-group-least-privilege-summary.md` | generated log and summary | yes |
| V004 Least privilege statements | `logs/aws-security-group-least-privilege-validation.log`; `configs/aws-security-group-least-privilege-summary.md` | generated log and summary | yes |
| V005 Terraform Security Group placeholder | `logs/aws-security-group-least-privilege-validation.log`; `configs/aws-security-group-least-privilege-summary.md` | generated log and summary | yes |
| V006 Terraform state and variables | `logs/aws-security-group-least-privilege-validation.log`; `configs/aws-security-group-least-privilege-summary.md` | generated log and summary | yes |
| V007 AWS credential and account safety | `logs/aws-security-group-least-privilege-validation.log`; `configs/aws-security-group-least-privilege-summary.md` | generated log and summary | yes |
| V008 Public IP safety | `logs/aws-security-group-least-privilege-validation.log`; `configs/aws-security-group-least-privilege-summary.md` | generated log and summary | yes |
| V009 Dangerous public inbound rules | `logs/aws-security-group-least-privilege-validation.log`; `configs/aws-security-group-least-privilege-summary.md` | generated log and summary | yes |
| V010 Public web exception | `logs/aws-security-group-least-privilege-validation.log`; `configs/aws-security-group-least-privilege-summary.md` | generated log and summary | yes |
| V011 Egress justification | `logs/aws-security-group-least-privilege-validation.log`; `configs/aws-security-group-least-privilege-summary.md` | generated log and summary | yes |
| V012 Remote backend | `logs/aws-security-group-least-privilege-validation.log`; `configs/aws-security-group-least-privilege-summary.md` | generated log and summary | yes |
| V013 Execution safety boundary | `logs/aws-security-group-least-privilege-validation.log`; `configs/aws-security-group-least-privilege-summary.md` | generated log and summary | yes |
| Script invocation and evidence inspection | `commands.md` | operator command record | yes |
| Final validation judgment | `validation.md` | validation result | yes |

## Evidence Notes

The log is reproducible. AWS CLI output, plans, state, account data, credentials, live rules, and screenshots are neither required nor permitted.
