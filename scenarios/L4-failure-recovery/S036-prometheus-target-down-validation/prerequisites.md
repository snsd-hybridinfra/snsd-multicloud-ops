# Prerequisites

- Repository scope lock and excluded-scope rules have been reviewed.
- Matching evidence directory exists at `evidence/L4-failure-recovery/S036-prometheus-target-down-validation/`.
- S028 Prometheus target discovery validation is planned before target DOWN behavior is interpreted.
- S029 Grafana dashboard validation remains separate and must not be reimplemented here.
- S030 Blackbox endpoint probe validation remains separate and must not be reimplemented here.
- Placeholder values are available for `<prometheus-endpoint>`, `<target-job>`, `<target-instance>`, `<node-exporter-target>`, `<db-exporter-target>`, `<blackbox-exporter-target>`, and `<recovery-threshold-seconds>`.
- No real public IPs, credentials, secrets, private keys, tfstate, kubeconfig, cloud account values, subscription IDs, tenant IDs, or account-specific values are required for this documentation skeleton.
