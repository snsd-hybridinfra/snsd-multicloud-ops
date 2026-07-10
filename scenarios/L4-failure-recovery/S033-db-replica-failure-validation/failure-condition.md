# Failure Condition

This scenario is considered failed or blocked if:

- Pre-failure Primary, Replica, or replication status cannot be established.
- Replica failure is not detected within the provisional detection threshold.
- Primary write availability fails during Replica outage.
- Replication interruption cannot be observed or explained.
- Replica restoration path is missing.
- Replication does not resume after restoration.
- Replica data is inconsistent with the Primary after recovery.
- Recovery time exceeds the CRITICAL threshold.
- Evidence is missing, unexplained, or not mapped to validation criteria.
- Real database passwords, credentials, public IPs, private keys, tfstate, kubeconfig, cloud account values, or account-specific values are introduced.
