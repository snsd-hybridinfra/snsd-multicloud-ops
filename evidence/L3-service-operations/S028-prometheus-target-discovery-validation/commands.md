# Commands

Scenario: S028-prometheus-target-discovery-validation
Level: L3-service-operations
Validation mode executed: Static
Live Prometheus validation: NOT_RUN

## Run Static Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-prometheus-target-discovery.ps1
```

## Optional Live Prometheus Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-prometheus-target-discovery.ps1 -LivePrometheus -PrometheusUrl "http://<prometheus-server-placeholder>"
```

Run only after explicit approval. The validator sends no credentials/cookies/authorization and stores neither the URL nor raw response.

## Inspect Evidence

```powershell
Get-Content evidence/L3-service-operations/S028-prometheus-target-discovery-validation/logs/prometheus-target-discovery-validation.log
Get-Content evidence/L3-service-operations/S028-prometheus-target-discovery-validation/configs/prometheus-target-discovery-summary.md
```

For manual lab collection, save no credentials or real endpoints. Retain only required job names, `health`, and `up` judgments after sanitizing targets, labels, cluster names, and environment identifiers. The generated `.log` is ignored.
