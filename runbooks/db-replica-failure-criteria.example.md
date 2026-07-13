# DB Replica Failure Criteria

| Failure Validation Phase | Evidence Source | Expected Condition | Failure Condition | Operational Judgment | Related Scenario | Evidence Reference |
|---|---|---|---|---|---|---|
| Pre-failure replica service state | status | active placeholder | inactive | baseline | S033 | pre sample |
| Pre-failure replication thread health | status | IO/SQL Yes | thread No | baseline | S033 | pre sample |
| Pre-failure replication lag | status | within threshold | NULL/excessive | baseline | S033 | pre sample |
| Manual replica failure injection | event | manual marker | automated | controlled fault | S033 | injection sample |
| Replica service failure detection | status | down detected | not detected | detected | S033 | detection sample |
| Replica replication failure detection | status | No/NULL/error | no signal | detected | S033 | detection sample |
| Primary availability during replica failure | primary | reachable/read-write | unavailable | isolated | S033 | primary sample |
| Recovery action placeholder | event | manual marker | automated | recovering | S033 | runbook |
| Post-recovery replica service state | status | active | inactive | recovered | S033 | post sample |
| Post-recovery replication thread health | status | IO/SQL Yes | No | recovered | S033 | post sample |
| Post-recovery replication lag | status | within threshold | NULL/excessive | recovered | S033 | post sample |
| Replication catch-up validation | review | caught up/no error | lag/error | recovered | S033 | catch-up sample |
