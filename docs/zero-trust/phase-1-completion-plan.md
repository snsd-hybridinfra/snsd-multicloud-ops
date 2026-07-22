# Phase 1 Completion Plan through Scheduled Runtime Validation

## Purpose

This plan governs the bounded non-production laboratory work required to move
from the current package baseline through `ZT-RV-001` and `ZT-SCH-001`. It does
not create a scenario, change the locked `S001`-`S050` set, establish
organization-wide Zero Trust implementation, or assign repository-wide
maturity.

The Phase 1 completion boundary remains `ZT-SCH-001`. Package implementation,
validation, acceptance, evidence continuity, and capability maturity remain
separate decisions.

## Starting baseline

| Package | Starting state | Required disposition |
|---|---|---|
| `ZT-FND-001` | `IMPLEMENTED / VALIDATED` with a current runtime regression caused by a stopped test instance | Restore the approved test target and record current validation honestly. |
| `ZT-NET-001` | `IMPLEMENTED / PARTIALLY_VALIDATED` | Restore the fixed path and close or retain the persistent ACL gap with explicit evidence. |
| `ZT-VIS-001` | `IMPLEMENTED / PARTIALLY_VALIDATED` | Establish bounded persistent central storage, source health, retention, and sanitized runtime evidence. |
| `ZT-ID-001` | `IMPLEMENTED / RUNTIME_VALIDATED / ACCEPTED` for one bounded non-production target | Preserve the accepted forced-command boundary; add centralized identity and MFA only through a safe pilot. |
| `ZT-DEV-001` through `ZT-CV-001` | Implemented at bounded package scopes; DEV- through CV remain partially runtime validated where stated | Preserve limitations and do not infer repeatability, continuous operation, or maturity. |
| `ZT-RV-001` | Campaign tooling implemented and locally validated; 0/3 accepted campaign runs | Execute only after the not-before gate and collect three independent consecutive successes at least 24 hours apart. |
| `ZT-SCH-001` | Not prepared; mandatory EC4 gate unmet | Do not prepare or install until ZT-RV-001 reaches REPEATABILITY_ACCEPTED / EC4. |

## Authorization and responsibility boundary

Codex is authorized to configure and validate virtual machines and virtual
network appliances in the disposable laboratory. Every change must have a
bounded target, a pre-change record, a rollback path, and post-change
validation. Credentials, private keys, MFA material, tokens, and raw runtime
output remain outside Git.

The laboratory owner retains responsibility for physical cabling, physical
switch ports, host firmware and virtualization settings, physical power or
hardware failure recovery, and physical capacity expansion. Codex must report
the smallest exact physical action when one of those boundaries blocks work.

Schedule installation remains a separate access-affecting change. Preparing
and reviewing `ZT-SCH-001` does not authorize installation. The Windows task
may be installed only after the user provides the exact approval required by
the installation-review package.

## Current execution status

| Wave | State | Accepted result |
|---|---|---|
| `P1-A` | `COMPLETE` | FND target restored; EVE boundary preserved; NET persistent directional ACL accepted at 39/0/0; VIS persistent sanitized storage passed health, retention, ingestion/query, secret scan, and restart retrieval. |
| `P1-B` | `COMPLETE` | Existing bounded ZT-ID-001 acceptance is preserved; ZT-DEV-001 is implemented and partially runtime validated for six aliases and one mandatory VM. Centralized identity and MFA stay outside this bounded Phase 1 identity package. |
| `P1-C` | `COMPLETE` | ZT-APP-001, ZT-DATA-001, and ZT-SYS-001 are implemented and partially runtime validated within unchanged, synthetic, and fixed-read-only boundaries. SYS assessed seven systems, matched five safe configuration authorities, and retained OpenStack at the explicit CURRENT_DEGRADED 46/0/4 boundary without remediation. |
| `P1-D` | `COMPLETE` | ZT-AUTO-001 remains bounded at 4 PASS/4 WARN/0 FAIL, and ZT-CV-001 completed one accepted manual cycle at 8 PASS/2 WARN/0 FAIL. CV is EC3 only; no schedule, remediation, maturity, or Phase 1 completion is claimed. |
| `P1-E` | `ACTIVE_NOT_STARTED` | ZT-RV-001 tooling and selection validate, but accepted campaign runs are 0/3. First execution is locked until 2026-07-23T04:57:52.159854Z; EC4 is absent. |
| `P1-F` | `BLOCKED_BY_EC4_GATE` | ZT-SCH-001 preparation and installation review must not begin until RV is REPEATABILITY_ACCEPTED / EC4. Installation later requires exact explicit user approval. |

## Execution waves

### Wave P1-A - Restore and close foundational gaps

1. Restore the approved OpenStack validation instance and re-run FND and NET
   validators.
