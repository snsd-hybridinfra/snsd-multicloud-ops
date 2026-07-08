# Failure Condition

S023 fails if Kubernetes Ingress routing cannot be validated or routes do not map to the intended services.

## Failure Conditions

- Ingress Controller is missing, unavailable, or not Ready.
- Ingress resource is missing.
- Web route maps to the wrong backend Service.
- API route maps to the wrong backend Service.
- Host-based routing cannot be validated with placeholder hostnames.
- Path-based routing reaches the wrong backend or no backend.
- Valid route times out.
- Valid route returns HTTP 5xx.
- Invalid path response is unexplained or inconsistent.
- `<ingress-host>` is unresolved where placeholder resolution is expected.
- Ingress events or controller logs cannot be captured when required.
- Evidence contains kubeconfig files, Kubernetes Secrets, TLS private keys, credentials, real public IPs, real DNS records, tfstate, or account-specific values.

## Blocked Conditions

- Validation cannot proceed because no approved placeholder ingress model exists.
- Future ingress route output, event output, or controller log output is unavailable.
- Required evidence files are missing.
