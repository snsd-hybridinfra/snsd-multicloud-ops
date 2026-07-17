# S005-openstack-network-provisioning-validation

| Field | Value |
|---|---|
| Scenario ID | S005 |
| Scenario Name | OpenStack Network Provisioning Validation |
| Level | L1 Foundation Validation |
| Category | Foundation |
| Primary Domain | OpenStack AIO control plane and Neutron network path |
| Related Components | Kolla-Ansible, Keystone, Nova, Neutron, Glance, Open vSwitch, EVE-NG VLAN 70 |
| Validation Type | Infrastructure Validation |
| Evidence Directory | evidence/L1-foundation/S005-openstack-network-provisioning-validation/ |
| Status | VALIDATED |

## Context

The operator deployed a disposable single-node OpenStack AIO environment on
Ubuntu Server 24.04 with Kolla-Ansible and the 2026.1 release configuration.
The environment uses a dedicated management interface and a provider interface
mapped through `physnet1` to `br-ex`. Environment-specific identifiers are
masked in repository evidence.

## Objective Summary

Validate the complete functional path from the registered OpenStack control
plane through Neutron provider and tenant networking to one tenant instance,
including EVE-NG VLAN 70 reachability, Floating IP DNAT, and instance outbound
connectivity.

## Scope Summary

S005 covers one disposable Kolla-Ansible AIO deployment, its minimum core
services, one provider network, one tenant network, one router, one instance,
one Floating IP, and their functional network path. It excludes Terraform
reproduction, detailed Security Group policy, HA, storage, backup, monitoring,
hardening, and cross-platform integration.

## Related Components

- Kolla-Ansible and OpenStack CLI command context
- Keystone, Nova, Placement, Glance, Neutron, and Horizon
- Open vSwitch `br-tun`, `br-int`, and `br-ex`
- EVE-NG VLAN 70 provider path

## Architecture Path

- Management: `<OPENSTACK_MANAGEMENT_IP>` -> `<KOLLA_INTERNAL_VIP>` -> API and Horizon endpoints.
- Provider: EVE-NG VLAN 70 -> provider NIC -> `physnet1` -> `br-ex` -> Neutron router external interface.
- Tenant: `br-int` -> router/DHCP namespaces -> `10.20.10.0/24` -> `<INSTANCE_FIXED_IP>`.
- End-to-end: EVE-NG -> `<ROUTER_EXTERNAL_IP>` / `<FLOATING_IP>` -> tenant instance.

## Actual Validated Results

- Kolla-Ansible bootstrap, prechecks, image pull, deploy, and post-deploy completed.
- Keystone authentication and core service/endpoint registration succeeded.
- Nova scheduler, conductor, compute, and the QEMU hypervisor were up.
- Neutron Open vSwitch, L3, DHCP, and metadata agents were alive/up.
- Provider and tenant networks, router, image, instance, and Floating IP were active.
- Router and DHCP namespaces were present.
- EVE-NG reached the router external interface after initial ARP convergence and reached the Floating IP on all recorded probes.
- The instance reached its tenant gateway and a public IPv4 endpoint; cloud-init completion markers were observed.
- `br-tun`, `br-int`, `br-ex`, patch ports, and the provider NIC mapping were verified.

## Validation Summary

V001-V021 are recorded as `PASS` from corroborating user-executed
control-plane and data-plane results. On 2026-07-16 Codex also executed the
single forced, read-only `validate-all` endpoint: 50 checks passed, no checks
failed, and the command exited with status 0. This endpoint does not provide a
general shell or mutation authority.

## Evidence Output Summary

- `evidence/L1-foundation/S005-openstack-network-provisioning-validation/validation.md`
- `evidence/L1-foundation/S005-openstack-network-provisioning-validation/logs/20260716-S005-openstack-aio-e2e-network.sanitized.txt`
- `evidence/L1-foundation/S005-openstack-network-provisioning-validation/configs/20260716-S005-openstack-aio-validation-summary.md`
- `evidence/L1-foundation/S005-openstack-network-provisioning-validation/logs/20260716-S005-codex-restricted-live-validation.sanitized.txt`
- `evidence/L1-foundation/S005-openstack-network-provisioning-validation/configs/20260716-S005-restricted-endpoint-security-summary.md`

## Interpretation

The Linux `LOCAL(br-ex)` OpenFlow entry reported `PORT_DOWN`/`LINK_DOWN`, but
the provider NIC was link-up and administratively up with a valid OpenFlow
port, and every required functional provider/Floating-IP path passed. This is
recorded as a false-negative indicator, not a forwarding failure. No manual
`ip link set br-ex up` action is prescribed.

## Security and Evidence Handling

The repository contains normalized operator-supplied results, not raw output.
Tokens, authentication files, IDs, UUIDs, MAC addresses, host management
addresses, dynamic resource addresses, keys, and credentials are omitted or
replaced with semantic placeholders.

## Known Limitations

- Single-node AIO; no HA or production resilience claim.
- Pre-built test Kolla images in a disposable lab.
- Controller and compute share one VM; provider connectivity uses one NIC.
- Cinder, Ceph, Heat, Octavia, Swift, and Magnum are disabled.
- Terraform reproduction, idempotency, destroy/recreate, persistent storage,
  backup/recovery, monitoring, security hardening, AWS/Azure, and Kubernetes
  integration are not validated by S005.

## Final Status

OpenStack AIO deployment and the provider-to-tenant end-to-end network path are
`VALIDATED`. The evidence package is `READY` for review.
