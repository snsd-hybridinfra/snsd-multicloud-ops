# Scope

## Included

- Kolla-Ansible AIO deployment completion in a disposable lab.
- Keystone token issuance without retaining the token value.
- Nova service and hypervisor health.
- Neutron agent health and router/DHCP namespace presence.
- One flat external provider network on `physnet1` and one tenant network.
- Neutron router, image, flavor, key-pair reference, one instance, and one Floating IP state.
- EVE-NG VLAN 70 to provider-network reachability.
- Instance gateway and outbound public IPv4 reachability.
- Open vSwitch `br-tun`, `br-int`, `br-ex`, patch-port, and provider-NIC mapping.
- Normalized, sanitized operator-supplied evidence dated 2026-07-16.

## Excluded

- Repository-driven OpenStack changes or credential access.
- Raw console output, `clouds.yaml`, openrc, passwords, tokens, keys, UUIDs, MAC addresses, and unmasked runtime addresses.
- Terraform reproduction, provider authentication, idempotency, plan/apply/destroy, and state.
- Detailed Security Group rule validation, which belongs to S016.
- Cinder, Ceph, Heat, Octavia, Swift, Magnum, HA, multi-node control plane, and production hardening.
- Backup/restore, monitoring, AWS/Azure, and Kubernetes integration.

## Assumptions

- The operator-supplied execution narrative is authoritative for the observed run.
- Provider and tenant CIDRs are approved lab design values; dynamic addresses use placeholders.
- Kolla-generated authentication material remains outside the repository.
