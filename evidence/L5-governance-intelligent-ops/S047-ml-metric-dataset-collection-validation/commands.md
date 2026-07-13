# Commands

Planned/not-run output note: live collection, security telemetry ingestion, and model training remain `NOT_RUN`; only the implemented static validator is executed.

Run static evidence validation:

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-ml-metric-dataset-collection.ps1
```

Inspect generated output:

```powershell
Get-Content evidence/L5-governance-intelligent-ops/S047-ml-metric-dataset-collection-validation/logs/ml-metric-dataset-collection-validation.log
Get-Content evidence/L5-governance-intelligent-ops/S047-ml-metric-dataset-collection-validation/configs/ml-metric-dataset-collection-validation-summary.md
```

Sanitized evidence from a disposable lab may be collected manually using the examples in `runbooks/ml-metric-dataset-collection-commands.example.md`, then scrubbed before review. The validator never queries Prometheus, Grafana, cloud APIs, SIEM, Wazuh, or EDR. Do not commit raw logs, packet payloads, PCAP files, production metrics, credentials, or production identifiers. S047 does not train a model; S048 owns anomaly detection and S049 owns anomaly reporting.
