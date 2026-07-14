# Lab Phase 1 Placeholder IP Plan

## Rules

The lab network is represented only as `<lab-cidr-placeholder>`. Actual addresses belong to the disposable local lab and must never be committed without masking. Repository evidence must replace every real address with the corresponding placeholder before review.

| VM Name | Role | Network Zone | Placeholder IP | Access Method | Required Ports | Evidence Scenarios |
|---|---|---|---|---|---|---|
| `bastion-vm` | Administrative entry point | Management / bastion zone | `<bastion-ip-placeholder>` | SSH from an approved lab management source | 22 | S008, S011-S016, S037 |
| `k3s-node` | k3s control/runtime node and sample service | Application zone | `<k3s-node-ip-placeholder>` | SSH through bastion; Kubernetes administration from approved control plane | 22, 6443, 80, 443 | S018, S021-S025, S031-S032, S035, S044 |
| `db-primary` | MariaDB primary | Internal data zone | `<db-primary-ip-placeholder>` | SSH through bastion; database access only from approved application/replication paths | 22, 3306 | S017, S026-S027, S034, S038-S040 |
| `db-replica` | MariaDB replica | Internal data zone | `<db-replica-ip-placeholder>` | SSH through bastion; replication access only from approved database path | 22, 3306 | S026-S027, S033, S038-S040 |
| `monitoring-vm` | Prometheus, Grafana, Blackbox, and approved exporters | Monitoring zone | `<monitoring-ip-placeholder>` | SSH through bastion; dashboards and metrics from approved management/application paths | 22, 3000, 9090, 9115, 9100 | S019-S020, S028-S030, S036, S040, S047-S049 |

## Logical Network Plan

| Network Item | Placeholder | Purpose | Commit Rule |
|---|---|---|---|
| Lab network | `<lab-cidr-placeholder>` | Disposable VM connectivity | Replace the actual CIDR in every committed artifact |
| Bastion address | `<bastion-ip-placeholder>` | Administrative path | Never commit the actual address or approved source range |
| k3s address | `<k3s-node-ip-placeholder>` | Cluster and sample-service path | Mask node, API, ingress, and endpoint addresses |
| Primary DB address | `<db-primary-ip-placeholder>` | Application write and replication source | Mask connection strings and internal topology values |
| Replica DB address | `<db-replica-ip-placeholder>` | Replication and recovery target | Mask replication source/target details |
| Monitoring address | `<monitoring-ip-placeholder>` | Metrics, dashboard, and probe services | Mask datasource URLs, targets, labels, and dashboard links |

## Access Policy

- Administrative SSH uses the bastion path only.
- The database roles remain in the internal data zone and are not public endpoints.
- Kubernetes administration is limited to the approved control-plane path.
- Monitoring interfaces are reachable only from approved lab management/application paths.
- Required ports describe the intended lab flow; they are not authorization to expose services publicly.

## Evidence Sanitization Requirement

Before committing command output, screenshots, configs, diagrams, or logs:

1. Replace actual addresses with the matching placeholder.
2. Replace actual hostnames with `<hostname-placeholder>`.
3. Remove usernames, interface identifiers, DNS names, URLs, and resource identifiers that reveal the lab environment.
4. Re-run repository safety validation.
5. If complete sanitization cannot be verified, commit a sanitized summary instead of the raw artifact.
