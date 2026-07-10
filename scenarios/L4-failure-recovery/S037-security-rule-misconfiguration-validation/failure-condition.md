# Failure Condition

This scenario is considered failed or blocked if:

- Pre-change rule baseline cannot be established.
- Misconfiguration is not detected within the provisional detection threshold.
- Public SSH, public DB, or overly broad inbound exposure remains after rollback.
- Required service access is not restored after rollback.
- Unauthorized source behavior cannot be reviewed or explained.
- Manual rollback decision points are unclear or missing.
- Rollback exceeds the CRITICAL threshold.
- Evidence is missing, unexplained, or not mapped to validation criteria.
- Documentation claims real-time blocking, WAF, IDS/IPS, EDR, SOAR, or CSPM capability.
- Real credentials, secrets, public IPs, private keys, tfstate, kubeconfig, cloud account values, subscription IDs, tenant IDs, or account-specific values are introduced.
