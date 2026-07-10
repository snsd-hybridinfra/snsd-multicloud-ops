# Failure Condition

S027 fails if MariaDB replication lag cannot be measured or exceeds the documented validation model.

## Failure Conditions

- Replica status command output is unavailable.
- `Seconds_Behind_Source` or `Seconds_Behind_Master` is missing or `NULL`.
- Replication is stopped.
- `db-replica-01` is missing or cannot report lag.
- `db-replica-02` is missing or cannot report lag.
- Primary timestamp write cannot be compared with replica timestamp reads.
- Replica timestamp is inconsistent with primary timestamp evidence.
- Lag is above the provisional CRITICAL threshold.
- Lag threshold evidence is missing.
- Metric mapping placeholder evidence is missing.
- Evidence contains database passwords, credentials, real public IPs, private keys, tfstate, kubeconfig content, cloud account values, or account-specific values.

## Blocked Conditions

- Validation cannot proceed because no approved placeholder lag measurement model exists.
- Future MariaDB replica status or timestamp evidence is unavailable.
- Required evidence files are missing.
