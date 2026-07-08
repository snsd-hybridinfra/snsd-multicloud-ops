# Architecture

## Relevant Components

- Control Plane: planned origin for workload validation commands.
- Kubernetes/k3s runtime: target service runtime for workload deployment validation.
- Namespace: represented by `<namespace>`.
- Web Deployment: represented by `<web-deployment>`.
- API Deployment: represented by `<api-deployment>`.
- Services: represented by `<web-service>` and `<api-service>`.
- ConfigMap placeholder: planned non-secret configuration reference.
- Secret template placeholder: planned secret reference without storing real Secret data.
- Container image reference: represented by `<container-image>`.

## Deployment Model

- Web and API workloads must be placed in the intended namespace.
- Deployments must have reviewable rollout status.
- Pods must reach Running and Ready states.
- Replica counts must match desired availability.
- Services must exist for planned internal or external routing.
- ConfigMap references must be present where required.
- Secret templates may be referenced by name only; real Secret values are prohibited.
- Resource requests and limits must be documented.
- Image tags must not use `latest`.

## Boundary Notes

This scenario validates workload deployment only. Node readiness, ingress routing, RBAC, and manifest policy are separate scenario responsibilities.
