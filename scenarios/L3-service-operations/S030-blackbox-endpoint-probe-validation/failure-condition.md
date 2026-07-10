# Failure Condition

This scenario is considered failed or blocked if:

- Blackbox Exporter service status cannot be reviewed.
- Required probe module placeholder mapping is missing.
- Web, API, Ingress, Nginx Reverse Proxy, AWS, Azure, OpenStack, or health check endpoint categories are not mapped.
- A planned probe returns failed status.
- A probe returns HTTP 5xx or an unexpected status code.
- A route timeout or DNS resolution failure is observed.
- Probe duration exceeds the approved latency threshold.
- Prometheus `probe_success` or `probe_http_status_code` query evidence cannot be collected when execution is approved.
- Probe evidence is missing, unexplained, or not mapped to validation criteria.
- Real public IPs, DNS records, credentials, secrets, private keys, TLS keys, certificates, tfstate, kubeconfig, or account-specific values are introduced.
