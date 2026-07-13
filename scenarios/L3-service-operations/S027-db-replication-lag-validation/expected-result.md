# Expected Result

S027 passes when required artifacts and thresholds are complete, normal evidence is healthy, warning evidence is correctly warned, and critical/NULL negative fixtures are rejected operationally by the parser.

Healthy fixtures require IO/SQL `Yes`, numeric lag, and empty errors. Critical classification is required for lag above 30, NULL, stopped threads, or non-empty errors. Legacy terminology is compatible with a warning.

No database/observability connection, SQL/API query, credential read, replication change, dump operation, or network access occurs. One expected warning is acceptable for the warning-range fixture.
