# Failure Condition

S026 fails if:

- A required runbook, command reference, playbook, or sample is missing.
- Topology/account/channel/binlog placeholders are incomplete.
- IO or SQL thread evidence is missing or `No`.
- Delay is missing, `NULL`, nonnumeric, or above the documented threshold.
- `Last_IO_Error` or `Last_SQL_Error` is missing or non-empty.
- Master file, position, or GTID uses non-placeholder values.
- A database credential, connection string, client credential flag, dump/export, address, account ID, UUID, or concrete host is detected.
- A database client, SQL-executing Ansible task, or destructive replication/user command is present.

Nonzero delay within threshold and legacy field terminology are warnings, not failures.
