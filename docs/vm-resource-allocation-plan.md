# VM Resource Allocation Plan

**Status: PLANNED - allocations are reservations, not implemented VMs.**

## Authoritative Allocation Table

| Role | vCPU | RAM | Thin/OS Disk | Additional Constraint |
|---|---:|---:|---:|---|
| EVE-NG | 2 | 4GB | 50GB thin | Appliance exists empty; no router, firewall, or zone exists |
| OpenStack All-in-One | 6 | 16GB | 120GB thin | Nested virtualization required |
| Bastion | 1 | 1GB | 12GB | Administrative entry role only |
| k3s-node | 2 | 4GB | 30GB | Local application runtime plan only |
| DB Primary | 1 | 2GB | 20GB | Local internal database plan only |
| DB Replica | 1 | 2GB | 20GB | Not an automatic failover claim |
| Monitoring | 2 | 3GB | 30GB | Prometheus/Grafana plan only |
| Backup | 1 | 1GB | 12GB OS | Backup data belongs on the secondary HDD |
| Full planned set | 16 | 33GB | 294GB nominal | Prohibited as a simultaneous execution profile |

Thin provisioning reduces initial physical use but does not remove the 294GB
maximum-growth obligation. The dedicated SSD has approximately 405GB available,
leaving approximately 111GB before hypervisor metadata, temporary files,
snapshots, and free-space reserve. Growth and snapshot usage must therefore be
monitored.

## OpenStack Initial Limit

- Maximum initial Nova instance count: 1.
- Initial Nova flavor target: approximately 1 vCPU and 1GB RAM.
- The Nova workload is nested inside the OpenStack All-in-One VM.
- Do not increase instance count or flavor size until host pressure, nested
  virtualization, storage growth, and cleanup have been observed safely.
- OpenStack All-in-One and the full local-service stack must never run together.

## Allocation Rules

- RAM allocations are hard planning ceilings, not proof of VM creation.
- vCPU values permit modest staged oversubscription but not simultaneous
  CPU-heavy validation.
- VM disks stay on the dedicated active-VM SSD.
- Backup payloads, ISO files, exports, packet captures, and raw local-only
  evidence stay on the secondary HDD.
- No VM disk, OpenStack image, snapshot, ISO, or backup repository belongs in
  the OneDrive-synchronized repository.

## Current Implementation State

The EVE-NG appliance and its in-lab router/switch nodes exist. Every separate
service or cloud VM row remains a future allocation.
