# S024-nginx-reverse-proxy-validation

| Field | Value |
|---|---|
| Scenario ID | S024 |
| Scenario Name | Nginx Reverse Proxy Validation |
| Level | L3 Service Operations Validation |
| Category | Service Operations |
| Primary Domain | Reverse proxy routing baseline |
| Related Components | Nginx example, upstream, backend service, HTTP evidence |
| Validation Type | Static local validation with optional explicit LiveHttp |
| Evidence Directory | evidence/L3-service-operations/S024-nginx-reverse-proxy-validation/ |
| Status | VALIDATED |

## Objective Summary

Validate a safe non-production Nginx reverse proxy model, required routing directives, forwarded headers, timeout baseline, and sanitized response evidence.

## Scope Summary

Static mode is authoritative for repository readiness and invokes neither Nginx nor curl. Optional live HTTP validation requires both `-LiveHttp` and `-TargetUrl`, sends one credential-free HEAD request, and stores only a sanitized status and timestamp.

## Validation Summary

Seventeen checks validate required files, upstream/server/location routing, `proxy_pass`, forwarded headers, timeout directives, rule coverage, sample evidence, address/domain/TLS/credential safety, and execution boundaries.

## Evidence Output Summary

Generated evidence is stored under the scenario evidence directory. S024 never reloads, restarts, or modifies Nginx and never stores credentials, cookies, tokens, TLS keys, certificates, target URLs, or response bodies.
