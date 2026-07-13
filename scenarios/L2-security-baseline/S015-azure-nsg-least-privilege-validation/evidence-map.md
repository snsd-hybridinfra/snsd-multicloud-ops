# Evidence Map

| Check ID | Validation Item | Evidence File | Required |
|---|---|---|---|
| V001 | Least privilege baseline | `logs/azure-nsg-least-privilege-validation.log`; `configs/azure-nsg-least-privilege-summary.md` | yes |
| V002 | NSG rule matrix | same generated evidence | yes |
| V003 | Required NSG placeholders | same generated evidence | yes |
| V004 | Least privilege statements | same generated evidence | yes |
| V005 | Terraform NSG placeholder | same generated evidence | yes |
| V006 | Terraform state and variables | same generated evidence | yes |
| V007 | Azure identity and secret safety | same generated evidence | yes |
| V008 | Public IP safety | same generated evidence | yes |
| V009 | Dangerous public inbound rules | same generated evidence | yes |
| V010 | Public web exception | same generated evidence | yes |
| V011 | Egress justification | same generated evidence | yes |
| V012 | Remote backend | same generated evidence | yes |
| V013 | Execution safety boundary | same generated evidence | yes |

`commands.md` documents execution and `validation.md` records final results. The generated log is ignored; the sanitized summary is tracked.
