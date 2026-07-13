# Failure Condition

The implementation fails on missing sections/mappings/evidence, invalid judgment/JSON, model or packet binaries, prohibited telemetry, real endpoints, secrets, LLM decisions, incident creation, or blocking claims.

S049 fails or is blocked if any of the following occur:

- Anomaly detection result reference is missing.
- Dataset reference is missing.
- Required report field is missing.
- Evidence reference is missing.
- Report output placeholder is missing.
- Inconclusive report state is not documented.
- Human review note is missing.
- Evidence is missing or cannot be mapped to validation checks.
- The scenario claims AI-based intrusion detection, malware detection, packet payload analysis, EDR, SIEM, SOAR, threat hunting, deep-learning-based detection, automatic response, automatic blocking, automated incident resolution, or production-grade ML security operations.
- Real ML output, real dataset records, real report output, credentials, tokens, API keys, secrets, public IPs, cloud account values, private keys, tfstate, kubeconfig, subscription IDs, tenant IDs, billing account IDs, or account-specific values are present.

If a failure is found, stop validation, preserve sanitized notes, and classify the report result as `REPORT_INVALID`, `REPORT_INCONCLUSIVE`, or `REPORT_OUT_OF_SCOPE` as appropriate.
