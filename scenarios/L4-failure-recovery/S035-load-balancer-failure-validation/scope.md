# Scope

## Included

- Pre-failure load balancer endpoint validation plan.
- Pre-failure backend health validation plan.
- Pre-failure Ingress route validation reference plan.
- Load balancer or reverse proxy entrypoint failure injection plan using placeholders.
- Reverse Proxy or upstream failure validation plan.
- Service endpoint impact validation plan.
- Health check failure detection plan.
- Blackbox probe failure reference.
- Backend service health during frontend failure validation plan.
- Manual recovery decision point documentation.
- Load balancer restoration validation plan.
- Post-recovery service health validation plan.
- Failure evidence collection plan.

## Target Traffic Components

- Kubernetes Ingress.
- Nginx Reverse Proxy.
- Load balancing health check endpoint.
- Web service endpoint.
- API service endpoint.
- Blackbox probe target.

## Failure Injection Scope

- Simulate load balancer or reverse proxy entrypoint outage using placeholder commands.
- Validate service endpoint impact.
- Validate health check failure detection.
- Validate Blackbox probe failure reference.
- Validate manual recovery procedure documentation.
- Validate traffic restoration after recovery.
- Capture before, failure, and after evidence using TODO placeholders.

## Important Boundary

- Do not claim automatic cross-cloud failover.
- Do not claim production-grade global traffic management.
- Do not introduce Route 53, Azure Traffic Manager, GSLB, service mesh, Istio, or Argo CD.
- This scenario handles load balancer failure through detection, impact validation, and manual recovery/runbook validation only.

## Runbook Decision Model

- Confirm load balancer or reverse proxy entrypoint outage.
- Confirm backend service health.
- Confirm whether failure is frontend entrypoint, upstream mapping, ingress, or backend.
- Decide whether to restart/reload reverse proxy, switch to known-good config, or route traffic through documented fallback endpoint.
- Validate restored endpoint response.
- Validate health check and Blackbox probe recovery.
- Record evidence and incident notes.

## Failure and Recovery Threshold Model

- DETECTED: Load balancer failure visible within `< 60 seconds`.
- WARNING: service restoration within `60-300 seconds`.
- CRITICAL: endpoint remains unavailable or recovery exceeds `300 seconds`.

These are provisional validation thresholds and must be replaced only when an approved operational threshold is documented.

## Excluded

- Real load balancer or Nginx configuration implementation.
- Automatic cross-cloud failover, production-grade global traffic management, Route 53, Azure Traffic Manager, GSLB, service mesh, Istio, and Argo CD.
- Real public IPs, DNS records, TLS private keys, certificates, credentials, secrets, private keys, tfstate, kubeconfig, cloud account values, subscription IDs, tenant IDs, or account-specific values.
- Load balancing health check baseline validation, which is handled in S025.
- Ingress routing validation, which is handled in S023.
- Nginx Reverse Proxy forwarding validation, which is handled in S024.
- Blackbox endpoint probe validation, which is handled in S030.
- Web Pod failure recovery, which is handled in S031.
- API service failure validation, which is handled in S032.
- Changes outside this scenario directory, its matching evidence directory, and the required tracking documents.
