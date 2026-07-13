# Scope

## Included

- Static validation of an Ingress manifest and its Service name/port/namespace alignment.
- Parsing of non-production ingress list, ingress describe, and endpoint samples.
- Host, path, class, backend, wildcard, TLS/Secret, and placeholder-address checks.
- Optional explicit read-only Ingress, Service, and Endpoints queries.
- Credential-file, endpoint, domain, address, secret-content, and execution safety.

## Excluded

- Automatic curl, live HTTP response, DNS, TLS, or real address validation.
- Apply, delete, patch, edit, replace, scale, rollout, or other resource mutation.
- Workload deployment (S022), Nginx proxy operation (S024), load-balancer health (S025), DNS model (S009), Nginx headers (S019), and manifest policy (S044).
