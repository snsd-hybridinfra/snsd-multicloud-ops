# Scope

## Included

- Web service post-recovery validation plan.
- API service post-recovery validation plan.
- Ingress route post-recovery validation plan.
- Nginx Reverse Proxy post-recovery validation plan.
- Load balancing health check post-recovery validation plan.
- MariaDB Primary-Replica post-recovery validation reference.
- Prometheus target UP post-recovery validation plan.
- Grafana dashboard visibility post-recovery validation plan.
- Blackbox endpoint probe post-recovery validation plan.
- Evidence-based final recovery judgment.

## Target Components

- Kubernetes Web workload.
- Kubernetes API workload.
- Kubernetes Service and Ingress.
- Nginx Reverse Proxy.
- Load balancing health endpoint.
- MariaDB Primary and Replica nodes.
- Prometheus targets.
- Grafana dashboards.
- Blackbox probe targets.

## Post-Recovery Judgment Model

- `RECOVERED`: all required service checks pass.
- `DEGRADED`: core service is reachable but one or more non-critical checks fail.
- `FAILED`: core service, DB dependency, or monitoring visibility remains unavailable.
- `INCONCLUSIVE`: required evidence is missing.

## Important Boundary

- Do not claim automatic DR.
- Do not claim production-grade HA.
- Do not claim automatic cross-cloud failover.
- Do not claim enterprise recovery orchestration.
- This scenario judges service recovery through observable health checks, response validation, DB state references, Prometheus target status, Grafana visibility, Blackbox probe status, and evidence capture.

## Excluded

- Real recovery script implementation.
- Real public IPs, database dumps, credentials, secrets, private keys, tfstate, kubeconfig, cloud account values, subscription IDs, tenant IDs, or account-specific values.
- Backup creation validation, which is handled in S038.
- Restore execution validation, which is handled in S039.
- Web Pod failure recovery validation, which is handled in S031.
- API service failure validation, which is handled in S032.
- DB Replica failure validation, which is handled in S033.
- DB Primary stop runbook validation, which is handled in S034.
- Load balancer failure validation, which is handled in S035.
- Prometheus target DOWN validation, which is handled in S036.
- Automatic cross-cloud failover and full disaster recovery automation.
- Changes outside this scenario directory, its matching evidence directory, and the required tracking documents.
