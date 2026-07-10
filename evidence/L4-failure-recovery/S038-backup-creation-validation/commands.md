# Commands

Scenario: S038-backup-creation-validation
Level: L4-failure-recovery
Capability: Backup Creation Validation

Record approved commands or manual actions used during validation. Do not include real command output yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Command Records

| Check ID | Purpose | Planned Command Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Validate backup directory structure | `Get-ChildItem <backup-root>` or approved equivalent | `<backup-root>` | TODO: `configs/backup-creation-summary.md` |
| V002 | Plan MariaDB logical backup placeholder | `<approved-db-backup-command-placeholder> --output <db-backup-file>` | `<db-backup-file>` | TODO: `logs/backup-creation-validation.log` |
| V003 | Plan Kubernetes manifest backup placeholder | `<approved-manifest-backup-command-placeholder> --output <manifest-backup-file>` | `<manifest-backup-file>` | TODO: `configs/backup-creation-summary.md` |
| V004 | Plan Nginx configuration backup placeholder | `<approved-config-backup-command-placeholder> --output <config-backup-file>` | `<config-backup-file>` | TODO: `configs/backup-creation-summary.md` |
| V005 | Plan observability configuration backup placeholder | `<approved-observability-backup-command-placeholder> --output <config-backup-file>` | `<config-backup-file>` | TODO: `configs/backup-creation-summary.md` |
| V006 | Validate backup file existence | `Test-Path <backup-file-placeholder>` or approved equivalent | `<db-backup-file>` / `<manifest-backup-file>` / `<config-backup-file>` | TODO: `screenshots/backup-file-list.png` |
| V007 | Validate backup file size sanity | `<approved-file-size-check-placeholder>` | `<backup-file-placeholder>` | TODO: `screenshots/backup-file-list.png` |
| V008 | Validate checksum generation | `<approved-checksum-command-placeholder> <backup-file-placeholder> > <checksum-file>` | `<checksum-file>` | TODO: `screenshots/backup-checksum-validation.png` |
| V009 | Capture backup metadata | Manual metadata review for date, category, filename, size, checksum | `<backup-date>` | TODO: `configs/backup-creation-summary.md` |
| V010 | Capture backup logs | Review backup command or runbook log placeholder | backup runbook | TODO: `logs/backup-creation-validation.log` |
| V011 | Validate retention placeholder | Manual review of retention placeholder | retention policy placeholder | TODO: `configs/backup-retention-placeholder.md` |

## Backup Metadata Placeholder

```text
Backup date: <backup-date>
Backup root: <backup-root>
Backup category: TODO
Backup file: TODO
Backup size: TODO
Checksum file: <checksum-file>
Checksum value: TODO
Sensitive content review: TODO
Retention placeholder: TODO
```

## Output Placeholder

```text
Execution timestamp: TODO
Operator: TODO
Backup root: <backup-root>
Command or manual review: TODO
Expected purpose: TODO
Sanitized output summary: TODO
```
