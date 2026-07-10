# Scope

## Included

- Grafana service access validation plan.
- Prometheus datasource connection validation plan.
- Infrastructure dashboard placeholder.
- Kubernetes dashboard placeholder.
- MariaDB dashboard placeholder.
- Blackbox endpoint dashboard placeholder.
- Multi-cloud service status dashboard placeholder.
- Dashboard panel data rendering validation plan.
- Dashboard time range validation plan.
- Dashboard screenshot evidence collection plan.

## Dashboard Categories

- On-Prem infrastructure node status.
- AWS service node status.
- Azure service node status.
- OpenStack service node status.
- Kubernetes/k3s node and workload status.
- MariaDB replication and availability status.
- Blackbox HTTP endpoint status.
- Service health summary.

## Excluded

- Real Grafana dashboard implementation.
- Grafana admin passwords, credentials, secrets, private keys, tfstate, kubeconfig, cloud account values, subscription IDs, tenant IDs, or account-specific files.
- Real public IPs or production endpoints.
- Grafana anonymous access denial, which is handled in S020.
- Prometheus target discovery validation, which is handled in S028.
- Blackbox endpoint probe validation, which is handled in S030.
- Alertmanager integration unless later documented separately.

## Placeholder Rules

Use placeholders such as `<grafana-endpoint>`, `<prometheus-datasource>`, `<dashboard-name>`, `<panel-name>`, and `<service-health-dashboard>`.
