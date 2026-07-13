# S035-load-balancer-failure-validation

| Field | Value |
|---|---|
| Scenario ID | S035 |
| Scenario Name | Load Balancer Failure Validation |
| Level | L4 Failure Recovery Validation |
| Category | Failure Recovery |
| Related Components | Load balancer, reverse proxy, two backends, client path, bypass/rollback |
| Validation Type | Static with optional explicit read-only LiveHttp |
| Evidence Directory | evidence/L4-failure-recovery/S035-load-balancer-failure-validation/ |
| Status | VALIDATED |

## Objective Summary

Validate LB failure isolation, healthy direct backends, manual recovery, and sanitized client-path evidence without changing services or traffic.

## Scope Summary

Static mode parses local samples. LiveHttp requires three explicit URLs and uses unauthenticated HEAD requests only; no response body is retained.

## Validation Summary

Seventeen checks cover artifacts, workflow, criteria, manual boundaries, metrics/response mapping, pre/failure/isolation/recovery/bypass evidence, timing, sensitive content, and execution safety.

## Evidence Output Summary

Committed samples are non-production and generated output stores judgments only.
