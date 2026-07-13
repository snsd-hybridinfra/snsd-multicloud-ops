# Commands

Planned/not-run note: live collection, training, deployment, and blocking remain `NOT_RUN`.

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-ml-anomaly-detection.ps1
Get-Content evidence/L5-governance-intelligent-ops/S048-ml-anomaly-detection-validation/logs/ml-anomaly-detection-validation.log
Get-Content evidence/L5-governance-intelligent-ops/S048-ml-anomaly-detection-validation/configs/ml-anomaly-detection-validation-summary.md
```

The optional local Python command is documented in the runbook and uses sanitized samples only. No Prometheus, Grafana, cloud, SIEM, Wazuh, EDR, raw log, packet, credential, production identifier, training/deployment, or automated blocking activity is allowed. S049 owns reporting.
