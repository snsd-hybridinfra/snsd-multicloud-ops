# Rollback Plan

S030 writes repository evidence only; no exporter or Prometheus rollback applies.

1. Stop if real/sensitive content is found.
2. Remove unsafe artifacts and restore placeholders.
3. Correct module/scrape/sample/parser issues locally.
4. Rerun Static validation.
5. Investigate live failures separately.
6. Revert invalid repository changes through version control.

Never start, reload, reconfigure, or mutate Prometheus/Blackbox from this validator.
