# ML Metric Dataset Quality Criteria — Sample / Non-Production

| Quality Area | Expected Condition | Failure Condition | Severity | Required Evidence | Related Scenario | Final Judgment |
|---|---|---|---|---|---|---|
| Required schema fields present | All required fields exist | Required field missing | Critical | `<evidence-path>` | S047 | DATASET_INVALID |
| Metric timestamp present | Timestamp exists | Timestamp missing | High | `<evidence-path>` | S047 | DATASET_INVALID |
| Metric value numeric | Numeric value | Non-numeric value | Critical | `<evidence-path>` | S047 | DATASET_INVALID |
| Normalized value present | Numeric normalized value | Missing/non-numeric | High | `<evidence-path>` | S047 | DATASET_INVALID |
| Collection window present | Start and end exist | Window missing | High | `<evidence-path>` | S047 | DATASET_EVIDENCE_INCOMPLETE |
| Dataset ID present | Placeholder ID exists | ID missing | High | `<evidence-path>` | S047 | DATASET_EVIDENCE_INCOMPLETE |
| Feature catalog mapping present | Feature maps to catalog | Mapping missing | High | `<evidence-path>` | S048 | DATASET_REVIEW_REQUIRED |
| Label placeholder valid | Allowed label | Invalid label | Critical | `<evidence-path>` | S048 | DATASET_INVALID |
| Duplicate row handling | Duplicates reviewed | Duplicates ignored | Medium | `<evidence-path>` | S047 | DATASET_WARNING |
| Missing value handling | Missing values reviewed | Missing values ignored | Medium | `<evidence-path>` | S047 | DATASET_WARNING |
| Metric source placeholder | Placeholder source only | Production source present | Critical | `<evidence-path>` | S047 | DATASET_INVALID |
| No raw log payload | Metric-only | Raw log content | Critical | `<evidence-path>` | S047 | DATASET_INVALID |
| No packet payload | No packet content | Packet content present | Critical | `<evidence-path>` | S047 | DATASET_INVALID |
| No credentials | No credential material | Credential detected | Critical | `<evidence-path>` | S047 | DATASET_INVALID |
| No real IPs | Placeholders only | Real IP detected | Critical | `<evidence-path>` | S047 | DATASET_INVALID |
| No real hostnames | Placeholders only | Real hostname detected | Critical | `<evidence-path>` | S047 | DATASET_INVALID |
| No production identifiers | Synthetic identifiers | Production identifier detected | Critical | `<evidence-path>` | S047 | DATASET_INVALID |
| S048 anomaly detection mapping | S048 mapped | Mapping missing | High | `<evidence-path>` | S048 | DATASET_EVIDENCE_INCOMPLETE |
| S049 report mapping | S049 mapped | Mapping missing | High | `<evidence-path>` | S049 | DATASET_EVIDENCE_INCOMPLETE |

Allowed final judgments: `DATASET_READY`, `DATASET_WARNING`, `DATASET_INVALID`, `DATASET_EVIDENCE_INCOMPLETE`, `DATASET_REVIEW_REQUIRED`.
