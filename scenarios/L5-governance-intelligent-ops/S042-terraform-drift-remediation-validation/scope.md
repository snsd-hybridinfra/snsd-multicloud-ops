# Scope

## Included

- Static validation of the remediation runbook, command boundaries, criteria, decision matrix, policy, JSON examples, S041 reference, decision, approval, plan, rollback, post-remediation sample, and manifest.
- Approved options: `REVERT_TO_TERRAFORM`, `CODIFY_APPROVED_CHANGE`, `INVESTIGATE_ONLY`, `REJECT_CHANGE`, and controlled documented exception.
- S043 policy and S045 cost mappings.

## Excluded

- Terraform `init`, `plan`, `apply`, `destroy`, `import`, state commands, remote-state access, provider/cloud API calls, real or automatic remediation.
- tfstate, tfvars, plan binaries, backend configuration, credentials, account/resource identifiers, real IP/CIDR values, and secrets.
- S041 detection internals, S043 Policy as Code, S045 Cost Guardrail, and S046 Resource Cleanup internals.

S042 is static local evidence validation and does not claim remediation was executed.
