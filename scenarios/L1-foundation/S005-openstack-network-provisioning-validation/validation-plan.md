# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Module files | Test four required module paths. | All module files exist. | `logs/openstack-network-provisioning-validation.log`, `configs/openstack-network-provisioning-summary.md` |
| V002 | Environment files | Test five required environment paths. | All environment files exist. | `logs/openstack-network-provisioning-validation.log`, `configs/openstack-network-provisioning-summary.md` |
| V003 | Example variable file | Test `terraform.tfvars.example`. | The safe example file exists. | `logs/openstack-network-provisioning-validation.log`, `configs/openstack-network-provisioning-summary.md` |
| V004 | State and real variable files | Scan Terraform paths for tfstate and non-example tfvars. | No unsafe generated or real-value file exists. | `logs/openstack-network-provisioning-validation.log`, `configs/openstack-network-provisioning-summary.md` |
| V005 | OpenStack authentication files | Scan repository filenames for `clouds.yaml` and openrc patterns. | No OpenStack authentication artifact exists. | `logs/openstack-network-provisioning-validation.log`, `configs/openstack-network-provisioning-summary.md` |
| V006 | OpenStack network resources | Search module `main.tf` for required resource block types. | Network, subnet, router, router interface, security group, and rule definitions exist. | `logs/openstack-network-provisioning-validation.log`, `configs/openstack-network-provisioning-summary.md` |
| V007 | Remote backend | Search target files for backend blocks. | No backend block exists. | `logs/openstack-network-provisioning-validation.log`, `configs/openstack-network-provisioning-summary.md` |
| V008 | Credential-like content | Scan target Terraform files for credentials, private keys, tokens, UUIDs, and secrets. | No forbidden content is detected. | `logs/openstack-network-provisioning-validation.log`, `configs/openstack-network-provisioning-summary.md` |
| V009 | OpenStack account assignments | Search target Terraform files for authentication and account assignments. | No account-specific assignment exists. | `logs/openstack-network-provisioning-validation.log`, `configs/openstack-network-provisioning-summary.md` |
| V010 | Example values | Compare example CIDRs, external network placeholder, and non-production marker with approved values. | Only approved non-production values exist. | `logs/openstack-network-provisioning-validation.log`, `configs/openstack-network-provisioning-summary.md` |
| V011 | Terraform formatting | Run `terraform fmt -check` only when Terraform exists. | Formatting passes or absence is recorded as a warning. | `logs/openstack-network-provisioning-validation.log`, `configs/openstack-network-provisioning-summary.md` |
| V012 | Terraform validate boundary | Record the provider initialization boundary. | Validate is skipped because init/provider download is prohibited. | `logs/openstack-network-provisioning-validation.log`, `configs/openstack-network-provisioning-summary.md` |

## Review Notes

V001-V010 are required checks. V011-V012 are informational readiness checks and do not trigger a non-zero exit.
