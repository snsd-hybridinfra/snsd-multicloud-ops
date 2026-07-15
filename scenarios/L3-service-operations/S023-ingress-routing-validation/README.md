# S023-ingress-routing-validation

| Field | Value |
|---|---|
| Scenario ID | S023 |
| Scenario Name | Ingress Routing Validation |
| Level | L3 Service Operations Validation |
| Category | Service Operations |
| Related Components | Ingress manifest, Service backend, endpoint evidence, optional read-only kubectl mode |
| Validation Type | Static by default; explicit optional live read-only validation; sanitized operator-provided real-lab evidence review |
| Evidence Directory | `evidence/L3-service-operations/S023-ingress-routing-validation/` |
| Status | VALIDATED |

## Objective Summary

Validate host/path routing from Kubernetes Ingress to a Service backend and endpoint evidence without storing cluster or TLS credentials. The dated record additionally verifies sanitized local-lab HTTP routing evidence.

## Scope Summary

Default execution validates repository files and samples only. `-LiveKubectl` explicitly enables four read-only resource queries; curl remains manual and is never executed by the validator.

## Validation Summary

Seventeen static checks validate files, commands, routing placeholders, Ingress scope, host/path, backend/port alignment, TLS safety, list/describe/endpoint evidence, address awareness, credentials, content, execution, and mode. A separate real-lab review confirms ready workload backends, a ClusterIP Service, an Ingress host/path mapping, a running Traefik controller, and a Host-header `200 OK` response.

## Evidence Output Summary

Three tracked samples and a sanitized summary accompany the static execution log. Static ADDRESS placeholder status remains WARN. The dated real-lab log and summary mask every environment identifier and retain no raw output or sensitive cluster material.
