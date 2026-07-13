# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Module files | Test four required module paths. | All module files exist. | `logs/azure-network-provisioning-validation.log`, `configs/azure-network-provisioning-summary.md` |
| V002 | Environment files | Test five required environment paths. | All environment files exist. | `logs/azure-network-provisioning-validation.log`, `configs/azure-network-provisioning-summary.md` |
| V003 | Example variable file | Test `terraform.tfvars.example`. | The safe example file exists. | `logs/azure-network-provisioning-validation.log`, `configs/azure-network-provisioning-summary.md` |
| V004 | State and real variable files | Scan Terraform paths for tfstate and non-example tfvars. | No unsafe generated or real-value file exists. | `logs/azure-network-provisioning-validation.log`, `configs/azure-network-provisioning-summary.md` |
| V005 | Azure network resources | Search module `main.tf` for required resource block types. | Resource group, VNet, subnet, NSG, route table, and NSG association definitions exist. | `logs/azure-network-provisioning-validation.log`, `configs/azure-network-provisioning-summary.md` |
| V006 | Remote backend | Search target files for backend blocks. | No backend block exists. | `logs/azure-network-provisioning-validation.log`, `configs/azure-network-provisioning-summary.md` |
| V007 | Credential-like content | Scan target Terraform files for credentials, private keys, identity IDs, and account-specific patterns. | No forbidden content is detected. | `logs/azure-network-provisioning-validation.log`, `configs/azure-network-provisioning-summary.md` |
| V008 | Azure identity assignments | Search target Terraform files for Azure identity assignments. | No tenant, subscription, client, or client-secret assignment exists. | `logs/azure-network-provisioning-validation.log`, `configs/azure-network-provisioning-summary.md` |
| V009 | Example values | Compare example CIDRs, location, and non-production marker with approved values. | Only approved non-production values exist. | `logs/azure-network-provisioning-validation.log`, `configs/azure-network-provisioning-summary.md` |
| V010 | Terraform formatting | Run `terraform fmt -check` only when Terraform exists. | Formatting passes or absence is recorded as a warning. | `logs/azure-network-provisioning-validation.log`, `configs/azure-network-provisioning-summary.md` |
| V011 | Terraform validate boundary | Record the provider initialization boundary. | Validate is skipped because init/provider download is prohibited. | `logs/azure-network-provisioning-validation.log`, `configs/azure-network-provisioning-summary.md` |

## Review Notes

V001-V009 are required checks. V010-V011 are informational readiness checks and do not trigger a non-zero exit.
