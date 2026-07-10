# Execution Plan

1. Confirm the scenario evidence directory exists for S025.
2. Identify placeholder load balancer endpoint as `<load-balancer-endpoint>`.
3. Identify placeholder backend Service as `<backend-service>`.
4. Identify placeholder Web and API pods as `<web-pod>` and `<api-pod>`.
5. Identify placeholder health endpoint as `<health-endpoint>`.
6. Record planned Kubernetes Service endpoint health checks.
7. Record planned Ingress backend and Nginx upstream health checks.
8. Record planned AWS, Azure, and OpenStack service entrypoint health placeholders.
9. Record planned HTTP `/health` response validation.
10. Record planned failed backend detection and limited traffic continuity checks.
11. Record planned health check log capture actions.
12. Record TODO placeholders in evidence files until approved execution produces sanitized output.

## Execution Boundaries

This plan does not create or modify load balancers, Kubernetes manifests, Nginx configuration, Blackbox Exporter probes, TLS assets, DNS records, or cloud resources. It only defines the review flow and evidence requirements for later approved validation.
