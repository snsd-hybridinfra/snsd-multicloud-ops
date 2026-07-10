# Scope

## Included

- Kubernetes Service endpoint health validation plan.
- Ingress backend health validation plan.
- Nginx Reverse Proxy upstream health validation plan.
- AWS service entrypoint health check placeholder.
- Azure service entrypoint health check placeholder.
- OpenStack service entrypoint health check placeholder.
- HTTP 200 health endpoint validation plan.
- Failed backend detection plan.
- Traffic continuity validation plan when one backend is unavailable.
- Blackbox Exporter health probe mapping placeholder.
- Health check log evidence collection plan.

## Excluded

- Real load balancer configuration implementation.
- TLS implementation.
- TLS private keys, certificates, credentials, secrets, private keys, tfstate, kubeconfig, cloud account values, subscription IDs, tenant IDs, or account-specific files.
- Real public IPs or production hostnames.
- Ingress routing validation, which is handled in S023.
- Nginx Reverse Proxy forwarding validation, which is handled in S024.
- Blackbox Endpoint Probe validation, which is handled in S030.
- Load balancer failure response, which is handled in S035.
- Global Load Balancing and automatic cross-cloud failover, which are excluded from v1 scope.

## Placeholder Rules

Use placeholders such as `<load-balancer-endpoint>`, `<backend-service>`, `<web-pod>`, `<api-pod>`, `<health-endpoint>`, and `<reverse-proxy-host>`.
