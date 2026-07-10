# S032-api-service-failure-validation

| Field | Value |
|---|---|
| Scenario ID | S032 |
| Scenario Name | API Service Failure Validation |
| Level | L4 Failure and Recovery Validation |
| Category | Failure Recovery |
| Primary Domain | Kubernetes/k3s API service failure detection and recovery |
| Related Components | Kubernetes/k3s, API Deployment, API Pod, API Service, Ingress API path, Nginx reverse proxy reference, Blackbox probe reference, Prometheus metric reference |
| Validation Type | Failure Recovery Validation |
| Evidence Directory | evidence/L4-failure-recovery/S032-api-service-failure-validation/ |
| Status | PLANNED |

## Objective Summary

Define and validate API service failure detection and recovery evidence for the SNSD Multi-Cloud Ops Kubernetes/k3s service runtime.

## Scope Summary

This scenario validates API service failure behavior only. It covers pre-failure API workload state, placeholder failure injection, API route failure detection, degraded health response, Ingress API path failure behavior, Blackbox and Prometheus references, workload restoration, API health recovery, and recovery time measurement.

## Validation Summary

Validation checks confirm that API Deployment, Pod, and Service endpoint state are captured before failure; failure injection is planned with placeholders; route and health failure behavior is detected; restoration is planned; recovery is measured; and failures such as missed detection, unexpected success during failure, `CrashLoopBackOff`, missing Service endpoint, persistent HTTP 5xx, or threshold breach are captured.

## Evidence Output Summary

Evidence must be recorded under `evidence/L4-failure-recovery/S032-api-service-failure-validation/`, with command plans in `commands.md`, validation results in `validation.md`, and future sanitized supporting artifacts under `configs/`, `logs/`, and `screenshots/`.
