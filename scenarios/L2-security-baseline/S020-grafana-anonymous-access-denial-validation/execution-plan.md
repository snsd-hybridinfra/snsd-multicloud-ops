# Execution Plan

1. Run `tools/validate-grafana-anonymous-access-denial.ps1` from the repository root.
2. Confirm the baseline, matrix, and non-production INI example.
3. Extract `[auth.anonymous]` and validate `enabled = false`.
4. Reject anonymous true-settings and environment override enablement.
5. Validate Viewer denial, authenticated access, credential-storage prohibitions, and all matrix areas.
6. Reject real passwords, Grafana tokens, datasource credentials, URLs, addresses, identifiers, and private material.
7. Confirm the validator contains no Grafana, container, curl, host, or network command and review evidence.

## Execution Boundary

The script does not run Grafana, start containers, curl services, connect to hosts, read environment secrets or credentials, or validate live login.
