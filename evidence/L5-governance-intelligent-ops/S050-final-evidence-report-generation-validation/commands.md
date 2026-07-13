# Commands

Planned/not-run note: live infrastructure and external reporting remain `NOT_RUN`.

```powershell
powershell -ExecutionPolicy Bypass -File tools/generate-final-evidence-report.ps1
powershell -ExecutionPolicy Bypass -File tools/validate-final-evidence-report.ps1
Get-Content evidence/L5-governance-intelligent-ops/S050-final-evidence-report-generation-validation/configs/final-evidence-report.generated.md
Get-Content evidence/L5-governance-intelligent-ops/S050-final-evidence-report-generation-validation/configs/final-evidence-report-summary.generated.json
Get-Content evidence/L5-governance-intelligent-ops/S050-final-evidence-report-generation-validation/logs/final-evidence-report-generation.log
```

S050 runs no Terraform, kubectl, cloud CLI, monitoring/billing/security query, packet analysis, remediation, or external service. It generates Markdown/JSON only, not PDF/PPTX, and claims no certification or production audit approval.
