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

## Sanitized Real-Lab Criteria

- `READY`: the Ingress exists and a request using the expected Host header returns a successful HTTP response.
- `PARTIAL`: the Ingress exists but its HTTP route is not reachable yet.
- `BLOCKED`: Ingress creation fails or no HTTP workload exists.
- Controller, Service/backend, route, response, and event output are retained only after sanitization.
- Local-lab success does not establish public internet exposure.
- Raw output, kubeconfig, service-account tokens, certificates, keys, passwords, and secrets are not committed.

## 2026-07-15 Real-Lab Result

**READY** - sanitized evidence confirms ready workload backends, a ClusterIP
Service, an Ingress host/path/backend rule, running Traefik components, and a
Host-header request returning `HTTP/1.1 200 OK` with an HTML body.
