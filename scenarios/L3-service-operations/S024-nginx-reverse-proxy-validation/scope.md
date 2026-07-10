# Scope

## Included

- AWS reverse proxy entrypoint validation plan.
- Azure reverse proxy entrypoint validation plan.
- OpenStack reverse proxy entrypoint validation plan.
- Reverse proxy to Kubernetes Ingress forwarding plan.
- Reverse proxy upstream mapping validation plan.
- Reverse proxy HTTP response validation plan.
- Reverse proxy health check placeholder.
- Access log evidence collection plan.
- Error log evidence collection plan.
- Nginx configuration syntax validation plan.

## Excluded

- Real Nginx configuration implementation.
- TLS implementation.
- TLS private keys, certificates, credentials, secrets, private keys, tfstate, kubeconfig, cloud account values, subscription IDs, tenant IDs, or account-specific files.
- Real public IPs or production hostnames.
- Nginx security header validation, which is handled in S019.
- Ingress routing validation, which is handled in S023.
- Load balancing health check validation, which is handled in S025.

## Placeholder Rules

Use placeholders such as `<aws-reverse-proxy>`, `<azure-reverse-proxy>`, `<openstack-reverse-proxy>`, `<ingress-endpoint>`, and `<upstream-service>`.
