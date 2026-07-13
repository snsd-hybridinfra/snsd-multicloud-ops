# Evidence Map

| Check ID | Validation Item | Evidence File | Required |
|---|---|---|---|
| V001 | Security header baseline | `logs/nginx-security-header-validation.log`; `configs/nginx-security-header-summary.md` | yes |
| V002 | Security header rule matrix | same generated evidence | yes |
| V003 | Nginx example config | same generated evidence | yes |
| V004 | Server token reduction | same generated evidence | yes |
| V005 | Required security headers | same generated evidence | yes |
| V006 | Required header values | same generated evidence | yes |
| V007 | Always directive | same generated evidence | yes |
| V008 | Baseline and matrix completeness | same generated evidence | yes |
| V009 | TLS material safety | same generated evidence | yes |
| V010 | Address and domain safety | same generated evidence | yes |
| V011 | Credential and account safety | same generated evidence | yes |
| V012 | Execution safety boundary | same generated evidence | yes |

`commands.md` documents execution and `validation.md` records final results. The generated log is ignored; the sanitized summary is tracked.
