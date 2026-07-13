# Cost Guardrail Commands — Examples Only

Run `powershell -ExecutionPolicy Bypass -File tools/validate-cost-guardrail.ps1`; safe local reviews include `git diff -- terraform/`, `git diff -- cost-governance/`, and `git diff -- policy/`.

`terraform plan -detailed-exitcode` and `terraform show -json <plan-file-placeholder>` are MANUAL LAB EVIDENCE CONVERSION ONLY. `<cloud-cost-estimate-command-placeholder>` and `<billing-export-review-command-placeholder>` are PLACEHOLDER ONLY.

The validator does not run Terraform, query billing/cloud APIs, or require an external cost tool. Real billing data and production financial reports are OUT OF SCOPE and must not be committed.
