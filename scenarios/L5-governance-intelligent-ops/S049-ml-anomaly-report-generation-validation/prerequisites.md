# Prerequisites

PowerShell and repository-local samples are sufficient; optional Python uses only the standard library.

- `docs/scope-lock.md` and `docs/excluded-scope.md` have been reviewed.
- S049 scenario and evidence directories exist.
- Dataset paths, report paths, metric names, detection outputs, review priorities, and evidence references use placeholders only.
- S047, S048, S050, S028, S029, and S030 boundaries are understood.
- No real ML output, real dataset records, real report output, credentials, tokens, API keys, secrets, public IPs, cloud account values, private keys, tfstate, kubeconfig, subscription IDs, tenant IDs, billing account IDs, or account-specific values are present.

## Related Scenario Boundaries

- S047 handles ML metric dataset collection.
- S048 handles ML anomaly detection validation.
- S050 handles final evidence report generation.
- S028 handles Prometheus target discovery.
- S029 handles Grafana dashboard validation.
- S030 handles Blackbox endpoint probe validation.
