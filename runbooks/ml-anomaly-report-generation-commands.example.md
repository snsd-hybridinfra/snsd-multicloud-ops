# ML Anomaly Report Generation Commands — Non-Production

```powershell
powershell -ExecutionPolicy Bypass -File tools/validate-ml-anomaly-report-generation.ps1
```

OPTIONAL MANUAL LOCAL SAMPLE ONLY:

```text
python ml-security/scripts/anomaly-report-generation.example.py --input ml-security/datasets/ml-anomaly-detection-output.sample.csv --metadata ml-security/datasets/ml-anomaly-detection-run-metadata.sample.yml --output ml-security/reports/ml-anomaly-report.sample.md --summary-output ml-security/reports/ml-anomaly-report-summary.sample.json
Get-Content ml-security/reports/ml-anomaly-report.sample.md
Get-Content ml-security/reports/ml-anomaly-report-summary.sample.json
```

The validator does not query Prometheus, Grafana, cloud APIs, SIEM, Wazuh, or EDR; train/deploy a model; call an LLM; create SOC incidents; or perform automated blocking. Outputs are synthetic/sanitized. S050 owns repository-wide reporting.
