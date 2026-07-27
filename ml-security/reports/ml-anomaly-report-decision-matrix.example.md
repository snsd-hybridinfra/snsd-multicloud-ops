# ML Anomaly Report Decision Matrix — Non-Production

| Report Evaluation Result | Example Evidence | Operational Meaning | Required Action | retired-numbered-case Mapping | Final Judgment |
|---|---|---|---|---|---|
| Report ready | `<evidence-path>` | complete | human review | retired-numbered-case | REPORT_READY |
| Report ready with warning | `<evidence-path>` | review | human review | retired-numbered-case | REPORT_WARNING |
| Report missing anomaly summary | `<evidence-path>` | incomplete | correct | retired-numbered-case | REPORT_EVIDENCE_INCOMPLETE |
| Report missing retired-numbered-case reference | `<evidence-path>` | unmapped | correct | retired-numbered-case | REPORT_INVALID |
| Report missing retired-numbered-case reference | `<evidence-path>` | unmapped | correct | retired-numbered-case | REPORT_INVALID |
| Report missing retired-numbered-case reference | `<evidence-path>` | unmapped | correct | retired-numbered-case | REPORT_INVALID |
| Report missing evidence reference | `<evidence-path>` | incomplete | correct | retired-numbered-case | REPORT_EVIDENCE_INCOMPLETE |
| Report contains raw log data | `<evidence-path>` | unsafe | reject | retired-numbered-case | REPORT_INVALID |
| Report contains real identifiers | `<evidence-path>` | unsafe | reject | retired-numbered-case | REPORT_INVALID |
| Report contains secret-like content | `<evidence-path>` | unsafe | reject | retired-numbered-case | REPORT_INVALID |
| Report recommends automated blocking | `<evidence-path>` | unsafe | reject | retired-numbered-case | REPORT_INVALID |
| Report contains LLM-based decision | `<evidence-path>` | unsafe | reject | retired-numbered-case | REPORT_INVALID |
| Report malformed | `<evidence-path>` | invalid | replace | retired-numbered-case | REPORT_INVALID |
