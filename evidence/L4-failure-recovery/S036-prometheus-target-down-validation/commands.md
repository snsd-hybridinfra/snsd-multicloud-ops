# Commands

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-prometheus-target-down.ps1
powershell -ExecutionPolicy Bypass -File tools/validate-prometheus-target-down.ps1 -LivePrometheus -PrometheusUrl "http://<prometheus-server-placeholder>"
powershell -ExecutionPolicy Bypass -File tools/validate-prometheus-target-down.ps1 -LivePrometheus -PrometheusUrl "http://<prometheus-server-placeholder>" -ExpectedJob "<scrape-job-name-placeholder>" -ExpectDown
Get-Content evidence/L4-failure-recovery/S036-prometheus-target-down-validation/logs/prometheus-target-down-validation.log
Get-Content evidence/L4-failure-recovery/S036-prometheus-target-down-validation/configs/prometheus-target-down-summary.md
```

LivePrometheus and exporter actions are `NOT_RUN` in committed evidence. Exporter stop/start are manual fault/recovery references only and never validator-executed.
