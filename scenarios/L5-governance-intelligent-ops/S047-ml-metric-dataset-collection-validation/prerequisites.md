# Prerequisites

The validator requires PowerShell and repository-local examples only. Python execution, Prometheus/Grafana access, cloud credentials, kubeconfig, and external ML libraries are not required.

- `docs/scope-lock.md` and `docs/excluded-scope.md` have been reviewed.
- S047 scenario and evidence directories exist.
- Metric names, queries, paths, filenames, target jobs, target instances, dataset windows, and collection scripts use placeholders only.
- S028, S029, S030, S048, S049, and S050 boundaries are understood.
- No real Prometheus output, dataset records, credentials, tokens, API keys, secrets, public IPs, cloud account values, private keys, tfstate, kubeconfig, subscription IDs, tenant IDs, billing account IDs, or account-specific values are present.

## Related Scenario Boundaries

- S028 handles Prometheus target discovery.
- S029 handles Grafana dashboard validation.
- S030 handles Blackbox endpoint probe validation.
- S048 handles ML anomaly detection validation.
- S049 handles ML anomaly report generation.
- S050 handles final evidence report generation.
