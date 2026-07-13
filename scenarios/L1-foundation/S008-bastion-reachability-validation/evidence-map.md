# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| V001 Reachability map file | `logs/bastion-reachability-validation.log`; `configs/bastion-reachability-summary.md` | generated log and summary | yes |
| V002 SSH access policy file | `logs/bastion-reachability-validation.log`; `configs/bastion-reachability-summary.md` | generated log and summary | yes |
| V003 Required access paths | `logs/bastion-reachability-validation.log`; `configs/bastion-reachability-summary.md` | generated log and summary | yes |
| V004 Required targets | `logs/bastion-reachability-validation.log`; `configs/bastion-reachability-summary.md` | generated log and summary | yes |
| V005 Required address placeholders | `logs/bastion-reachability-validation.log`; `configs/bastion-reachability-summary.md` | generated log and summary | yes |
| V006 Bastion-only administration | `logs/bastion-reachability-validation.log`; `configs/bastion-reachability-summary.md` | generated log and summary | yes |
| V007 Direct public SSH denial | `logs/bastion-reachability-validation.log`; `configs/bastion-reachability-summary.md` | generated log and summary | yes |
| V008 SSH key authentication policy | `logs/bastion-reachability-validation.log`; `configs/bastion-reachability-summary.md` | generated log and summary | yes |
| V009 Password login denial policy | `logs/bastion-reachability-validation.log`; `configs/bastion-reachability-summary.md` | generated log and summary | yes |
| V010 Root login denial policy | `logs/bastion-reachability-validation.log`; `configs/bastion-reachability-summary.md` | generated log and summary | yes |
| V011 Numeric IP safety | `logs/bastion-reachability-validation.log`; `configs/bastion-reachability-summary.md` | generated log and summary | yes |
| V012 Sensitive and account content | `logs/bastion-reachability-validation.log`; `configs/bastion-reachability-summary.md` | generated log and summary | yes |
| V013 Execution safety boundary | `logs/bastion-reachability-validation.log`; `configs/bastion-reachability-summary.md` | generated log and summary | yes |
| Script invocation and evidence inspection | `commands.md` | operator command record | yes |
| Final validation judgment | `validation.md` | validation result | yes |

## Evidence Notes

The log is reproducible. SSH output, reachability output, keys, credentials, routes, DNS results, cloud output, and screenshots are neither required nor permitted.
