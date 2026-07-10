# Commands

Scenario: S049-ml-anomaly-report-generation-validation
Level: L5-governance-intelligent-ops
Capability: ML Anomaly Report Generation Validation

Record approved commands or manual review actions used during validation. Do not include real ML output, real dataset records, or real report output yet; use TODO placeholders until execution is approved and sanitized.

Do not include secrets, credentials, tokens, kubeconfig content, tfstate, private keys, account IDs, tenant IDs, subscription IDs, project IDs, public IPs, or private IPs tied to a real environment.

## Planned Review Records

| Check ID | Purpose | Planned Review Pattern | Target | Output Location |
|---|---|---|---|---|
| V001 | Validate anomaly detection result reference. | Review S048 detection output placeholder | Detection reference | `configs/ml-anomaly-report-generation-summary.md` |
| V002 | Validate dataset reference. | Review `<dataset-file>` placeholder from S047 | Dataset reference | `configs/ml-anomaly-report-schema.md` |
| V003 | Validate report input schema. | Review required report schema placeholders | `<report-file>` | `configs/ml-anomaly-report-schema.md` |
| V004 | Validate required report fields. | Review required field list | `<report-file>` | `configs/ml-anomaly-report-schema.md` |
| V005 | Validate report summary section. | Review summary section placeholder | `<report-file>` | `configs/ml-anomaly-report-section-mapping.md` |
| V006 | Validate affected component section. | Review provider or zone, component, job, and instance placeholders | `<target-job>`, `<target-instance>` | `configs/ml-anomaly-report-section-mapping.md` |
| V007 | Validate metric anomaly detail section. | Review metric, observed value, baseline, threshold, and anomaly result placeholders | `<metric-name>` | `configs/ml-anomaly-report-section-mapping.md` |
| V008 | Validate review priority placeholder. | Review `<review-priority>` placeholder | `<report-file>` | `configs/ml-anomaly-report-section-mapping.md` |
| V009 | Validate recommended investigation placeholder. | Review recommended investigation text placeholder | `<report-file>` | `configs/ml-anomaly-report-section-mapping.md` |
| V010 | Validate evidence reference mapping. | Review `<evidence-reference>` placeholder | Evidence references | `configs/ml-anomaly-report-generation-summary.md` |
| V011 | Validate human review note placeholder. | Review human review note placeholder | `<report-file>` | `configs/ml-anomaly-report-section-mapping.md` |
| V012 | Apply report judgment state. | Classify result as `REPORT_READY`, `REPORT_PARTIAL`, `REPORT_INVALID`, `REPORT_INCONCLUSIVE`, or `REPORT_OUT_OF_SCOPE` | `<report-file>` | `configs/ml-anomaly-report-judgment-model.md` |

## Report Schema Placeholder

```text
report_id: TODO placeholder
generated_at: TODO
scenario_id: S049
dataset_reference: <dataset-file>
detection_reference: TODO S048 placeholder
affected_component: TODO
provider_or_zone: TODO placeholder
metric_name: <metric-name>
observed_value: TODO
baseline_or_threshold: <anomaly-threshold>
anomaly_judgment: TODO
review_priority: <review-priority>
recommended_investigation: TODO
evidence_reference: <evidence-reference>
human_review_note: TODO
report_file: <report-file>
target_job: <target-job>
target_instance: <target-instance>
anomaly_score: <anomaly-score>
```

## Output Placeholder

```text
TODO: Paste sanitized anomaly report generation summaries or manual validation notes here after approval.
TODO: Do not paste real report output, real ML output, real dataset records, credentials, tokens, API keys, secrets, cloud account values, public IPs, tfstate, kubeconfig content, private keys, subscription IDs, tenant IDs, billing account IDs, or account-specific values.
```
