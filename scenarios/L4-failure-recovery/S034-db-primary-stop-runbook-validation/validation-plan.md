# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Pre-failure Primary status validation plan | Plan Primary status review for `<db-primary-host>`. | DB Primary is available before stop event. | `commands.md`, `logs/db-primary-stop-runbook-validation.log`, `validation.md` |
| V002 | Pre-failure Replica status validation plan | Plan Replica status review for `<db-replica-host>`. | DB Replicas are available before Primary stop event. | `commands.md`, `screenshots/db-primary-before-stop.png`, `validation.md` |
| V003 | Pre-failure replication status validation plan | Plan `SHOW REPLICA STATUS` or `SHOW SLAVE STATUS` review. | Replication state is known before Primary stop event. | `commands.md`, `configs/db-primary-stop-runbook-summary.md`, `validation.md` |
| V004 | Primary stop failure injection plan | Plan Primary stop using placeholder commands. | Failure injection targets the Primary stop event only. | `commands.md`, `logs/db-primary-stop-runbook-validation.log`, `validation.md` |
| V005 | Primary write failure detection validation plan | Plan write-path check against `<db-primary-host>` during outage. | Primary write path failure is detected. | `commands.md`, `screenshots/db-primary-during-stop.png`, `validation.md` |
| V006 | Application DB dependency impact placeholder validation plan | Record expected application impact placeholder. | Application impact is documented without real app data. | `commands.md`, `configs/db-primary-stop-runbook-summary.md`, `validation.md` |
| V007 | Replica state during Primary outage validation plan | Review Replica state while Primary is stopped. | Replica state during outage is documented. | `commands.md`, `configs/db-primary-stop-runbook-summary.md`, `validation.md` |
| V008 | Manual runbook decision point validation plan | Review manual decision points. | Decision points are explicit and do not claim automatic failover. | `commands.md`, `configs/db-primary-stop-decision-points.md`, `validation.md` |
| V009 | Primary restoration validation plan | Plan Primary restoration using placeholder action. | Primary restoration path is documented. | `commands.md`, `logs/db-primary-stop-runbook-validation.log`, `validation.md` |
| V010 | Post-recovery replication state validation plan | Review replication state after Primary restoration. | Replication state after recovery is documented. | `commands.md`, `screenshots/db-primary-after-recovery.png`, `validation.md` |
| V011 | Recovery time measurement plan | Measure outage detection and Primary restoration duration. | Detection and restoration timing is recorded and compared with thresholds. | `commands.md`, `configs/db-primary-recovery-threshold.md`, `validation.md` |
| V012 | Failure condition for Primary outage not detected, unclear decision point, accidental automatic failover claim, Primary restoration failure, replication not resumed, application dependency unavailable, or missing evidence | Evaluate findings against explicit failure conditions. | Runbook issues produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates manual DB Primary stop runbook behavior only; it does not implement automatic failover, HA DB behavior, Galera, ProxySQL, or split-brain automation.
