# Zero Trust Implementation Phase Gates

Phase gates are evidence decisions. They do not automatically promote a capability or scenario. The repository maintainer is the default owner; destructive testing and status acceptance require explicit human approval.

## Gate ZT-0 — Documentation Authority

- **Owner:** repository maintainer.
- **Required inputs:** 52-capability catalog, baseline, backlog, schemas, source traceability, validator output.
- **Required outputs:** accepted taxonomy/backlog snapshot and documented limitations.
- **Pass criteria:** 52 capabilities represented; schemas and sync pass; no unsupported maturity/status claim; scenario lock and sensitive-data checks pass.
- **Fail criteria:** missing/duplicate capability, broken authority, overclaim, unauthorized future scenario ID, or validator failure.
- **Waiver process:** no waiver for taxonomy count, source traceability, secret exposure, or scenario lock; other exceptions require dated rationale, owner, expiry, and remediation issue.
- **Evidence:** validator logs and version-controlled catalog/baseline/backlog diff.

## Gate ZT-1 — Foundation Readiness

- **Owner:** laboratory infrastructure owner and evidence reviewer.
- **Required inputs:** stable lab connectivity, bounded inventory, administrative-access design, evidence conventions, recovery prerequisites.
- **Required outputs:** approved foundation package and known-good rollback baseline.
- **Pass criteria:** assets are identifiable; required access is restricted; infrastructure validation is repeatable; evidence can be sanitized; recovery prerequisites exist.
- **Fail criteria:** unknown critical asset, uncontrolled administration, missing rollback, unrepeatable result, or sensitive evidence handling.
- **Waiver process:** only non-security-critical laboratory availability issues may be time-bounded; access/secret/rollback failures cannot be waived.
- **Evidence:** inventory, sanitized connectivity/access results, configuration baseline, backup/recovery prerequisite record.

## Gate ZT-2 — Control Implementation Readiness

- **Owner:** control-pattern owner and repository maintainer.
- **Required inputs:** approved capability scope, dependency status, control pattern, secret handling, implementation/validation/rollback plan.
- **Required outputs:** approved implementation package with bounded target maturity.
- **Pass criteria:** dependencies are evidenced or explicitly blocked; scope is locked; enforcement and rollback are identified; no new technology bypasses ADR governance.
- **Fail criteria:** circular/unmet dependency, ambiguous authority, missing rollback, unsupported product/scope expansion, or secret requirement without safe handling.
- **Waiver process:** a missing non-critical dependency may be isolated and marked PARTIAL; security authority and rollback cannot be waived.
- **Evidence:** backlog record, dependency review, control pattern, validation plan, approval record.

## Gate ZT-3 — Runtime Validation Readiness

- **Owner:** test operator and independent evidence reviewer where practical.
- **Required inputs:** implemented bounded control, approved test data, positive/negative/bypass/failure/recovery procedures, sanitizer, cleanup plan.
- **Required outputs:** authorized test run package.
- **Pass criteria:** preconditions pass; target is isolated; expected outcomes are explicit; destructive actions have explicit approval; evidence paths are safe.
- **Fail criteria:** production target, missing test data/sanitizer, uncontrolled blast radius, missing cleanup, or implicit destructive authorization.
- **Waiver process:** destructive and sensitive-data safeguards have no waiver; an omitted non-destructive test must be recorded as a limitation and prevents full acceptance.
- **Evidence:** preflight output, test authorization, procedure/version, sanitization checklist.

## Gate ZT-4 — Capability Acceptance

- **Owner:** evidence acceptance authority named in the verification plan.
- **Required inputs:** observed results, sanitized artifacts, limitations, cleanup/rollback result, current backlog/baseline.
- **Required outputs:** accepted, partial, inconclusive, blocked, or rejected judgment and reassessment proposal.
- **Pass criteria:** success criteria and required negative/recovery paths pass; evidence authority accepts artifacts; limitations and residual risk are recorded.
- **Fail criteria:** unsupported PASS, incomplete evidence chain, unsafe final state, status mismatch, or maturity inference beyond the lab boundary.
- **Waiver process:** a partial capability can be accepted only as PARTIALLY_VALIDATED/PARTIAL evidence; it cannot receive a stronger maturity/status.
- **Evidence:** validation summary, accepted artifacts, rollback proof, updated status proposal and review note.

## Gate ZT-5 — Continuous Operation

- **Owner:** laboratory operations owner.
- **Required inputs:** accepted repeatable checks, drift rule, alert handling, rollback/recovery, reassessment cadence.
- **Required outputs:** periodic evidence set and capability-gap delta.
- **Pass criteria:** repeated checks are deterministic; drift and collection failure are visible; response is bounded; recovery succeeds; reassessment is traceable.
- **Fail criteria:** silent collection failure, uncontrolled automation, stale evidence presented as current, or failed rollback.
- **Waiver process:** temporary monitoring gaps require owner, reason, expiry, affected capabilities, and compensating manual check.
- **Evidence:** repeated run records, drift/alert disposition, response/rollback result, maturity reassessment diff.

## Wave-to-gate use

| Wave | Minimum gate before implementation | Acceptance gate |
|---|---|---|
| W0 Governance and Evidence Foundation | ZT-0 | ZT-4 |
| W1 Infrastructure and Trust Foundations | ZT-1 | ZT-4 |
| W2 Identity, Endpoint, and Workload Controls | ZT-2 | ZT-4 |
| W3 Application, Software, and Data Protection | ZT-2 and ZT-3 | ZT-4 |
| W4 Visibility, Correlation, and Automated Response | ZT-3 | ZT-4 and ZT-5 prerequisites |
| W5 Continuous Verification and Maturity Reassessment | ZT-5 | periodic ZT-4 reassessment |
