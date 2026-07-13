# Rollback Plan

Static S028 only writes aggregate evidence; Prometheus rollback is never performed.

1. Stop if real/sensitive endpoint or authentication content is detected.
2. Remove the unsafe artifact and restore placeholders.
3. Correct config/sample/parser mismatches without contacting Prometheus.
4. Rerun Static validation.
5. Investigate live failures outside this scenario under separate authorization.
6. Revert invalid repository changes through version control.

Never start, reload, reconfigure, or mutate Prometheus from this validator.
