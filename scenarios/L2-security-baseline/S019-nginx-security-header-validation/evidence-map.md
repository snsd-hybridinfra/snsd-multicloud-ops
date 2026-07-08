# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Nginx configuration syntax validation plan | `commands.md`; `configs/nginx-security-header-summary.md`; `validation.md` | command plan, header summary, validation record | yes |
| server_tokens off validation plan | `commands.md`; `configs/nginx-security-policy.md`; `validation.md` | command plan, security policy, validation record | yes |
| X-Content-Type-Options header validation plan | `commands.md`; `configs/nginx-security-policy.md`; `validation.md` | command plan, security policy, validation record | yes |
| X-Frame-Options header validation plan | `commands.md`; `configs/nginx-security-policy.md`; `validation.md` | command plan, security policy, validation record | yes |
| Referrer-Policy header validation plan | `commands.md`; `configs/nginx-security-policy.md`; `validation.md` | command plan, security policy, validation record | yes |
| Content-Security-Policy placeholder validation plan | `commands.md`; `configs/nginx-security-policy.md`; `validation.md` | command plan, security policy, validation record | yes |
| HTTP response header capture using curl -I plan | `commands.md`; `logs/nginx-security-header-validation.log`; `screenshots/nginx-security-header-test.png`; `validation.md` | command plan, validation log, screenshot reference, validation record | yes |
| Access log capture plan | `commands.md`; `logs/nginx-security-header-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Error log capture plan | `commands.md`; `logs/nginx-security-header-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Failure condition for missing security header, exposed server version, invalid Nginx configuration, or unexplained response behavior | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real Nginx output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
