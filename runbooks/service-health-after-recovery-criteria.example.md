# Service Health After Recovery Criteria

| Health Domain | Evidence Source | Expected Healthy State | Failure State | Operational Judgment | Related Scenario | Evidence Reference |
|---|---|---|---|---|---|---|
| Web service health | HTTP | 200 | 5xx/timeout | critical | S031 | web sample |
| API service health | HTTP | 200 | 5xx/timeout | critical | S032 | API sample |
| Load balancer health | HTTP | 200 | 5xx/timeout | critical | S035 | LB sample |
| Kubernetes deployment rollout | workload | successful | failed | critical | S031-S032 | workload sample |
| Kubernetes pod readiness | workload | Running Ready 1/1 | unhealthy | critical | S031-S032 | workload sample |
| Kubernetes service endpoints | endpoints | non-empty placeholder | none | critical | S031-S032 | endpoint sample |
| DB primary availability | DB sample | available | unavailable | critical | S034 | DB sample |
| DB replica availability | DB sample | available | unavailable | critical | S033 | DB sample |
| Replication lag | replication | threads Yes/lag 0 | No/NULL/excessive | critical | S033-S034 | replication sample |
| Prometheus target health | targets/up | up/up=1 | down/up=0 | monitoring | S036 | Prometheus sample |
| Blackbox endpoint probe | probe | success=1/status 200 | success=0 | monitoring | S030 | probe sample |
| Alert cleared state | alerts | inactive/resolved | firing | monitoring | S036 | alert sample |
| Backup creation reference | reference | S038/checksum | missing | required | S038 | reference sample |
| Restore execution reference | reference | S039/consistency | missing | required | S039 | reference sample |
| Final recovery summary | summary | PASS/RECOVERED | other | final | S040 | final summary |
