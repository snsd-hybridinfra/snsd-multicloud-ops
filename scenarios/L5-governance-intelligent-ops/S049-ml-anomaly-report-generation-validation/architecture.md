# Architecture

Implemented flow: S047/S048 references -> deterministic report template and JSON summary -> local validator -> S050 handoff.

S049 models anomaly report generation as a placeholder evidence workflow.

## Components

- Dataset file placeholder: `<dataset-file>`.
- Report file placeholder: `<report-file>`.
- Metric name placeholder: `<metric-name>`.
- Target job placeholder: `<target-job>`.
- Target instance placeholder: `<target-instance>`.
- Anomaly score placeholder: `<anomaly-score>`.
- Anomaly threshold placeholder: `<anomaly-threshold>`.
- Review priority placeholder: `<review-priority>`.
- Evidence reference placeholder: `<evidence-reference>`.
- Evidence directory: `evidence/L5-governance-intelligent-ops/S049-ml-anomaly-report-generation-validation/`.

## Flow

1. Reference S048 anomaly detection output.
2. Reference S047 dataset input.
3. Define report input schema and required fields.
4. Map report summary, affected component, metric detail, priority, investigation, evidence, and human review sections.
5. Document report output file placeholder.
6. Classify report completeness using the Report Judgment Model.
7. Capture TODO evidence references in commands, validation notes, configs, logs, and screenshots.

This architecture does not generate production reports, automate incident response, or integrate with SIEM, EDR, SOAR, or commercial security tooling.
