# Commands

Scenario: S039-restore-execution-validation
Level: L4-failure-recovery
Capability: Restore Execution Validation

Record approved commands or manual actions used during validation. Do not include real command output yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Command Records

| Check ID | Purpose | Planned Command Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Select backup artifact | `Get-ChildItem <backup-root>` or approved equivalent | `<backup-root>` | TODO: `configs/restore-artifact-selection.md`, `screenshots/restore-artifact-selection.png` |
| V002 | Verify backup checksum before restore | `<approved-checksum-verify-command-placeholder> <checksum-file>` | `<checksum-file>` | TODO: `configs/restore-execution-summary.md` |
| V003 | Confirm restore target | Manual review of `<restore-target>` | `<restore-target>` | TODO: `configs/restore-execution-summary.md` |
| V004 | Plan MariaDB logical restore placeholder | `<approved-db-restore-command-placeholder> --input <db-backup-file> --target <restore-target>` | `<db-backup-file>` | TODO: `logs/restore-execution-validation.log` |
| V005 | Plan Kubernetes manifest restore placeholder | `<approved-manifest-restore-command-placeholder> --input <manifest-backup-file> --target <restore-target>` | `<manifest-backup-file>` | TODO: `configs/restore-execution-summary.md` |
| V006 | Plan Nginx configuration restore placeholder | `<approved-config-restore-command-placeholder> --input <config-backup-file> --target <restore-target>` | `<config-backup-file>` | TODO: `configs/restore-execution-summary.md` |
| V007 | Plan observability configuration restore placeholder | `<approved-observability-restore-command-placeholder> --input <config-backup-file> --target <restore-target>` | `<config-backup-file>` | TODO: `configs/restore-execution-summary.md` |
| V008 | Capture restore log | Review `<restore-log>` after placeholder restore runbook | `<restore-log>` | TODO: `logs/restore-execution-validation.log` |
| V009 | Validate restore result sanity | `<approved-restore-sanity-check-placeholder>` | `<restore-target>` | TODO: `screenshots/restore-execution-result.png` |
| V010 | Validate restore abort conditions | Manual review of abort checklist | restore runbook | TODO: `configs/restore-abort-conditions.md` |
| V011 | Validate restore rollback placeholder | Manual review of rollback placeholder | restore runbook | TODO: `configs/restore-abort-conditions.md` |

## Restore Metadata Placeholder

```text
Backup root: <backup-root>
Selected artifact: TODO
Checksum file: <checksum-file>
Restore target: <restore-target>
Restore log: <restore-log>
Checksum verification result: TODO
Restore invocation: TODO
Sanity check result: TODO
Abort condition review: TODO
Rollback placeholder: TODO
```

## Output Placeholder

```text
Execution timestamp: TODO
Operator: TODO
Command or manual review: TODO
Expected purpose: TODO
Sanitized output summary: TODO
```
