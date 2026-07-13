# Failure Condition

The validator fails if:

- A baseline, matrix, metric reference, or fixture is missing.
- Thresholds, lag fields, thread relationships, NULL interpretation, or matrix entries are incomplete.
- Normal/warning fixtures are unhealthy or outside their ranges.
- The critical fixture is not recognized above 30.
- The NULL fixture does not demonstrate NULL plus a stopped thread and placeholder error.
- A required lag/thread/error field is missing or malformed.
- Credentials, connection strings, dumps, observability credentials, addresses, IDs, URLs, or concrete environment data are detected.
- A database/HTTP client, external query, SQL, or destructive replication path is invoked.

The warning fixture and legacy-only terminology produce WARN without a nonzero exit.
