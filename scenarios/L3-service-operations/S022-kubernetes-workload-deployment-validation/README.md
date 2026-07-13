# S022-kubernetes-workload-deployment-validation

| Field | Value |
|---|---|
| Scenario ID | S022 |
| Scenario Name | Kubernetes Workload Deployment Validation |
| Level | L3 Service Operations Validation |
| Category | Service Operations |
| Related Components | namespace, Deployment, Service, command reference, sample deployment/pod evidence |
| Validation Type | Static by default; explicit optional live read-only validation |
| Evidence Directory | `evidence/L3-service-operations/S022-kubernetes-workload-deployment-validation/` |
| Status | VALIDATED |

## Objective Summary

Validate safe Kubernetes workload manifests and deployment evidence without storing cluster credentials or requiring live access.

## Scope Summary

Default execution validates repository documents, manifests, and sample evidence only. `-LiveKubectl` explicitly enables two read-only workload listings and stores aggregate status rather than raw rows.

## Validation Summary

Sixteen checks validate files, commands, manifest structure, labels/selectors, probes/resources/image, unsafe patterns, deployment and Pod readiness, restarts, credential safety, sensitive content, and mode boundaries.

## Evidence Output Summary

Tracked deployment and Pod samples and a sanitized summary accompany an ignored execution log in the S022 evidence directory.
