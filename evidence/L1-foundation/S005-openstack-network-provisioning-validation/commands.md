# Commands

Scenario: S005-openstack-network-provisioning-validation
Level: L1-foundation
Capability: OpenStack Network Provisioning Validation
Target: `<target-node>`
Execution timestamp: TODO

Record sanitized output only. Do not include OpenStack credentials, `openrc` content, `clouds.yaml` content, tokens, tfstate, private keys, project IDs, real public IPs, private IPs, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | OpenStack CLI authentication validation plan | `openstack token issue` or approved non-secret auth check after future approval | Confirm authentication validation method without storing credentials. | TODO: record sanitized output after approved execution. |
| V002 | OpenStack network list validation plan | `openstack network list` | Confirm planned network listing method and distinguish provider and tenant networks. | TODO: record sanitized output after approved execution. |
| V003 | Provider network existence validation plan | `openstack network show <openstack-provider-network-name>` | Confirm provider network reference as external or dependency-owned. | TODO: record sanitized output after approved execution. |
| V004 | Tenant network creation validation plan | `openstack network show <openstack-tenant-network-name>` | Confirm tenant network lookup method. | TODO: record sanitized output after approved execution. |
| V005 | Tenant subnet creation validation plan | `openstack subnet show <openstack-tenant-subnet-name>` | Confirm tenant subnet lookup method. | TODO: record sanitized output after approved execution. |
| V006 | Router creation validation plan | `openstack router show <openstack-router-name>` | Confirm router lookup method. | TODO: record sanitized output after approved execution. |
| V007 | Router interface validation plan | `openstack port list --router <openstack-router-name>` | Confirm router interface lookup method. | TODO: record sanitized output after approved execution. |
| V008 | Security group baseline validation plan | `openstack security group show <openstack-security-group-name>` | Confirm security group baseline lookup method. | TODO: record sanitized output after approved execution. |
| V009 | Floating IP availability validation plan | `openstack floating ip list` | Confirm floating IP availability review method. | TODO: record sanitized output after approved execution. |
| V010 | Terraform or OpenStack CLI output capture plan | `terraform output` or approved OpenStack CLI show/list commands | Capture sanitized output names and placeholder values only. | TODO: record sanitized output after approved execution. |
| V011 | Missing network, subnet, router, interface, or security group failure condition | Review missing-resource validation results. | Confirm missing required resources are marked `FAIL` or `BLOCKED`. | TODO: record decision after execution. |
| V012 | Rollback using Terraform destroy or OpenStack CLI cleanup checklist | `terraform destroy` or approved OpenStack CLI cleanup only after future explicit approval | Confirm rollback checklist exists for approved lab execution. | TODO: record checklist result after approved execution. |

## Planned Supporting Evidence

- `configs/openstack-network-plan-summary.md`
- `logs/openstack-network-validation.log`
- `screenshots/openstack-network-resource-view.png`
