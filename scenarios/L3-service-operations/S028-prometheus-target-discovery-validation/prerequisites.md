# Prerequisites

## Required Previous Scenarios

- S007-multi-cloud-inventory-validation: defines placeholder service and evidence targets.
- S021-kubernetes-node-readiness-validation: defines Kubernetes/k3s node target assumptions.
- S026-mariadb-primary-replica-replication-validation: defines DB topology assumptions.
- S027-db-replication-lag-validation: defines DB lag metric mapping assumptions.

## Required Tools or References

- Prometheus service and configuration validation capability, when future execution is approved.
- HTTP access to placeholder `<prometheus-endpoint>`, when future execution is approved.
- Evidence model from `docs/evidence-model.md`.
- Placeholder naming rules from `docs/naming-rules.md`.

## Safety Preconditions

- Do not add credentials, secrets, private keys, tfstate, kubeconfig content, cloud account values, subscription IDs, tenant IDs, or account-specific values.
- Do not record real public IPs.
- Do not implement Prometheus configuration, exporters, alerting, or Alertmanager as part of this scenario skeleton.
