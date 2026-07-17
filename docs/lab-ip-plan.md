# Authoritative Lab IP Address and Reservation Plan

**Status: EVE-NG gateways (S002) and the OpenStack provider/tenant path (S005)
VALIDATED; other service hosts and cloud integrations remain planned.**

## Status and Safety Rule

This is a planning document. Planned 10.x CIDRs below are reservations, not
evidence of deployed interfaces. The actual Bootstrap Management Network CIDR
and runtime host addresses are tied to the local environment and are therefore
masked under repository policy.

## Aggregate Plan

| Domain | Aggregate / Network | Status | Purpose |
|---|---|---|---|
| Bootstrap Management | `<bootstrap-management-cidr>` | Existing local network; exact value not committed | Installation, repair, initial evidence, and migration path |
| On-Prem service zones | `10.10.0.0/16` | Router-on-a-Stick gateways implemented | EVE-NG-controlled DMZ, Kubernetes, database, monitoring, backup, and OpenStack provider zones |
| OpenStack private cloud | `10.20.0.0/16` | Partially implemented | `10.20.10.0/24` tenant network validated; other subnets remain reserved |
| AWS Public Cloud A | `10.30.0.0/16` | Planned reservation | Minimum VPC validation environment |
| Azure Public Cloud B | `10.40.0.0/16` | Planned reservation | Minimum VNet validation environment |
| Optional WireGuard | `10.255.0.0/16` | Reserved / optional | Future overlay only; not an implementation dependency |

## Bootstrap Runtime Address Placeholders

| Role | Committed Value | Rule |
|---|---|---|
| Bastion | `<bastion-runtime-ip-masked>` | Actual bootstrap address stays in private/local planning only |
| Kubernetes node | `<k3s-runtime-ip-masked>` | Mask in evidence and committed configs |
| DB primary | `<db-primary-runtime-ip-masked>` | Mask connection and listener values |
| DB replica | `<db-replica-runtime-ip-masked>` | Planned bootstrap value remains private |
| Monitoring | `<monitoring-runtime-ip-masked>` | Planned bootstrap value remains private |

## EVE-NG Bootstrap Address Policy

| Interface | Network role | Committed value | Route rule |
|---|---|---|---|
| `pnet0` | VMware NAT bootstrap | `<eve-nat-ip-masked>` | Owns the only observed default route via `<vmware-nat-gateway-masked>` |
| `pnet1` | VMware host-only management | `<eve-management-ip-masked>` | Connected route only; no default gateway |
| `pnet2`-`pnet7` | Future Layer-2 Cloud attachment | No Layer-3 address committed | No route or gateway is claimed |
| `pnet8`, `pnet9` | Unattached placeholders | None | No carrier and no physical member |

This observed bootstrap posture is separate from the implemented router
subinterfaces below. Router, NAT/PAT, and ACL outcomes are represented by the
sanitized S002 execution evidence; runtime WAN and management values remain
masked.

## On-Prem Service-Zone Reservations

| VLAN / Zone | CIDR | Gateway | Reference Host Reservation | Current State |
|---|---|---|---|---|
| VLAN 20 / DMZ | `10.10.20.0/24` | `10.10.20.1` | Test endpoint remains non-authoritative | Gateway implemented; service VM integration pending |
| Kubernetes | `10.10.30.0/24` | `10.10.30.1` | k3s node `10.10.30.10` | Application runtime |
| Database | `10.10.40.0/24` | `10.10.40.1` | Primary `10.10.40.10`; replica `10.10.40.11` | Internal data platform |
| Monitoring | `10.10.50.0/24` | `10.10.50.1` | Monitoring `10.10.50.10` | Metrics, dashboards, and probes |
| Backup | `10.10.60.0/24` | `10.10.60.1` | Backup `10.10.60.10` | Backup repository and restore staging |
| VLAN 70 / OpenStack Provider | `10.10.70.0/24` | `10.10.70.1` | Controlled pool `10.10.70.100-10.10.70.199` | Gateway and OpenStack provider/Floating-IP integration validated |

Within each `/24`, `.1` is implemented as the EVE router gateway, `.2-.9` for network
services, `.10-.19` for fixed role hosts, `.20-.99` for later fixed lab roles,
and `.100-.254` for controlled ephemeral allocation. Reference host
reservations do not prove that any service VM exists.

## Cloud Reservations

| Platform | Network | Purpose | Reservation Rule |
|---|---|---|---|
| OpenStack | `10.20.10.0/24` | Primary tenant subnet | Validated; instance address remains masked |
| OpenStack | `10.10.70.0/24` | Provider/external network | Discovered and validated; dynamic router/Floating IP values remain masked |
| AWS | `10.30.10.0/24` | Public validation subnet | Temporary public path only when approved |
| AWS | `10.30.20.0/24` | Private validation subnet | Preferred temporary compute placement where practical |
| AWS | `10.30.30.0/24` | Reserved subnet | No default deployment |
| Azure | `10.40.10.0/24` | Public validation subnet | Temporary public path only when approved |
| Azure | `10.40.20.0/24` | Private validation subnet | Preferred temporary compute placement where practical |
| Azure | `10.40.30.0/24` | Reserved subnet | No default deployment |

## NIC and Gateway Planning

| Role | Bootstrap NIC | Service NIC | Default Gateway Rule |
|---|---|---|---|
| Bastion | Retained during migration | Bastion/Transit zone | Only one active default route; document management return path |
| Kubernetes | Retained until service validation passes | Kubernetes zone | Service-zone gateway after migration; API remains non-public |
| DB primary/replica | Retained until DB validation passes | Database zone | No public default route; required updates use controlled path |
| Monitoring | Retained until scrape paths pass | Monitoring zone | No public dashboard route |
| Backup | Optional bootstrap during build | Backup zone | Restricted flows to approved backup/restore sources |

Dual-NIC migration must check asymmetric routing, DNS, source-host grants,
Kubernetes node/Ingress addresses, Prometheus targets, and firewall/ACL return
paths before removing bootstrap connectivity.

## CIDR Conflict Check

| Check | Result |
|---|---|
| `10.10.0.0/16` vs `10.20.0.0/16` | PASS - no overlap |
| `10.10.0.0/16` vs `10.30.0.0/16` | PASS - no overlap |
| `10.10.0.0/16` vs `10.40.0.0/16` | PASS - no overlap |
| OpenStack vs AWS vs Azure aggregates | PASS - distinct `/16` ranges |
| Optional `10.255.0.0/16` vs defined aggregates | PASS - no overlap |
| Bootstrap network vs planned aggregates | LOCAL CHECK REQUIRED because committed bootstrap CIDR is masked |
| OpenStack provider `10.10.70.0/24` vs tenant/public-cloud aggregates | PASS - provider is inside the On-Prem aggregate and distinct from tenant/AWS/Azure ranges |

The conflict check must be repeated against the host LAN, VPN clients,
hypervisor networks, EVE-NG management, cloud provider network, and any overlay
before apply.

## External Address

The actual external address is always represented as
`<external-address-masked>`. It is not part of an internal CIDR reservation and
may expose only approved HTTP/HTTPS ingress under
`docs/external-address-policy.md`.

## Non-Production Disclaimer

These are disposable lab reservations. They do not prove allocation,
reachability, routing, or cloud resource creation.
