# Validation

Scenario: S027-db-replication-lag-validation
Level: L3-service-operations
Capability: MariaDB Replication Lag Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real MariaDB replication lag output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Replica status command validation plan | Replica status output can be reviewed. | TODO | NOT_RUN | `commands.md`; `logs/db-replication-lag-validation.log` |
| V002 | Seconds_Behind_Source / Seconds_Behind_Master field validation plan | Lag field is present and not `NULL`. | TODO | NOT_RUN | `commands.md`; `logs/db-replication-lag-validation.log` |
| V003 | Primary timestamp write validation plan | Primary timestamp write can be performed during approved validation. | TODO | NOT_RUN | `commands.md`; `logs/db-replication-lag-validation.log` |
| V004 | Replica timestamp read validation plan | Replica timestamp read can be compared to primary timestamp. | TODO | NOT_RUN | `commands.md`; `logs/db-replication-lag-validation.log` |
| V005 | Replica lag threshold comparison plan | Lag can be categorized as NORMAL, WARNING, or CRITICAL. | TODO | NOT_RUN | `commands.md`; `configs/db-replication-lag-threshold.md` |
| V006 | db-replica-01 lag validation plan | `db-replica-01` lag is measurable and within documented status. | TODO | NOT_RUN | `commands.md`; `logs/db-replication-lag-validation.log` |
| V007 | db-replica-02 lag validation plan | `db-replica-02` lag is measurable and within documented status. | TODO | NOT_RUN | `commands.md`; `logs/db-replication-lag-validation.log` |
| V008 | Replication lag metric mapping placeholder | Metric mapping is documented without installing exporters. | TODO | NOT_RUN | `commands.md`; `configs/db-replication-lag-metric-mapping.md` |
| V009 | Lag evidence capture plan | Lag evidence can be reviewed without secrets or real IPs. | TODO | NOT_RUN | `commands.md`; `logs/db-replication-lag-validation.log`; `screenshots/db-replication-lag-status.png` |
| V010 | Failure condition for NULL lag value, replication stopped, lag above threshold, missing replica, inconsistent timestamp, or missing evidence | Lag validation failures produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Provisional Thresholds

| Status | Threshold | Status |
|---|---|---|
| NORMAL | `< 5 seconds` | NOT_RUN |
| WARNING | `5-30 seconds` | NOT_RUN |
| CRITICAL | `> 30 seconds` | NOT_RUN |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- DB replication lag threshold summary is captured: NOT_READY
- DB replication lag metric mapping is captured: NOT_READY
- DB replication lag validation log is captured: NOT_READY
- DB replication lag screenshot is captured: NOT_READY

## Notes

This scenario validates MariaDB replication lag only. Access control is handled in S017, primary-replica replication setup in S026, exporter installation and Prometheus target discovery in S028, failure response in S033 and S034, and backup/restore in S038 and S039. Galera Cluster, ProxySQL, DB automatic failover, and split-brain automation are excluded from v1 scope.
