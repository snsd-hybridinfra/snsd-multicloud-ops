# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| V001 Kolla deployment workflow | `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt` | normalized execution result | yes |
| V002 Keystone authentication | `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt` | sanitized result | yes |
| V003 Core services and endpoints | `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt` | sanitized inventory | yes |
| V004 Nova services | `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt` | sanitized health result | yes |
| V005 Hypervisor | `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt` | sanitized health result | yes |
| V006 Neutron agents | `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt` | sanitized health result | yes |
| V007 Provider network | `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt` | sanitized resource result | yes |
| V008 Tenant network and DHCP | `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt` | sanitized resource result | yes |
| V009 Router | `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt` | sanitized resource result | yes |
| V010 Image | `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt` | sanitized resource result | yes |
| V011 Instance | `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt` | sanitized resource result | yes |
| V012 Floating IP | `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt` | sanitized resource result | yes |
| V013 Neutron namespaces | `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt` | sanitized namespace result | yes |
| V014 OVS provider mapping | `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt` | sanitized OVS result | yes |
| V015 EVE external-router reachability | `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt` | normalized probe result | yes |
| V016 EVE Floating IP reachability | `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt` | normalized probe result | yes |
| V017 Instance gateway reachability | `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt` | cloud-init result | yes |
| V018 Instance Internet reachability | `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt` | cloud-init result | yes |
| V019 Cloud-init completion | `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt` | marker result | yes |
| V020 False-negative analysis | `configs/20260716-S005-openstack-aio-validation-summary.md` | interpretation | yes |
| V021 Evidence sanitization | `configs/20260716-S005-openstack-aio-validation-summary.md` | safety review | yes |
| Command categories | `commands.md` | sanitized command reference | yes |
| Final judgment | `validation.md` | validation record | yes |

## Evidence Notes

The log is a normalized record of operator-supplied real execution, not a raw
terminal transcript. Dynamic identifiers and sensitive values are omitted or
replaced with placeholders. Screenshots are not required for this evidence set.
