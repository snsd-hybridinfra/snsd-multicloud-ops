# Commands

Scenario: S035-load-balancer-failure-validation
Level: L4-failure-recovery
Capability: Load Balancer Failure Validation

Record approved commands or manual actions used during validation. Do not include real command output yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Command Records

| Check ID | Purpose | Planned Command Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Capture pre-failure load balancer endpoint response | `curl <load-balancer-endpoint>` or approved equivalent | `<load-balancer-endpoint>` | TODO: `screenshots/load-balancer-before-failure.png` |
| V002 | Capture pre-failure backend health | `<approved-backend-health-check-placeholder>` | `<backend-service>` | TODO: `configs/load-balancer-failure-summary.md` |
| V003 | Reference pre-failure Ingress route | Manual review of S023 route baseline | `<ingress-host>` | TODO: `configs/load-balancer-failure-summary.md` |
| V004 | Inject load balancer or reverse proxy entrypoint failure | `<approved-entrypoint-stop-command-placeholder>` | `<reverse-proxy-host>` or `<load-balancer-endpoint>` | TODO: `logs/load-balancer-failure-validation.log` |
| V005 | Detect endpoint failure | `curl <web-endpoint>` and `curl <api-endpoint>` or approved equivalents | `<web-endpoint>`, `<api-endpoint>` | TODO: `screenshots/load-balancer-during-failure.png` |
| V006 | Detect health check failure | `curl <health-endpoint>` or approved equivalent | `<health-endpoint>` | TODO: `logs/load-balancer-failure-validation.log` |
| V007 | Reference Blackbox probe failure | Manual review of S030 probe behavior | `<health-endpoint>` | TODO: `configs/load-balancer-failure-summary.md` |
| V008 | Confirm backend health during frontend failure | `<approved-backend-health-check-placeholder>` | `<backend-service>` | TODO: `configs/load-balancer-failure-summary.md` |
| V009 | Record manual recovery decision points | Manual review of decision point checklist | manual runbook | TODO: `configs/load-balancer-decision-points.md` |
| V010 | Restore load balancer or reverse proxy entrypoint | `<approved-entrypoint-start-or-reload-command-placeholder>` | `<reverse-proxy-host>` or `<load-balancer-endpoint>` | TODO: `logs/load-balancer-failure-validation.log` |
| V011 | Validate post-recovery HTTP responses | `curl <web-endpoint>` and `curl <api-endpoint>` or approved equivalents | `<web-endpoint>`, `<api-endpoint>` | TODO: `screenshots/load-balancer-after-recovery.png` |
| V012 | Measure detection and recovery time | Manual timestamp comparison between outage action, detection, restoration, and recovered response | `<recovery-threshold-seconds>` | TODO: `configs/load-balancer-recovery-threshold.md` |

## Manual Decision Point Placeholder

```text
Confirm load balancer or reverse proxy entrypoint outage: TODO
Confirm backend service health: TODO
Classify failure as frontend entrypoint, upstream mapping, ingress, or backend: TODO
Choose manual recovery action: TODO
Validate restored endpoint response: TODO
Validate health check and Blackbox probe recovery: TODO
Record evidence and incident notes: TODO
```

## Output Placeholder

```text
Execution timestamp: TODO
Operator: TODO
Load balancer endpoint: <load-balancer-endpoint>
Reverse proxy host: <reverse-proxy-host>
Backend service: <backend-service>
Command or manual review: TODO
Expected purpose: TODO
Sanitized output summary: TODO
```
