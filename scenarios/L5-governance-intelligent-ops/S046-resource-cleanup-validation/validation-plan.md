# Validation Plan

| Check ID | Validation Item | Expected Result | Evidence |
|---|---|---|---|
| V001 | Required artifacts | All runbook, policy, rules, inputs, samples, and manifest exist. | `logs/resource-cleanup-validation.log` |
| V002 | Command boundary | Inventory is manual-only; deletion commands are `OUT OF SCOPE`. | `runbooks/resource-cleanup-commands.example.md` |
| V003 | Rules | Judgment states, exception fields, and cleanup domains are present. | `cost-governance/resource-cleanup-rules.example.yml` |
| V004 | Example inputs | Ready, blocked, and exception inputs have consistent expected judgments. | `cost-governance/resource-cleanup-input-*.example.json` |
| V005 | Rule load and inventory | Sanitized rule and candidate metadata are present. | `logs/cleanup-rule-load.sample.txt`, `logs/cleanup-candidate-inventory.sample.txt` |
| V006 | Cleanup ready | Ownership, retention, low risk, and S045 mapping are present. | `logs/cleanup-evaluation-ready.sample.txt` |
| V007 | Cleanup blocked | Blocking reasons are explicit. | `logs/cleanup-evaluation-blocked.sample.txt` |
| V008 | Exception | Required approved-exception fields are present. | `logs/cleanup-exception-approval.sample.txt` |
| V009 | Impact | Impact classification is complete. | `logs/cleanup-impact-classification.sample.txt` |
| V010 | Cleanup plan | A plan exists and confirms no deletion by the validator. | `logs/cleanup-plan.sample.txt` |
| V011 | Final summary | Rules are validated and no live operation occurred. | `logs/cleanup-final-summary.sample.txt` |
| V012 | Manifest mappings | S041, S042, S043, S045, and S050 mappings exist. | `configs/resource-cleanup-validation-manifest.sample.yml` |
| V013 | Policy | Ownership, retention, cost, dependency, rollback, approval, and deletion boundaries exist. | `policy/resource-cleanup-policy.example.md` |
| V014 | Artifact safety | State, tfvars, `.terraform`, and kubeconfig are absent. | `logs/resource-cleanup-validation.log` |
| V015 | Sensitive/execution safety | No real identifier, network, credential, key, CLI execution, or deletion occurs. | `logs/resource-cleanup-validation.log` |
| V016 | Maturity | Placeholder-only governance maturity is explicitly warned. | `configs/resource-cleanup-validation-summary.md` |

All checks are implemented by `tools/validate-resource-cleanup.ps1` in `StaticEvidence` mode.
