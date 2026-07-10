# Prerequisites

- `docs/scope-lock.md` and `docs/excluded-scope.md` have been reviewed.
- S048 scenario and evidence directories exist.
- Dataset paths, metric names, baseline windows, detection windows, anomaly scores, thresholds, target jobs, and target instances use placeholders only.
- S047, S049, S050, S028, S029, and S030 boundaries are understood.
- No real ML output, real dataset records, credentials, tokens, API keys, secrets, public IPs, cloud account values, private keys, tfstate, kubeconfig, subscription IDs, tenant IDs, billing account IDs, or account-specific values are present.

## Related Scenario Boundaries

- S047 handles ML metric dataset collection.
- S049 handles ML anomaly report generation.
- S050 handles final evidence report generation.
- S028 handles Prometheus target discovery.
- S029 handles Grafana dashboard validation.
- S030 handles Blackbox endpoint probe validation.
