# Rollback Plan

Validation is read-only; rollback removes unsafe output, restores sanitized templates, and reruns the validator.

This skeleton does not generate real reports or automate response workflows, so rollback is documentation-focused.

1. Stop validation if credentials, tokens, API keys, secrets, public IPs, cloud account values, private keys, tfstate, kubeconfig content, real report output, or account-specific data appear.
2. Remove unsafe evidence and replace it with sanitized placeholders.
3. Mark unsupported AI security, SIEM, EDR, SOAR, deep learning, automatic response, blocking, or incident-resolution claims as out of scope.
4. Record missing detection result, dataset reference, report field, evidence reference, or human review note in `validation.md`.
5. Keep dataset collection in S047, anomaly detection in S048, and final evidence reporting in S050.
6. Do not add production ML reporting, SIEM, EDR, SOAR, threat hunting, packet payload analysis, malware detection, or commercial security tooling unless scope changes through an ADR.

No report deletion, model rollback, response rollback, or security tooling rollback is performed by this scenario skeleton.
