# Validation Result

- Actual Result: Static validation completed with zero critical failures and one expected timing warning.
- Status: PASS

| Check ID | Check Description | Expected Condition | Evidence File | Result |
|---|---|---|---|---|
| V001 | Required artifacts | Complete | samples/summary | PASS |
| V002 | Workflow/placeholders | Complete | runbook/summary | PASS |
| V003 | Manual fault boundary | Manual-only | commands/summary | PASS |
| V004 | Criteria matrix | Complete | criteria/summary | PASS |
| V005 | Pre Pod | Healthy | pre Pod sample | PASS |
| V006 | Pre endpoint | Non-empty | pre endpoint sample | PASS |
| V007 | Pre HTTP | Healthy | pre HTTP sample | PASS |
| V008 | Injection | Manual | injection sample | PASS |
| V009 | Failure detection | Present | detection sample | PASS |
| V010 | Post Pod | Healthy replacement | post Pod sample | PASS |
| V011 | Post endpoint | Non-empty | post endpoint sample | PASS |
| V012 | Post HTTP | Healthy | post HTTP sample | PASS |
| V013 | Rollout | Successful | rollout sample | PASS |
| V014 | Recovered state | No bad indicators | post samples | PASS |
| V015 | Timing | Numeric or review | injection sample | WARN |
| V016 | Sensitive-content safety | No findings | summary | PASS |
| V017 | Execution safety | Read-only | validator | PASS |
| V018 | LiveKubectl | Explicit/read-only | generated log | NOT_RUN |
| V019 | LiveHttp | Explicit/read-only | generated log | NOT_RUN |

Static execution is the committed validation result. Live modes require explicit authorization.
