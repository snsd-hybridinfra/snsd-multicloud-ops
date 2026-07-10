# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Dataset input reference validation plan | `commands.md`; `configs/ml-detection-input-schema.md`; `validation.md` | review plan, input schema, validation record | yes |
| Dataset schema readiness validation plan | `configs/ml-detection-input-schema.md`; `validation.md` | input schema, validation record | yes |
| Baseline window definition validation plan | `configs/ml-anomaly-detection-summary.md`; `validation.md` | detection summary, validation record | yes |
| Detection window definition validation plan | `configs/ml-anomaly-detection-summary.md`; `validation.md` | detection summary, validation record | yes |
| Threshold or anomaly score placeholder validation plan | `configs/ml-anomaly-detection-summary.md`; `screenshots/ml-anomaly-threshold-review.png`; `validation.md` | detection summary, screenshot reference, validation record | yes |
| Node metric anomaly detection placeholder validation plan | `configs/ml-anomaly-target-mapping.md`; `validation.md` | target mapping, validation record | yes |
| Kubernetes workload anomaly detection placeholder validation plan | `configs/ml-anomaly-target-mapping.md`; `validation.md` | target mapping, validation record | yes |
| MariaDB metric anomaly detection placeholder validation plan | `configs/ml-anomaly-target-mapping.md`; `validation.md` | target mapping, validation record | yes |
| Blackbox probe anomaly detection placeholder validation plan | `configs/ml-anomaly-target-mapping.md`; `validation.md` | target mapping, validation record | yes |
| Endpoint latency anomaly detection placeholder validation plan | `configs/ml-anomaly-target-mapping.md`; `validation.md` | target mapping, validation record | yes |
| Anomaly judgment state validation plan | `configs/ml-anomaly-judgment-model.md`; `validation.md` | judgment model, validation record | yes |
| Human review note placeholder validation plan | `configs/ml-anomaly-detection-summary.md`; `validation.md` | detection summary, validation record | yes |
| Failure condition for missing dataset, invalid dataset schema, missing baseline, missing threshold, false unsupported security claim, inconclusive result not documented, sensitive data exposure, or missing evidence | `validation.md`; `logs/ml-anomaly-detection-validation.log`; `screenshots/ml-anomaly-detection-result.png` | failure criteria, validation log, screenshot reference | yes |

No real ML output or dataset records have been collected. Use TODO placeholders until execution is approved and outputs are sanitized.
