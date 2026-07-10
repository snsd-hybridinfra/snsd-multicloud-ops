# Rollback Plan

This scenario is documentation-only, so rollback means reverting unsafe documentation or evidence changes rather than changing MariaDB replication state.

## Rollback Steps

1. Stop validation if evidence includes database passwords, credentials, real public IPs, private keys, tfstate, kubeconfig content, cloud account values, or account-specific values.
2. Remove sensitive values from evidence and replace them with placeholders.
3. Mark affected validation checks as `BLOCKED` until sanitized evidence is available.
4. If future review identifies missing replica, stopped replication, replication error, inconsistent data, missing binary log configuration, or missing replication user, record the finding as `FAIL`.
5. Do not configure replication, create users, change binary logs, perform failover, or modify database data from this scenario.
6. Update tracking files if the scenario status changes.

## Recovery Notes

Corrective action should restore replication configuration, user placeholders, topology consistency, or replica status through a separately approved implementation task, then repeat evidence collection with sanitized outputs.
