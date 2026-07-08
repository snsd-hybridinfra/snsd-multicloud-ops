# Scope

## Included

- Reverse Proxy security header baseline.
- Ingress response header validation plan.
- Server version exposure reduction.
- HTTP method restriction placeholder.
- Security header validation using `curl -I`.
- Nginx configuration syntax validation plan.
- Access log evidence collection plan.
- Error log evidence collection plan.
- Required headers: `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, and `Content-Security-Policy` placeholder.
- `Strict-Transport-Security` placeholder if TLS is enabled later.

## Excluded

- Real Nginx configuration implementation.
- Real TLS implementation.
- TLS private keys, certificates, credentials, tfstate, kubeconfig, or account-specific files.
- Real public IP addresses or production endpoints.
- Ingress routing validation, which is handled in S023.
- Load balancing validation, which is handled in S025.

## Placeholder Rules

Use placeholders such as `<service-endpoint>`, `<reverse-proxy-host>`, and `<ingress-host>`.
