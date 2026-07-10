# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Kubernetes Service endpoint health validation plan | Plan endpoint health review for `<backend-service>`. | Kubernetes Service has healthy backend endpoints. | `commands.md`, `configs/backend-endpoint-health-summary.md`, `validation.md` |
| V002 | Ingress backend endpoint health validation plan | Plan backend health review from ingress perspective. | Ingress backend endpoint health is reviewable. | `commands.md`, `configs/load-balancing-health-check-summary.md`, `validation.md` |
| V003 | Nginx upstream health validation plan | Plan upstream health review from `<reverse-proxy-host>`. | Nginx upstream target health is reviewable. | `commands.md`, `configs/load-balancing-health-check-summary.md`, `validation.md` |
| V004 | AWS service entrypoint health check plan | Document placeholder health check for AWS service entrypoint. | AWS entrypoint health check model is defined. | `commands.md`, `configs/load-balancing-health-check-summary.md`, `validation.md` |
| V005 | Azure service entrypoint health check plan | Document placeholder health check for Azure service entrypoint. | Azure entrypoint health check model is defined. | `commands.md`, `configs/load-balancing-health-check-summary.md`, `validation.md` |
| V006 | OpenStack service entrypoint health check plan | Document placeholder health check for OpenStack service entrypoint. | OpenStack entrypoint health check model is defined. | `commands.md`, `configs/load-balancing-health-check-summary.md`, `validation.md` |
| V007 | HTTP /health endpoint response validation plan | Plan HTTP response check for `<health-endpoint>`. | Health endpoint returns expected HTTP 200 response. | `commands.md`, `logs/load-balancing-health-check-validation.log`, `screenshots/load-balancing-health-check-test.png`, `validation.md` |
| V008 | Backend unavailable detection plan | Plan detection check for one unavailable backend. | Unavailable backend is detected and documented. | `commands.md`, `logs/load-balancing-health-check-validation.log`, `validation.md` |
| V009 | Traffic continuity validation plan with one backend unavailable | Plan limited continuity check when one backend is unavailable. | Traffic continuity behavior is documented without claiming global failover. | `commands.md`, `logs/load-balancing-health-check-validation.log`, `validation.md` |
| V010 | Health check log capture plan | Plan sanitized health check log capture. | Health check logs are available without sensitive values. | `commands.md`, `logs/load-balancing-health-check-validation.log`, `validation.md` |
| V011 | Failure condition for all backends unhealthy, health endpoint missing, HTTP 5xx, route timeout, stale endpoint, or no health evidence | Evaluate findings against explicit failure conditions. | Health check failures produce `FAIL` or `BLOCKED` status. | `validation.md` |

## Review Notes

Every validation item must map to evidence. This scenario validates health checks only; ingress routing is handled in S023, reverse proxy forwarding in S024, blackbox probes in S030, and load balancer failure response in S035.
