# Scope

## Included

- MariaDB backup creation validation plan.
- Kubernetes manifest backup placeholder.
- Nginx configuration backup placeholder.
- Prometheus/Grafana configuration backup placeholder.
- Backup destination structure validation plan.
- Backup file naming rule validation plan.
- Backup file existence validation plan.
- Backup file size sanity validation plan.
- Backup checksum validation plan.
- Backup metadata validation plan.
- Backup log evidence collection plan.
- Backup retention placeholder validation plan.

## Target Backup Categories

- MariaDB logical backup placeholder.
- Kubernetes manifest backup placeholder.
- Nginx reverse proxy config backup placeholder.
- Observability config backup placeholder.
- Security baseline config summary placeholder.
- Scenario evidence backup placeholder.

## Backup Validation Model

- Backup command or runbook invocation placeholder.
- Backup output file existence.
- Backup size sanity check.
- Backup checksum creation.
- Backup metadata recording.
- Backup log capture.
- Backup retention placeholder.
- Backup evidence mapping.

## Important Boundary

- Do not claim production-grade PITR.
- Do not claim enterprise backup software integration.
- Do not claim offsite immutable backup unless documented later.
- Do not include real sensitive backup content.
- This scenario validates backup creation through file existence, metadata, checksum, and evidence capture only.

## Excluded

- Real backup scripts or automation implementation.
- Real database dumps, real credentials, passwords, secrets, private keys, tfstate, kubeconfig, cloud account values, subscription IDs, tenant IDs, public IPs, or account-specific values.
- Restore execution validation, which is handled in S039.
- Service health after recovery validation, which is handled in S040.
- DB replication validation, which is handled in S026.
- DB failure scenarios, which are handled in S033 and S034.
- Commercial-grade point-in-time recovery, enterprise backup software integration, and offsite immutable backup claims.
- Changes outside this scenario directory, its matching evidence directory, and the required tracking documents.
