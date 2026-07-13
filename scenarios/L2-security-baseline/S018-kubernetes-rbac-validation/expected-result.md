# Expected Result

## Pass Criteria

- V001 through V014 return `PASS`.
- Application and monitoring workloads use distinct namespace-scoped identities and bindings.
- No cluster-wide, wildcard, default-account, or application-secret privilege exists.
- Monitoring permissions remain read-only.
- No live cluster access or manifest application occurs.

## Evidence Criteria

The ignored log and tracked summary contain sanitized static-validation results only and no kubeconfig, tokens, certificates, keys, endpoints, Secret data, or account-specific values.
