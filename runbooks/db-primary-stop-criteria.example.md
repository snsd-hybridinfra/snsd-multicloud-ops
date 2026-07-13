# DB Primary Stop Criteria

| Validation Phase | Evidence Source | Expected Condition | Failure Condition | Operational Judgment | Related Scenario | Evidence Reference |
|---|---|---|---|---|---|---|
| Pre-stop primary service state | primary | active | inactive | baseline | S034 | pre primary |
| Pre-stop primary role confirmation | primary | role available | unknown | baseline | S034 | pre primary |
| Pre-stop replica replication health | replica | threads Yes/lag 0 | unhealthy | baseline | S034 | pre replica |
| Manual primary stop event | event | manual marker | automated | controlled | S034 | stop event |
| Primary service down detection | primary | inactive/refused | not detected | detected | S034 | down sample |
| Application write impact detection | app | unavailable/503 | not assessed | impacted | S034 | write sample |
| Replica state during primary outage | replica | source unavailable/read-only | writable | isolated | S034 | outage replica |
| No automatic replica promotion confirmation | replica | not promoted | promoted | boundary | S034 | outage replica |
| Manual primary recovery action | event | manual marker | automated | recovering | S034 | recovery event |
| Post-recovery primary service state | primary | active | inactive | recovered | S034 | post primary |
| Post-recovery primary role confirmation | primary | restored | missing | recovered | S034 | post primary |
| Post-recovery replication health | replica | threads Yes/lag 0 | unhealthy | recovered | S034 | post replica |
| Replication catch-up validation | review | within threshold/no error | lag/error | recovered | S034 | catch-up |
