# Commands

Scenario: S030-blackbox-endpoint-probe-validation
Level: L3-service-operations
Validation mode executed: Static
Live Blackbox validation: NOT_RUN

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-blackbox-endpoint-probe.ps1
```

Optional, explicitly approved live validation:

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-blackbox-endpoint-probe.ps1 -LiveBlackbox -BlackboxExporterUrl "http://<blackbox-exporter-placeholder>:9115" -TargetUrl "http://<endpoint-url-placeholder>"
```

Inspect evidence:

```powershell
Get-Content evidence/L3-service-operations/S030-blackbox-endpoint-probe-validation/logs/blackbox-endpoint-probe-validation.log
Get-Content evidence/L3-service-operations/S030-blackbox-endpoint-probe-validation/configs/blackbox-endpoint-probe-summary.md
```

Manual evidence collection must omit credentials, tokens, cookies, authorization, real URLs/endpoints/domains/addresses, and raw responses. Retain only sanitized probe metrics and placeholder endpoint name.
