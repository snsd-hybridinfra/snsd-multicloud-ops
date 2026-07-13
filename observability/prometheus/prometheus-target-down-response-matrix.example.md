# Prometheus Target Down Response Matrix

| Signal | Example Evidence | Meaning | Immediate Check | Recovery / Rollback Action | Validation Owner Scenario |
|---|---|---|---|---|---|
| target health up | health up | scrape healthy | up value | none | S036 |
| target health down | health down | scrape failed | last error | inspect exporter | S036 |
| up = 1 | query value 1 | target reachable | target state | none | S036 |
| up = 0 | query value 0 | target unavailable | exporter/path | manual recovery | S036 |
| scrape error | placeholder | scrape failed | error category | investigate | S036 |
| context deadline exceeded | placeholder | timeout | network/exporter | investigate | S036 |
| connection refused | placeholder | listener unavailable | service state | manual start | S036 |
| no route to host placeholder | placeholder | path unavailable | routing | separate runbook | S036 |
| alert firing | firing | sustained target down | target/up | recover | S036 |
| alert resolved | inactive | condition cleared | target/up | close | S036 |
| post-recovery target up | up/value 1 | recovered | timing | complete | S036 |
