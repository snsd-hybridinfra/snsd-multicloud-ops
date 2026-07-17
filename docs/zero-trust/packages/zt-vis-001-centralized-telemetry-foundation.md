# ZT-VIS-001 Centralized Telemetry and Security Event Correlation Foundation

## Purpose, scope, and status

ZT-VIS-001 centralizes selected sanitized validator and repository-validation
summaries into one local JSONL event model and applies deterministic correlation.
It is IMPLEMENTED and PARTIALLY_VALIDATED. Current maturity is UNASSESSED and
the bounded target is INITIAL.

The package maps conservatively to ZT-7.1, ZT-7.2, ZT-7.3, ZT-8.2, and ZT-8.6.
ZT-7.4 is excluded because no user/device behavior analysis exists.

## Current-state audit and architecture decision

Prometheus and Grafana artifacts are configuration examples only. No running
Prometheus, Grafana, Loki, Promtail, Alloy, Elasticsearch, OpenSearch, Logstash,
Filebeat, Fluent Bit, or central syslog service was evidenced. Host capacity
also requires staged VM execution.

The selected architecture is therefore a repository-controlled local JSONL
pipeline over the existing restricted validators. Loki/Alloy/Grafana is the
future user-installed candidate for persistent centralized storage and
dashboarding. Multiple competing stacks, Wazuh, and commercial SIEM products
were rejected.

~~~mermaid
flowchart LR
  O["OpenStack validator"] --> C["Local collector"]
  E["EVE validator"] --> C
  R["Router validator"] --> C
  G["Repository validator"] --> C
  C --> J["Ignored sanitized runtime JSONL"]
~~~

## Event and correlation model

The event schema distinguishes event time from ingestion time, preserves source
type, uses normalized severity, permits null values, and never invents actor
identity. Sensitive dynamic identifiers are redacted before normalization.

~~~mermaid
flowchart LR
  S["Sanitized summaries"] --> N["Normalizer"]
  N --> V["Schema checks"]
  V --> J["JSONL events"]
  J --> C["Deterministic rules"]
  C --> F["Findings"]
~~~

Seven explainable rules cover authentication repetition, restricted-command
denial, validator failure/freshness, service health, network health, and
evidence-generation failure. Allowed actions are LOG, ALERT, CREATE_EVIDENCE,
and REQUIRE_REVIEW only. No rule blocks, terminates, isolates, or modifies
policy.

## Security, minimization, and retention

Collection invokes only existing forced-command endpoints with BatchMode.
There is no direct administrator credential, SSH restriction bypass, remote
host change, broad filesystem scan, Docker socket mount, or personal workstation
collection. Raw runtime is stored only under .runtime/zero-trust/telemetry/ and
is ignored. Reviewed summaries contain no usernames, addresses, UUIDs, tokens,
MAC addresses, or private paths.

Operational monitoring reports health and validator state. Security analytics
is limited to normalized, deterministic correlation. Neither is described as a
complete SIEM, UEBA system, production SOC, or continuous trust evaluator.

## Validation and evidence flow

~~~mermaid
flowchart LR
  L["Live collection"] --> S["Sanitization"]
  S --> N["164 normalized events"]
  N --> C["Live correlation"]
  T["Controlled fixture"] --> C
  C --> E["Reviewed package evidence"]
  E --> H["Human review boundary"]
~~~

Four running sources produced 164 normalized events with zero rejections.
Live correlation produced no finding, while the controlled validator-failure
fixture produced one expected finding. The package returned 8 PASS, 0 WARN,
0 FAIL, and exit code 0.

## Limitations and remaining gaps

No persistent central storage, dashboard, host journal ingestion, alert
delivery, behavior analytics, or automated response is implemented. A Monitoring
VM plus user-installed Docker/Compose, Grafana, Loki, and Alloy is required for
the next persistent-storage increment. Rollback is documented in
[zt-vis-001-rollback.md](zt-vis-001-rollback.md).
