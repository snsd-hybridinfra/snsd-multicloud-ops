# Evidence Map

| Validation Check | Evidence |
|---|---|
| V001 Required artifacts | Runbooks, rules, criteria, decision matrices, policy, inputs, samples, and generated validator log |
| V002 Command boundary | `runbooks/resource-cleanup-commands.example.md` |
| V003 Rules | `cost-governance/resource-cleanup-rules.example.yml` |
| V004 Example inputs | `cost-governance/resource-cleanup-input-*.example.json` |
| V005 Rule load and inventory | `logs/cleanup-rule-load.sample.txt`, `logs/cleanup-candidate-inventory.sample.txt` |
| V006 Cleanup ready | `logs/cleanup-evaluation-ready.sample.txt` |
| V007 Cleanup blocked | `logs/cleanup-evaluation-blocked.sample.txt` |
| V008 Exception | `logs/cleanup-exception-approval.sample.txt` |
| V009 Impact | `logs/cleanup-impact-classification.sample.txt` |
| V010 Cleanup plan | `logs/cleanup-plan.sample.txt` |
| V011 Final summary | `logs/cleanup-final-summary.sample.txt` |
| V012 Manifest mappings | `configs/resource-cleanup-validation-manifest.sample.yml` |
| V013 Policy | `policy/resource-cleanup-policy.example.md` |
| V014 Artifact safety | `logs/resource-cleanup-validation.log` |
| V015 Sensitive/execution safety | `logs/resource-cleanup-validation.log` |
| V016 Maturity | `configs/resource-cleanup-validation-summary.md` |

Generated evidence contains no live inventory or deletion output. Screenshots are not required for this static validation.
