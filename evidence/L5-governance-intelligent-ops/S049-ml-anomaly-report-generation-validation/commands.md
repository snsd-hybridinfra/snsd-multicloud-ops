# Commands

Planned/not-run note: live collection, model operations, LLM analysis, incident creation, and blocking remain `NOT_RUN`.

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-ml-anomaly-report-generation.ps1
Get-Content evidence/L5-governance-intelligent-ops/S049-ml-anomaly-report-generation-validation/logs/ml-anomaly-report-generation-validation.log
Get-Content evidence/L5-governance-intelligent-ops/S049-ml-anomaly-report-generation-validation/configs/ml-anomaly-report-generation-validation-summary.md
```

Optional deterministic Python reporting is documented in the runbook. No live/cloud/security telemetry, raw data, credentials, production identifiers, model/LLM operations, blocking, or incident automation is allowed. S050 owns final reporting.
