# S031-web-pod-failure-recovery-validation

| Field | Value |
|---|---|
| Scenario ID | S031 |
| Scenario Name | Web Pod Failure Recovery Validation |
| Level | L4 Failure Recovery Validation |
| Category | Failure Recovery |
| Primary Domain | Controlled Web Pod recovery evidence |
| Related Components | Deployment, Pods, rollout, Service endpoints |
| Validation Type | Static with optional explicit read-only LiveKubectl |
| Evidence Directory | evidence/L4-failure-recovery/S031-web-pod-failure-recovery-validation/ |
| Status | VALIDATED |

## Objective Summary

Validate a controlled manual Pod-failure runbook, replacement/rollout/endpoint recovery criteria, and sanitized evidence without modifying Kubernetes.

## Scope Summary

Static mode invokes no kubectl. LiveKubectl requires namespace/deployment and runs four read-only commands only. Pod deletion is documented as manual disposable-lab fault injection and never automated.

## Validation Summary

Sixteen checks cover files, workflow, criteria, command boundary, pre/post Pod state, manual event, rollout, endpoints, timing, unhealthy indicators, credentials/endpoints, and execution safety.

## Evidence Output Summary

Recovery time is intentionally unmeasured and produces WARN. S031 stores no kubeconfig, token, certificate, key, cluster endpoint, IP, UID, raw live rows, or secret.
