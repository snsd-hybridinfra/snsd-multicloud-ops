# P1-CV-001 Recovery Record

This directory records the sanitized, reviewable outcome of the 2026-07-27
bounded cross-capability validation action. The action implemented and ran the
fixed read-only ZT-CV-001 workflow, exposed a mandatory FND acceptance blocker,
and stopped before P1-RV-001.

- `target-audit.yaml` records the bounded target and rollback boundary.
- `runtime-results.yaml` records the final execution and decision.
- `validation-results.yaml` records acceptance, negative, persistence,
  rollback, and evidence-integrity checks.
- `completion-report.md` explains why the action is blocked rather than
  completed.

Raw runtime output remains ignored and is not an authority.
