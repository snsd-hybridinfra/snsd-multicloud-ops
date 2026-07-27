# Authoritative Multi-Cloud Lab Architecture Baseline

**Status: PARTIALLY IMPLEMENTED — EVE-NG routing and the OpenStack AIO
provider/tenant network path are validated; later platforms remain planned.**

## Purpose and Authority

This document is the authoritative platform baseline for the non-production
SNSD Multi-Cloud Secure Operations Validation Platform. It defines responsibility
and trust boundaries only; it does not provision resources or prove that planned
components exist.

Related authoritative documents:

- `docs/lab-build-order.md` - canonical phase order;
- `docs/lab-network-zone-plan.md` - network zones and flow policy;
- `docs/lab-ip-plan.md` - address reservations and conflict checks;
- `docs/platform-responsibility-matrix.md` - platform ownership;
- `docs/cloud-cost-guardrails.md` - provider cost limits;
- `docs/resource-lifecycle-policy.md` - creation and cleanup lifecycle;
- `docs/external-address-policy.md` - optional external exposure boundary;
- `docs/host-capacity-baseline.md` - observed host capacity and reserve;
- `docs/vm-resource-allocation-plan.md` - authoritative planned VM sizing;
- `docs/lab-execution-profiles.md` - mutually exclusive staged power profiles;
- `docs/storage-and-snapshot-policy.md` - disk roles, retention, and repository boundary;
- `docs/adr/ADR-0001-multicloud-network-and-platform-baseline.md` - decision record.

## Host Capacity Boundary

The planned VM set totals 33GB RAM and therefore cannot run simultaneously on
the approximately 31.9GiB effective-memory host. Lab work must use Profiles A-D
from `docs/lab-execution-profiles.md`, preserve approximately 8GB for Windows
and virtualization overhead, and keep OpenStack separate from the complete
local-service stack. Capacity planning is not VM implementation evidence.

## Platform Positioning

| Axis | Authoritative Role | Boundary |
|---|---|---|
| EVE-NG / On-Prem | Network-control axis for zoning, routing, ACLs, and network failure paths | Does not become the application or database platform |
| OpenStack | Private Cloud axis; single-node AIO, Neutron provider/tenant networks, router, one instance, and one Floating IP are operator-validated | Terraform reproduction, Security Group policy, drift, cleanup, HA, storage, and hardening remain unvalidated |
| AWS | Minimal Public Cloud A validation environment | One temporary EC2 maximum; free-tier/credit bounded; not a full runtime platform |
| Azure | Minimal Public Cloud B validation environment | One temporary VM maximum; free-tier/credit bounded; not a full runtime platform |
| Local Kubernetes | Application runtime for workloads, Ingress, reverse proxy, load balancing, and controlled failures | Not EKS/AKS and not a public management plane |
| Local MariaDB | Internal primary/replica data platform for access control, replication, backup, and restore | Never publicly exposed |
| External address | Optional HTTP/HTTPS entry for availability and Blackbox checks | No SSH, database, Kubernetes API, cloud API, monitoring, or EVE-NG management exposure |

## Logical Architecture

```text
Optional external client
  | HTTP/HTTPS only via <external-address-masked>
  v
Local Kubernetes Ingress -> Service -> application Pods
  | approved application-to-database flow
  v
Local MariaDB primary/replica

Control workstation -> Bootstrap Management Network -> Bastion
                                             |
                                             v
EVE-NG On-Prem zones and ACL boundary
  |                 |                  |
  v                 v                  v
OpenStack        AWS minimum        Azure minimum
Private Cloud    validation env     validation env
```

The optional WireGuard aggregate is reserved for later connectivity but is not
a mandatory dependency.

## Bootstrap Management Versus Service Networks

The Bootstrap Management Network exists so hosts can be installed, repaired,
and migrated before EVE-NG service zones are complete. Its actual CIDR and host
addresses are private local planning values and remain masked in the repository.

Service networks under the planned On-Prem aggregate separate Bastion/transit,
Kubernetes, database, monitoring, and backup responsibilities. Migration is a
future implementation action; current documents must not imply it already
occurred.

## Security Boundaries

- Administrative access enters through the approved control/Bastion path.
- Database access is limited to approved application, replication, backup, and
  administration sources.
- Kubernetes API, OpenStack API, Prometheus, Grafana, EVE-NG management, SSH,
  and database ports are not public services.
- Public ingress, when enabled, is limited to HTTP/HTTPS and short validation
  windows.
- Cloud Security Groups/NSGs, OpenStack Security Groups, and On-Prem ACLs use
  least privilege and must have rollback evidence.

## Evidence State

- retired-numbered-case contains the validated EVE-NG routing/NAT/ACL foundation evidence.
- retired-numbered-case contains operator-executed OpenStack AIO control-plane and end-to-end
  provider/tenant/Floating-IP evidence normalized by Codex.
- Kubernetes, MariaDB, monitoring, backup/recovery, AWS, and Azure remain
  unvalidated.
- Previous static, sample, synthetic, or provenance-uncertain artifacts remain
  quarantined as non-evidence.

This baseline does not create successor numbered scenario or imply completion of unrelated scenarios.

## Non-Production Disclaimer

All resources described here are disposable lab resources. This is not a
production topology, HA/DR commitment, compliance certification, cloud-spend
authorization, or proof that a planned resource exists.
