# Validation

Scenario: S033-db-replica-failure-validation
Level: L4-failure-recovery
Capability: DB Replica Failure Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real MariaDB command output or DB Replica failure evidence has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Pre-failure Primary status validation plan | DB Primary is available before Replica failure. | TODO | NOT_RUN | `commands.md`; `logs/db-replica-failure-validation.log` |
| V002 | Pre-failure Replica status validation plan | Target DB Replica is available before failure. | TODO | NOT_RUN | `commands.md`; `screenshots/db-replica-before-failure.png` |
| V003 | Pre-failure replication status validation plan | Replication is running before failure. | TODO | NOT_RUN | `commands.md`; `configs/db-replica-failure-summary.md` |
| V004 | Replica failure injection plan | Failure injection targets one Replica only. | TODO | NOT_RUN | `commands.md`; `logs/db-replica-failure-validation.log` |
| V005 | Failed Replica detection validation plan | Failed Replica is detected as unavailable. | TODO | NOT_RUN | `commands.md`; `screenshots/db-replica-during-failure.png` |
| V006 | Primary write availability during Replica failure validation plan | DB Primary remains writable during Replica failure. | TODO | NOT_RUN | `commands.md`; `logs/db-replica-failure-validation.log` |
| V007 | Application DB dependency impact placeholder validation plan | Application DB dependency impact is documented without real app data. | TODO | NOT_RUN | `commands.md`; `configs/db-replica-failure-summary.md` |
| V008 | Replica restoration validation plan | Replica restoration path is documented. | TODO | NOT_RUN | `commands.md`; `logs/db-replica-failure-validation.log` |
| V009 | Replication resume validation plan | Replication resumes after Replica restoration. | TODO | NOT_RUN | `commands.md`; `configs/db-replica-failure-summary.md` |
| V010 | Post-recovery consistency validation plan | Replica data is consistent with the Primary after recovery. | TODO | NOT_RUN | `commands.md`; `screenshots/db-replica-after-recovery.png` |
| V011 | Recovery time measurement plan | Detection and recovery timing is recorded and compared with thresholds. | TODO | NOT_RUN | `commands.md`; `configs/db-replica-recovery-threshold.md` |
| V012 | Failure condition for Primary write failure, Replica failure not detected, replication not resumed, inconsistent replica data, excessive recovery time, or missing evidence | DB Replica failure or recovery issues produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- DB Replica failure summary is captured: NOT_READY
- DB Replica recovery threshold summary is captured: NOT_READY
- DB Replica failure validation log is captured: NOT_READY
- Before, during, and after screenshots are captured: NOT_READY

## Provisional Failure and Recovery Thresholds

- DETECTED: Replica failure visible within `< 60 seconds`.
- WARNING: Replica recovery within `60-300 seconds`.
- CRITICAL: Replica recovery failed or replication does not resume.

## Notes

This scenario validates DB Replica failure behavior only. MariaDB access control is handled in S017, Primary-Replica replication setup in S026, DB replication lag in S027, DB primary stop runbook in S034, and backup/restore in S038 and S039. Galera Cluster, ProxySQL, DB automatic failover, and split-brain automation are excluded from v1 scope.
