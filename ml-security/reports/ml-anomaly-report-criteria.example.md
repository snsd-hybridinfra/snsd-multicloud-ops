# ML Anomaly Report Criteria — Non-Production

| Report Area | Input Evidence | Expected Condition | Failure Condition | Required Review | Related Scenario | Final Judgment |
|---|---|---|---|---|---|---|
| Report metadata | `<evidence-path>` | complete | missing | human | S049 | REPORT_INVALID |
| Dataset reference | S047 | present | missing | human | S047 | REPORT_EVIDENCE_INCOMPLETE |
| Detection run reference | S048 | present | missing | human | S048 | REPORT_EVIDENCE_INCOMPLETE |
| Anomaly count summary | S048 | present | missing | human | S049 | REPORT_INVALID |
| Warning count summary | S048 | present | missing | human | S049 | REPORT_INVALID |
| Review-required count summary | S048 | present | missing | human | S049 | REPORT_INVALID |
| Top anomaly candidate list | S048 | present when anomaly exists | absent | human | S048 | REPORT_WARNING |
| Affected feature group summary | S048 | present | absent | human | S048 | REPORT_WARNING |
| Operational interpretation | `<recommendation-placeholder>` | deterministic | LLM decision | human | S049 | REPORT_INVALID |
| Recommended operator action | `<recommendation-placeholder>` | review only | automated blocking | human | S049 | REPORT_INVALID |
| Out-of-scope action disclaimer | policy | present | absent | human | S049 | REPORT_WARNING |
| Evidence reference mapping | `<evidence-path>` | present | missing | human | S050 | REPORT_EVIDENCE_INCOMPLETE |
| Privacy / secret safety | safety evidence | pass | unsafe content | human | S049 | REPORT_INVALID |
| S047 mapping | S047 | present | missing | human | S047 | REPORT_INVALID |
| S048 mapping | S048 | present | missing | human | S048 | REPORT_INVALID |
| S050 mapping | S050 | present | missing | human | S050 | REPORT_INVALID |
