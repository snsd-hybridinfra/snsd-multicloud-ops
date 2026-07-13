# S021-kubernetes-node-readiness-validation

| Field | Value |
|---|---|
| Scenario ID | S021 |
| Scenario Name | Kubernetes Node Readiness Validation |
| Level | L3 Service Operations Validation |
| Category | Service Operations |
| Related Components | readiness model, command reference, sample node evidence, optional read-only kubectl mode |
| Validation Type | Static by default; explicit optional live read-only validation |
| Evidence Directory | `evidence/L3-service-operations/S021-kubernetes-node-readiness-validation/` |
| Status | VALIDATED |

## Objective Summary

Validate the Kubernetes node readiness model and safely parse readiness evidence without storing cluster credentials or requiring live access.

## Scope Summary

Default execution validates repository documents and sample evidence only. `-LiveKubectl` explicitly enables the single read-only command `kubectl get nodes --no-headers` and stores status counts rather than raw live rows.

## Validation Summary

Twelve checks validate files, command references, readiness rules, placeholder nodes, Ready/NotReady status, scheduling awareness, credential-file and content safety, live-command restrictions, and selected mode.

## Evidence Output Summary

Tracked sample output and a sanitized summary accompany an ignored execution log in the S021 evidence directory.
