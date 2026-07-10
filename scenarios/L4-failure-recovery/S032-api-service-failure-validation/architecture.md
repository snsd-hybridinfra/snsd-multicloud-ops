# Architecture

This scenario models API service failure detection and recovery within the Kubernetes/k3s workload and service routing path.

## Relevant Components

- Namespace placeholder: `<namespace>`.
- API Deployment placeholder: `<api-deployment>`.
- API Pod placeholder: `<api-pod>`.
- API Service placeholder: `<api-service>`.
- API health endpoint placeholder: `<api-health-endpoint>`.
- Ingress host and path placeholders: `<ingress-host>`, `<api-path>`.
- Recovery threshold placeholder: `<recovery-threshold-seconds>`.
- Nginx Reverse Proxy reference from S024.
- Blackbox API probe reference from S030.
- Prometheus target or probe metric reference from S028/S030.
- Evidence store: `evidence/L4-failure-recovery/S032-api-service-failure-validation/`.

## Failure and Recovery Flow

1. Capture pre-failure API Deployment, Pod, Service endpoint, API route, and health state.
2. Simulate API workload failure using a placeholder command.
3. Validate route failure and health endpoint degradation.
4. Reference Ingress, Nginx Reverse Proxy, Blackbox, and Prometheus observations without reimplementing those scenarios.
5. Restore the API workload using an approved placeholder rollback action.
6. Validate API health and route recovery.
7. Record detection and recovery timing against provisional thresholds.

This scenario does not define or change Kubernetes manifests. It validates failure behavior expected after workload deployment and routing are already handled by earlier scenarios.
