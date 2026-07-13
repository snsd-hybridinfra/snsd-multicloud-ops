# MariaDB Primary-Replica Replication Validation

This runbook defines static, repository-side evaluation of sanitized replication evidence. It never connects to MariaDB or executes SQL.

## Topology and Stream Model

- Primary node: `<db-primary-host>`
- Replica node: `<db-replica-host>`
- Replication account: `<replication-db-user>`
- Replication channel: `<replication-channel>`
- Binary log: `<binlog-file-placeholder>` at `<binlog-position-placeholder>`
- Optional GTID representation: `<gtid-placeholder>`

The primary binary log / replication stream carries ordered changes to the replica. Evidence must prove that both the replica IO thread and replica SQL thread are running.

## Expected State

- `Replica_IO_Running: Yes` and `Replica_SQL_Running: Yes`, or accepted legacy `Slave_*` equivalents.
- `Seconds_Behind_Source` or `Seconds_Behind_Master` is numeric and not `NULL`.
- Static sample lag is `0`; nonzero values are compared with the non-production threshold documented in the validation notes.
- `Last_IO_Error` and `Last_SQL_Error` are empty.
- Master/source status contains symbolic file and position values only.

S027 owns detailed replication-delay policy and trend validation. S026 only verifies that delay evidence is present, parseable, and within the local sample threshold.

## Failure Indicators

IO or SQL thread `No`, missing thread evidence, `NULL` delay, delay above the documented threshold, or a non-empty IO/SQL error is a failure. Legacy `SHOW SLAVE STATUS` terminology is accepted with a warning for compatibility.

## Evidence Collection Model

Sanitized lab output may be copied into `<evidence-path>` only after replacing hosts, users, channels, binary-log names/positions, GTIDs, database names, and environment identifiers with approved placeholders.

Static evidence validation reads committed samples only. Real database validation would require separate authorization and manual collection; it is not performed by this scenario or its validator.
