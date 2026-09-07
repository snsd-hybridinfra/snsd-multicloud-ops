# Zero Trust Package Phase Gates

## Gate 0 - Authority integrity

Require canonical capability taxonomy, package-flow validity, synchronized package metadata, no unsupported status or maturity claim, no tracked runtime, and no sensitive data.

## Gate 1 - Foundation readiness

Require bounded assets, restricted access, evidence rules, execution authority, recovery prerequisites, sanitization, and rollback.

## Gate 2 - Control implementation readiness

Require approved capability scope, package ownership, technical target, dependency status, implementation plan, validation classes, operational impact, rollback, and evidence requirements.

## Gate 3 - Runtime validation readiness

Require an isolated approved target, explicit positive and negative outcomes, bypass and failure handling, sanitizer, cleanup, and separate approval for destructive or service-affecting actions.

## Gate 4 - Package acceptance

Require observed results, resolved sanitized evidence, rollback or cleanup result, limitations, residual gaps, and a status decision that does not exceed evidence.

## Gate 5 - Repeatable operation and deferred final scheduling

Phase 1 requires deterministic repeatability through bounded EC4. Scheduled
runtime is deferred to the final Phase 5 project gate, where it requires failure
visibility, freshness, retention, disable and rollback controls, corrected
scheduler correlation, and separately approved execution identity and target
scope.

The three historical RV executions exceed the P7D freshness limit. Historical
EC4 evidence remains preserved but does not satisfy the current freshness gate.
One new manual execution is accepted in the separate refresh window, leaving
the current result at 1/3, `STALE / EC3 / IN_PROGRESS`.
The reviewed `P1-RV-FRESHNESS-001` exception permits Phase 2 local preparation
only; it cannot satisfy the final scheduling or P5-ACC-001 gates.

No gate automatically promotes a capability, package, evidence-continuity level, compliance state, or maturity.
