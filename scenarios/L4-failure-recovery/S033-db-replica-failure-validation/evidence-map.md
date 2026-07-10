# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Pre-failure Primary status validation plan | `commands.md`; `logs/db-replica-failure-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Pre-failure Replica status validation plan | `commands.md`; `screenshots/db-replica-before-failure.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Pre-failure replication status validation plan | `commands.md`; `configs/db-replica-failure-summary.md`; `validation.md` | command plan, failure summary, validation record | yes |
| Replica failure injection plan | `commands.md`; `logs/db-replica-failure-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Failed Replica detection validation plan | `commands.md`; `screenshots/db-replica-during-failure.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Primary write availability during Replica failure validation plan | `commands.md`; `logs/db-replica-failure-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Application DB dependency impact placeholder validation plan | `commands.md`; `configs/db-replica-failure-summary.md`; `validation.md` | command plan, failure summary, validation record | yes |
| Replica restoration validation plan | `commands.md`; `logs/db-replica-failure-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Replication resume validation plan | `commands.md`; `configs/db-replica-failure-summary.md`; `validation.md` | command plan, failure summary, validation record | yes |
| Post-recovery consistency validation plan | `commands.md`; `screenshots/db-replica-after-recovery.png`; `validation.md` | command plan, screenshot reference, validation record | yes |
| Recovery time measurement plan | `commands.md`; `configs/db-replica-recovery-threshold.md`; `validation.md` | command plan, threshold summary, validation record | yes |
| Failure condition for Primary write failure, Replica failure not detected, replication not resumed, inconsistent replica data, excessive recovery time, or missing evidence | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real MariaDB command output or DB Replica failure evidence has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
