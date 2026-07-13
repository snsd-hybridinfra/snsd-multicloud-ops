# Objective

## Objective Statement

Validate that a non-production Kubernetes Deployment and Service define consistent, observable, resource-bounded workload behavior and that captured evidence indicates availability.

## Success Measures

- Namespace, Deployment, Service, README, command reference, and samples exist.
- Labels and selectors align; readiness/liveness probes and requests/limits exist.
- The image uses a fixed non-latest tag.
- Unsafe host, privileged, Secret, image-pull-secret, cluster-binding, and NodePort patterns are absent.
- Deployment replicas are fully ready/available; Pods are Running and ready.
- Static mode never invokes kubectl; optional live mode remains read-only.
