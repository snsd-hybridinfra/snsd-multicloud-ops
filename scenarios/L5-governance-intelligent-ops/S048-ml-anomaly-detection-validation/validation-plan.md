# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Dataset input reference validation plan | Reference S047 `<dataset-file>` placeholder. | Dataset input is referenced or marked missing. | `commands.md`, `configs/ml-detection-input-schema.md`, `validation.md` |
| V002 | Dataset schema readiness validation plan | Review required detection input fields. | Dataset schema is ready or issue is recorded. | `configs/ml-detection-input-schema.md`, `validation.md` |
| V003 | Baseline window definition validation plan | Review `<baseline-window>` placeholder. | Baseline window is defined. | `configs/ml-anomaly-detection-summary.md`, `validation.md` |
| V004 | Detection window definition validation plan | Review `<detection-window>` placeholder. | Detection window is defined. | `configs/ml-anomaly-detection-summary.md`, `validation.md` |
| V005 | Threshold or anomaly score placeholder validation plan | Review `<anomaly-score>` and `<anomaly-threshold>` placeholders. | Threshold or score is documented. | `configs/ml-anomaly-detection-summary.md`, `screenshots/ml-anomaly-threshold-review.png`, `validation.md` |
| V006 | Node metric anomaly detection placeholder validation plan | Map CPU, memory, disk, and network anomaly placeholders. | Node anomaly targets are mapped. | `configs/ml-anomaly-target-mapping.md`, `validation.md` |
| V007 | Kubernetes workload anomaly detection placeholder validation plan | Map pod restart and readiness anomaly placeholders. | Kubernetes anomaly targets are mapped. | `configs/ml-anomaly-target-mapping.md`, `validation.md` |
| V008 | MariaDB metric anomaly detection placeholder validation plan | Map availability or replication anomaly placeholders. | MariaDB anomaly target is mapped. | `configs/ml-anomaly-target-mapping.md`, `validation.md` |
| V009 | Blackbox probe anomaly detection placeholder validation plan | Map `probe_success` and HTTP status anomaly placeholders. | Blackbox anomaly targets are mapped. | `configs/ml-anomaly-target-mapping.md`, `validation.md` |
| V010 | Endpoint latency anomaly detection placeholder validation plan | Map endpoint latency anomaly placeholder. | Endpoint latency anomaly target is mapped. | `configs/ml-anomaly-target-mapping.md`, `validation.md` |
| V011 | Anomaly judgment state validation plan | Apply anomaly judgment states. | Result is classified as `ANOMALY_NOT_DETECTED`, `ANOMALY_DETECTED`, `ANOMALY_WARNING`, `ANOMALY_INCONCLUSIVE`, or `ANOMALY_OUT_OF_SCOPE`. | `configs/ml-anomaly-judgment-model.md`, `validation.md` |
| V012 | Human review note placeholder validation plan | Review detection result note placeholder. | Human review note is documented. | `configs/ml-anomaly-detection-summary.md`, `validation.md` |
| V013 | Failure condition for missing dataset, invalid dataset schema, missing baseline, missing threshold, false unsupported security claim, inconclusive result not documented, sensitive data exposure, or missing evidence | Evaluate findings against explicit failure conditions. | Anomaly detection issues produce `FAIL` or `BLOCKED` status. | `validation.md`, `logs/ml-anomaly-detection-validation.log`, `screenshots/ml-anomaly-detection-result.png` |

Every validation item must map to evidence. This scenario validates operational metric anomaly detection only.
