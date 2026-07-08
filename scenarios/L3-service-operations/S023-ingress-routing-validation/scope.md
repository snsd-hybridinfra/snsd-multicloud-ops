# Scope

## Included

- Ingress Controller readiness validation plan.
- Web service ingress route validation plan.
- API service ingress route validation plan.
- Host-based routing placeholder.
- Path-based routing placeholder.
- Service backend mapping validation plan.
- HTTP response validation plan.
- Ingress event evidence collection plan.
- Ingress controller log evidence collection plan.
- Ingress-to-service connectivity validation plan.

## Excluded

- Real Kubernetes manifest implementation.
- Real kubeconfig files, Kubernetes Secrets, TLS private keys, credentials, private keys, tfstate, cloud account values, subscription IDs, tenant IDs, or account-specific files.
- Real public IPs or real DNS records.
- TLS implementation.
- Workload deployment validation, which is handled in S022.
- Nginx security header validation, which is handled in S019.
- Load balancing health check validation, which is handled in S025.
- Kubernetes manifest policy validation, which is handled in S044.

## Placeholder Rules

Use placeholders such as `<ingress-host>`, `<web-service>`, `<api-service>`, `<namespace>`, `<ingress-controller>`, and `<service-endpoint>`.
