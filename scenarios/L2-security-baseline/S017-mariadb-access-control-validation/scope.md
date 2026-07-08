# Scope

## Included

- On-Prem DB Primary access policy validation plan.
- On-Prem DB Replica access policy validation plan.
- Application user access model validation plan.
- Replication user access model validation plan.
- Backup user access model validation plan.
- Denial of public DB access.
- Denial of direct Web node DB access.
- Cloud App/API node to DB access placeholder validation.
- Bastion or management-only administrative access placeholder validation.
- MariaDB user, host, and grant validation plan.
- Network-level DB port exposure validation plan.

## Excluded

- Real MariaDB configuration implementation.
- Real database passwords, credentials, private keys, tfstate, kubeconfig, or account-specific files.
- Real public IP addresses or production CIDR values.
- MariaDB replication validation, which is handled in S026.
- DB replication lag validation, which is handled in S027.
- Backup validation, which is handled in S038.
- Restore validation, which is handled in S039.

## Placeholder Rules

Use placeholders such as `<db-primary-host>`, `<db-replica-host>`, `<app-db-user>`, `<replication-user>`, `<backup-user>`, and `<app-node-cidr>`.
