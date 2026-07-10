# Failure Condition

This scenario is considered failed or blocked if:

- Backup destination structure is missing or unclear.
- Required backup file is missing after approved execution.
- Backup file is zero-size or fails size sanity expectations.
- Backup checksum is missing.
- Backup metadata is missing or incomplete.
- Backup command or runbook invocation fails.
- Backup evidence is missing, unexplained, or not mapped to validation criteria.
- Sensitive backup content, database passwords, credentials, secrets, private keys, tfstate, kubeconfig, cloud account values, or account-specific values are introduced.
- Documentation claims production-grade PITR, enterprise backup software integration, or immutable offsite backup without later scope approval.
