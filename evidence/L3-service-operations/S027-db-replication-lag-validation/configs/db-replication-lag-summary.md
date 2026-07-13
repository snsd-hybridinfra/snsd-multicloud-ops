# DB Replication Lag Summary

- Scenario: S027-db-replication-lag-validation
- Generated: 2026-07-13T12:24:10+09:00
- Validation mode: **StaticEvidence**
- Required file check result: **PASS**
- Threshold model check result: **PASS**
- Normal lag evidence result: **NORMAL**
- Warning lag evidence result: **WARNING**
- Critical lag evidence result: **EXPECTED_CRITICAL_DETECTED**
- NULL lag evidence result: **EXPECTED_NULL_FAILURE_DETECTED**
- Thread health parsing result: **PASS**
- Error field parsing result: **PASS**
- Secret-safety check result: **PASS**
- Final judgment: **PASS**

| Check ID | Check | Result | Detail |
|---|---|---|---|
| V001 | Required baseline and sample files | PASS | Three baseline artifacts and four lag fixtures exist. |
| V002 | Replication lag threshold model | PASS | Normal, warning, critical, NULL, thread, and error judgments are complete. |
| V003 | Prometheus metric placeholders | PASS | Four metric names and S028/S029 boundaries are documented without a live target. |
| V004 | Normal lag evidence | PASS | Healthy threads and lag in the 0-5 second range were parsed. |
| V005 | Warning lag evidence | WARN | Expected warning fixture was correctly classified in the 6-30 second range. |
| V006 | Critical lag negative fixture | PASS | Lag above 30 seconds was detected and classified as an expected CRITICAL fixture. |
| V007 | NULL lag negative fixture | PASS | NULL lag, unhealthy thread, and symbolic error were detected as an expected failure fixture. |
| V008 | Thread health parsing | PASS | Healthy fixture threads and the negative fixture IO failure were distinguished. |
| V009 | Replication error parsing | PASS | Positive fixtures have empty errors and the negative fixture has only the approved placeholder error. |
| V010 | Replication terminology | PASS | Modern Replica fields are present. |
| V011 | Database credential and connection safety | PASS | No database credential, connection string, or client credential flag exists. |
| V012 | Database dump file safety | PASS | No dump or production SQL export exists; the marked access-control example is excluded. |
| V013 | Observability credential safety | PASS | No Prometheus/Grafana credential or credential-bearing URL exists. |
| V014 | Address and account-specific safety | PASS | No numeric address, account identifier, UUID, or concrete observability URL exists. |
| V015 | Static execution boundary | PASS | No database client, SQL, Prometheus/Grafana query, or destructive replication path is invoked. |
| V016 | Validation mode | PASS | StaticEvidence mode parsed four marked fixtures without database or observability access. |

## Fixture Interpretation

Normal and warning files are positive range fixtures. Critical and NULL files are negative fixtures that must be rejected operationally; detecting those states makes the validator check pass.
