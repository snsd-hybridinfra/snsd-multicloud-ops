# S025-load-balancing-health-check-validation

| Field | Value |
|---|---|
| Scenario ID | S025 |
| Scenario Name | Load Balancing Health Check Validation |
| Level | L3 Service Operations Validation |
| Category | Service Operations |
| Primary Domain | Backend health and passive upstream routing |
| Related Components | Load-balancing layer, backend pool, health endpoint, sanitized HTTP evidence |
| Validation Type | Static local validation with optional explicit LiveHttp |
| Evidence Directory | evidence/L3-service-operations/S025-load-balancing-health-check-validation/ |
| Status | VALIDATED |

## Objective Summary

Validate the repository's backend pool, health endpoint, timeout/retry, unhealthy-threshold, passive routing, and sanitized health-evidence model.

## Scope Summary

Static mode invokes neither Nginx nor curl and makes no network request. Optional LiveHttp requires explicit load-balancer and backend health URLs, sends cookie-free HEAD requests, and stores indexed statuses only.

## Validation Summary

Seventeen checks cover required artifacts, pool members, health route and status, passive retry/timeouts, rule coverage, sample parsing, sensitive-content safety, active-health boundaries, and guarded execution.

## Evidence Output Summary

S025 does not modify Nginx or a load balancer, perform automatic failover, claim Nginx Plus active checks, or store targets, bodies, headers, credentials, cookies, tokens, TLS material, domains, or numeric addresses.
