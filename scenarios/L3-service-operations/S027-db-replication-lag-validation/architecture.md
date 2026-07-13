# Architecture

## Evidence Classification

```text
sanitized replica status
  -> lag field + IO/SQL threads + error fields
  -> NORMAL (0-5)
  -> WARNING (6-30)
  -> CRITICAL (>30 or NULL/thread/error failure)
  -> aggregate evidence
```

The primary, replica, and channel remain symbolic. Metric names document a future observation interface but are never queried by S027.

## Fixture Semantics

Normal and warning samples are positive range fixtures. Critical and NULL samples are negative fixtures. A validator PASS for a negative fixture means the unsafe operational state was correctly identified, not that the state is acceptable.

No database or observability endpoint, credential, process, SQL engine, or network is accessed.
