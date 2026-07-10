# Scope

## Included

- DB Primary node role validation plan.
- DB Replica node role validation plan.
- Replication user placeholder model.
- Binary log configuration validation plan.
- Replica source configuration validation plan.
- Primary write and replica read validation plan.
- Replication status validation plan.
- Replication error detection plan.
- Replication topology evidence collection plan.
- Target DB nodes: `db-primary-01`, `db-replica-01`, and `db-replica-02`.

## Excluded

- Real MariaDB configuration implementation.
- Real database passwords, credentials, private keys, tfstate, kubeconfig, cloud account values, or account-specific files.
- Real public IP addresses.
- MariaDB access control validation, which is handled in S017.
- DB replication lag validation, which is handled in S027.
- DB replica failure validation, which is handled in S033.
- DB primary stop runbook validation, which is handled in S034.
- Backup and restore validation, which are handled in S038 and S039.
- Galera Cluster, ProxySQL, DB automatic failover, and split-brain automation, which are excluded from v1 scope.

## Placeholder Rules

Use placeholders such as `<db-primary-host>`, `<db-replica-host>`, `<replication-user>`, `<replication-password-placeholder>`, `<test-database>`, and `<test-table>`.
