# ML Anomaly Detection Commands — Non-Production

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-ml-anomaly-detection.ps1
```

OPTIONAL MANUAL LOCAL SAMPLE ONLY:

```text
python ml-security/scripts/metric-anomaly-detection.example.py --input ml-security/datasets/ml-anomaly-detection-input.sample.csv --output ml-security/datasets/ml-anomaly-detection-output.sample.csv --profile ml-security/models/ml-anomaly-threshold-profile.example.yml
Get-Content ml-security/datasets/ml-anomaly-detection-output.sample.csv | Select-Object -First 10
Import-Csv ml-security/datasets/ml-anomaly-detection-output.sample.csv | Where-Object { $_.anomaly_decision -eq "ANOMALY_DETECTED" }
```

The validation script does not query Prometheus, Grafana, cloud APIs, SIEM, Wazuh, or EDR; does not train or deploy a model; and performs no automated blocking. Output must be synthetic or sanitized. S049 owns the human-readable anomaly report.
