# Commands

Scenario: S036-prometheus-target-down-validation
Level: L4-failure-recovery
Capability: Prometheus Target Down Validation

Record approved commands or manual actions used during validation. Do not include real command output yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Command Records

| Check ID | Purpose | Planned Command Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Capture pre-failure Prometheus service status | `curl <prometheus-endpoint>/-/ready` or approved equivalent | `<prometheus-endpoint>` | TODO: `logs/prometheus-target-down-validation.log` |
| V002 | Capture pre-failure target UP status | Review `<prometheus-endpoint>/targets` or query `up{job="<target-job>",instance="<target-instance>"}` | `<target-job>`, `<target-instance>` | TODO: `screenshots/prometheus-target-before-failure.png` |
| V003 | Inject one target failure | `<approved-exporter-stop-command-placeholder>` or `<approved-endpoint-outage-command-placeholder>` | `<target-instance>` | TODO: `logs/prometheus-target-down-validation.log` |
| V004 | Validate `/targets` DOWN state | Review `<prometheus-endpoint>/targets` | `<target-job>`, `<target-instance>` | TODO: `screenshots/prometheus-target-during-failure.png` |
| V005 | Validate query-based DOWN state | Prometheus query: `up{job="<target-job>",instance="<target-instance>"}` | `<target-job>`, `<target-instance>` | TODO: `configs/prometheus-query-mapping.md` |
| V006 | Capture target failure timestamp | Manual timestamp comparison of failure action and DOWN observation | `<target-instance>` | TODO: `configs/prometheus-target-down-summary.md` |
| V007 | Restore exporter or endpoint | `<approved-exporter-start-command-placeholder>` or `<approved-endpoint-restore-command-placeholder>` | `<target-instance>` | TODO: `logs/prometheus-target-down-validation.log` |
| V008 | Validate post-recovery target UP state | Review `<prometheus-endpoint>/targets` | `<target-job>`, `<target-instance>` | TODO: `screenshots/prometheus-target-after-recovery.png` |
| V009 | Measure detection time | Compare failure action timestamp with DOWN observation timestamp | `<recovery-threshold-seconds>` | TODO: `configs/prometheus-target-down-threshold.md` |
| V010 | Measure recovery time | Compare restoration action timestamp with recovered UP observation timestamp | `<recovery-threshold-seconds>` | TODO: `configs/prometheus-target-down-threshold.md` |

## Query Placeholder

```text
Prometheus endpoint: <prometheus-endpoint>
Target job: <target-job>
Target instance: <target-instance>
Query: up{job="<target-job>",instance="<target-instance>"}
Expected pre-failure value: TODO
Expected during-failure value: TODO
Expected post-recovery value: TODO
```

## Output Placeholder

```text
Execution timestamp: TODO
Operator: TODO
Target category: TODO
Target job: <target-job>
Target instance: <target-instance>
Command or manual review: TODO
Expected purpose: TODO
Sanitized output summary: TODO
```
