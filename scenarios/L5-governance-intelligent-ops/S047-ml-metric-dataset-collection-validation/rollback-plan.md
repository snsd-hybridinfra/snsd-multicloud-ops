# Rollback Plan

Validation is read-only. Rollback removes unsafe or malformed sample evidence, restores sanitized placeholders, and reruns the validator; it never changes a monitoring system or ML runtime.

This skeleton does not collect real datasets or run ML workflows, so rollback is documentation-focused.

1. Stop validation if credentials, tokens, API keys, secrets, public IPs, cloud account values, private keys, tfstate, kubeconfig content, or account-specific data appear.
2. Remove unsafe evidence and replace it with sanitized placeholders.
3. Mark unsupported AI security claims as blocked or out of scope.
4. Record missing metric source, schema, timestamp, label, or dataset file evidence in `validation.md`.
5. Keep anomaly detection in S048 and anomaly reporting in S049.
6. Do not add SIEM, EDR, SOAR, threat hunting, packet payload analysis, malware detection, or deep learning tooling unless scope changes through an ADR.

No dataset deletion, model rollback, Prometheus configuration rollback, or ML pipeline rollback is performed by this scenario skeleton.
