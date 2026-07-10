# Failure Condition

This scenario is considered failed or blocked if:

- Pre-failure Primary, Replica, or replication status cannot be established.
- Primary outage is not detected within the provisional detection threshold.
- Primary write failure cannot be observed or explained during outage.
- Application dependency impact is unclear.
- Manual decision points are unclear or missing.
- Documentation accidentally claims automatic failover or HA DB behavior.
- Primary restoration path is missing or fails.
- Replication does not resume or cannot be reviewed after recovery.
- Application dependency remains unavailable after Primary restoration.
- Evidence is missing, unexplained, or not mapped to validation criteria.
- Real database passwords, credentials, public IPs, private keys, tfstate, kubeconfig, cloud account values, or account-specific values are introduced.
