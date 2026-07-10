# Architecture

This scenario models failure detection and recovery for one MariaDB Replica in the On-Prem Internal Server Zone.

## Relevant Components

- DB Primary node: `db-primary-01` represented by `<db-primary-host>`.
- DB Replica nodes: `db-replica-01` and `db-replica-02` represented by `<db-replica-host>`.
- Replication user placeholder: `<replication-user>`.
- Test database and table placeholders: `<test-database>`, `<test-table>`.
- Recovery threshold placeholder: `<replica-recovery-threshold-seconds>`.
- Application DB dependency impact placeholder.
- Evidence store: `evidence/L4-failure-recovery/S033-db-replica-failure-validation/`.

## Failure and Recovery Flow

1. Capture pre-failure Primary status, Replica status, and replication status.
2. Simulate one Replica outage using placeholder commands.
3. Confirm the failed Replica is detected as unavailable.
4. Confirm Primary write availability continues during the Replica outage.
5. Record application DB dependency impact as a placeholder observation.
6. Restore the failed Replica using an approved placeholder recovery action.
7. Validate replication resumes.
8. Validate post-recovery replica consistency.
9. Measure detection and recovery timing against provisional thresholds.

This scenario does not implement replication setup, automatic failover, ProxySQL, Galera, or split-brain automation.
