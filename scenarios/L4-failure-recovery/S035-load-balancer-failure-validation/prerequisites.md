# Prerequisites

- Repository scope lock and excluded-scope rules have been reviewed.
- Matching evidence directory exists at `evidence/L4-failure-recovery/S035-load-balancer-failure-validation/`.
- S023 Ingress routing validation is planned before Ingress route behavior is referenced.
- S024 Nginx Reverse Proxy validation is planned before reverse proxy forwarding behavior is referenced.
- S025 load balancing health check validation is planned before health check failure behavior is interpreted.
- S030 Blackbox endpoint probe validation is planned before probe failure is referenced.
- S031 Web Pod failure recovery and S032 API service failure validation remain separate and must not be reimplemented here.
- Placeholder values are available for `<load-balancer-endpoint>`, `<reverse-proxy-host>`, `<ingress-host>`, `<backend-service>`, `<web-endpoint>`, `<api-endpoint>`, `<health-endpoint>`, and `<recovery-threshold-seconds>`.
- No real public IPs, DNS records, TLS private keys, certificates, credentials, secrets, tfstate, kubeconfig, cloud account values, or account-specific values are required for this documentation skeleton.
