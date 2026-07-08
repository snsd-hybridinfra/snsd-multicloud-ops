# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | OpenStack CLI authentication validation plan | Document planned authentication check without storing `openrc` or `clouds.yaml`. | Authentication validation approach is defined without credentials. | `commands.md`, `configs/openstack-network-plan-summary.md`, `validation.md` |
| V002 | OpenStack network list validation plan | Document planned `openstack network list` review. | Network listing approach distinguishes provider and tenant networks. | `commands.md`, `logs/openstack-network-validation.log`, `validation.md` |
| V003 | Provider network existence validation plan | Define how `<openstack-provider-network-name>` would be confirmed. | Provider Network is validated as pre-existing or dependency-owned. | `configs/openstack-network-plan-summary.md`, `validation.md`, `screenshots/openstack-network-resource-view.png` |
| V004 | Tenant network creation validation plan | Define how `<openstack-tenant-network-name>` would be confirmed. | Tenant Network validation method is documented. | `configs/openstack-network-plan-summary.md`, `validation.md`, `screenshots/openstack-network-resource-view.png` |
| V005 | Tenant subnet creation validation plan | Define how `<openstack-tenant-subnet-name>` would be confirmed. | Tenant Subnet validation method is documented. | `configs/openstack-network-plan-summary.md`, `validation.md` |
| V006 | Router creation validation plan | Define how `<openstack-router-name>` would be confirmed. | Router validation method is documented. | `commands.md`, `logs/openstack-network-validation.log`, `validation.md` |
| V007 | Router interface validation plan | Define router-to-subnet interface validation. | Router Interface validation method is documented. | `commands.md`, `logs/openstack-network-validation.log`, `validation.md` |
| V008 | Security group baseline validation plan | Define baseline security group validation checks. | Security Group baseline validation method is documented without rule implementation. | `configs/openstack-network-plan-summary.md`, `validation.md` |
| V009 | Floating IP availability validation plan | Define floating IP availability check as a placeholder. | Floating IP availability validation method is documented. | `commands.md`, `logs/openstack-network-validation.log`, `validation.md` |
| V010 | Terraform or OpenStack CLI output capture plan | Define expected sanitized output capture. | Output capture method is documented without tfstate or credentials. | `commands.md`, `logs/openstack-network-validation.log`, `validation.md` |
| V011 | Missing network, subnet, router, interface, or security group failure condition | Define explicit missing-resource failure criteria. | Missing required OpenStack resources produce `FAIL` or `BLOCKED` status. | `validation.md` |
| V012 | Rollback using Terraform destroy or OpenStack CLI cleanup checklist | Define future approved teardown checklist. | Rollback steps are documented without execution. | `commands.md`, `validation.md` |

## Review Notes

Every validation item must map to evidence. Provider Network and Tenant Network roles must remain distinct in all future execution evidence.
