# Validation Plan

| Check ID | Validation Item | Method | Expected Result | Evidence |
|---|---|---|---|---|
| V001 | Required probe baseline files | Test five paths. | All exist. | commands; summary |
| V002 | Blackbox module definitions | Match HTTP/TCP settings. | Complete. | exporter config; summary |
| V003 | Prometheus Blackbox scrape placeholder | Match probe/relabel fields. | Complete. | scrape config; summary |
| V004 | Probe metrics and threshold model | Match metrics/ranges. | Complete. | baseline/matrix; summary |
| V005 | Probe rule matrix | Match nine areas. | Complete. | matrix; summary |
| V006 | Probe command reference | Match four examples. | Complete. | command example; summary |
| V007 | Required probe samples | Test four paths. | All exist. | samples; summary |
| V008 | Healthy probe evidence | Success=1, status accepted, duration <=2. | Healthy. | success sample; summary |
| V009 | Warning duration evidence | Success=1, duration >2..5. | Expected WARN. | warning sample; summary |
| V010 | Failure negative fixture | Detect success=0/status0/timeout. | Expected failure detected. | failure sample; summary |
| V011 | Prometheus probe query sample | Parse three healthy metrics. | Valid. | query sample; summary |
| V012 | Credential token cookie and TLS safety | Scan sensitive config/content. | None. | log; summary |
| V013 | Endpoint URL address and domain safety | Scan concrete targets. | None. | log; summary |
| V014 | Account and identifier safety | Scan IDs/UUIDs. | None. | log; summary |
| V015 | Execution safety boundary | Reject clients/reload; guard live. | Safe. | script; summary |
| V016 | Validation mode and live probe result | Evaluate Static/live. | Safe/pass/auth warn. | log; summary |
