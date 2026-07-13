# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Module files | Test four required module paths. | All module files exist. | `logs/aws-network-provisioning-validation.log`, `configs/aws-network-provisioning-summary.md` |
| V002 | Environment files | Test five required environment paths. | All environment files exist. | `logs/aws-network-provisioning-validation.log`, `configs/aws-network-provisioning-summary.md` |
| V003 | Example variable file | Test `terraform.tfvars.example`. | The safe example file exists. | `logs/aws-network-provisioning-validation.log`, `configs/aws-network-provisioning-summary.md` |
| V004 | State and real variable files | Scan Terraform paths for tfstate and non-example tfvars. | No unsafe generated or real-value file exists. | `logs/aws-network-provisioning-validation.log`, `configs/aws-network-provisioning-summary.md` |
| V005 | AWS network resources | Search module `main.tf` for required resource block types. | VPC, subnet, route table, internet gateway, and security group definitions exist. | `logs/aws-network-provisioning-validation.log`, `configs/aws-network-provisioning-summary.md` |
| V006 | Remote backend | Search target files for backend blocks. | No backend block exists. | `logs/aws-network-provisioning-validation.log`, `configs/aws-network-provisioning-summary.md` |
| V007 | Credential-like content | Scan target files for credential, private-key, and account-ID patterns. | No forbidden content is detected. | `logs/aws-network-provisioning-validation.log`, `configs/aws-network-provisioning-summary.md` |
| V008 | Example values | Compare example CIDRs with the approved list and marker. | Only approved non-production examples exist. | `logs/aws-network-provisioning-validation.log`, `configs/aws-network-provisioning-summary.md` |
| V009 | Terraform formatting | Run `terraform fmt -check` only when Terraform exists. | Formatting passes or absence is recorded as a warning. | `logs/aws-network-provisioning-validation.log`, `configs/aws-network-provisioning-summary.md` |
| V010 | Terraform validate boundary | Record the provider initialization boundary. | Validate is skipped because init/provider download is prohibited. | `logs/aws-network-provisioning-validation.log`, `configs/aws-network-provisioning-summary.md` |

## Review Notes

V001-V008 are required checks. V009-V010 are informational readiness checks and do not trigger a non-zero exit.
