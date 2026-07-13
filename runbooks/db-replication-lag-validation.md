# Database Replication Lag Validation

This runbook defines static evaluation of sanitized MariaDB replication-lag evidence without database or observability-system access.

## Purpose and Topology

- Primary: `<db-primary-host>`
- Replica: `<db-replica-host>`
- Channel: `<replication-channel>`
- Evidence: `<evidence-path>`

`Seconds_Behind_Master` or `Seconds_Behind_Source` estimates how far replica application trails the source stream. It is meaningful only when both the replica IO thread and replica SQL thread are running.

## Threshold Model

| State | Placeholder | Non-production range |
|---|---|---|
| Normal | `<normal-lag-threshold-seconds>` | 0 through 5 seconds |
| Warning | `<warning-lag-threshold-seconds>` | greater than 5 through 30 seconds |
| Critical | `<critical-lag-threshold-seconds>` | greater than 30 seconds or `NULL` |

`NULL` is critical because lag cannot be established, commonly alongside a stopped IO/SQL thread or replication error. An IO or SQL thread not running and any non-empty `Last_IO_Error` or `Last_SQL_Error` are failure indicators regardless of numeric lag.

## Evidence Model

Normal and warning samples are positive health fixtures. Critical and NULL samples are negative fixtures used to prove that the parser classifies unsafe evidence; they are not claims of a healthy system.

S026 owns base replication health and topology validation. S027 owns threshold classification and sanitized lag evidence. Real MariaDB collection, Prometheus queries, and Grafana queries are outside this validator.
