# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | Least privilege baseline | Baseline exists. | `logs/azure-nsg-least-privilege-validation.log`, `configs/azure-nsg-least-privilege-summary.md` |
| V002 | NSG rule matrix | Matrix exists. | same generated evidence |
| V003 | Required NSG placeholders | Five NSGs exist. | same generated evidence |
| V004 | Least privilege statements | Required rules and placeholders exist. | same generated evidence |
| V005 | Terraform NSG placeholder | NSG and association exist; rule intent is documented. | same generated evidence |
| V006 | Terraform state and variables | No state, real tfvars, or auto tfvars exists. | same generated evidence |
| V007 | Azure identity and secret safety | No forbidden identity or secret content exists. | same generated evidence |
| V008 | Public IP safety | No real-looking public address exists. | same generated evidence |
| V009 | Dangerous public inbound rules | No dangerous port uses `Internet` or `0.0.0.0/0`. | same generated evidence |
| V010 | Public web exception | Only public-web ports 80/443 are public. | same generated evidence |
| V011 | Egress justification | Egress policy and review example exist. | same generated evidence |
| V012 | Remote backend | No backend block exists. | same generated evidence |
| V013 | Execution safety boundary | No Azure CLI, Terraform mutation, or network command exists. | same generated evidence |

Every check is required and maps to generated evidence by check ID.
