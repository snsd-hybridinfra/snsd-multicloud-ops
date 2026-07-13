# Scope

## Included

- Static validation of the drift runbook, command boundaries, criteria, decision matrix, policy, sanitized plan JSON, evidence samples, classification, and manifest.
- Detailed-exit-code interpretation and security/public exposure severity classification.
- Detection-to-remediation mapping to S042 and policy mapping to S043.

## Excluded

- Terraform `init`, `plan`, `apply`, `destroy`, `import`, state commands, remote-state access, and cloud API queries.
- Drift remediation, real provider credentials, tfstate, tfvars, plan binaries, backend configuration, account/resource IDs, real IP/CIDR values, and secrets.
- S042 remediation, S043 Policy as Code, S045 Cost Guardrail, and S046 Resource Cleanup internals.

S041 is static local evidence validation only and makes no production-grade IaC governance or automated-remediation claim.
