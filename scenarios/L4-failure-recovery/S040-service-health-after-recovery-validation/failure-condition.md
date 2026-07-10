# Failure Condition

This scenario is considered failed, degraded, or inconclusive if:

- Web service remains unavailable after recovery.
- API service remains unavailable after recovery.
- Ingress or Nginx Reverse Proxy response is unavailable or inconsistent.
- Load balancing health endpoint remains unhealthy.
- DB Primary dependency is unavailable.
- DB Replica state cannot be reviewed when required.
- Prometheus target visibility is missing.
- Grafana dashboard visibility is missing.
- Blackbox probe fails after recovery.
- Recovery evidence is inconsistent or cannot be reconciled.
- Degraded state is not documented.
- Final judgment is missing.
- Documentation claims automatic DR, production-grade HA, automatic cross-cloud failover, or enterprise recovery orchestration.
- Credentials, secrets, public IPs, database dumps, private keys, tfstate, kubeconfig, or account-specific values are introduced.
