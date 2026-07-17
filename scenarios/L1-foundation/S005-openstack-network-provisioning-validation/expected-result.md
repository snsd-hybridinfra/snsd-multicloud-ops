# Expected Result

## Success Conditions

- The AIO deployment and post-deploy authentication complete.
- Required core services, endpoints, Nova services, hypervisor, and Neutron agents are healthy.
- Provider and tenant networks, router, image, instance, and Floating IP are active.
- Router/DHCP namespaces and the OVS provider path are present.
- EVE-NG reaches the Neutron external router and Floating IP.
- The tenant instance reaches its gateway and the public IPv4 network.
- Cloud-init completion is observed.
- Sanitized evidence supports every validation item.

## Required Evidence

- `commands.md`
- `validation.md`
- `logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt`
- `configs/20260716-S005-openstack-aio-validation-summary.md`

## Completion Criteria

S005 is `VALIDATED` only when V001-V021 are `PASS`. This verdict does not
advance S006, S016, or any HA, storage, backup, monitoring, governance, AWS,
Azure, or Kubernetes scenario.
