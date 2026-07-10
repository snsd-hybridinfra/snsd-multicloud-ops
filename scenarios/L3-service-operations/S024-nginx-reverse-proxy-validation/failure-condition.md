# Failure Condition

S024 fails if the Nginx reverse proxy forwarding path cannot be validated or provider-level entrypoints do not forward to the intended upstream.

## Failure Conditions

- Nginx service is down or service status cannot be reviewed.
- Nginx configuration syntax validation fails.
- AWS reverse proxy endpoint does not respond as expected.
- Azure reverse proxy endpoint does not respond as expected.
- OpenStack reverse proxy endpoint does not respond as expected.
- Upstream mapping points to the wrong `<upstream-service>`.
- Reverse proxy does not forward to `<ingress-endpoint>`.
- Valid reverse proxy route times out.
- Valid reverse proxy route returns HTTP 5xx.
- Access logs or error logs are missing when required for evidence.
- Evidence contains TLS private keys, certificates, credentials, secrets, real public IPs, tfstate, kubeconfig content, cloud account values, subscription IDs, tenant IDs, or account-specific values.

## Blocked Conditions

- Validation cannot proceed because no approved placeholder reverse proxy model exists.
- Future service status, syntax, response, or log output is unavailable.
- Required evidence files are missing.
