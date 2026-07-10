# Prerequisites

- Repository scope lock and excluded-scope rules have been reviewed.
- Matching evidence directory exists at `evidence/L4-failure-recovery/S032-api-service-failure-validation/`.
- S021 Kubernetes node readiness validation is planned before recovery execution.
- S022 Kubernetes workload deployment validation is planned before API failure injection.
- S023 Ingress routing validation is planned before API path failure behavior is referenced.
- S024 Nginx Reverse Proxy validation is planned before proxy forwarding behavior is referenced.
- S025 load balancing health check validation is planned before health behavior is compared.
- S030 Blackbox endpoint probe validation is planned before API probe failure is referenced.
- S031 Web Pod failure recovery validation is separate and must not be reimplemented here.
- Placeholder values are available for `<namespace>`, `<api-deployment>`, `<api-pod>`, `<api-service>`, `<api-health-endpoint>`, `<ingress-host>`, `<api-path>`, and `<recovery-threshold-seconds>`.
- No real kubeconfig, Kubernetes secrets, credentials, private keys, tfstate, cloud account values, or account-specific values are required for this documentation skeleton.
