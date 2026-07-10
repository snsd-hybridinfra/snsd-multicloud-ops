# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| DB Primary node role validation plan | `commands.md`; `configs/mariadb-replication-topology.md`; `validation.md` | command plan, topology summary, validation record | yes |
| DB Replica node role validation plan | `commands.md`; `configs/mariadb-replication-topology.md`; `validation.md` | command plan, topology summary, validation record | yes |
| MariaDB replication configuration validation plan | `commands.md`; `configs/mariadb-replication-config-summary.md`; `validation.md` | command plan, config summary, validation record | yes |
| Binary log configuration validation plan | `commands.md`; `configs/mariadb-replication-config-summary.md`; `validation.md` | command plan, config summary, validation record | yes |
| Replication user existence placeholder validation plan | `commands.md`; `configs/mariadb-replication-config-summary.md`; `validation.md` | command plan, config summary, validation record | yes |
| Primary write test validation plan | `commands.md`; `logs/mariadb-replication-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Replica read consistency validation plan | `commands.md`; `logs/mariadb-replication-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| SHOW REPLICA STATUS or SHOW SLAVE STATUS validation plan | `commands.md`; `logs/mariadb-replication-validation.log`; `screenshots/mariadb-replication-status.png`; `validation.md` | command plan, validation log, screenshot reference, validation record | yes |
| Replication error field validation plan | `commands.md`; `logs/mariadb-replication-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Replication topology capture plan | `commands.md`; `configs/mariadb-replication-topology.md`; `validation.md` | command plan, topology summary, validation record | yes |
| Failure condition for missing replica, replication stopped, replication error, inconsistent data, missing binary log configuration, or missing replication user | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real MariaDB replication output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
