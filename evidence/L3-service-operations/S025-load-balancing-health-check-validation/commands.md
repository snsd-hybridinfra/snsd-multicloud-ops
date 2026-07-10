# Commands

Scenario: S025-load-balancing-health-check-validation
Level: L3-service-operations
Capability: Load Balancing Health Check Validation
Target: `<load-balancer-endpoint>`
Execution timestamp: TODO

Record sanitized output only. Do not include TLS private keys, certificates, credentials, secrets, real public IPs, tfstate, kubeconfig content, cloud account values, subscription IDs, tenant IDs, or account-specific values.

| Check ID | Validation Item | Planned Command or Action | Purpose | Output |
|---|---|---|---|---|
| V001 | Kubernetes Service endpoint health validation plan | Plan endpoint health review for `<backend-service>`. | Confirm Service endpoints represent healthy backends. | TODO: record sanitized output after approved execution. |
| V002 | Ingress backend endpoint health validation plan | Plan backend health review from Ingress perspective. | Confirm Ingress backend endpoint health is reviewable. | TODO: record sanitized output after approved execution. |
| V003 | Nginx upstream health validation plan | Plan upstream health review from `<reverse-proxy-host>`. | Confirm Nginx upstream health is reviewable. | TODO: record sanitized output after approved execution. |
| V004 | AWS service entrypoint health check plan | Document placeholder health check for AWS service entrypoint. | Confirm AWS entrypoint health model exists. | TODO: record sanitized output after approved execution. |
| V005 | Azure service entrypoint health check plan | Document placeholder health check for Azure service entrypoint. | Confirm Azure entrypoint health model exists. | TODO: record sanitized output after approved execution. |
| V006 | OpenStack service entrypoint health check plan | Document placeholder health check for OpenStack service entrypoint. | Confirm OpenStack entrypoint health model exists. | TODO: record sanitized output after approved execution. |
| V007 | HTTP /health endpoint response validation plan | Plan HTTP response check for `<health-endpoint>`. | Confirm health endpoint returns expected HTTP 200. | TODO: record sanitized output after approved execution. |
| V008 | Backend unavailable detection plan | Plan health review with one backend unavailable. | Confirm unavailable backend is detected. | TODO: record sanitized output after approved execution. |
| V009 | Traffic continuity validation plan with one backend unavailable | Plan limited continuity check when one backend is unavailable. | Confirm continuity behavior is documented without global failover claims. | TODO: record sanitized output after approved execution. |
| V010 | Health check log capture plan | Review sanitized health check logs. | Confirm health check evidence can be captured. | TODO: record sanitized output after approved execution. |
| V011 | Failure condition for all backends unhealthy, health endpoint missing, HTTP 5xx, route timeout, stale endpoint, or no health evidence | Review validation findings against failure criteria. | Confirm health check failures result in `FAIL` or `BLOCKED`. | TODO: record decision after execution. |

## Planned Supporting Evidence

- `configs/load-balancing-health-check-summary.md`
- `configs/backend-endpoint-health-summary.md`
- `logs/load-balancing-health-check-validation.log`
- `screenshots/load-balancing-health-check-test.png`
