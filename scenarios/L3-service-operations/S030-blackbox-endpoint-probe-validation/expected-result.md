# Expected Result

S030 passes when modules/scrape/matrix/metrics are complete, healthy evidence is normal, warning evidence is warned, failure evidence is rejected, query JSON is healthy, and safety checks find no concrete/sensitive content.

Static mode makes no query. LiveBlackbox passes for `probe_success=1` and HTTP 200/204, warns for exporter 401/403, and fails for invalid/unreachable URLs, exporter 5xx, unacceptable responses, timeout, or failed metrics.

One expected warning from the warning-duration fixture is acceptable.
