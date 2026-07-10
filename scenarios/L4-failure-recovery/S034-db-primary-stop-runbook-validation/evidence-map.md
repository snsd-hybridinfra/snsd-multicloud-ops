# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Pre-failure Primary status validation plan | `commands.md`; `logs/db-primary-stop-runbook-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Pre-failure Replica status validation plan | `commands.md`; `screenshots/db-primary-before-stop.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Pre-failure replication status validation plan | `commands.md`; `configs/db-primary-stop-runbook-summary.md`; `validation.md` | command plan, runbook summary, validation record | yes |
| Primary stop failure injection plan | `commands.md`; `logs/db-primary-stop-runbook-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Primary write failure detection validation plan | `commands.md`; `screenshots/db-primary-during-stop.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Application DB dependency impact placeholder validation plan | `commands.md`; `configs/db-primary-stop-runbook-summary.md`; `validation.md` | command plan, runbook summary, validation record | yes |
| Replica state during Primary outage validation plan | `commands.md`; `configs/db-primary-stop-runbook-summary.md`; `validation.md` | command plan, runbook summary, validation record | yes |
| Manual runbook decision point validation plan | `commands.md`; `configs/db-primary-stop-decision-points.md`; `validation.md` | command plan, decision point summary, validation record | yes |
| Primary restoration validation plan | `commands.md`; `logs/db-primary-stop-runbook-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Post-recovery replication state validation plan | `commands.md`; `screenshots/db-primary-after-recovery.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Recovery time measurement plan | `commands.md`; `configs/db-primary-recovery-threshold.md`; `validation.md` | command plan, threshold summary, validation record | yes |
| Failure condition for Primary outage not detected, unclear decision point, accidental automatic failover claim, Primary restoration failure, replication not resumed, application dependency unavailable, or missing evidence | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real MariaDB command output or DB Primary stop evidence has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
