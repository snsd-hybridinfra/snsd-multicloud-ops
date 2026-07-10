# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Replica status command validation plan | Plan sanitized `SHOW REPLICA STATUS` or `SHOW SLAVE STATUS` capture. | Replica status output can be reviewed. | `commands.md`, `logs/db-replication-lag-validation.log`, `validation.md` |
| V002 | Seconds_Behind_Source / Seconds_Behind_Master field validation plan | Review lag field from replica status output. | Lag field is present and not `NULL`. | `commands.md`, `logs/db-replication-lag-validation.log`, `validation.md` |
| V003 | Primary timestamp write validation plan | Plan placeholder timestamp write to `<test-database>.<test-table>`. | Primary timestamp write can be performed during approved validation. | `commands.md`, `logs/db-replication-lag-validation.log`, `validation.md` |
| V004 | Replica timestamp read validation plan | Plan timestamp read from each replica. | Replica timestamp read can be compared to primary timestamp. | `commands.md`, `logs/db-replication-lag-validation.log`, `validation.md` |
| V005 | Replica lag threshold comparison plan | Compare lag value to provisional thresholds. | Lag can be categorized as NORMAL, WARNING, or CRITICAL. | `commands.md`, `configs/db-replication-lag-threshold.md`, `validation.md` |
| V006 | db-replica-01 lag validation plan | Review lag for `db-replica-01`. | `db-replica-01` lag is measurable and within documented status. | `commands.md`, `logs/db-replication-lag-validation.log`, `validation.md` |
| V007 | db-replica-02 lag validation plan | Review lag for `db-replica-02`. | `db-replica-02` lag is measurable and within documented status. | `commands.md`, `logs/db-replication-lag-validation.log`, `validation.md` |
| V008 | Replication lag metric mapping placeholder | Document DB exporter and Prometheus metric mapping placeholder. | Metric mapping is documented without installing exporters. | `commands.md`, `configs/db-replication-lag-metric-mapping.md`, `validation.md` |
| V009 | Lag evidence capture plan | Capture lag status, threshold, and metric mapping evidence. | Lag evidence can be reviewed without secrets or real IPs. | `commands.md`, `logs/db-replication-lag-validation.log`, `screenshots/db-replication-lag-status.png`, `validation.md` |
| V010 | Failure condition for NULL lag value, replication stopped, lag above threshold, missing replica, inconsistent timestamp, or missing evidence | Evaluate findings against explicit failure conditions. | Lag validation failures produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Provisional Threshold Table

| Status | Threshold | Use |
|---|---|---|
| NORMAL | `< 5 seconds` | Expected healthy lag during validation. |
| WARNING | `5-30 seconds` | Review required; not automatically failed unless policy says so later. |
| CRITICAL | `> 30 seconds` | Treat as failed validation unless explicitly justified. |

## Review Notes

Every validation item must map to evidence. This scenario validates replication lag only; replication setup is handled in S026, access control in S017, exporter discovery in S028, and failure response in S033 and S034.
