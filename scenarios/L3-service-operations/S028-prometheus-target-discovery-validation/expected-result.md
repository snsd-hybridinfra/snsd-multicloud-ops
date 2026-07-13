# Expected Result

S028 passes when all artifacts exist, six jobs and discovery targets are defined, JSON samples parse, every required target is `up`, every required query series equals `1`, labels are complete, and safety checks find no concrete/sensitive content.

Static mode makes no query. LivePrometheus passes when all known required jobs are present/healthy, warns when APIs are reachable but the lab lacks placeholder jobs, and fails on API/parse errors or known required jobs that are down/zero.

Only sanitized known-job judgments and timestamps may be generated; URLs, raw endpoints, labels, and responses are never evidence.
