# Rollback Plan

This scenario is documentation-only, so rollback means reverting unsafe documentation or evidence changes rather than changing Grafana dashboards.

## Rollback Steps

1. Stop validation if evidence includes Grafana passwords, credentials, secrets, real public IPs, private keys, tfstate, kubeconfig content, cloud account values, subscription IDs, tenant IDs, or account-specific values.
2. Remove sensitive values from evidence and replace them with placeholders.
3. Mark affected validation checks as `BLOCKED` until sanitized evidence is available.
4. If future review identifies missing datasource, query failure, empty dashboard, broken panel, no data, missing screenshot, or anonymous exposure, record the finding as `FAIL`.
5. Do not create or modify Grafana dashboards, datasource credentials, Prometheus configuration, or Alertmanager integration from this scenario.
6. Update tracking files if the scenario status changes.

## Recovery Notes

Corrective action should restore dashboard visibility, datasource connectivity, panel rendering, or screenshot evidence through a separately approved implementation task, then repeat evidence collection with sanitized outputs.
