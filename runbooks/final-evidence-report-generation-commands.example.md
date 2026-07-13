# Final Evidence Report Commands — Local Repository Check Only

```powershell
powershell -ExecutionPolicy Bypass -File tools/generate-final-evidence-report.ps1
powershell -ExecutionPolicy Bypass -File tools/validate-final-evidence-report.ps1
powershell -ExecutionPolicy Bypass -File tools/validate-repo-structure.ps1
powershell -ExecutionPolicy Bypass -File tools/validate-scenario-quality.ps1
git status --short
git diff -- docs/
git diff -- evidence/
```

All commands are LOCAL REPOSITORY CHECK ONLY. Scripts do not query live infrastructure, invoke cloud CLIs/kubectl, query Prometheus/Grafana, or generate PDF/PPTX. Outputs are Markdown/JSON only and require no credentials.
