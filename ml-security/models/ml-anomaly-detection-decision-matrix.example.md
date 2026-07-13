# ML Anomaly Detection Decision Matrix — Non-Production

| Detection Result | Example Evidence | Operational Meaning | Required Action | Report Mapping | Final Judgment |
|---|---|---|---|---|---|
| No anomaly | `<evidence-path>` | baseline | record | S049 | ANOMALY_DETECTION_PASS |
| Warning-level deviation | `<evidence-path>` | review | human review | S049 | ANOMALY_DETECTION_WARNING |
| Confirmed anomaly candidate | `<evidence-path>` | candidate | human review | S049 | ANOMALY_DETECTED |
| Multiple correlated anomaly candidates | `<evidence-path>` | correlation candidate | human review | S049 | ANOMALY_REVIEW_REQUIRED |
| Dataset evidence incomplete | `<evidence-path>` | input incomplete | return to S047 | S049 | ANOMALY_EVIDENCE_INCOMPLETE |
| Invalid metric value | `<evidence-path>` | invalid input | reject | S049 | ANOMALY_VALIDATION_FAILED |
| Invalid anomaly score | `<evidence-path>` | invalid output | reject | S049 | ANOMALY_VALIDATION_FAILED |
| Missing threshold profile | `<evidence-path>` | configuration missing | block | S049 | ANOMALY_VALIDATION_FAILED |
| Review required | `<evidence-path>` | operator decision needed | review | S049 | ANOMALY_REVIEW_REQUIRED |
| Out-of-scope security telemetry detected | `<evidence-path>` | scope violation | reject | S049 | ANOMALY_VALIDATION_FAILED |
