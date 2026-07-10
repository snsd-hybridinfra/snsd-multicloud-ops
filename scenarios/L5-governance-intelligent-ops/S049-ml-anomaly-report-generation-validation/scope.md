# Scope

## Included

- Anomaly detection result input validation reference.
- Report generation input schema placeholder.
- Report summary section definition.
- Affected component section definition.
- Metric anomaly detail section definition.
- Severity or review priority placeholder.
- Human review note section.
- Recommended investigation placeholder.
- Evidence reference mapping.
- Report output file placeholder.
- Report completeness validation plan.

## Target Report Sections

- Report title.
- Report generation timestamp.
- Detection scenario reference.
- Dataset reference.
- Affected provider or zone placeholder.
- Affected component type placeholder.
- Target job and target instance.
- Metric name.
- Observed metric value.
- Baseline or threshold reference.
- Anomaly judgment result.
- Review priority placeholder.
- Recommended investigation placeholder.
- Evidence links or file references.
- Human review note placeholder.

## Required Report Fields

- `report_id` placeholder
- `generated_at`
- `scenario_id`
- `dataset_reference`
- `detection_reference`
- `affected_component`
- `provider_or_zone` placeholder
- `metric_name`
- `observed_value`
- `baseline_or_threshold`
- `anomaly_judgment`
- `review_priority`
- `recommended_investigation`
- `evidence_reference`
- `human_review_note`

## Report Judgment Model

- `REPORT_READY`: Required report sections and evidence references are present.
- `REPORT_PARTIAL`: Report exists but some optional sections are incomplete.
- `REPORT_INVALID`: Report structure or required fields are missing.
- `REPORT_INCONCLUSIVE`: Detection result or dataset evidence is insufficient.
- `REPORT_OUT_OF_SCOPE`: Report requires SIEM, EDR, packet, log, malware, or threat hunting analysis.

## Excluded

- Production ML reporting.
- Deep learning.
- Real ML output, real dataset records, or real report output in this skeleton.
- AI-based intrusion detection, malware detection, packet payload analysis, EDR, SIEM, SOAR, threat hunting capability, automatic response, automatic blocking, automated incident resolution, or production-grade ML security operations.
- SIEM, Wazuh, Elastic, EDR, SOAR, threat hunting, packet payload analysis, malware detection, commercial security tooling, or new technologies.
- Real public IPs, cloud account IDs, credentials, tokens, API keys, secrets, private keys, tfstate, kubeconfig, subscription IDs, tenant IDs, billing account IDs, or account-specific values.
- ML metric dataset collection, handled in S047.
- ML anomaly detection validation, handled in S048.
- Final evidence report generation, handled in S050.
- Prometheus target discovery validation, handled in S028.
- Grafana dashboard validation, handled in S029.
- Blackbox endpoint probe validation, handled in S030.
