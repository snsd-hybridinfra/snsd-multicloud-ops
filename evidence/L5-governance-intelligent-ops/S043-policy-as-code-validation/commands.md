# Commands

Run `powershell -ExecutionPolicy Bypass -File tools/validate-policy-as-code.ps1`, then inspect `logs/policy-as-code-validation.log` and `configs/policy-as-code-validation-summary.md`.

Disposable-lab evidence must be sanitized manually. The validator does not run Terraform, OPA, Conftest, cloud CLIs/APIs, or enforcement. OPA/Conftest examples are optional. Do not commit state, tfvars, plan binaries, backend values, credentials, or identifiers. S044 owns manifest policy and S045 cost guardrails. Live execution: `NOT_RUN`.
