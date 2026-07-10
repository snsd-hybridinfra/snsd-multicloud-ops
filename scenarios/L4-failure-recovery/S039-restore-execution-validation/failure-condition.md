# Failure Condition

This scenario is considered failed or blocked if:

- Backup artifact is missing or cannot be selected.
- Checksum verification fails or checksum evidence is missing.
- Restore target is wrong, unclear, or unsafe.
- Restore command or runbook invocation fails.
- Restore result is incomplete or fails sanity checks.
- Restore log is missing.
- Restore abort conditions are missing or ignored.
- Restore rollback placeholder is missing.
- Evidence is missing, unexplained, or not mapped to validation criteria.
- Sensitive backup content, database passwords, credentials, secrets, private keys, tfstate, kubeconfig, cloud account values, or account-specific values are introduced.
- Documentation claims production-grade PITR, automated full disaster recovery, or enterprise backup software integration without later scope approval.
