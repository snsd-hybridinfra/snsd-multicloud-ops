# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | DB Primary node role validation plan | Review planned role for `db-primary-01`. | Primary node role is documented and identifiable. | `commands.md`, `configs/mariadb-replication-topology.md`, `validation.md` |
| V002 | DB Replica node role validation plan | Review planned roles for `db-replica-01` and `db-replica-02`. | Replica node roles are documented and identifiable. | `commands.md`, `configs/mariadb-replication-topology.md`, `validation.md` |
| V003 | MariaDB replication configuration validation plan | Review planned replication configuration summary. | Replication configuration is documented for primary and replicas. | `commands.md`, `configs/mariadb-replication-config-summary.md`, `validation.md` |
| V004 | Binary log configuration validation plan | Review primary binary log configuration plan. | Binary log configuration is present in the planned model. | `commands.md`, `configs/mariadb-replication-config-summary.md`, `validation.md` |
| V005 | Replication user existence placeholder validation plan | Review `<replication-user>` placeholder model. | Replication user placeholder is defined without real password values. | `commands.md`, `configs/mariadb-replication-config-summary.md`, `validation.md` |
| V006 | Primary write test validation plan | Plan placeholder write to `<test-database>.<test-table>` on primary. | Primary write test can be performed in future approved execution. | `commands.md`, `logs/mariadb-replication-validation.log`, `validation.md` |
| V007 | Replica read consistency validation plan | Plan read consistency check on replicas. | Replica reads match expected primary test data. | `commands.md`, `logs/mariadb-replication-validation.log`, `validation.md` |
| V008 | SHOW REPLICA STATUS or SHOW SLAVE STATUS validation plan | Plan sanitized replication status capture. | Replication status can be reviewed on each replica. | `commands.md`, `logs/mariadb-replication-validation.log`, `screenshots/mariadb-replication-status.png`, `validation.md` |
| V009 | Replication error field validation plan | Review replication status error fields. | Replication error fields are empty or explicitly documented. | `commands.md`, `logs/mariadb-replication-validation.log`, `validation.md` |
| V010 | Replication topology capture plan | Capture planned primary-replica topology summary. | Topology identifies primary and replicas without secrets or real IPs. | `commands.md`, `configs/mariadb-replication-topology.md`, `validation.md` |
| V011 | Failure condition for missing replica, replication stopped, replication error, inconsistent data, missing binary log configuration, or missing replication user | Evaluate findings against explicit failure conditions. | Replication failures produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates MariaDB Primary-Replica replication only; access control is handled in S017, lag in S027, failures in S033 and S034, and backup/restore in S038 and S039.
