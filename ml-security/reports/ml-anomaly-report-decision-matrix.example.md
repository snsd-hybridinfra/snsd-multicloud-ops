# ML Anomaly Report Decision Matrix — Non-Production

| Report Evaluation Result | Example Evidence | Operational Meaning | Required Action | S050 Mapping | Final Judgment |
|---|---|---|---|---|---|
| Report ready | `<evidence-path>` | complete | human review | S050 | REPORT_READY |
| Report ready with warning | `<evidence-path>` | review | human review | S050 | REPORT_WARNING |
| Report missing anomaly summary | `<evidence-path>` | incomplete | correct | S050 | REPORT_EVIDENCE_INCOMPLETE |
| Report missing S047 reference | `<evidence-path>` | unmapped | correct | S050 | REPORT_INVALID |
| Report missing S048 reference | `<evidence-path>` | unmapped | correct | S050 | REPORT_INVALID |
| Report missing S050 reference | `<evidence-path>` | unmapped | correct | S050 | REPORT_INVALID |
| Report missing evidence reference | `<evidence-path>` | incomplete | correct | S050 | REPORT_EVIDENCE_INCOMPLETE |
| Report contains raw log data | `<evidence-path>` | unsafe | reject | S050 | REPORT_INVALID |
| Report contains real identifiers | `<evidence-path>` | unsafe | reject | S050 | REPORT_INVALID |
| Report contains secret-like content | `<evidence-path>` | unsafe | reject | S050 | REPORT_INVALID |
| Report recommends automated blocking | `<evidence-path>` | unsafe | reject | S050 | REPORT_INVALID |
| Report contains LLM-based decision | `<evidence-path>` | unsafe | reject | S050 | REPORT_INVALID |
| Report malformed | `<evidence-path>` | invalid | replace | S050 | REPORT_INVALID |
