# S022-kubernetes-workload-deployment-validation

| Field | Value |
|---|---|
| Scenario ID | S022 |
| Scenario Name | Kubernetes Workload Deployment Validation |
| Level | L3 Service Operations Validation |
| Category | Service Operations |
| Related Components | namespace, Deployment, Service, command reference, sample deployment/pod evidence |
| Validation Type | Static by default; explicit optional live read-only validation; sanitized operator-provided real-lab evidence review |
| Evidence Directory | `evidence/L3-service-operations/S022-kubernetes-workload-deployment-validation/` |
| Status | VALIDATED |

## Objective Summary

Validate safe Kubernetes workload manifests and deployment evidence without storing cluster credentials. The 2026-07-14 record additionally validates sanitized operator-provided real-lab output.

## Scope Summary

Default execution validates repository documents, manifests, and sample evidence only. `-LiveKubectl` explicitly enables two read-only workload listings and stores aggregate status rather than raw rows.

## Validation Summary

Sixteen static checks validate files, commands, manifest structure, labels/selectors, probes/resources/image, unsafe patterns, deployment and Pod readiness, restarts, credential safety, sensitive content, and mode boundaries. A separate real-lab review confirms an Active namespace, a fully available two-replica Deployment and ReplicaSet, two Running Pods, a ClusterIP Service, and normal lifecycle events.

## Evidence Output Summary

Tracked deployment and Pod samples and static summary accompany the static execution log. The dated sanitized real-lab log and validation summary retain no raw terminal output, address, user, host/node, namespace, workload identifier, kubeconfig, token, certificate, key, password, or secret.
