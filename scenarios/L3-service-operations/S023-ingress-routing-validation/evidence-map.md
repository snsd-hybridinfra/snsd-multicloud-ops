# Evidence Map

| Check ID | Validation Item | Evidence File | Required |
|---|---|---|---|
| V001 | Ingress documentation | `logs/ingress-routing-validation.log`; `configs/ingress-routing-summary.md` | yes |
| V002 | Ingress example files | files; generated evidence | yes |
| V003 | Ingress sample evidence | three samples; generated evidence | yes |
| V004 | Required command examples | generated evidence | yes |
| V005 | Routing model and placeholders | generated evidence | yes |
| V006 | Ingress object and scope | manifest; generated evidence | yes |
| V007 | Host and path routing | manifest; generated evidence | yes |
| V008 | Backend Service reference | Ingress/Service; generated evidence | yes |
| V009 | Ingress and TLS safety | generated evidence | yes |
| V010 | Ingress list evidence | sample or sanitized live judgment | yes |
| V011 | Ingress backend evidence | sample or sanitized live judgment | yes |
| V012 | Endpoint evidence | sample or sanitized live judgment | yes |
| V013 | Ingress address awareness | generated evidence | yes |
| V014 | Kubernetes/TLS credential files | generated evidence | yes |
| V015 | Routing content safety | generated evidence | yes |
| V016 | Execution safety boundary | generated evidence | yes |
| V017 | Validation mode | generated evidence | yes |

`commands.md` documents both modes and the manual-only curl example. Raw live resource rows are not repository evidence.
