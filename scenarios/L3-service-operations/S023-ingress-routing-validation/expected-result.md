# Expected Result

## Static Pass Criteria

- Sixteen checks PASS and ADDRESS awareness produces one expected WARN.
- Ingress route, backend Service, and endpoint evidence align on host, path, name, and port.
- No unsafe TLS, Secret, credential, real endpoint/domain/address, or mutation content exists.
- kubectl and curl are not invoked.

## Optional Live Criteria

Ingress, described backend, Service, and non-empty Endpoints must all exist through four successful read-only queries.

## Evidence Criteria

Evidence records mode, file/manifest/backend/endpoint/secret results and final judgment without raw live rows or sensitive data.
