# Scope

## Included

- Replica lag measurement validation plan.
- `SHOW REPLICA STATUS` or `SHOW SLAVE STATUS` lag field validation plan.
- `Seconds_Behind_Source` or `Seconds_Behind_Master` validation plan.
- Primary write timestamp placeholder validation plan.
- Replica read delay validation plan.
- Replication lag threshold definition.
- Lag evidence collection plan.
- DB exporter metric mapping placeholder.
- Prometheus metric integration placeholder.
- Target DB nodes: `db-primary-01`, `db-replica-01`, and `db-replica-02`.

## Excluded

- Real MariaDB configuration implementation.
- Real database passwords, credentials, private keys, tfstate, kubeconfig, cloud account values, or account-specific files.
- Real public IP addresses.
- MariaDB access control validation, which is handled in S017.
- Primary-Replica replication validation, which is handled in S026.
- DB replica failure validation, which is handled in S033.
- DB primary stop runbook validation, which is handled in S034.
- Backup and restore validation, which are handled in S038 and S039.
- DB exporter installation and Prometheus target discovery, which are handled in S028.
- Galera Cluster, ProxySQL, DB automatic failover, and split-brain automation, which are excluded from v1 scope.

## Provisional Thresholds

- NORMAL: less than 5 seconds.
- WARNING: 5 to 30 seconds.
- CRITICAL: greater than 30 seconds.

These are provisional validation thresholds only. Replace them later only when a real operational threshold is documented and approved.

## Placeholder Rules

Use placeholders such as `<db-primary-host>`, `<db-replica-host>`, `<replication-user>`, `<test-database>`, `<test-table>`, and `<lag-threshold-seconds>`.
