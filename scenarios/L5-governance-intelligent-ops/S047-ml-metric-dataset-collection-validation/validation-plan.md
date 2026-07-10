# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Prometheus metric source availability reference validation plan | Reference S028 and `<prometheus-endpoint>` placeholder. | Metric source is referenced without real output. | `commands.md`, `configs/ml-metric-source-mapping.md`, `validation.md` |
| V002 | Metric query input validation plan | Review `<metric-query>` placeholders. | Metric queries are documented as placeholders. | `commands.md`, `configs/ml-metric-dataset-collection-summary.md`, `validation.md` |
| V003 | Node metric dataset collection placeholder validation plan | Map node CPU, memory, disk, and network placeholders. | Node metric categories are mapped. | `configs/ml-metric-source-mapping.md`, `validation.md` |
| V004 | Kubernetes metric dataset collection placeholder validation plan | Map pod restart and readiness placeholders. | Kubernetes metric categories are mapped. | `configs/ml-metric-source-mapping.md`, `validation.md` |
| V005 | MariaDB metric dataset collection placeholder validation plan | Map availability or replication placeholders. | MariaDB metric category is mapped. | `configs/ml-metric-source-mapping.md`, `validation.md` |
| V006 | Blackbox metric dataset collection placeholder validation plan | Map `probe_success` and `probe_http_status_code` placeholders. | Blackbox metric categories are mapped. | `configs/ml-metric-source-mapping.md`, `validation.md` |
| V007 | Dataset schema validation plan | Review required dataset fields. | Dataset schema includes all required fields. | `configs/ml-metric-dataset-schema.md`, `validation.md` |
| V008 | Timestamp field validation plan | Review `timestamp` placeholder. | Timestamp field is present and reviewable. | `configs/ml-metric-dataset-schema.md`, `validation.md` |
| V009 | Metric value field validation plan | Review `metric_value` placeholder. | Metric value field is present and numeric policy is documented. | `configs/ml-metric-dataset-schema.md`, `validation.md` |
| V010 | Target label consistency validation plan | Review `target_job`, `target_instance`, `provider_or_zone`, and `component_type` placeholders. | Target labels are consistent. | `configs/ml-metric-dataset-schema.md`, `configs/ml-metric-source-mapping.md`, `validation.md` |
| V011 | Dataset file existence placeholder validation plan | Review `<dataset-file>` placeholder. | Dataset file path is documented without real records. | `commands.md`, `configs/ml-metric-dataset-collection-summary.md`, `validation.md` |
| V012 | Dataset quality state validation plan | Apply dataset quality states. | Result is classified as `DATASET_READY`, `DATASET_PARTIAL`, `DATASET_INVALID`, `DATASET_EMPTY`, or `DATASET_INCONCLUSIVE`. | `configs/ml-dataset-quality-model.md`, `validation.md` |
| V013 | Failure condition for missing metric source, empty dataset, invalid timestamp, missing target label, inconsistent schema, unsupported AI security claim, sensitive data exposure, or missing evidence | Evaluate findings against explicit failure conditions. | Dataset collection issues produce `FAIL` or `BLOCKED` status. | `validation.md`, `logs/ml-metric-dataset-collection-validation.log`, `screenshots/ml-metric-query-result.png`, `screenshots/ml-dataset-schema-validation.png` |

Every validation item must map to evidence. This scenario validates metric dataset collection only.
