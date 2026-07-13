# Scope

## Included

- Static runbook, threshold matrix, metric reference, and four sample checks.
- Lag ranges: normal 0-5, warning 6-30, critical above 30, and critical NULL.
- Modern `Replica_*` and compatible legacy `Slave_*` fields.
- IO/SQL thread and IO/SQL error-field parsing.
- Expected warning and negative-fixture classification.
- Credential, connection, dump, observability-credential, address, identifier, and execution safety.

## Excluded

- MariaDB connection/client/SQL execution or replication changes.
- Prometheus/Grafana connection, query, credential, scrape target, or dashboard access.
- Real hosts, users, passwords, connection strings, database names, binlogs, GTIDs, dumps, or environment labels.
- Automatic remediation/failover and S017/S026/S028/S029/S033/S034 responsibilities.
