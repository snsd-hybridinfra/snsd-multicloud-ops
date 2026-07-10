# Commands

Scenario: S027-db-replication-lag-validation
Level: L3-service-operations
Capability: MariaDB Replication Lag Validation
Target: `<db-replica-host>`
Execution timestamp: TODO

Record sanitized output only. Do not include database passwords, credentials, real public IPs, private keys, tfstate, kubeconfig content, cloud account values, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | Replica status command validation plan | Plan sanitized `SHOW REPLICA STATUS` or `SHOW SLAVE STATUS` capture on each replica. | Confirm replica status output is available. | TODO: record sanitized output after approved execution. |
| V002 | Seconds_Behind_Source / Seconds_Behind_Master field validation plan | Review lag field in replica status output. | Confirm lag field is present and not `NULL`. | TODO: record sanitized output after approved execution. |
| V003 | Primary timestamp write validation plan | Plan placeholder timestamp write to `<test-database>.<test-table>` on `<db-primary-host>`. | Confirm primary timestamp can be used for lag measurement. | TODO: record sanitized output after approved execution. |
| V004 | Replica timestamp read validation plan | Plan placeholder timestamp read from each `<db-replica-host>`. | Confirm replica timestamp can be compared to primary timestamp. | TODO: record sanitized output after approved execution. |
| V005 | Replica lag threshold comparison plan | Compare lag to provisional NORMAL, WARNING, and CRITICAL thresholds. | Confirm lag can be categorized. | TODO: record sanitized output after approved execution. |
| V006 | db-replica-01 lag validation plan | Review lag for `db-replica-01`. | Confirm replica lag is measurable. | TODO: record sanitized output after approved execution. |
| V007 | db-replica-02 lag validation plan | Review lag for `db-replica-02`. | Confirm replica lag is measurable. | TODO: record sanitized output after approved execution. |
| V008 | Replication lag metric mapping placeholder | Document DB exporter and Prometheus metric placeholders. | Confirm future metric mapping is defined without installing exporters. | TODO: record sanitized output after approved execution. |
| V009 | Lag evidence capture plan | Capture lag status, threshold, and mapping evidence. | Confirm lag evidence is reviewable. | TODO: record sanitized output after approved execution. |
| V010 | Failure condition for NULL lag value, replication stopped, lag above threshold, missing replica, inconsistent timestamp, or missing evidence | Review validation findings against failure criteria. | Confirm lag failures result in `FAIL` or `BLOCKED`. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/db-replication-lag-threshold.md`
- `configs/db-replication-lag-metric-mapping.md`
- `logs/db-replication-lag-validation.log`
- `screenshots/db-replication-lag-status.png`
