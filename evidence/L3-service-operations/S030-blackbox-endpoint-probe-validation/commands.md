# Commands

Scenario: S030-blackbox-endpoint-probe-validation
Level: L3-service-operations
Capability: Blackbox Endpoint Probe Validation

Record approved commands or manual actions used during validation. Do not include real command output yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Command Records

| Check ID | Purpose | Planned Command Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Review Blackbox Exporter service status | `systemctl status <blackbox-exporter-service>` or approved equivalent | `<blackbox-exporter-endpoint>` | TODO: `logs/blackbox-endpoint-probe-validation.log` |
| V002 | Review probe module placeholder | `grep <probe-module> <blackbox-config-placeholder>` or approved equivalent | `<blackbox-exporter-endpoint>` | TODO: `configs/blackbox-endpoint-probe-summary.md` |
| V003 | Probe web endpoint | `curl "<blackbox-exporter-endpoint>/probe?target=<web-endpoint>&module=<probe-module>"` | `<web-endpoint>` | TODO: `logs/blackbox-endpoint-probe-validation.log` |
| V004 | Probe API endpoint | `curl "<blackbox-exporter-endpoint>/probe?target=<api-endpoint>&module=<probe-module>"` | `<api-endpoint>` | TODO: `logs/blackbox-endpoint-probe-validation.log` |
| V005 | Probe Ingress host endpoint | `curl "<blackbox-exporter-endpoint>/probe?target=<ingress-host>&module=<probe-module>"` | `<ingress-host>` | TODO: `screenshots/blackbox-probe-result.png` |
| V006 | Probe Nginx Reverse Proxy endpoint | `curl "<blackbox-exporter-endpoint>/probe?target=<reverse-proxy-host>&module=<probe-module>"` | `<reverse-proxy-host>` | TODO: `screenshots/blackbox-probe-result.png` |
| V007 | Map AWS service endpoint placeholder | Manual review of endpoint mapping | `<aws-service-endpoint>` | TODO: `configs/blackbox-target-mapping.md` |
| V008 | Map Azure service endpoint placeholder | Manual review of endpoint mapping | `<azure-service-endpoint>` | TODO: `configs/blackbox-target-mapping.md` |
| V009 | Map OpenStack service endpoint placeholder | Manual review of endpoint mapping | `<openstack-service-endpoint>` | TODO: `configs/blackbox-target-mapping.md` |
| V010 | Review HTTP status code metric | Prometheus query: `probe_http_status_code{target="<probe-target>"}` | `<probe-target>` | TODO: `configs/blackbox-prometheus-query-mapping.md` |
| V011 | Review probe duration metric | Prometheus query: `probe_duration_seconds{target="<probe-target>"}` | `<probe-target>` | TODO: `logs/blackbox-endpoint-probe-validation.log` |
| V012 | Review probe success metric | Prometheus query: `probe_success{target="<probe-target>"}` | `<probe-target>` | TODO: `screenshots/prometheus-blackbox-query-result.png` |
| V013 | Review probe HTTP status code query | Prometheus query: `probe_http_status_code{target="<probe-target>"}` | `<probe-target>` | TODO: `screenshots/prometheus-blackbox-query-result.png` |

## Output Placeholder

```text
Execution timestamp: TODO
Operator: TODO
Target endpoint category: TODO
Command or manual review: TODO
Expected purpose: TODO
Sanitized output summary: TODO
```
