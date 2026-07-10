# Commands

Scenario: S033-db-replica-failure-validation
Level: L4-failure-recovery
Capability: DB Replica Failure Validation

Record approved commands or manual actions used during validation. Do not include real command output yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Command Records

| Check ID | Purpose | Planned Command Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Capture pre-failure Primary status | `mysql --host=<db-primary-host> --user=<placeholder-user> --execute "<primary-status-query-placeholder>"` | `<db-primary-host>` | TODO: `logs/db-replica-failure-validation.log` |
| V002 | Capture pre-failure Replica status | `mysql --host=<db-replica-host> --user=<placeholder-user> --execute "<replica-status-query-placeholder>"` | `<db-replica-host>` | TODO: `screenshots/db-replica-before-failure.png` |
| V003 | Capture pre-failure replication status | `mysql --host=<db-replica-host> --user=<placeholder-user> --execute "SHOW REPLICA STATUS\\G"` or `SHOW SLAVE STATUS\\G` | `<db-replica-host>` | TODO: `configs/db-replica-failure-summary.md` |
| V004 | Inject one Replica outage | `<approved-replica-stop-command-placeholder>` | `<db-replica-host>` | TODO: `logs/db-replica-failure-validation.log` |
| V005 | Detect failed Replica | `<approved-replica-health-check-placeholder>` | `<db-replica-host>` | TODO: `screenshots/db-replica-during-failure.png` |
| V006 | Validate Primary write availability | `mysql --host=<db-primary-host> --user=<placeholder-user> --execute "<primary-write-test-placeholder>"` | `<db-primary-host>` | TODO: `logs/db-replica-failure-validation.log` |
| V007 | Record application DB dependency impact placeholder | Manual review of expected dependency impact | `<test-database>` | TODO: `configs/db-replica-failure-summary.md` |
| V008 | Restore failed Replica | `<approved-replica-start-command-placeholder>` | `<db-replica-host>` | TODO: `logs/db-replica-failure-validation.log` |
| V009 | Validate replication resume | `mysql --host=<db-replica-host> --user=<placeholder-user> --execute "SHOW REPLICA STATUS\\G"` or `SHOW SLAVE STATUS\\G` | `<db-replica-host>` | TODO: `configs/db-replica-failure-summary.md` |
| V010 | Validate post-recovery consistency | `mysql --host=<db-replica-host> --user=<placeholder-user> --execute "<consistency-check-placeholder>"` | `<test-database>.<test-table>` | TODO: `screenshots/db-replica-after-recovery.png` |
| V011 | Measure detection and recovery time | Manual timestamp comparison between outage action, detection, restoration, and replication resume | `<replica-recovery-threshold-seconds>` | TODO: `configs/db-replica-recovery-threshold.md` |

## Output Placeholder

```text
Execution timestamp: TODO
Operator: TODO
Primary host: <db-primary-host>
Replica host: <db-replica-host>
Test database/table: <test-database>.<test-table>
Command or manual review: TODO
Expected purpose: TODO
Sanitized output summary: TODO
```
