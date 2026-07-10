# Failure Condition

S025 fails if backend health cannot be validated or the service traffic layer cannot provide reviewable health evidence.

## Failure Conditions

- All backend endpoints are unhealthy.
- `<health-endpoint>` is missing.
- Health endpoint returns HTTP 5xx.
- Health route times out.
- Kubernetes Service endpoint list is stale or does not match expected backends.
- Ingress backend health cannot be reviewed.
- Nginx upstream health cannot be reviewed.
- Provider service entrypoint health placeholder is missing.
- Traffic continuity with one backend unavailable is claimed without evidence.
- Health check logs or evidence cannot be captured.
- Evidence contains TLS private keys, certificates, credentials, secrets, real public IPs, tfstate, kubeconfig content, cloud account values, subscription IDs, tenant IDs, or account-specific values.

## Blocked Conditions

- Validation cannot proceed because no approved placeholder health check model exists.
- Future endpoint, response, or health log output is unavailable.
- Required evidence files are missing.
