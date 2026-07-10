# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Pre-failure Primary status validation plan | Plan Primary status review for `<db-primary-host>`. | DB Primary is available before Replica failure. | `commands.md`, `logs/db-replica-failure-validation.log`, `validation.md` |
| V002 | Pre-failure Replica status validation plan | Plan Replica status review for `<db-replica-host>`. | Target DB Replica is available before failure. | `commands.md`, `screenshots/db-replica-before-failure.png`, `validation.md` |
| V003 | Pre-failure replication status validation plan | Plan `SHOW REPLICA STATUS` or `SHOW SLAVE STATUS` review. | Replication is running before failure. | `commands.md`, `configs/db-replica-failure-summary.md`, `validation.md` |
| V004 | Replica failure injection plan | Plan one Replica outage using placeholder commands. | Failure injection targets one Replica only. | `commands.md`, `logs/db-replica-failure-validation.log`, `validation.md` |
| V005 | Failed Replica detection validation plan | Review Replica availability after failure. | Failed Replica is detected as unavailable. | `commands.md`, `screenshots/db-replica-during-failure.png`, `validation.md` |
| V006 | Primary write availability during Replica failure validation plan | Plan write test against `<db-primary-host>`. | DB Primary remains writable during Replica failure. | `commands.md`, `logs/db-replica-failure-validation.log`, `validation.md` |
| V007 | Application DB dependency impact placeholder validation plan | Record expected application impact placeholder. | Application DB dependency impact is documented without real app data. | `commands.md`, `configs/db-replica-failure-summary.md`, `validation.md` |
| V008 | Replica restoration validation plan | Plan restoration of the failed Replica. | Replica restoration path is documented. | `commands.md`, `logs/db-replica-failure-validation.log`, `validation.md` |
| V009 | Replication resume validation plan | Plan post-restoration replication status review. | Replication resumes after Replica restoration. | `commands.md`, `configs/db-replica-failure-summary.md`, `validation.md` |
| V010 | Post-recovery consistency validation plan | Plan consistency check for `<test-database>` and `<test-table>`. | Replica data is consistent with the Primary after recovery. | `commands.md`, `screenshots/db-replica-after-recovery.png`, `validation.md` |
| V011 | Recovery time measurement plan | Measure failure detection and Replica recovery duration. | Detection and recovery timing is recorded and compared with thresholds. | `commands.md`, `configs/db-replica-recovery-threshold.md`, `validation.md` |
| V012 | Failure condition for Primary write failure, Replica failure not detected, replication not resumed, inconsistent replica data, excessive recovery time, or missing evidence | Evaluate findings against explicit failure conditions. | DB Replica failure or recovery issues produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates DB Replica failure behavior only; access control is handled in S017, replication setup in S026, replication lag in S027, DB primary stop runbook in S034, and backup/restore in S038 and S039.
