# Service Health After Recovery Decision Matrix

| Signal | Healthy Evidence | Degraded Evidence | Failed Evidence | Required Action | Final Judgment |
|---|---|---|---|---|---|
| Web HTTP status | 200 | slow placeholder | 5xx/unavailable | investigate | RECOVERED/FAILED |
| API HTTP status | 200 | warning placeholder | 5xx/unavailable | investigate | RECOVERED/FAILED |
| Load balancer HTTP status | 200 | partial placeholder | 5xx/unavailable | investigate | RECOVERED/FAILED |
| Pod readiness | Running 1/1 | restart warning | 0/1/unhealthy | investigate | RECOVERED/FAILED |
| Service endpoint availability | placeholder endpoint | reduced placeholder | none | investigate | RECOVERED/FAILED |
| DB primary status | available | warning placeholder | unavailable | investigate | RECOVERED/FAILED |
| DB replica status | available | lag warning | unavailable | investigate | RECOVERED/FAILED |
| Replication lag | 0/within threshold | elevated | NULL/excessive | investigate | RECOVERED/FAILED |
| Prometheus up metric | 1 | unrelated target warning | 0 | investigate | RECOVERED/DEGRADED/FAILED |
| Blackbox probe_success | 1 | duration warning | 0 | investigate | RECOVERED/DEGRADED/FAILED |

Judgment rules: `RECOVERED` only when all critical domains are healthy; `DEGRADED` for a non-critical warning with user-facing health; `FAILED` for unhealthy Web/API/LB/DB critical evidence; `INCOMPLETE` when S038/S039 evidence is missing; `REVIEW_REQUIRED` for internally consistent placeholder-only unresolved risk.
