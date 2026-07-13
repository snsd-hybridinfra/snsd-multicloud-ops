# Failure Condition

S028 fails if:

- A baseline/config/matrix/command/sample is missing.
- A required job/target/Kubernetes discovery field is absent.
- Targets or up evidence is invalid JSON, missing a job, down, or zero.
- A job label is missing from the sanitized label sample.
- Basic auth, bearer token, authorization config, TLS material/path, credential, token, cookie, account ID, UUID, real URL/domain/address, or Kubernetes endpoint is detected.
- Static mode invokes curl/Prometheus/network or includes a reload path.
- LivePrometheus lacks a valid URL, cannot parse/query APIs, or finds a known required job down/zero.

A reachable live lab missing placeholder jobs is WARN, not a claim of successful full implementation.
