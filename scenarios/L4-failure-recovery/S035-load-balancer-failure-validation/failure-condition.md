# Failure Condition

This scenario is considered failed or blocked if:

- Pre-failure load balancer endpoint or backend health cannot be established.
- Load balancer failure is not detected within the provisional detection threshold.
- Backend diagnosis is wrong or backend health remains unknown.
- All endpoints are unavailable and impact cannot be isolated.
- Health check failure is not detected or cannot be explained.
- Manual recovery procedure is unclear or missing.
- Documentation claims automatic cross-cloud failover or production-grade global traffic management.
- Endpoint restoration fails or exceeds the CRITICAL threshold.
- Evidence is missing, unexplained, or not mapped to validation criteria.
- Real public IPs, DNS records, TLS private keys, certificates, credentials, secrets, tfstate, kubeconfig, cloud account values, or account-specific values are introduced.
