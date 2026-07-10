# Commands

Scenario: S034-db-primary-stop-runbook-validation
Level: L4-failure-recovery
Capability: DB Primary Stop Runbook Validation

Record approved commands or manual actions used during validation. Do not include real command output yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Command Records

| Check ID | Purpose | Planned Command Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Capture pre-failure Primary status | `mysql --host=<db-primary-host> --user=<placeholder-user> --execute "<primary-status-query-placeholder>"` | `<db-primary-host>` | TODO: `logs/db-primary-stop-runbook-validation.log` |
| V002 | Capture pre-failure Replica status | `mysql --host=<db-replica-host> --user=<placeholder-user> --execute "<replica-status-query-placeholder>"` | `<db-replica-host>` | TODO: `screenshots/db-primary-before-stop.png` |
| V003 | Capture pre-failure replication status | `mysql --host=<db-replica-host> --user=<placeholder-user> --execute "SHOW REPLICA STATUS\\G"` or `SHOW SLAVE STATUS\\G` | `<db-replica-host>` | TODO: `configs/db-primary-stop-runbook-summary.md` |
| V004 | Inject Primary stop event | `<approved-primary-stop-command-placeholder>` | `<db-primary-host>` | TODO: `logs/db-primary-stop-runbook-validation.log` |
| V005 | Detect Primary write failure | `mysql --host=<db-primary-host> --user=<placeholder-user> --execute "<primary-write-test-placeholder>"` | `<db-primary-host>` | TODO: `screenshots/db-primary-during-stop.png` |
| V006 | Record application DB dependency impact placeholder | Manual review of expected dependency impact | `<test-database>` | TODO: `configs/db-primary-stop-runbook-summary.md` |
| V007 | Validate Replica state during Primary outage | `mysql --host=<db-replica-host> --user=<placeholder-user> --execute "<replica-state-query-placeholder>"` | `<db-replica-host>` | TODO: `configs/db-primary-stop-runbook-summary.md` |
| V008 | Record manual runbook decision points | Manual review of decision point checklist | manual runbook | TODO: `configs/db-primary-stop-decision-points.md` |
| V009 | Restore Primary service | `<approved-primary-start-command-placeholder>` | `<db-primary-host>` | TODO: `logs/db-primary-stop-runbook-validation.log` |
| V010 | Validate post-recovery replication state | `mysql --host=<db-replica-host> --user=<placeholder-user> --execute "SHOW REPLICA STATUS\\G"` or `SHOW SLAVE STATUS\\G` | `<db-replica-host>` | TODO: `screenshots/db-primary-after-recovery.png` |
| V011 | Measure detection and restoration time | Manual timestamp comparison between Primary stop, outage detection, restoration, and replication state review | `<primary-recovery-threshold-seconds>` | TODO: `configs/db-primary-recovery-threshold.md` |

## Manual Decision Point Placeholder

```text
Confirm Primary outage: TODO
Confirm Replica replication state before outage: TODO
Confirm application impact: TODO
Restore Primary or defer future manual promotion decision: TODO
Validate restored Primary service: TODO
Validate replication state after recovery: TODO
Record evidence and incident notes: TODO
```

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
