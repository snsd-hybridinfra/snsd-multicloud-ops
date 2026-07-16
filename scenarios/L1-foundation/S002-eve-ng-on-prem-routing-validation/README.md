# S002-eve-ng-on-prem-routing-validation

| Field | Value |
|---|---|
| Scenario ID | S002 |
| Scenario Name | EVE-NG On-Prem Routing Validation |
| Level | L1 Foundation Validation |
| Category | Foundation |
| Primary Domain | EVE-NG host, Layer-2, Router-on-a-Stick, NAT/PAT, and directional ACL validation |
| Evidence Directory | `evidence/L1-foundation/S002-eve-ng-on-prem-routing-validation/` |
| Status | VALIDATED |

## Objective Summary

Validate the disposable EVE-NG network foundation from host bridge readiness
through VLAN routing, NAT/PAT, directional ACL behavior, configuration
persistence, and post-test cleanup using sanitized real execution evidence.

## Current Judgment

The network foundation, six VLAN gateways, Router-on-a-Stick, NAT/PAT,
directional ACL test, reverse-direction permit, and configuration persistence
are represented by the required E001-E014 outputs. Host-only ping, SSH/22,
HTTP/80, KVM,
live router/switch state, VLAN/trunk/subinterface/route, NAT/counter,
persistence, pre-ACL allowed, post-ACL denied, reverse-direction permitted, and
post-ACL-removal cleanup results are evidenced. S002 is `VALIDATED` with
`READY` evidence.

Service VM and OpenStack integration are `NOT_STARTED` and are not completion
criteria for this scenario.

## Scope Summary

S002 covers the EVE-NG host network, KVM readiness, router/switch boot, VLANs,
802.1Q trunk, router subinterfaces, connected/default routes, NAT/PAT,
directional ACL behavior, reverse-path validation, persistence, and cleanup.
It excludes service VMs and every cloud/platform integration.

## Related Components

- `SNSD-R1` and `SNSD-SW1`
- VMware NAT and host-only management paths
- `pnet0` through `pnet7`
- VLANs 20, 30, 40, 50, 60, and 70
- `docs/lab-network-zone-plan.md`
- `docs/lab-ip-plan.md`

## Validation Summary

The committed evidence proves the EVE host/KVM posture, live router/switch
state, VLAN/trunk/subinterfaces/routes, NAT/PAT, configuration persistence,
pre-ACL allow, post-ACL denial, reverse permit, and gateway/public connectivity.
All required evidence categories are mapped; the result is `PASS`.

## Evidence Output Summary

- `logs/20260715-S002-eve-uplink-bootstrap.sanitized.txt`
- `logs/20260716-S002-routing-acl-connectivity.sanitized.txt`
- `logs/20260716-S002-kvm-availability.sanitized.txt`
- `logs/20260716-S002-router-switch-network-state.sanitized.txt`
- `logs/20260716-S002-post-acl-cleanup.sanitized.txt`
- `logs/20260716-S002-management-reachability.sanitized.txt`
- `configs/20260716-S002-network-foundation-topology-summary.md`
- `configs/20260716-S002-required-evidence-gap-matrix.md`
- `commands.md`
- `validation.md`
