# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Nginx service status validation plan | `commands.md`; `logs/nginx-reverse-proxy-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Nginx configuration syntax validation plan using nginx -t | `commands.md`; `configs/nginx-reverse-proxy-summary.md`; `validation.md` | command plan, proxy summary, validation record | yes |
| AWS reverse proxy endpoint response validation plan | `commands.md`; `logs/nginx-reverse-proxy-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Azure reverse proxy endpoint response validation plan | `commands.md`; `logs/nginx-reverse-proxy-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| OpenStack reverse proxy endpoint response validation plan | `commands.md`; `logs/nginx-reverse-proxy-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Reverse proxy upstream mapping validation plan | `commands.md`; `configs/nginx-upstream-mapping.md`; `validation.md` | command plan, upstream mapping, validation record | yes |
| Reverse proxy to Ingress forwarding validation plan | `commands.md`; `configs/nginx-upstream-mapping.md`; `validation.md` | command plan, upstream mapping, validation record | yes |
| HTTP 200 response validation plan | `commands.md`; `logs/nginx-reverse-proxy-validation.log`; `screenshots/nginx-reverse-proxy-test.png`; `validation.md` | command plan, validation log, screenshot reference, validation record | yes |
| Access log capture plan | `commands.md`; `logs/nginx-reverse-proxy-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Error log capture plan | `commands.md`; `logs/nginx-reverse-proxy-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Failure condition for Nginx down, invalid config, wrong upstream, route timeout, HTTP 5xx, or missing access/error logs | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real Nginx reverse proxy output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
