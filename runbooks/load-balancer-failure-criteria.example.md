# Load Balancer Failure Criteria

| Validation Phase | Evidence Source | Expected Condition | Failure Condition | Operational Judgment | Related Scenario | Evidence Reference |
|---|---|---|---|---|---|---|
| Pre-failure load balancer health | HTTP | 200 | unhealthy | baseline | S035 | pre LB |
| Pre-failure backend health | HTTP | both 200 | backend unhealthy | baseline | S035 | pre backend |
| Manual load balancer failure injection | event | manual | automated | controlled | S035 | injection |
| Load balancer down detection | HTTP/service | 503/refused/timeout/inactive | no signal | detected | S035 | down |
| Client-facing service impact | client | failed/503/timeout | not assessed | impacted | S035 | client impact |
| Backend direct availability during LB failure | HTTP | both 200 | backend failure | isolated | S035 | backend during fault |
| Manual recovery action | event | manual | automated | recovering | S035 | recovery |
| Post-recovery load balancer health | HTTP | 200/restored | unhealthy | recovered | S035 | post LB |
| Post-recovery client-facing service health | HTTP | 200/restored | unhealthy | recovered | S035 | post client |
| Manual bypass / rollback validation | document | bypass and rollback documented | missing | controlled | S035 | bypass sample |
| Recovery time threshold | timing | within threshold | exceeded/missing | review | S035 | summary |
