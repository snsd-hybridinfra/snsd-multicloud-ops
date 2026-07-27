# ML Metric Dataset Decision Matrix — Sample / Non-Production

| Evaluation Result | Example Evidence | Operational Meaning | Required Action | ML Pipeline Impact | Final Judgment |
|---|---|---|---|---|---|
| Dataset schema valid | `<evidence-path>` | Schema accepted | Continue review | Eligible | DATASET_READY |
| Dataset ready for retired-numbered-case | `<evidence-path>` | Quality and mappings pass | Hand off reference | Eligible | DATASET_READY |
| Dataset has missing values | `<evidence-path>` | Completeness reduced | Review/impute outside retired-numbered-case | Hold | DATASET_WARNING |
| Dataset has invalid labels | `<evidence-path>` | Label constraint failed | Correct sample | Stop | DATASET_INVALID |
| Dataset has non-numeric metric values | `<evidence-path>` | Numeric constraint failed | Correct sample | Stop | DATASET_INVALID |
| Dataset has duplicate rows | `<evidence-path>` | Duplicate handling needed | Review | Hold | DATASET_REVIEW_REQUIRED |
| Dataset contains raw logs | `<evidence-path>` | Scope/privacy violation | Remove and investigate | Stop | DATASET_INVALID |
| Dataset contains real IPs or hostnames | `<evidence-path>` | Identifier safety violation | Remove and investigate | Stop | DATASET_INVALID |
| Dataset contains secrets | `<evidence-path>` | Secret safety violation | Remove and investigate | Stop | DATASET_INVALID |
| Dataset missing feature catalog mapping | `<evidence-path>` | Feature meaning unknown | Add mapping | Hold | DATASET_EVIDENCE_INCOMPLETE |
| Dataset malformed | `<evidence-path>` | File cannot be parsed | Replace sample | Stop | DATASET_INVALID |
