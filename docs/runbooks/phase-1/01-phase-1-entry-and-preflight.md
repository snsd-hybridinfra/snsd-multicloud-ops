# Phase 1 Entry and Preflight

```json runbook-metadata
{
  "runbook_id": "RB-P1-001",
  "title": "Phase 1 Entry and Preflight",
  "phase": "PHASE_1",
  "related_packages": ["P1-REC-002", "P1-HYG-001", "P1-RUN-BASE"],
  "owner_domain": "REPOSITORY_GOVERNANCE",
  "supported_target_types": ["REPOSITORY_LOCAL"],
  "procedure_status": "IMPLEMENTED",
  "validation_status": "VALIDATED_LOCAL",
  "runtime_required": false,
  "live_execution_permitted": false,
  "required_authority": "CODEX_REPOSITORY_READ_ONLY",
  "evidence_authority": "CODEX_EXECUTED_LOCAL",
  "last_reviewed": "2026-07-19",
  "limitations": ["Readiness describes repository safety only and does not validate a Phase 1 runtime package."]
}
```

## Purpose

Decide whether bounded Phase 1 repository work may start without requiring a
clean working tree or disturbing recovered user work.

## Scope

Read-only Git, scenario-lock, runtime-tracking, authority, and sensitive-data
preflight. It does not authorize deployment, remediation, live collection, or
Git state-changing operations.

## Related Phase

Phase 1 remains `PARTIAL` / `PARTIALLY_VALIDATED` / `NOT_COMPLETE`.

## Related Package or Governance Action

P1-REC-002 supplies the authority map; P1-HYG-001 supplies repository-safe
validation; P1-RUN-BASE supplies this operator baseline.

## Supported Target Types

Repository-local worktree on the approved `main` baseline only.

## Current Procedure Status

`IMPLEMENTED`. Every step is available as a repository-local read-only check.

## Current Validation Status

`VALIDATED_LOCAL`. This is not runtime or package validation.

## Evidence Authority

`CODEX_EXECUTED_LOCAL` for recorded preflight facts only.

## Required Authority

No additional approval for the listed read-only checks. Any operation outside
them requires the owning runbook and explicit authority.

## User-Performed Physical or Approval Steps

Confirm any unexplained concurrent edit, authority conflict, or requested
scope expansion. No physical infrastructure action is part of this procedure.

## Codex or Automation-Managed Steps

Capture the full Git candidate inventory, compare it after a stability window,
check authorities and locks, and issue one readiness decision.

## Prerequisites

Repository root is known; Git is available; AGENTS.md, scope lock, excluded
scope, Zero Trust governance, and the applicable package records are readable.

## Inputs

Expected branch and commit, prior inventory or handoff reference, approved file
boundary, intended action ID, and protected path list.

## Secret Inputs

None. Do not request, paste, read, or store credentials, tokens, private keys,
cloud configuration, kubeconfig, account identifiers, or raw runtime output.

## Service Impact

None. All listed operations inspect repository state only.

## Security Impact

The procedure prevents unsafe secret tracking, runtime tracking, scenario
expansion, overwrite of recovered work, and unauthorized scope promotion.

## Preflight Checks

Verify branch and HEAD/origin alignment; zero staged paths; no merge, rebase,
cherry-pick, revert, or bisect state; no concurrent writer; no tracked runtime;
50 ignored `.runtime/zero-trust/` files; exactly S001-S050 with no later ID; no
likely real tracked secret; and a resolvable runbook authority root.

## Procedure

1. Read the governing documents and the relevant package or scenario record.
2. Capture each tracked-modified, staged, and untracked path with Git state,
   size, UTC modification time, and SHA-256.
3. Run the following read-only inspection group.

```json command-metadata
{
  "commands": [
    "git status --short",
    "git status --branch",
    "git diff --stat",
    "git diff --name-status",
    "git diff --check",
    "git rev-parse HEAD",
    "git rev-parse origin/main",
    "git ls-files .runtime",
    "git check-ignore -v .runtime/zero-trust/"
  ],
  "command_status": "AVAILABLE_READ_ONLY",
  "execution_owner": "CODEX_OR_AUTOMATION",
  "approval_required": false,
  "runtime_target": "REPOSITORY_LOCAL",
  "expected_effect": "Inspect Git and runtime-ignore state without changing it.",
  "evidence_output": "In-memory preflight inventory and decision record.",
  "rollback_reference": "No rollback; stop if before/after state differs."
}
```

4. Wait at least five seconds and recapture the same inventory.
5. Compare unrelated state for equality; a dirty tree is acceptable when it is
   stable and explained.
6. Issue exactly one readiness state.

Never use reset, clean, stash, checkout, restore, discard, forced move, stage,
commit, or push as a preflight repair.

## Expected Output

One of `READY`, `READY_WITH_WARNINGS`, `REVIEW_REQUIRED`, `BLOCKED`, or
`NOT_READY`, plus branch, commit, counts, lock checks, authority result,
before/after fingerprints, protected files, and limitations.

## Validation

Confirm every required fact is present, the two inventories are equal, and the
decision follows the rule below: expected dirty state may be ready; unexplained
drift requires review or blocking; a hard safety violation is not ready.

## Pass Criteria

`READY` or `READY_WITH_WARNINGS`; approved baseline and authorities resolve;
unrelated state is unchanged; no prohibited condition exists.

## Stop Conditions

Changed HEAD/origin, unexplained inventory drift, active Git operation,
concurrent writer, staged work, tracked runtime, likely real secret, a scenario
beyond S050,
unresolved runbook ID conflict, unknown authority root, or required action
outside the authorized file boundary.

## Failure Handling

Return `REVIEW_REQUIRED`, `BLOCKED`, or `NOT_READY` with the exact failed gate.
Do not attempt cleanup or overwrite user work.

## Rollback

No repository change should exist. If a read-only claim is contradicted by a
before/after difference, stop, identify the changed paths, and require review.

## Evidence

Record only sanitized local facts needed for the action audit. Do not track raw
runtime data or the inventory when it exposes environment-specific values.

## Escalation

Escalate unexplained drift, conflicting authority, secret exposure, protected
path overlap, or a new package/scenario requirement to the user.

## Known Limitations

Opaque handoff fingerprints are comparable only when their calculation method
and scope are known. Component counts, hashes, and stable before/after state
remain required.

## Related Architecture

`docs/zero-trust/target-architecture/operator-interface-contract.md` and the
P1-REC-002 authority map.

## Related Runbooks

RB-P1-002 for repository-safe validation and RB-P1-003 for evidence handling.
