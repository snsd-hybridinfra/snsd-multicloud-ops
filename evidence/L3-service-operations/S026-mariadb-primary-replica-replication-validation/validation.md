# Validation

Scenario: S026-mariadb-primary-replica-replication-validation
Level: L3-service-operations
Capability: MariaDB Primary-Replica Replication Validation
Reviewer: TBD
Date: TBD
Overall status: PARTIAL

No real MariaDB replication output has been collected yet. This file defines the validation record that must be completed during future approved execution.

| Check ID | Validation Item | Expected Result | Actual Result | Status | Evidence |
|---|---|---|---|---|---|
| V001 | DB Primary node role validation plan | Primary node role is documented and identifiable. | TODO | NOT_RUN | `commands.md`; `configs/mariadb-replication-topology.md` |
| V002 | DB Replica node role validation plan | Replica node roles are documented and identifiable. | TODO | NOT_RUN | `commands.md`; `configs/mariadb-replication-topology.md` |
| V003 | MariaDB replication configuration validation plan | Replication configuration is documented for primary and replicas. | TODO | NOT_RUN | `commands.md`; `configs/mariadb-replication-config-summary.md` |
| V004 | Binary log configuration validation plan | Binary log configuration is present in the planned model. | TODO | NOT_RUN | `commands.md`; `configs/mariadb-replication-config-summary.md` |
| V005 | Replication user existence placeholder validation plan | Replication user placeholder is defined without real password values. | TODO | NOT_RUN | `commands.md`; `configs/mariadb-replication-config-summary.md` |
| V006 | Primary write test validation plan | Primary write test can be performed in future approved execution. | TODO | NOT_RUN | `commands.md`; `logs/mariadb-replication-validation.log` |
| V007 | Replica read consistency validation plan | Replica reads match expected primary test data. | TODO | NOT_RUN | `commands.md`; `logs/mariadb-replication-validation.log` |
| V008 | SHOW REPLICA STATUS or SHOW SLAVE STATUS validation plan | Replication status can be reviewed on each replica. | TODO | NOT_RUN | `commands.md`; `logs/mariadb-replication-validation.log`; `screenshots/mariadb-replication-status.png` |
| V009 | Replication error field validation plan | Replication error fields are empty or explicitly documented. | TODO | NOT_RUN | `commands.md`; `logs/mariadb-replication-validation.log` |
| V010 | Replication topology capture plan | Topology identifies primary and replicas without secrets or real IPs. | TODO | NOT_RUN | `commands.md`; `configs/mariadb-replication-topology.md` |
| V011 | Failure condition for missing replica, replication stopped, replication error, inconsistent data, missing binary log configuration, or missing replication user | Replication failures produce `FAIL` or `BLOCKED` status. | TODO | NOT_RUN | `validation.md` |

## Evidence Completeness

- Commands are planned: PARTIAL
- Validation outputs are captured: NOT_READY
- MariaDB replication topology is captured: NOT_READY
- MariaDB replication config summary is captured: NOT_READY
- MariaDB replication validation log is captured: NOT_READY
- MariaDB replication status screenshot is captured: NOT_READY

## Notes

This scenario validates MariaDB Primary-Replica replication only. Access control is handled in S017, replication lag in S027, replica failure in S033, primary stop runbook validation in S034, and backup/restore in S038 and S039. Galera Cluster, ProxySQL, DB automatic failover, and split-brain automation are excluded from v1 scope.
