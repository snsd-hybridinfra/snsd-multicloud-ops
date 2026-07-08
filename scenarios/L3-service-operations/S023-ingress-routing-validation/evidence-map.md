# Evidence Map

| Validation Item | Evidence File | Evidence Type | Required |
|---|---|---|---|
| Ingress Controller pod readiness validation plan | `commands.md`; `configs/ingress-routing-summary.md`; `validation.md` | command plan, routing summary, validation record | yes |
| Ingress resource existence validation plan | `commands.md`; `configs/ingress-routing-summary.md`; `validation.md` | command plan, routing summary, validation record | yes |
| Web route backend mapping validation plan | `commands.md`; `configs/ingress-backend-mapping.md`; `validation.md` | command plan, backend mapping, validation record | yes |
| API route backend mapping validation plan | `commands.md`; `configs/ingress-backend-mapping.md`; `validation.md` | command plan, backend mapping, validation record | yes |
| Host-based routing validation plan | `commands.md`; `logs/ingress-routing-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Path-based routing validation plan | `commands.md`; `logs/ingress-routing-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| HTTP 200 response validation plan | `commands.md`; `logs/ingress-routing-validation.log`; `screenshots/ingress-routing-test.png`; `validation.md` | command plan, validation log, screenshot reference, validation record | yes |
| Invalid path response validation plan | `commands.md`; `logs/ingress-routing-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Ingress event capture plan | `commands.md`; `logs/ingress-routing-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Ingress controller log capture plan | `commands.md`; `logs/ingress-routing-validation.log`; `validation.md` | command plan, validation log, validation record | yes |
| Failure condition for missing ingress controller, missing ingress resource, wrong backend service, route timeout, HTTP 5xx, or unresolved hostname | `validation.md` | failure criteria and status record | yes |

## Evidence Notes

No real ingress routing output has been collected yet. Use TODO placeholders until execution is approved and outputs are sanitized.
