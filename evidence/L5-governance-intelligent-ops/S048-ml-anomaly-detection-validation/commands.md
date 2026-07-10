# Commands

Scenario: S048-ml-anomaly-detection-validation
Level: L5-governance-intelligent-ops
Capability: ML Anomaly Detection Validation

Record approved commands or manual review actions used during validation. Do not include real ML output or real dataset records yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Review Records

| Check ID | Purpose | Planned Review Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Validate dataset input reference. | Review `<dataset-file>` placeholder from S047 | Dataset placeholder | `configs/ml-detection-input-schema.md` |
| V002 | Validate dataset schema readiness. | Review required detection input fields | `<dataset-file>` | `configs/ml-detection-input-schema.md` |
| V003 | Validate baseline window definition. | Review `<baseline-window>` placeholder | `<metric-name>` | `configs/ml-anomaly-detection-summary.md` |
| V004 | Validate detection window definition. | Review `<detection-window>` placeholder | `<metric-name>` | `configs/ml-anomaly-detection-summary.md` |
| V005 | Validate threshold or anomaly score placeholder. | Review `<anomaly-score>` and `<anomaly-threshold>` | `<metric-name>` | `configs/ml-anomaly-detection-summary.md`, `screenshots/ml-anomaly-threshold-review.png` |
| V006 | Map node metric anomaly placeholders. | Review CPU, memory, disk, and network anomaly placeholders | Node metrics | `configs/ml-anomaly-target-mapping.md` |
| V007 | Map Kubernetes workload anomaly placeholders. | Review pod restart and readiness anomaly placeholders | Kubernetes metrics | `configs/ml-anomaly-target-mapping.md` |
| V008 | Map MariaDB metric anomaly placeholders. | Review DB availability or replication anomaly placeholders | MariaDB metrics | `configs/ml-anomaly-target-mapping.md` |
| V009 | Map Blackbox probe anomaly placeholders. | Review probe success and HTTP status anomaly placeholders | Blackbox metrics | `configs/ml-anomaly-target-mapping.md` |
| V010 | Map endpoint latency anomaly placeholder. | Review endpoint latency increase placeholder | Endpoint latency metric | `configs/ml-anomaly-target-mapping.md` |
| V011 | Apply anomaly judgment state. | Classify result as `ANOMALY_NOT_DETECTED`, `ANOMALY_DETECTED`, `ANOMALY_WARNING`, `ANOMALY_INCONCLUSIVE`, or `ANOMALY_OUT_OF_SCOPE` | Detection result placeholder | `configs/ml-anomaly-judgment-model.md` |
| V012 | Validate human review note placeholder. | Review detection result note placeholder | Detection result placeholder | `configs/ml-anomaly-detection-summary.md` |

## Detection Input Placeholder

```text
Dataset file: <dataset-file>
Metric name: <metric-name>
Metric value: TODO
Timestamp: TODO
Target job: <target-job>
Target instance: <target-instance>
Baseline window: <baseline-window>
Detection window: <detection-window>
Anomaly score: <anomaly-score>
Anomaly threshold: <anomaly-threshold>
Detection result: TODO
Review note: TODO
Judgment: TODO (ANOMALY_NOT_DETECTED | ANOMALY_DETECTED | ANOMALY_WARNING | ANOMALY_INCONCLUSIVE | ANOMALY_OUT_OF_SCOPE)
```

## Output Placeholder

```text
TODO: Paste sanitized anomaly detection review summaries or manual validation notes here after approval.
TODO: Do not paste real ML output, real dataset records, credentials, tokens, API keys, secrets, cloud account values, public IPs, tfstate, kubeconfig content, private keys, subscription IDs, tenant IDs, billing account IDs, or account-specific values.
```
