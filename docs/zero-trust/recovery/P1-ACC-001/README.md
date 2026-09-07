# P1-ACC-001 acceptance preflight record

This directory records the evidence-based Phase 1 acceptance preflight and its
default-deny decision.

The package decisions through `ZT-RV-001` are present, but the newest accepted
RV execution was more than seven days old at the recorded assessment time. The
same read-only assessment logic used by the RV package returned `STALE`, zero
currently accepted records, and `EC3_ONE_TIME_RUNTIME`. The P1-ACC-001 stop
condition therefore applied and the historical action was
`BLOCKED_STALE_EVIDENCE`.

ADR 0014 and `acceptance-decision-with-gaps.yaml` subsequently supersede only
the phase-entry result. Phase 1 is `COMPLETED_WITH_GAPS`, Phase 2 local
preparation is authorized, and the stale assessment remains unchanged as a
mandatory final-gate residual risk.

The corresponding current records are `validation-results-with-gaps.yaml` and
`completion-report-with-gaps.md`. The original validation and completion files
remain preserved as the historical default-deny record.

No live validator ran. No target, scheduler, package status, maturity, or
compliance state changed. ZT-SCH-001 remains disabled and deferred to final
Phase 5.

After that acceptance decision, the operator separately authorized a manual
read-only RV refresh while Phase 2 local work continued. The first refreshed
execution was accepted on 2026-08-20, making the new window 1/3 at
`STALE / EC3 / IN_PROGRESS`. This later runtime event does not rewrite the
historical default-deny assessment or the accepted-with-gaps decision.

Files:

- `authority-audit.yaml`: reviewed authorities and freshness preflight
- `evidence-index.yaml`: exact predecessor decision and sanitized evidence authorities
- `acceptance-decision.yaml`: formal default-deny decision and bounded recovery
- `validation-results.yaml`: read-only decision checks
- `completion-report.md`: concise outcome and non-claims
- `rv-refresh-progress.yaml`: current separately reviewed RV freshness window

The recovery path stays inside the existing `ZT-RV-001` package: after separate
live authorization, complete the remaining two eligible manual read-only
executions at least 24 hours apart and rerun P1-ACC-001. The scheduler is not
required.
