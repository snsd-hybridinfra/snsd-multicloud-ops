# Lab Network Zone Plan

**Status: EVE-NG network foundation and OpenStack provider/tenant integration
VALIDATED with READY evidence. Other service VMs remain NOT_STARTED.**

## Purpose

This document records the operator-confirmed non-production EVE-NG network
foundation and retains planned policy for later service integration. The
configuration is implemented in the disposable lab; this repository stores no
device binary, proprietary image detail, raw console output, credential, or
unsanitized runtime identifier.

## Observed EVE-NG Host Bootstrap

The following host-side bridge state was observed on 2026-07-15. It is not
evidence of an internal routed topology.

| EVE-NG bridge | VMware role | Observed state | Boundary |
|---|---|---|---|
| `pnet0` / `eth0` | VMware NAT bootstrap uplink | Bridge, masked address, and sole EVE-host default route observed | Gateway and public-connectivity probes are retained in sanitized form |
| `pnet1` / `eth1` | VMware host-only management | Bridge/address, ping, SSH/22, and HTTP/80 evidenced; topology UI image reviewed | HTTPS/443 accurately recorded unavailable |
| `pnet2`-`pnet7` / `eth2`-`eth7` | Future EVE-NG Cloud attachment | Layer-2 bridge membership observed | No router, zone, or Layer-3 reachability claim |
| `pnet8`, `pnet9` | Unassigned placeholders | No carrier and no attached physical interface | Not ready for Cloud attachment |

Runtime addresses, networks, gateways, MAC addresses, and bridge identifiers
are retained only in sanitized form under retired-numbered-case evidence.

## Implemented Network Foundation

| Layer | Implemented state | Repository evidence boundary |
|---|---|---|
| Compute capability | EVE-NG KVM acceleration available | Sanitized KVM module output exists |
| Network devices | `SNSD-R1` Cisco 3725 and `SNSD-SW1` Cisco vIOS L2 booted | Live CLI state output proves both operational; no image details committed |
| Router persistence | Configuration register corrected to `0x2102`; reload persistence confirmed | Register and NVRAM-loaded interface state exists; reload transcript not retained |
| Physical link | Router-switch duplex mismatch corrected | Connected full-duplex switch status exists |
| Layer 2 | VLANs 20, 30, 40, 50, 60, and 70 configured | Sanitized VLAN and trunk output exists |
| Layer 3 | Router-on-a-Stick with six 802.1Q subinterfaces | Six up/up subinterfaces and connected routes evidenced |
| WAN | VMware NAT-side DHCP uplink and default route | Sanitized WAN/default-route output exists; addresses remain masked |
| NAT | PAT overload for `10.10.0.0/16` validated | Translations, statistics, NAT ACL matches, and public connectivity evidenced |
| ACL | Pre-ACL DMZ-to-Kubernetes allow, post-ACL deny, reverse permit, and gateway/internet preservation evidenced | Explicit deny responses and post-removal restoration are retained; a directional ACL counter was not required or retained |

The implementation record and E001-E014 sanitized evidence chain are complete.
retired-numbered-case is `VALIDATED` with evidence readiness `READY`.

## Zone Model

| Zone | Planned CIDR | Owner | Permitted Purpose | Default Posture |
|---|---|---|---|---|
| Bootstrap Management | `<bootstrap-management-cidr>` | Local lab operator | EVE-NG SSH/HTTP management | Ping, SSH/22, and HTTP/80 validated; runtime address masked |
| DMZ | `10.10.20.0/24` | EVE-NG / On-Prem | Controlled edge/test endpoint segment | VLAN/gateway implemented; service integration pending |
| Kubernetes | `10.10.30.0/24` | Local Kubernetes | Workload, Ingress, and Service traffic | VLAN/gateway implemented; service VM not started |
| Database | `10.10.40.0/24` | Local MariaDB | Primary/replica, application DB access, backup | VLAN/gateway implemented; DB VMs not started |
| Monitoring | `10.10.50.0/24` | Observability stack | Scrape, dashboard, and probe traffic | VLAN/gateway implemented; monitoring VM not started |
| Backup | `10.10.60.0/24` | Backup role | Backup repository and restore staging | VLAN/gateway implemented; backup VM not started |
| OpenStack Provider | `10.10.70.0/24` | EVE-NG / OpenStack | Flat provider network and Floating IP path | VLAN gateway, `physnet1`, `br-ex`, router external interface, and reachability validated |
| OpenStack Tenant | `10.20.10.0/24` | OpenStack | Private-cloud instance validation | Tenant network, DHCP, router path, one instance, and outbound connectivity validated; Security Group policy remains retired-numbered-case |
| AWS | `10.30.0.0/16` | AWS Terraform environment | Minimum public-cloud validation | SG-controlled; temporary resources only |
| Azure | `10.40.0.0/16` | Azure Terraform environment | Minimum public-cloud validation | NSG-controlled; temporary resources only |
| Optional Overlay | `10.255.0.0/16` | Connectivity owner | Optional WireGuard transit | Disabled unless separately approved |

## Default Flow Matrix

| Source | Destination | Planned Flow | Decision |
|---|---|---|---|
| Approved control workstation | Bastion | SSH administration | ALLOW through approved source rule only |
| Bastion | Service-zone hosts | SSH/management required by runbook | ALLOW least privilege |
| Kubernetes workloads | MariaDB primary | Application database port | ALLOW from approved application source only |
| MariaDB primary | MariaDB replica | Replication | ALLOW dedicated replication flow |
| Monitoring | Approved nodes/exporters | Metric scrape | ALLOW explicit targets/ports |
| Backup | MariaDB/approved services | Backup/restore flow | ALLOW only during controlled operation |
| External address | Kubernetes Ingress | HTTP/HTTPS | OPTIONAL ALLOW during approved window |
| Public/external | SSH, DB, Kubernetes API, OpenStack API, Prometheus, Grafana, EVE-NG management | Management/data access | DENY |
| Any zone | Any unspecified zone/port | Unapproved flow | DENY by default |

## EVE-NG Responsibility

EVE-NG is the On-Prem network-control axis. It owns routing, zone boundaries,
ACL enforcement, and controlled network failure-path validation. Device
management addresses and real configuration output must be sanitized before
commit.

## Migration Controls

1. Retain bootstrap connectivity while adding the service NIC.
2. Validate gateway, return route, DNS, and ACL policy.
3. Revalidate retired-numbered-case, retired-numbered-case, retired-numbered-case, retired-numbered-case, and retired-numbered-case on the service path.
4. Update monitoring and backup targets.
5. Remove or restrict bootstrap service traffic only after rollback is proven.

retired-numbered-case and retired-numbered-case do not require full repetition solely for address normalization
unless node or workload runtime configuration changes.

## Non-Production Disclaimer

The EVE-NG VLAN/gateway topology (retired-numbered-case) and one OpenStack AIO provider/tenant
network path (retired-numbered-case) are validated from operator-executed results. Planned
service flows do not prove that Kubernetes, database, monitoring, backup,
public-cloud, HA, storage, or production security controls exist.
