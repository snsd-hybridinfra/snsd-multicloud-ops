# Architecture

This scenario models a manual response to a load balancer or reverse proxy entrypoint outage. It does not model automatic cross-cloud failover or production-grade global traffic management.

## Relevant Components

- Load balancer endpoint placeholder: `<load-balancer-endpoint>`.
- Reverse proxy host placeholder: `<reverse-proxy-host>`.
- Ingress host placeholder: `<ingress-host>`.
- Backend service placeholder: `<backend-service>`.
- Web endpoint placeholder: `<web-endpoint>`.
- API endpoint placeholder: `<api-endpoint>`.
- Health endpoint placeholder: `<health-endpoint>`.
- Recovery threshold placeholder: `<recovery-threshold-seconds>`.
- Blackbox probe target reference from S030.
- Evidence store: `evidence/L4-failure-recovery/S035-load-balancer-failure-validation/`.

## Failure and Recovery Flow

1. Capture pre-failure load balancer endpoint response.
2. Capture pre-failure backend health and Ingress route reference.
3. Simulate load balancer or reverse proxy entrypoint outage using placeholder commands.
4. Validate endpoint impact and health check failure.
5. Reference Blackbox probe failure without reimplementing S030.
6. Confirm backend service health during frontend failure.
7. Record manual recovery decision points.
8. Restore or reload the entrypoint using an approved placeholder recovery action.
9. Validate post-recovery HTTP response, health check, and probe recovery.
10. Record detection and recovery timing against provisional thresholds.

This scenario separates frontend entrypoint diagnosis from backend workload failure, Web Pod failure, and API service failure.
