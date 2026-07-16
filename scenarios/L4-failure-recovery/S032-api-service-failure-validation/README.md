# S032-api-service-failure-validation

| Field | Value |
|---|---|
| Scenario ID | S032 |
| Scenario Name | API Service Failure Validation |
| Level | L4 Failure Recovery Validation |
| Category | Failure Recovery |
| Related Components | API Deployment, Pod, Service, endpoints, rollout, HTTP health |
| Validation Type | Static with optional explicit read-only LiveKubectl and LiveHttp |
| Evidence Directory | evidence/L4-failure-recovery/S032-api-service-failure-validation/ |
| Status | NOT_STARTED |

## Objective Summary

Validate the API failure runbook, criteria, and sanitized pre-failure/failure/recovery evidence without modifying Kubernetes or storing production API data.

## Scope Summary

Static mode performs no network or cluster access. LiveKubectl requires Namespace, DeploymentName, and ServiceName and runs five read-only queries. LiveHttp requires ApiHealthUrl and sends an unauthenticated HEAD request only.

## Validation Summary

Nineteen checks cover files, placeholders, manual fault boundaries, criteria, Pod/endpoint/HTTP evidence, failure detection, rollout, timing, secret safety, and optional live read-only state.

## Evidence Output Summary

The generated log and summary contain sanitized judgments. Committed samples are non-production, and live raw output or HTTP response bodies are not retained.
