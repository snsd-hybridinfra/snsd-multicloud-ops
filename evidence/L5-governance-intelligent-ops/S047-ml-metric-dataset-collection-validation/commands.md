# Commands

Scenario: S047-ml-metric-dataset-collection-validation
Level: L5-governance-intelligent-ops
Capability: ML Metric Dataset Collection Validation

Record approved commands or manual review actions used during validation. Do not include real Prometheus output or real dataset records yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Review Records

| Check ID | Purpose | Planned Review Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Reference Prometheus metric source availability. | Review `<prometheus-endpoint>` placeholder and S028 boundary | Metric source placeholder | `configs/ml-metric-source-mapping.md` |
| V002 | Validate metric query input placeholders. | Review `<metric-query>` values without running real queries | Metric query placeholders | `configs/ml-metric-dataset-collection-summary.md` |
| V003 | Map node metric dataset placeholders. | Review CPU, memory, disk, and network placeholders | Node metrics | `configs/ml-metric-source-mapping.md` |
| V004 | Map Kubernetes metric dataset placeholders. | Review pod restart and readiness placeholders | Kubernetes metrics | `configs/ml-metric-source-mapping.md` |
| V005 | Map MariaDB metric dataset placeholders. | Review availability or replication placeholders | MariaDB metrics | `configs/ml-metric-source-mapping.md` |
| V006 | Map Blackbox metric dataset placeholders. | Review `probe_success` and `probe_http_status_code` placeholders | Blackbox metrics | `configs/ml-metric-source-mapping.md` |
| V007 | Validate dataset schema. | Review required fields list | `<dataset-file>` | `configs/ml-metric-dataset-schema.md` |
| V008 | Validate timestamp field placeholder. | Review `timestamp` field definition | `<dataset-file>` | `configs/ml-metric-dataset-schema.md` |
| V009 | Validate metric value field placeholder. | Review `metric_value` field definition | `<dataset-file>` | `configs/ml-metric-dataset-schema.md` |
| V010 | Validate target label consistency. | Review `<target-job>`, `<target-instance>`, provider or zone, and component type placeholders | Dataset labels | `configs/ml-metric-dataset-schema.md`, `configs/ml-metric-source-mapping.md` |
| V011 | Validate dataset file existence placeholder. | Review `<dataset-file>` path placeholder | `<dataset-file>` | `configs/ml-metric-dataset-collection-summary.md` |
| V012 | Apply dataset quality state. | Classify result as `DATASET_READY`, `DATASET_PARTIAL`, `DATASET_INVALID`, `DATASET_EMPTY`, or `DATASET_INCONCLUSIVE` | Dataset placeholder | `configs/ml-dataset-quality-model.md` |

## Dataset Schema Placeholder

```text
timestamp: TODO
metric_name: TODO
metric_value: TODO
target_job: <target-job>
target_instance: <target-instance>
provider_or_zone: TODO placeholder
component_type: TODO placeholder
collection_window: <dataset-window>
anomaly_label: TODO placeholder for future S048 use
notes: TODO
dataset_file: <dataset-file>
collection_script: <collection-script>
```

## Output Placeholder

```text
TODO: Paste sanitized metric dataset collection summaries or manual validation notes here after approval.
TODO: Do not paste real Prometheus output, real dataset records, credentials, tokens, API keys, secrets, cloud account values, public IPs, tfstate, kubeconfig content, private keys, subscription IDs, tenant IDs, billing account IDs, or account-specific values.
```
