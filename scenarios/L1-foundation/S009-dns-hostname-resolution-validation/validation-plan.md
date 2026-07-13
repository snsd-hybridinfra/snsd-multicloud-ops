# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Hostname map file | Test the map path. | Map exists. | `logs/dns-hostname-resolution-validation.log`, `configs/dns-hostname-resolution-summary.md` |
| V002 | DNS policy file | Test the policy path. | Policy exists. | `logs/dns-hostname-resolution-validation.log`, `configs/dns-hostname-resolution-summary.md` |
| V003 | Non-production marker | Search the map header. | Explicit marker exists. | `logs/dns-hostname-resolution-validation.log`, `configs/dns-hostname-resolution-summary.md` |
| V004 | Required host aliases | Search for twelve aliases. | Every alias exists. | `logs/dns-hostname-resolution-validation.log`, `configs/dns-hostname-resolution-summary.md` |
| V005 | Required domain placeholders | Search for six domain tokens. | Every domain exists. | `logs/dns-hostname-resolution-validation.log`, `configs/dns-hostname-resolution-summary.md` |
| V006 | Required address placeholders | Search for eight address tokens. | Every address token exists. | `logs/dns-hostname-resolution-validation.log`, `configs/dns-hostname-resolution-summary.md` |
| V007 | Hostname naming convention | Check policy wording. | Naming convention is documented. | `logs/dns-hostname-resolution-validation.log`, `configs/dns-hostname-resolution-summary.md` |
| V008 | Zone separation model | Check policy wording. | Zone/domain separation is documented. | `logs/dns-hostname-resolution-validation.log`, `configs/dns-hostname-resolution-summary.md` |
| V009 | Internal DNS boundary | Check policy wording. | Internal-only public-DNS independence is explicit. | `logs/dns-hostname-resolution-validation.log`, `configs/dns-hostname-resolution-summary.md` |
| V010 | Resolution policy rules | Search for seven operational statements. | Every statement exists. | `logs/dns-hostname-resolution-validation.log`, `configs/dns-hostname-resolution-summary.md` |
| V011 | Numeric IP safety | Scan both model files. | No numeric IP exists. | `logs/dns-hostname-resolution-validation.log`, `configs/dns-hostname-resolution-summary.md` |
| V012 | Sensitive and account content | Scan for assignments, keys, access keys, IDs, UUIDs, and tokens. | No forbidden content exists. | `logs/dns-hostname-resolution-validation.log`, `configs/dns-hostname-resolution-summary.md` |
| V013 | DNS zone export artifacts | Inspect inventory and topology filenames. | No zone or resolver export exists. | `logs/dns-hostname-resolution-validation.log`, `configs/dns-hostname-resolution-summary.md` |
| V014 | Execution safety boundary | Scan validator source for DNS and external commands. | No prohibited command exists. | `logs/dns-hostname-resolution-validation.log`, `configs/dns-hostname-resolution-summary.md` |

## Review Notes

All checks are required and any failure produces a non-zero exit.
