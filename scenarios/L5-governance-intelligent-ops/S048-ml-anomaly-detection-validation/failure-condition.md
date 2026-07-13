# Failure Condition

The implementation fails on missing/short/malformed datasets, invalid scores or decisions, absent S047/S049/S050 mappings, model binaries, prohibited telemetry, real endpoints, secrets, or claims of live execution/training/deployment/blocking.

S048 fails or is blocked if any of the following occur:

- Dataset input reference is missing.
- Dataset schema is invalid or not ready.
- Baseline window is missing.
- Detection window is missing.
- Threshold or anomaly score placeholder is missing.
- Inconclusive result is not documented.
- Human review note is missing.
- Evidence is missing or cannot be mapped to validation checks.
- The scenario claims AI-based intrusion detection, malware detection, packet payload analysis, EDR, SIEM, SOAR, threat hunting, deep-learning-based detection, automatic response, automatic blocking, or production-grade ML security operations.
- Real ML output, real dataset records, credentials, tokens, API keys, secrets, public IPs, cloud account values, private keys, tfstate, kubeconfig, subscription IDs, tenant IDs, billing account IDs, or account-specific values are present.

If a failure is found, stop validation, preserve sanitized notes, and classify the anomaly result as `ANOMALY_INCONCLUSIVE` or `ANOMALY_OUT_OF_SCOPE` as appropriate.
