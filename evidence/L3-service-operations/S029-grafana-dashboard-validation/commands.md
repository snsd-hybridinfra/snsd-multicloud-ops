# Commands

Scenario: S029-grafana-dashboard-validation
Level: L3-service-operations
Validation mode executed: Static
Live Grafana validation: NOT_RUN

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-grafana-dashboard.ps1
```

Optional, explicitly approved live validation:

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-grafana-dashboard.ps1 -LiveGrafana -GrafanaUrl "http://<grafana-server-placeholder>"
```

Inspect generated evidence:

```powershell
Get-Content evidence/L3-service-operations/S029-grafana-dashboard-validation/logs/grafana-dashboard-validation.log
Get-Content evidence/L3-service-operations/S029-grafana-dashboard-validation/configs/grafana-dashboard-summary.md
```

Manual lab evidence must omit credentials, tokens, cookies, authorization, URLs, UIDs, IDs, and datasource secrets. Retain only sanitized title, panel titles/count, and datasource name/type. The validator never imports or mutates dashboards.
