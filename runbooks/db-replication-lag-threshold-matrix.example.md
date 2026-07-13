# DB Replication Lag Threshold Matrix Example

NON-PRODUCTION EXAMPLE.

| Lag Condition | Evidence Field | Expected Value / Range | Operational Judgment | Required Action | Related Scenario | Evidence Reference |
|---|---|---|---|---|---|---|
| Seconds_Behind_Master = 0 | `Seconds_Behind_Master` | `0` | NORMAL | Continue observation | S026 | `<evidence-path>` |
| Seconds_Behind_Master between 1 and 5 | `Seconds_Behind_Master` | `1..5` | NORMAL | Continue observation | S026 | `<evidence-path>` |
| Seconds_Behind_Master greater than 5 and less than or equal to 30 | `Seconds_Behind_Master` | `6..30` | WARNING | Review load and stream progress | S027 | `<evidence-path>` |
| Seconds_Behind_Master greater than 30 | `Seconds_Behind_Master` | `>30` | CRITICAL | Investigate before recovery decision | S027 | `<evidence-path>` |
| Seconds_Behind_Master NULL | `Seconds_Behind_Master` | `NULL` | CRITICAL | Inspect threads and errors | S027 | `<evidence-path>` |
| IO thread not running | `Replica_IO_Running` or `Slave_IO_Running` | `No` | CRITICAL | Investigate source-stream failure | S033 | `<evidence-path>` |
| SQL thread not running | `Replica_SQL_Running` or `Slave_SQL_Running` | `No` | CRITICAL | Investigate apply failure | S033 | `<evidence-path>` |
| Last_IO_Error non-empty | `Last_IO_Error` | non-empty | CRITICAL | Preserve sanitized error evidence | S033 | `<evidence-path>` |
| Last_SQL_Error non-empty | `Last_SQL_Error` | non-empty | CRITICAL | Preserve sanitized error evidence | S033 | `<evidence-path>` |
