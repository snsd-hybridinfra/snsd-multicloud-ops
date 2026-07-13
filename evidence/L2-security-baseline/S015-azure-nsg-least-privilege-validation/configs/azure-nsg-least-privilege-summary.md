# Azure NSG Least Privilege Summary

- Scenario: S015-azure-nsg-least-privilege-validation
- Generated: 2026-07-13T10:38:21+09:00
- Overall result: **PASS**
- Scope: local baseline, matrix, Terraform placeholder, and safety checks

| Check ID | Check | Result | Detail |
|---|---|---|---|
| V001 | Least privilege baseline | PASS | Baseline document exists. |
| V002 | NSG rule matrix | PASS | Rule matrix exists. |
| V003 | Required NSG placeholders | PASS | All five placeholder NSGs are documented. |
| V004 | Least privilege statements | PASS | All required inbound, internal, egress, placeholder, and evidence statements exist. |
| V005 | Terraform NSG placeholder | PASS | NSG and association resources exist; individual rule intent is safely documented. |
| V006 | Terraform state and variables | PASS | No tfstate, real tfvars, or auto tfvars file exists. |
| V007 | Azure identity and secret safety | PASS | No identity value, credential, key, password value, or token value was detected. |
| V008 | Public IP safety | PASS | No real-looking public IP address is present. |
| V009 | Dangerous public inbound rules | PASS | No dangerous port permits public inbound access. |
| V010 | Public web exception | PASS | Only HTTP and HTTPS on azure-public-web-nsg use public inbound exposure. |
| V011 | Egress justification | PASS | Egress policy and a review-required example are documented. |
| V012 | Remote backend | PASS | No Terraform backend block is configured. |
| V013 | Execution safety boundary | PASS | The validator contains no Azure CLI, Terraform mutation, or network execution command. |

## Safety Boundary

This validation read repository files only. It did not authenticate to Azure, invoke Azure CLI, query NSGs, run Terraform init/plan/apply, read credentials, or modify resources.
