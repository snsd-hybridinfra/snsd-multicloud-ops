# ML Anomaly Report Criteria — Non-Production

| Report Area | Input Evidence | Expected Condition | Failure Condition | Required Review | Related Scenario | Final Judgment |
|---|---|---|---|---|---|---|
| Report metadata | `<evidence-path>` | complete | missing | human | retired-numbered-case | REPORT_INVALID |
| Dataset reference | retired-numbered-case | present | missing | human | retired-numbered-case | REPORT_EVIDENCE_INCOMPLETE |
| Detection run reference | retired-numbered-case | present | missing | human | retired-numbered-case | REPORT_EVIDENCE_INCOMPLETE |
| Anomaly count summary | retired-numbered-case | present | missing | human | retired-numbered-case | REPORT_INVALID |
| Warning count summary | retired-numbered-case | present | missing | human | retired-numbered-case | REPORT_INVALID |
| Review-required count summary | retired-numbered-case | present | missing | human | retired-numbered-case | REPORT_INVALID |
| Top anomaly candidate list | retired-numbered-case | present when anomaly exists | absent | human | retired-numbered-case | REPORT_WARNING |
| Affected feature group summary | retired-numbered-case | present | absent | human | retired-numbered-case | REPORT_WARNING |
| Operational interpretation | `<recommendation-placeholder>` | deterministic | LLM decision | human | retired-numbered-case | REPORT_INVALID |
| Recommended operator action | `<recommendation-placeholder>` | review only | automated blocking | human | retired-numbered-case | REPORT_INVALID |
| Out-of-scope action disclaimer | policy | present | absent | human | retired-numbered-case | REPORT_WARNING |
| Evidence reference mapping | `<evidence-path>` | present | missing | human | retired-numbered-case | REPORT_EVIDENCE_INCOMPLETE |
| Privacy / secret safety | safety evidence | pass | unsafe content | human | retired-numbered-case | REPORT_INVALID |
| retired-numbered-case mapping | retired-numbered-case | present | missing | human | retired-numbered-case | REPORT_INVALID |
| retired-numbered-case mapping | retired-numbered-case | present | missing | human | retired-numbered-case | REPORT_INVALID |
| retired-numbered-case mapping | retired-numbered-case | present | missing | human | retired-numbered-case | REPORT_INVALID |
