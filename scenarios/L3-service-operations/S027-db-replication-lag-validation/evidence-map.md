# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Replica status command validation plan | `commands.md`; `logs/db-replication-lag-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Seconds_Behind_Source / Seconds_Behind_Master field validation plan | `commands.md`; `logs/db-replication-lag-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Primary timestamp write validation plan | `commands.md`; `logs/db-replication-lag-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Replica timestamp read validation plan | `commands.md`; `logs/db-replication-lag-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Replica lag threshold comparison plan | `commands.md`; `configs/db-replication-lag-threshold.md`; `validation.md` | command plan, threshold summary, validation record | yes |
| db-replica-01 lag validation plan | `commands.md`; `logs/db-replication-lag-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| db-replica-02 lag validation plan | `commands.md`; `logs/db-replication-lag-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Replication lag metric mapping placeholder | `commands.md`; `configs/db-replication-lag-metric-mapping.md`; `validation.md` | command plan, metric mapping, validation record | yes |
| Lag evidence capture plan | `commands.md`; `logs/db-replication-lag-validation.log`; `screenshots/db-replication-lag-status.png`; `validation.md` | command plan, validation log, screenshot reference, validation record | yes |
| Failure condition for NULL lag value, replication stopped, lag above threshold, missing replica, inconsistent timestamp, or missing evidence | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real MariaDB replication lag output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
