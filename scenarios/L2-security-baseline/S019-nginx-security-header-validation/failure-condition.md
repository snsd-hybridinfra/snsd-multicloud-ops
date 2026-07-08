# Failure Condition

S019 fails if the Nginx security header model allows unsafe or unexplained web response behavior.

## Failure Conditions

- Nginx configuration syntax validation fails or cannot be performed.
- `server_tokens off` or equivalent version exposure reduction is missing.
- `X-Content-Type-Options` is missing.
- `X-Frame-Options` is missing.
- `Referrer-Policy` is missing.
- `Content-Security-Policy` placeholder is missing or undocumented.
- `Strict-Transport-Security` is claimed without a later approved TLS implementation.
- `curl -I` response header evidence cannot be captured or reviewed.
- Access or error logs cannot be captured when required for evidence.
- Response behavior is unexplained, inconsistent, or not mapped to validation evidence.
- Evidence contains TLS private keys, certificates, credentials, real public IPs, tfstate, kubeconfig content, or account-specific values.

## Blocked Conditions

- Validation cannot proceed because no approved placeholder endpoint exists.
- Future Nginx syntax, response header, or log output is unavailable.
- Required evidence files are missing.
