# Scope

## Included

- Prometheus service status validation plan.
- Prometheus configuration syntax validation plan.
- Node Exporter target discovery validation plan.
- Kubernetes target discovery placeholder.
- kube-state-metrics target discovery placeholder.
- Blackbox Exporter target discovery placeholder.
- DB Exporter target discovery placeholder.
- AWS service zone target placeholder.
- Azure service zone target placeholder.
- OpenStack service zone target placeholder.
- On-Prem Internal Server Zone target placeholder.
- Prometheus `/targets` page evidence collection plan.
- Target label consistency validation plan.

## Target Categories

- On-Prem infrastructure nodes.
- AWS service nodes.
- Azure service nodes.
- OpenStack service nodes.
- Kubernetes/k3s nodes.
- MariaDB DB nodes.
- Blackbox HTTP probe targets.
- kube-state-metrics target.

## Excluded

- Real Prometheus configuration implementation.
- Credentials, secrets, private keys, tfstate, kubeconfig, cloud account values, subscription IDs, tenant IDs, or account-specific files.
- Real public IPs or production hostnames.
- Grafana dashboard validation, which is handled in S029.
- Blackbox endpoint probe validation, which is handled in S030.
- DB replication lag validation, which is handled in S027.
- Prometheus alerting and Alertmanager integration unless later documented separately.

## Placeholder Rules

Use placeholders such as `<prometheus-endpoint>`, `<node-exporter-target>`, `<db-exporter-target>`, `<blackbox-exporter-target>`, and `<kube-state-metrics-target>`.
