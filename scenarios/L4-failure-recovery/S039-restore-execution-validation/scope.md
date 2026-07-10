# Scope

## Included

- MariaDB restore execution validation plan.
- Kubernetes manifest restore placeholder.
- Nginx configuration restore placeholder.
- Prometheus/Grafana configuration restore placeholder.
- Backup artifact selection validation plan.
- Backup checksum verification before restore validation plan.
- Restore target confirmation validation plan.
- Restore command or runbook invocation placeholder.
- Restore log evidence collection plan.
- Restore result sanity validation plan.
- Restore rollback or abort condition documentation.

## Target Restore Categories

- MariaDB logical restore placeholder.
- Kubernetes manifest restore placeholder.
- Nginx reverse proxy config restore placeholder.
- Observability config restore placeholder.
- Security baseline config summary restore placeholder.
- Scenario evidence restore placeholder.

## Restore Validation Model

- Backup artifact selection.
- Backup checksum verification.
- Restore target confirmation.
- Restore command or runbook invocation placeholder.
- Restore execution log capture.
- Restore result sanity check.
- Restore abort condition.
- Restore rollback placeholder.
- Restore evidence mapping.

## Important Boundary

- Do not claim production-grade PITR.
- Do not claim enterprise backup software integration.
- Do not claim automated full disaster recovery.
- Do not restore real sensitive data.
- Do not include real backup contents in the repository.
- This scenario validates restore execution through artifact selection, checksum verification, controlled restore procedure, logs, and post-restore evidence.

## Excluded

- Real restore scripts or automation implementation.
- Real production data restore.
- Real database dumps, credentials, passwords, secrets, private keys, tfstate, kubeconfig, cloud account values, subscription IDs, tenant IDs, public IPs, or account-specific values.
- Backup creation validation, which is handled in S038.
- Service health after recovery validation, which is handled in S040.
- DB replication validation, which is handled in S026.
- DB failure scenarios, which are handled in S033 and S034.
- Commercial-grade point-in-time recovery, enterprise backup software integration, and automated full disaster recovery claims.
- Changes outside this scenario directory, its matching evidence directory, and the required tracking documents.
