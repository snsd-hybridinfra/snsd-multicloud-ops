# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | Security Group baseline | Baseline exists. | generated log and summary |
| V002 | Security Group rule matrix | Matrix exists. | generated log and summary |
| V003 | Required Security Group placeholders | Five groups exist. | generated log and summary |
| V004 | Least privilege statements | Required rules and placeholders exist. | generated log and summary |
| V005 | Terraform Security Group placeholders | Group and management rule resources exist. | generated log and summary |
| V006 | Terraform state and variables | No state, real tfvars, or auto tfvars exists. | generated log and summary |
| V007 | OpenStack configuration files | No clouds.yaml or openrc exists. | generated log and summary |
| V008 | OpenStack identity and secret safety | No forbidden identity or secret content exists. | generated log and summary |
| V009 | Public IP safety | No real-looking public address exists. | generated log and summary |
| V010 | Dangerous public ingress rules | No dangerous port uses `0.0.0.0/0`. | generated log and summary |
| V011 | Public web exception | Only public-web ports 80/443 are public. | generated log and summary |
| V012 | Egress justification | Egress policy and review example exist. | generated log and summary |
| V013 | Remote backend | No backend block exists. | generated log and summary |
| V014 | Execution safety boundary | No OpenStack CLI, Terraform mutation, or network command exists. | generated log and summary |

Every check maps by ID to `logs/openstack-security-group-validation.log` and `configs/openstack-security-group-summary.md`.
