# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Reachability map file | Test the map path. | Map exists. | `logs/bastion-reachability-validation.log`, `configs/bastion-reachability-summary.md` |
| V002 | SSH access policy file | Test the policy path. | Policy exists. | `logs/bastion-reachability-validation.log`, `configs/bastion-reachability-summary.md` |
| V003 | Required access paths | Search for seven exact symbolic paths. | Every path exists. | `logs/bastion-reachability-validation.log`, `configs/bastion-reachability-summary.md` |
| V004 | Required targets | Search for eight target aliases. | Every target exists. | `logs/bastion-reachability-validation.log`, `configs/bastion-reachability-summary.md` |
| V005 | Required address placeholders | Search for eight address tokens. | Every token exists. | `logs/bastion-reachability-validation.log`, `configs/bastion-reachability-summary.md` |
| V006 | Bastion-only administration | Check access-policy wording. | Bastion-only model is documented. | `logs/bastion-reachability-validation.log`, `configs/bastion-reachability-summary.md` |
| V007 | Direct public SSH denial | Check access-policy wording. | Direct public SSH is denied. | `logs/bastion-reachability-validation.log`, `configs/bastion-reachability-summary.md` |
| V008 | SSH key authentication policy | Check access-policy wording. | Key authentication is required. | `logs/bastion-reachability-validation.log`, `configs/bastion-reachability-summary.md` |
| V009 | Password login denial policy | Check access-policy wording. | Password login is denied. | `logs/bastion-reachability-validation.log`, `configs/bastion-reachability-summary.md` |
| V010 | Root login denial policy | Check access-policy wording. | Root login is denied. | `logs/bastion-reachability-validation.log`, `configs/bastion-reachability-summary.md` |
| V011 | Numeric IP safety | Scan both model files. | No numeric IP exists. | `logs/bastion-reachability-validation.log`, `configs/bastion-reachability-summary.md` |
| V012 | Sensitive and account content | Scan for assignments, key paths, access keys, account IDs, UUIDs, and tokens. | No forbidden content exists. | `logs/bastion-reachability-validation.log`, `configs/bastion-reachability-summary.md` |
| V013 | Execution safety boundary | Scan validator source for active connection commands. | No prohibited command exists. | `logs/bastion-reachability-validation.log`, `configs/bastion-reachability-summary.md` |

## Review Notes

All checks are required and any failure produces a non-zero exit.
