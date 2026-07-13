# Scope

## Included

- Static runbook, command reference, non-executing Ansible placeholder, and three sanitized sample checks.
- Modern `Replica_*` and compatible legacy `Slave_*` IO/SQL fields.
- `Seconds_Behind_Source` or `Seconds_Behind_Master` parsing against a sample threshold.
- Empty `Last_IO_Error` and `Last_SQL_Error` validation.
- Symbolic binary-log file, position, GTID, topology, account, and channel checks.
- Credential, connection, dump, address, identifier, and execution safety.

## Excluded

- MariaDB connection, client invocation, SQL execution, or credential reads.
- Replication start, stop, reset, repair, reconfiguration, user changes, or automatic failover.
- Real users, passwords, hosts, connection strings, binlog/GTID values, database names, dumps, and production exports.
- S017, S027, S033, S034, S038, and S039 responsibilities.
