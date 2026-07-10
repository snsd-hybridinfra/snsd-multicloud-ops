# Commands

Scenario: S026-mariadb-primary-replica-replication-validation
Level: L3-service-operations
Capability: MariaDB Primary-Replica Replication Validation
Target: `<db-primary-host>`
Execution timestamp: TODO

Record sanitized output only. Do not include database passwords, credentials, real public IPs, private keys, tfstate, kubeconfig content, cloud account values, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | DB Primary node role validation plan | Review role assignment for `db-primary-01` as `<db-primary-host>`. | Confirm primary role is documented. | TODO: record sanitized output after approved execution. |
| V002 | DB Replica node role validation plan | Review role assignments for `db-replica-01` and `db-replica-02` as `<db-replica-host>`. | Confirm replica roles are documented. | TODO: record sanitized output after approved execution. |
| V003 | MariaDB replication configuration validation plan | Review planned replication configuration summary. | Confirm replication configuration is reviewable. | TODO: record sanitized output after approved execution. |
| V004 | Binary log configuration validation plan | Review planned primary binary log configuration. | Confirm binary log configuration is present. | TODO: record sanitized output after approved execution. |
| V005 | Replication user existence placeholder validation plan | Review `<replication-user>` and `<replication-password-placeholder>` model. | Confirm replication user placeholder exists without a real password. | TODO: record sanitized output after approved execution. |
| V006 | Primary write test validation plan | Plan placeholder write to `<test-database>.<test-table>` on primary. | Confirm future write consistency test is defined. | TODO: record sanitized output after approved execution. |
| V007 | Replica read consistency validation plan | Plan read check from each replica for placeholder test data. | Confirm future replica consistency check is defined. | TODO: record sanitized output after approved execution. |
| V008 | SHOW REPLICA STATUS or SHOW SLAVE STATUS validation plan | Plan sanitized status capture from each replica. | Confirm replication status can be reviewed. | TODO: record sanitized output after approved execution. |
| V009 | Replication error field validation plan | Review planned replication status error fields. | Confirm replication errors are detected. | TODO: record sanitized output after approved execution. |
| V010 | Replication topology capture plan | Capture planned topology for primary and replicas. | Confirm topology evidence is reviewable. | TODO: record sanitized output after approved execution. |
| V011 | Failure condition for missing replica, replication stopped, replication error, inconsistent data, missing binary log configuration, or missing replication user | Review validation findings against failure criteria. | Confirm replication failures result in `FAIL` or `BLOCKED`. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/mariadb-replication-topology.md`
- `configs/mariadb-replication-config-summary.md`
- `logs/mariadb-replication-validation.log`
- `screenshots/mariadb-replication-status.png`
