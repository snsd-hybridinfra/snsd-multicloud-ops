# Architecture

This scenario models a manual response to a MariaDB Primary stop event. It does not model automatic failover, automatic promotion, or HA DB behavior.

## Relevant Components

- DB Primary node: `db-primary-01` represented by `<db-primary-host>`.
- DB Replica nodes: `db-replica-01` and `db-replica-02` represented by `<db-replica-host>`.
- Replication user placeholder: `<replication-user>`.
- Test database and table placeholders: `<test-database>`, `<test-table>`.
- Primary recovery threshold placeholder: `<primary-recovery-threshold-seconds>`.
- Manual runbook decision points.
- Application DB dependency impact placeholder.
- Evidence store: `evidence/L4-failure-recovery/S034-db-primary-stop-runbook-validation/`.

## Manual Runbook Flow

1. Capture pre-failure Primary, Replica, and replication status.
2. Simulate Primary stop using placeholder commands.
3. Validate Primary write path failure.
4. Validate Replica state during Primary outage.
5. Document application dependency impact.
6. Record manual decision points and incident notes.
7. Restore Primary using an approved placeholder recovery action.
8. Validate restored Primary service.
9. Validate post-recovery replication state.
10. Record detection and recovery timing against provisional thresholds.

Replica promotion is not implemented or claimed in this scenario. Any manual promotion procedure is a future out-of-scope decision.
