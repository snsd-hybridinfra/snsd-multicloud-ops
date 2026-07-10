# Prerequisites

## Required Previous Scenarios

- S020-grafana-anonymous-access-denial-validation: defines login requirement and anonymous access denial assumptions.
- S028-prometheus-target-discovery-validation: defines Prometheus target discovery assumptions.
- S027-db-replication-lag-validation: defines DB metric mapping assumptions for future MariaDB panels.
- S025-load-balancing-health-check-validation: defines service health check assumptions for dashboard summary views.

## Required Tools or References

- Grafana service access capability, when future execution is approved.
- Prometheus datasource placeholder such as `<prometheus-datasource>`.
- Evidence model from `docs/evidence-model.md`.
- Placeholder naming rules from `docs/naming-rules.md`.

## Safety Preconditions

- Do not add Grafana passwords, credentials, secrets, private keys, tfstate, kubeconfig content, cloud account values, subscription IDs, tenant IDs, or account-specific values.
- Do not record real public IPs.
- Do not implement Grafana dashboards, datasource credentials, Alertmanager, or Prometheus configuration as part of this scenario skeleton.
