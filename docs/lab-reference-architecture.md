# Lab Phase 1 Reference Virtual Lab Architecture

## Purpose

This document defines the minimum non-production virtual lab used to collect sanitized, reviewable evidence for the locked S001-S050 scenario set. It is a planning reference for later lab construction; it does not provision infrastructure, assign real addresses, or prove that any live scenario has passed.

## Relationship to S001-S050

The lab supplies reusable hosts and network boundaries for evidence collection without changing scenario ownership or acceptance criteria.

- L1 scenarios establish the control plane, routing, inventory, reachability, naming, and evidence foundations.
- L2 scenarios validate access-control and least-privilege baselines.
- L3 scenarios validate service, database, traffic, and observability operations.
- L4 scenarios use controlled, disposable experiments and documented rollback.
- L5 scenarios evaluate governance artifacts, sanitized metrics, and final evidence aggregation.

Evidence remains stored under each existing scenario at `<evidence-path>`. Lab results supplement sample evidence; they do not create a new scenario or replace the canonical S001-S050 model.

## Minimum Lab Topology

```text
Control workstation
  |
  v
bastion-vm ---- management boundary ---- <lab-network-placeholder>
  |                    |                         |
  |                    |                         +-- monitoring stack
  |                    +-- k3s-node
  +-- internal data zone
                         +-- db-primary
                         +-- db-replica
```

All logical names and addresses in this document are placeholders. A real implementation must use disposable non-production resources and sanitize collected evidence before committing it.

## VM Role Table

| Logical VM Role | Address Placeholder | Primary Responsibility | Related Scenario Areas | Evidence Boundary |
|---|---|---|---|---|
| `bastion-vm` | `<bastion-ip-placeholder>` | Controlled administrative entry point, SSH path verification, and management-zone separation | S008, S011-S016, S037 | Record sanitized reachability and policy results only; never commit keys, usernames, or source addresses |
| `k3s-node` | `<k3s-node-ip-placeholder>` | Non-production k3s runtime for sample workloads, ingress, service health, and controlled workload-failure exercises | S018, S021-S025, S031-S032, S035, S044 | Do not commit kubeconfig, service-account tokens, cluster identifiers, or unsanitized manifests |
| `db-primary` | `<db-primary-ip-placeholder>` | MariaDB primary role for access, replication, backup, and controlled stop/recovery evidence | S017, S026-S027, S034, S038-S040 | Do not commit database credentials, dumps, user data, or actual internal addresses |
| `db-replica` | `<db-replica-ip-placeholder>` | MariaDB replica role for replication, lag, replica-failure, and recovery evidence | S026-S027, S033, S038-S040 | Commit only sanitized status output and synthetic test data |
| `monitoring stack` | `<monitoring-ip-placeholder>` | Prometheus, Grafana, Blackbox Exporter, and approved exporter evidence collection | S019-S020, S028-S030, S036, S040, S047-S049 | Do not commit session cookies, Authorization headers, tokens, raw production metrics, or real endpoint labels |

Every VM should use a lab-only hostname represented in repository documentation as `<hostname-placeholder>`.

## Role Boundaries

### bastion-vm

- Provides the only planned administrative path into internal lab roles.
- Supports evidence for approved-source access and denied direct-access paths.
- Does not store committed private keys or real administrator identity data.

### k3s-node

- Runs only disposable sample workloads required by existing Kubernetes scenarios.
- Keeps application data synthetic and replaceable.
- Separates live lab execution from committed sanitized manifests and logs.

### db-primary and db-replica

- Use synthetic records solely to demonstrate replication, lag, backup, restore, and recovery behavior.
- Remain in an internal data zone and are not exposed as public services.
- Use manual, documented rollback and recovery where required by L4 scenarios.

### monitoring stack

- Collects lab-only infrastructure and service metrics.
- Produces screenshots and exported summaries only after labels, endpoints, and identifiers are masked.
- Does not operate as SIEM, EDR, SOAR, or production monitoring.

## Optional EVE-NG Integration

EVE-NG may be introduced after the minimum VM lab is stable to represent routing, segmentation, and controlled transit boundaries for S002 and related network scenarios. EVE-NG device names, management addresses, configurations, and screenshots must be sanitized before entering evidence directories. The optional integration does not change the locked platform architecture.

## Optional Public Cloud Integration

Later phases may attach disposable AWS, Azure, or OpenStack resources to the same evidence process for the scenarios that already own those providers. Public-cloud work requires separate user authorization, cost controls, placeholder-safe documentation, and sanitized outputs. Lab Phase 1 neither authenticates to a provider nor creates cloud resources.

## Evidence Collection Boundary

- Collect only commands and outputs required by an existing scenario validation plan.
- Store evidence in the matching `<evidence-path>` under `logs/`, `screenshots/`, or `configs/`.
- Keep useful sample files and add real sanitized lab evidence alongside them.
- Mask actual addresses, hostnames, usernames, resource identifiers, URLs, and authentication material.
- Stop collection if output contains an unknown sensitive value; create a sanitized summary instead.

## Non-Production Disclaimer

This reference architecture is for a disposable portfolio lab. It is not a production design, availability commitment, security certification, external audit result, or authorization to access any live cloud or organizational network.
