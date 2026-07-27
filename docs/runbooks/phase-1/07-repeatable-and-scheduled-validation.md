# Repeatable and Scheduled Validation

```json runbook-metadata
{"runbook_id":"RB-P1-007","phase":"PHASE_1","related_packages":["ZT-CV-001","ZT-RV-001","ZT-SCH-001"],"procedure_status":"DESIGN_SPECIFICATION","validation_status":"NOT_VALIDATED","live_execution_permitted":false}
```

## Purpose

Define predecessor gates for cross-capability, repeatable, and scheduled validation without installing or executing automation.

## Current boundary

ZT-CV-001, ZT-RV-001, and ZT-SCH-001 are NOT_IMPLEMENTED / NOT_VALIDATED. No scheduler, job, CI workflow, execution identity, automatic retry, notification integration, or accepted repeatability evidence exists.

## Required sequence

1. CV validates FND, NET, VIS, and ID together and records conflicts or missing controls.
2. RV repeats an accepted deterministic CV plan and proves evidence consistency.
3. SCH may be designed and installed only after RV acceptance and separate scheduler approval.
4. Scheduled validation must detect missed or failed runs, verify freshness and retention, and support disable and rollback.

## Pass criteria

For this design-only runbook, package states remain unpromoted, no schedule exists, no live target changes, and Phase 1 remains NOT_COMPLETE.