2. Preserve the EVE-NG 42/42 restricted validation boundary.
3. Apply a bounded, rollback-ready virtual-router ACL only after the live
   configuration, allow path, and deny path are explicit.
4. Connect the existing monitoring VM through the approved virtual network
   path and implement persistent telemetry storage with bounded retention.

Exit gate: no unresolved FND regression; NET is accepted at its honest scope;
VIS has persistent sanitized storage or an explicit blocking result.

### Wave P1-B - Identity, device, and workload foundations

1. Preserve the accepted bounded `ZT-ID-001` forced-command identity and keep
   centralized identity, OIDC, application RBAC, and MFA enforcement as a
   separately governed later dependency.
2. Implement `ZT-DEV-001` inventory, compliance, software, vulnerability, and
   patch-state validation without automatic patching or reboot.
3. Use one non-critical workload as the common bounded pilot for device,
   application, data, and system evidence where this does not blur each
   package's acceptance boundary.

Exit gate: identity and device inventories validate; privileged and
non-interactive identities remain separated; no operator access is lost.

### Wave P1-C - Application, data, and system controls

1. Implement `ZT-APP-001` inventories, secure-deployment gates, secret checks,
   an SBOM boundary, and bounded runtime health validation.
2. Implement `ZT-DATA-001` inventory, classification, least-privilege access,
   encryption assessment, detection-only DLP, and isolated backup/restore
   assurance using synthetic or repository-generated data.
3. Implement `ZT-SYS-001` inventory, configuration authority, drift checks,
   service exposure, privileged-access review, and recovery readiness.

Exit gate: mandatory local tests pass, live evidence is sanitized, no live
source data is overwritten, and restoration claims are backed by an isolated
restore test.

### Wave P1-D - Safe automation and integrated verification

1. Implement `ZT-AUTO-001` with a fixed action registry, default-deny policy,
   deterministic plans, approval levels, timeouts, locks, and read-only or
   proposal-only execution.
2. Implement `ZT-CV-001` verification classes, freshness, acceptance,
   regression, exception, and maturity-proposal logic.
3. Execute one integrated read-only cycle. Classify one cycle as at most
   `EC3_ONE_TIME_RUNTIME`; do not label it continuous.

Exit gate: no executable mutation action, no arbitrary shell or SSH target,
no automatic authoritative-document update, and the integrated cycle has an
accurate execution authority and sanitized evidence.

### Wave P1-E - Repeatable runtime campaign

1. Select exactly one `ZT-CV-001`-recommended capability and deterministic
   validator.
2. Execute the `ZT-RV-001` campaign at least three independent times.
3. Enforce at least 24 hours between accepted runs unless the validated policy
   contains a stricter requirement.
4. Require three consecutive successes, zero blocking failures, stable plan,
   validator and target-scope fingerprints, security-boundary success, and
   sanitizer success.

Exit gate: `REPEATABILITY_ACCEPTED` and `EC4_REPEATABLE_RUNTIME`. Duplicate,
replayed, copied, check-only, or insufficiently separated records do not count.

### Wave P1-F - Scheduled runtime validation

1. Prepare `ZT-SCH-001` only after the RV campaign reaches EC4.
2. Generate and validate deterministic Task Scheduler XML without installing
   it.
3. Complete `ZT-SCH-002` installation review. The task remains uninstalled and
   approval remains `PROPOSED` during review.
4. Obtain the exact explicit user approval, install only the reviewed task,
   and verify the installed definition against approved hashes.
5. Accumulate at least three valid `SCHEDULED_TRIGGER` executions on three
   distinct scheduled dates, with no blocking missed run or security failure.

Exit gate: scheduled acceptance policy passes and `EC5_SCHEDULED_RUNTIME` is
supported by actual scheduled executions. Daily scheduling is not continuous
monitoring (`EC6`) and does not establish continuous enforcement (`EC7`).

## Package acceptance rules

- Documentation or configuration alone cannot establish runtime validation.
- A partial package may satisfy a successor gate only when that successor's
  policy explicitly permits the limitation and the limitation is recorded.
- A failed mandatory check is not downgraded to a warning for convenience.
- Every VM or virtual-network mutation requires post-change verification and a
  recorded rollback path.
- Status files are updated only after the corresponding evidence exists.
- Scenario counts and scenario states remain unchanged unless a separate
  scenario task explicitly authorizes their modification.

## Validation and publication gate

After each cohesive package, run the package validator, all Zero Trust
validators, the full Python test suite, repository structure validation,
secret and privacy checks, scenario-lock checks, and Git diff checks. Keep raw
runtime artifacts under ignored `.runtime/zero-trust/` paths. Publish only
reviewed, sanitized, text-only evidence.

Phase 1 is not complete until every required predecessor gate is resolved and
the scheduled-runtime acceptance evidence supports EC5. EC6, EC7, Advanced,
Optimal, certification, and enterprise-wide claims remain outside this Phase 1
completion decision.
