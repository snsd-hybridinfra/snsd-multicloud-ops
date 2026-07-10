# Failure Condition

This scenario is considered failed or blocked if:

- Pre-failure Prometheus service or target UP state cannot be established.
- Target DOWN state is not detected within the provisional detection threshold.
- Prometheus scrape configuration is invalid or cannot be reviewed.
- Required target label, job, or instance mapping is missing.
- `up{job="<target-job>"}` query evidence does not reflect target state.
- Target remains DOWN after restoration.
- Recovery time exceeds the CRITICAL threshold.
- Evidence is missing, unexplained, or not mapped to validation criteria.
- Documentation claims Alertmanager integration, automated notification, or SOAR-style response.
- Real credentials, secrets, public IPs, private keys, tfstate, kubeconfig, cloud account values, or account-specific values are introduced.
