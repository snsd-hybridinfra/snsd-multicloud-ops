# ML Metric Dataset Collection Commands — Non-Production Examples

Run static validation:

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-ml-metric-dataset-collection.ps1
```

MANUAL DISPOSABLE LAB EXAMPLE ONLY; never run from the validator:

```text
curl "http://<prometheus-server-placeholder>/api/v1/query_range?query=<metric-query-placeholder>&start=<start-placeholder>&end=<end-placeholder>&step=<step-placeholder>"
```

OPTIONAL MANUAL LAB EXAMPLE ONLY:

```text
python <script-placeholder> --input <prometheus-export-placeholder> --output <dataset-file-placeholder>
Get-Content <dataset-file-placeholder> | Select-Object -First 5
Import-Csv <dataset-file-placeholder> | Select-Object -First 5
```

The validation script does not query Prometheus, Grafana, cloud APIs, SIEM, Wazuh, or EDR and does not train a model. Production metrics, raw logs, packet payloads, PCAP data, credentials, and production identifiers must not be committed. Only sanitized or synthetic metric datasets are allowed.
