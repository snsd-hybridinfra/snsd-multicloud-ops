# Failure Condition

S026 fails if MariaDB Primary-Replica replication cannot be validated or the replication topology is incomplete.

## Failure Conditions

- `db-primary-01` role is missing or inconsistent.
- `db-replica-01` or `db-replica-02` role is missing or inconsistent.
- Replica source configuration is missing.
- Binary log configuration is missing from the planned primary model.
- `<replication-user>` placeholder is missing.
- Replication status indicates replication stopped.
- Replication status reports an error condition.
- Primary write test cannot be verified on replicas.
- Replica read consistency check shows inconsistent data.
- Replication topology evidence cannot be captured.
- Evidence contains database passwords, credentials, real public IPs, private keys, tfstate, kubeconfig content, cloud account values, or account-specific values.

## Blocked Conditions

- Validation cannot proceed because no approved placeholder replication topology exists.
- Future MariaDB replication status or consistency evidence is unavailable.
- Required evidence files are missing.
