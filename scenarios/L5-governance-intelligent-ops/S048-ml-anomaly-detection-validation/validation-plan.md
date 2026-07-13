# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | Required artifacts | All S048 artifacts exist. | `logs/ml-anomaly-detection-validation.log` |
| V002 | Command safety | No live query/training/deployment/blocking. | command runbook |
| V003 | Threshold profile | Static profile, methods, and decisions exist. | threshold profile |
| V004 | Input dataset | 20 numeric rows and required columns. | input CSV |
| V005 | Detection output | 20 valid rows with normal, warning/review, and anomaly decisions. | output CSV |
| V006 | Invalid output | Deliberate invalid score/decision recognized. | invalid CSV |
| V007 | Run metadata | S047/S049/S050 mapped. | metadata YAML |
| V008 | Detection evidence | Profile/input/run/pass/fail/classification consistent. | sample logs |
| V009 | Privacy | Prohibited telemetry and identifiers absent. | privacy log |
| V010 | Final summary | No live/training/deployment/blocking and anomaly sample recorded. | final sample |
| V011 | Manifest | Required fields and mappings exist. | manifest |
| V012 | Policy | Metric-only and human review boundaries exist. | policy |
| V013 | Binary safety | No trained model/packet binary. | validator log |
| V014 | Sensitive/execution safety | No real endpoint, secret, or external execution. | validator log |
| V015 | Optional script | Deterministic standard-library logic only. | Python example |
| V016 | Maturity | Synthetic threshold limitation warned. | summary |
