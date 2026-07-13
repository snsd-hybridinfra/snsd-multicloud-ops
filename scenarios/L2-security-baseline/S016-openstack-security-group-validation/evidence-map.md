# Evidence Map

| Check ID | Validation Item | Evidence File | Required |
|---|---|---|---|
| V001 | Security Group baseline | `logs/openstack-security-group-validation.log`; `configs/openstack-security-group-summary.md` | yes |
| V002 | Security Group rule matrix | same generated evidence | yes |
| V003 | Required Security Group placeholders | same generated evidence | yes |
| V004 | Least privilege statements | same generated evidence | yes |
| V005 | Terraform Security Group placeholders | same generated evidence | yes |
| V006 | Terraform state and variables | same generated evidence | yes |
| V007 | OpenStack configuration files | same generated evidence | yes |
| V008 | OpenStack identity and secret safety | same generated evidence | yes |
| V009 | Public IP safety | same generated evidence | yes |
| V010 | Dangerous public ingress rules | same generated evidence | yes |
| V011 | Public web exception | same generated evidence | yes |
| V012 | Egress justification | same generated evidence | yes |
| V013 | Remote backend | same generated evidence | yes |
| V014 | Execution safety boundary | same generated evidence | yes |

`commands.md` documents execution and `validation.md` records final results. The generated log is ignored; the sanitized summary is tracked.
