# Failure Condition

S047 fails or is blocked if any of the following occur:

- Metric source reference is missing.
- Metric query input is missing.
- Dataset file placeholder is missing.
- Dataset is empty, invalid, or has inconsistent schema.
- Timestamp field is missing or invalid.
- Metric value field is missing.
- Target labels are missing or inconsistent.
- Required dataset fields are not documented.
- Evidence is missing or cannot be mapped to validation checks.
- The scenario claims AI-based intrusion detection, malware detection, packet payload analysis, EDR, SIEM, SOAR, threat hunting, deep-learning-based detection, or production-grade ML security operations.
- Real Prometheus output, real dataset records, credentials, tokens, API keys, secrets, public IPs, cloud account values, private keys, tfstate, kubeconfig, subscription IDs, tenant IDs, billing account IDs, or account-specific values are present.

If a failure is found, stop validation, preserve sanitized notes, and classify the dataset result as `DATASET_INVALID`, `DATASET_EMPTY`, or `DATASET_INCONCLUSIVE` as appropriate.
