# Architecture

## Relevant Components

- Control Plane: planned origin for ingress validation commands.
- Kubernetes/k3s runtime: target service runtime for ingress routing validation.
- Ingress Controller: represented by `<ingress-controller>`.
- Ingress resource: placeholder route definition in `<namespace>`.
- Web Service: represented by `<web-service>`.
- API Service: represented by `<api-service>`.
- Ingress host: represented by `<ingress-host>`.
- Service endpoint: represented by `<service-endpoint>`.

## Routing Model

- The Ingress Controller must be ready before route checks can run.
- Web routes must map to `<web-service>`.
- API routes must map to `<api-service>`.
- Host-based routing must use placeholder hostnames only.
- Path-based routing must use placeholder paths only.
- HTTP 200 response checks must validate expected reachable routes.
- Invalid path checks must validate expected denial or not-found behavior.
- Ingress events and controller logs must support route troubleshooting evidence.

## Boundary Notes

This scenario validates ingress routing only. TLS, security headers, workload deployment, load balancing health checks, and manifest policy are separate scenario responsibilities.
