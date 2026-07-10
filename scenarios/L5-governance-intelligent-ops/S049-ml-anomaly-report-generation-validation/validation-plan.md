# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Anomaly detection result reference validation plan | Reference S048 detection output placeholder. | Detection result is referenced or marked missing. | `commands.md`, `configs/ml-anomaly-report-generation-summary.md`, `validation.md` |
| V002 | Dataset reference validation plan | Reference S047 `<dataset-file>` placeholder. | Dataset reference is documented. | `commands.md`, `configs/ml-anomaly-report-schema.md`, `validation.md` |
| V003 | Report input schema validation plan | Review report schema placeholder. | Report input schema is documented. | `configs/ml-anomaly-report-schema.md`, `validation.md` |
| V004 | Required report field validation plan | Review required report fields. | Required fields are present or issue is recorded. | `configs/ml-anomaly-report-schema.md`, `validation.md` |
| V005 | Report summary section validation plan | Review summary section placeholder. | Summary section is defined. | `configs/ml-anomaly-report-section-mapping.md`, `validation.md` |
| V006 | Affected component section validation plan | Review provider or zone, component, target job, and target instance placeholders. | Affected component section is defined. | `configs/ml-anomaly-report-section-mapping.md`, `validation.md` |
| V007 | Metric anomaly detail section validation plan | Review metric, observed value, baseline, threshold, and anomaly judgment placeholders. | Metric detail section is defined. | `configs/ml-anomaly-report-section-mapping.md`, `validation.md` |
| V008 | Review priority placeholder validation plan | Review `<review-priority>` placeholder. | Review priority is documented. | `configs/ml-anomaly-report-section-mapping.md`, `validation.md` |
| V009 | Recommended investigation placeholder validation plan | Review recommended investigation placeholder. | Investigation guidance is documented for human review. | `configs/ml-anomaly-report-section-mapping.md`, `validation.md` |
| V010 | Evidence reference mapping validation plan | Review `<evidence-reference>` placeholder. | Evidence references are mapped. | `configs/ml-anomaly-report-generation-summary.md`, `validation.md` |
| V011 | Human review note placeholder validation plan | Review human review note placeholder. | Human review note is documented. | `configs/ml-anomaly-report-section-mapping.md`, `validation.md` |
| V012 | Report judgment state validation plan | Apply report judgment states. | Result is classified as `REPORT_READY`, `REPORT_PARTIAL`, `REPORT_INVALID`, `REPORT_INCONCLUSIVE`, or `REPORT_OUT_OF_SCOPE`. | `configs/ml-anomaly-report-judgment-model.md`, `validation.md` |
| V013 | Failure condition for missing detection result, missing dataset reference, missing required report field, missing evidence reference, unsupported security claim, inconclusive report not documented, sensitive data exposure, or missing evidence | Evaluate findings against explicit failure conditions. | Report generation issues produce `FAIL` or `BLOCKED` status. | `validation.md`, `logs/ml-anomaly-report-generation-validation.log`, `screenshots/ml-anomaly-report-validation-result.png` |

Every validation item must map to evidence. This scenario validates human-reviewable anomaly report generation only.
