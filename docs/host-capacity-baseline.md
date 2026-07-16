# Host Capacity Baseline

**Status: PLANNED - observed host capacity only; no VM existence is implied.**

## Purpose

This document is the authoritative Lab Phase 0 capacity baseline for staging the
non-production lab. It records only capacity needed for planning. Disk serial
numbers, device identifiers, and other unique hardware identifiers are excluded.

## Observed Host Capacity

| Resource | Observed Capacity | Planning Interpretation |
|---|---:|---|
| CPU class | AMD Ryzen 5 5600X | Consumer desktop CPU suitable for staged lab workloads |
| Physical cores | 6 | Avoid sustained simultaneous CPU-heavy stacks |
| Logical processors | 12 | Keep each execution profile within a moderate vCPU budget |
| Installed memory | Approximately 32GB | Marketing/installed capacity reference only |
| Effective memory | Approximately 31.9GiB | Authoritative memory value for profile arithmetic |
| Dedicated active-VM SSD available | Approximately 405GB | Active thin-provisioned VM disks only |
| Secondary HDD available | Approximately 227GB | ISO, exports, packet captures, backups, and raw local-only evidence |
| System drive free | Approximately 31GB | Repository and small documents only |

The values are a point-in-time planning observation. They do not prove that any
planned VM, network, cloud, service, or scenario exists.

## Memory and CPU Budget

- Preserve at least approximately 8GB for Windows and virtualization overhead.
- The resulting maximum planned guest-memory envelope is approximately 23.9GiB.
- Do not allocate the complete 33GB planned VM set at the same time.
- Use the execution profiles in `docs/lab-execution-profiles.md`.
- OpenStack is CPU- and memory-intensive and runs only in its dedicated staged
  profiles.
- A Nova guest consumes resources inside the OpenStack All-in-One allocation;
  it is not an additional host-side VM allocation.

## Capacity Gates

Before powering on a profile:

1. Confirm enough free host memory exists for its guest total plus the 8GB host
   reserve.
2. Confirm active SSD free space can accommodate current thin-disk growth and
   temporary snapshot overhead.
3. Confirm the previous profile is powered off, not merely suspended.
4. Reject any unplanned VM or Nova instance that exceeds the profile.
5. Stop and revise the plan if memory pressure, paging, disk pressure, or nested
   virtualization instability appears.

## Current Implementation State

The EVE-NG appliance and its in-lab router/switch nodes now exist. No capacity
value in this document proves any separate service or cloud VM exists, and it
is not scenario validation evidence.
