# Validation

Scenario: S034-db-primary-stop-runbook-validation
Level: L4-failure-recovery
Capability: DB Primary Stop Runbook Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real MariaDB command output or DB Primary stop evidence has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | Pre-failure Primary status validation plan | DB Primary is available before stop event. | TODO | NOT_RUN | `commands.md`; `logs/db-primary-stop-runbook-validation.log` |
| V002 | Pre-failure Replica status validation plan | DB Replicas are available before Primary stop event. | TODO | NOT_RUN | `commands.md`; `screenshots/db-primary-before-stop.png` |
| V003 | Pre-failure replication status validation plan | Replication state is known before Primary stop event. | TODO | NOT_RUN | `commands.md`; `configs/db-primary-stop-runbook-summary.md` |
| V004 | Primary stop failure injection plan | Failure injection targets the Primary stop event only. | TODO | NOT_RUN | `commands.md`; `logs/db-primary-stop-runbook-validation.log` |
| V005 | Primary write failure detection validation plan | Primary write path failure is detected. | TODO | NOT_RUN | `commands.md`; `screenshots/db-primary-during-stop.png` |
| V006 | Application DB dependency impact placeholder validation plan | Application impact is documented without real app data. | TODO | NOT_RUN | `commands.md`; `configs/db-primary-stop-runbook-summary.md` |
| V007 | Replica state during Primary outage validation plan | Replica state during outage is documented. | TODO | NOT_RUN | `commands.md`; `configs/db-primary-stop-runbook-summary.md` |
| V008 | Manual runbook decision point validation plan | Decision points are explicit and do not claim automatic failover. | TODO | NOT_RUN | `commands.md`; `configs/db-primary-stop-decision-points.md` |
| V009 | Primary restoration validation plan | Primary restoration path is documented. | TODO | NOT_RUN | `commands.md`; `logs/db-primary-stop-runbook-validation.log` |
| V010 | Post-recovery replication state validation plan | Replication state after recovery is documented. | TODO | NOT_RUN | `commands.md`; `screenshots/db-primary-after-recovery.png` |
| V011 | Recovery time measurement plan | Detection and restoration timing is recorded and compared with thresholds. | TODO | NOT_RUN | `commands.md`; `configs/db-primary-recovery-threshold.md` |
| V012 | Failure condition for Primary outage not detected, unclear decision point, accidental automatic failover claim, Primary restoration failure, replication not resumed, application dependency unavailable, or missing evidence | Runbook issues produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- DB Primary stop runbook summary is captured: NOT_READY
- DB Primary recovery threshold summary is captured: NOT_READY
- DB Primary stop decision points are captured: NOT_READY
- DB Primary stop runbook validation log is captured: NOT_READY
- Before, during, and after screenshots are captured: NOT_READY

## Provisional Failure and Recovery Thresholds

- DETECTED: Primary outage visible within `< 60 seconds`.
- WARNING: Primary restoration within `60-300 seconds`.
- CRITICAL: Primary recovery failed or application dependency remains unavailable.

## Boundary Notes

This scenario validates manual runbook response only. It does not implement or claim automatic DB failover, HA DB behavior, Galera Cluster, ProxySQL, or split-brain automation. Any manual Replica promotion is a future out-of-scope procedure.
