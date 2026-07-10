# Rollback Plan

1. Stop report planning when an inconsistent status, missing input, sensitive value, or unsupported claim is detected.
2. Mark the affected validation check `FAIL`, `PARTIAL`, or `BLOCKED` as appropriate.
3. Remove or redact unsafe values while preserving a sanitized issue reference.
4. Return inconsistent tracking data to its owning scenario for correction.
5. Recalculate coverage and completeness after corrections are reviewed.
6. Use `FINAL_REPORT_INCONCLUSIVE`, `FINAL_REPORT_INVALID`, or `FINAL_REPORT_OUT_OF_SCOPE` when a valid summary cannot be produced.
7. Record the rollback reason, affected input, and follow-up in `validation.md`.
8. Do not present a draft as a completed final report.
