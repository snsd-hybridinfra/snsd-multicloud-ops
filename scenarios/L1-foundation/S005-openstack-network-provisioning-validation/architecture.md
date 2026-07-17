# Architecture

## Relevant Components

| Plane | Components | Validated Responsibility |
|---|---|---|
| Management | management NIC, `<KOLLA_INTERNAL_VIP>`, Keystone, Nova, Neutron, Glance, Horizon | API authentication, registration, scheduling, and administration |
| Provider | EVE-NG VLAN 70, provider NIC, `physnet1`, `br-ex` | External Layer-2 attachment and router/Floating-IP path |
| Integration | `phy-br-ex`, `int-br-ex`, `br-int`, router namespace | Open vSwitch patching, routing, NAT/DNAT |
| Tenant | DHCP namespace, `10.20.10.0/24`, `<INSTANCE_FIXED_IP>` | DHCP, fixed address, default gateway, guest data path |

## Logical Flow

```text
Management:
<OPENSTACK_MANAGEMENT_IP> -> <KOLLA_INTERNAL_VIP> -> OpenStack APIs / Horizon

Provider and tenant data path:
EVE-NG VLAN 70 -> provider NIC -> physnet1 -> br-ex
  -> phy-br-ex -> int-br-ex -> br-int
  -> <ROUTER_NAMESPACE> -> Floating IP DNAT
  -> tenant network -> <INSTANCE_FIXED_IP>
```

## Network Plan

- Provider: `10.10.70.0/24`, gateway `10.10.70.1`, controlled allocation pool `10.10.70.100-10.10.70.199`.
- Tenant: `10.20.10.0/24`, gateway `10.20.10.1`.
- Management address and Kolla internal VIP are masked.

## False-Negative Boundary

`LOCAL(br-ex)` OpenFlow state alone is not a pass/fail criterion. Provider NIC
link/admin state, positive `ofport`, bridge membership, patch-path state, router
reachability, Floating IP reachability, and instance egress form the functional
judgment.

## Out-of-Scope Components

Persistent storage, HA, advanced TLS, production hardening, load balancing,
Kubernetes, monitoring, backup, and public-cloud integrations are not part of
this scenario.
