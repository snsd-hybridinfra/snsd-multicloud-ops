# Rollback Plan

This scenario is documentation-only, so rollback means reverting unsafe documentation or evidence changes rather than changing MariaDB replication state.

## Rollback Steps

1. Stop validation if evidence includes database passwords, credentials, real public IPs, private keys, tfstate, kubeconfig content, cloud account values, or account-specific values.
2. Remove sensitive values from evidence and replace them with placeholders.
3. Mark affected validation checks as `BLOCKED` until sanitized evidence is available.
4. If future review identifies `NULL` lag values, stopped replication, lag above threshold, missing replica, inconsistent timestamp, or missing evidence, record the finding as `FAIL`.
5. Do not configure MariaDB replication, create users, install exporters, configure Prometheus, perform failover, or modify database data from this scenario.
6. Update tracking files if the scenario status changes.

## Recovery Notes

Corrective action should restore measurable replica status, timestamp consistency, or lag threshold compliance through a separately approved implementation task, then repeat evidence collection with sanitized outputs.
