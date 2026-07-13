# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| V001 Hostname map file | `logs/dns-hostname-resolution-validation.log`; `configs/dns-hostname-resolution-summary.md` | generated log and summary | yes |
| V002 DNS policy file | `logs/dns-hostname-resolution-validation.log`; `configs/dns-hostname-resolution-summary.md` | generated log and summary | yes |
| V003 Non-production marker | `logs/dns-hostname-resolution-validation.log`; `configs/dns-hostname-resolution-summary.md` | generated log and summary | yes |
| V004 Required host aliases | `logs/dns-hostname-resolution-validation.log`; `configs/dns-hostname-resolution-summary.md` | generated log and summary | yes |
| V005 Required domain placeholders | `logs/dns-hostname-resolution-validation.log`; `configs/dns-hostname-resolution-summary.md` | generated log and summary | yes |
| V006 Required address placeholders | `logs/dns-hostname-resolution-validation.log`; `configs/dns-hostname-resolution-summary.md` | generated log and summary | yes |
| V007 Hostname naming convention | `logs/dns-hostname-resolution-validation.log`; `configs/dns-hostname-resolution-summary.md` | generated log and summary | yes |
| V008 Zone separation model | `logs/dns-hostname-resolution-validation.log`; `configs/dns-hostname-resolution-summary.md` | generated log and summary | yes |
| V009 Internal DNS boundary | `logs/dns-hostname-resolution-validation.log`; `configs/dns-hostname-resolution-summary.md` | generated log and summary | yes |
| V010 Resolution policy rules | `logs/dns-hostname-resolution-validation.log`; `configs/dns-hostname-resolution-summary.md` | generated log and summary | yes |
| V011 Numeric IP safety | `logs/dns-hostname-resolution-validation.log`; `configs/dns-hostname-resolution-summary.md` | generated log and summary | yes |
| V012 Sensitive and account content | `logs/dns-hostname-resolution-validation.log`; `configs/dns-hostname-resolution-summary.md` | generated log and summary | yes |
| V013 DNS zone export artifacts | `logs/dns-hostname-resolution-validation.log`; `configs/dns-hostname-resolution-summary.md` | generated log and summary | yes |
| V014 Execution safety boundary | `logs/dns-hostname-resolution-validation.log`; `configs/dns-hostname-resolution-summary.md` | generated log and summary | yes |
| Script invocation and evidence inspection | `commands.md` | operator command record | yes |
| Final validation judgment | `validation.md` | validation result | yes |

## Evidence Notes

The log is reproducible. Resolver output, live DNS records, zones, credentials, host data, cloud output, and screenshots are neither required nor permitted.
