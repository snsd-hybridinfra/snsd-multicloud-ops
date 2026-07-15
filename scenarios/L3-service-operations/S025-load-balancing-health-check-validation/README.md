# S025-load-balancing-health-check-validation

| Field | Value |
|---|---|
| Scenario ID | S025 |
| Scenario Name | Load Balancing Health Check Validation |
| Level | L3 Service Operations Validation |
| Category | Service Operations |
| Primary Domain | Backend health and passive upstream routing |
| Related Components | Load-balancing layer, backend pool, health endpoint, sanitized HTTP evidence |
| Validation Type | Static local validation with optional explicit LiveHttp; sanitized operator-provided real virtual-lab readiness evidence review |
| Evidence Directory | evidence/L3-service-operations/S025-load-balancing-health-check-validation/ |
| Status | VALIDATED |

## Objective Summary

Validate the repository's backend pool, health endpoint, timeout/retry, unhealthy-threshold, passive routing, and sanitized health-evidence model. The dated record additionally validates Kubernetes readiness-based Service endpoint eligibility in a local virtual lab.

## Scope Summary

Static mode invokes neither Nginx nor curl and makes no network request. Optional LiveHttp requires explicit load-balancer and backend health URLs, sends cookie-free HEAD requests, and stores indexed statuses only.

## Validation Summary

Seventeen static checks cover required artifacts, pool members, health route and status, passive retry/timeouts, rule coverage, sample parsing, sensitive-content safety, active-health boundaries, and guarded execution. A separate three-state real-lab review confirms normal two-backend traffic, exclusion of one running-but-NotReady Pod, continuity through the healthy endpoint, and endpoint/distribution restoration.

## Evidence Output Summary

S025 does not modify Nginx or a public load balancer, claim production failover or Nginx Plus active checks, or store raw targets, bodies, headers, credentials, cookies, tokens, TLS material, domains, or numeric addresses. The controlled lab test changed only a readiness sentinel file inside one running Pod; it did not delete a Pod or test S031 self-healing.
