# Commands

Scenario: S040-service-health-after-recovery-validation
Level: L4-failure-recovery
Capability: Service Health After Recovery Validation

Record approved commands or manual actions used during validation. Do not include real command output yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Command Records

| Check ID | Purpose | Planned Command Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Validate Web service HTTP response | `curl <web-endpoint>` or approved equivalent | `<web-endpoint>` | TODO: `screenshots/service-health-after-recovery-web-api.png` |
| V002 | Validate API service HTTP response | `curl <api-endpoint>` or approved equivalent | `<api-endpoint>` | TODO: `screenshots/service-health-after-recovery-web-api.png` |
| V003 | Validate Ingress route | `curl <ingress-host>` or approved equivalent | `<ingress-host>` | TODO: `logs/service-health-after-recovery-validation.log` |
| V004 | Validate Nginx Reverse Proxy | `curl <reverse-proxy-host>` or approved equivalent | `<reverse-proxy-host>` | TODO: `logs/service-health-after-recovery-validation.log` |
| V005 | Validate load balancing health endpoint | `curl <health-endpoint>` or approved equivalent | `<health-endpoint>` | TODO: `configs/post-recovery-checklist.md` |
| V006 | Reference MariaDB Primary availability | Manual review of DB Primary evidence | `<db-primary-host>` | TODO: `configs/service-health-after-recovery-summary.md` |
| V007 | Reference MariaDB Replica state | Manual review of DB Replica evidence | `<db-replica-host>` | TODO: `configs/service-health-after-recovery-summary.md` |
| V008 | Validate Prometheus target UP state | Review `<prometheus-endpoint>/targets` or approved query | `<prometheus-endpoint>` | TODO: `screenshots/service-health-after-recovery-monitoring.png` |
| V009 | Validate Grafana dashboard visibility | Manual review of `<grafana-endpoint>` | `<grafana-endpoint>` | TODO: `screenshots/service-health-after-recovery-monitoring.png` |
| V010 | Validate Blackbox probe success | Prometheus query: `probe_success{target="<probe-target>"}` | recovered service endpoints | TODO: `configs/post-recovery-checklist.md` |
| V011 | Record final recovery judgment | Manual comparison against judgment model | post-recovery evidence set | TODO: `configs/post-recovery-judgment-model.md`, `screenshots/service-health-after-recovery-final-judgment.png` |

## Final Judgment Placeholder

```text
Web service result: TODO
API service result: TODO
Ingress result: TODO
Reverse proxy result: TODO
Health endpoint result: TODO
DB Primary result: TODO
DB Replica result: TODO
Prometheus result: TODO
Grafana result: TODO
Blackbox result: TODO
Final judgment: TODO (RECOVERED | DEGRADED | FAILED | INCONCLUSIVE)
Evidence reviewer: TODO
```

## Output Placeholder

```text
Execution timestamp: TODO
Operator: TODO
Command or manual review: TODO
Expected purpose: TODO
Sanitized output summary: TODO
```
