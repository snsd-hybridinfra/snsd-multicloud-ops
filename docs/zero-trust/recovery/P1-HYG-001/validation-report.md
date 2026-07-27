# P1-HYG-001 Validation Report

## Executive Summary

P1-HYG-001 repaired repository validation hygiene only. Default aggregate
scenario validation is read-only, the retired-numbered-case strict-mode collection failure is
fixed, and no package, maturity, scenario, runtime, monitoring, or identity
state changed.

## Baseline Verification

- Branch: `main`
- HEAD/origin: `593f1f2c270a6338043d57cda5a4cea1d43f9342`
- Tracked modifications: 11
- Untracked files: 96
- Staged files: 0
- Tracked runtime files: 0
- Ignored `.runtime/zero-trust/` files: 50
- Scenarios: retired numbered scenario framework exactly; successor numbered scenario absent
- Opening fingerprint: `9ded7512022c4b864e8bfa36ba3050bf925eaa329af823a5eb4b5025fbb7cd1d`
- Five-second concurrent-writer check: stable

No merge, rebase, cherry-pick, or bisect state existed. The tracked secret
checks passed before modification.

## Validator Discovery

`retired aggregate validator` called two repository validators and discovered
scenario validators through `tools/validate-*.ps1`. The repaired exclusion set
removes the non-scenario `validate-zero-trust.ps1`, leaving exactly 50 scenario
validators. All 50 scenario validators contain a repository-writing command.
retired-numbered-case is `tools/validate-kubernetes-node-readiness.ps1`; no prior PowerShell
regression test covered its collection shapes.

## Retired Aggregate Validator Root Cause

The no-argument command created retired-numbered-case directories, ran repository-writing child
validators in the source tree, and unconditionally wrote its own log and
summary. `SNSD_REPO_WIDE_STATIC_ONLY=1` prevented live behavior but did not
prevent `New-Item` or `Set-Content`. P1-0 recorded 21 generated untracked files
before restoring its captured state. Exact removed names were not retained, so
this report records the authoritative path families rather than inventing a
list.

## retired-numbered-case Root Cause

The original conditional assignment returned `$null` for zero rows and could
return one `PSCustomObject` for one row; only multiple rows reliably returned
`Object[]`. `Set-StrictMode -Version Latest` then rejected
`$activeNodes.Count`. The missing sample exposed the zero-row case.

## Implemented Repair

- Default aggregate mode uses an isolated OS temporary repository copy.
- `.git` and protected `.runtime` are never copied.
- Aggregate report generation is skipped by default.
- Explicit `-GenerateReports` preserves reviewed mutating behavior and was not run.
- Exactly 50 scenario validators are evaluated.
- Exit 0/1/2 distinguish pass, validation failure, and wrapper/immutability failure.
- retired-numbered-case uses a typed parser and `Generic.List[object]` before count or iteration.
- Malformed input is a failure, not an empty success.

## Repository Immutability Guard

The reusable guard records path, two-character Git state, size, UTC timestamp,
and SHA-256 for all tracked/staged/untracked candidates. It accepts an existing
dirty tree and requires exact before/after equality. Regression fixtures prove
new files, changed hashes, and staged state are detected.

## Static Regression Tests

- Repository safety PowerShell cases: 8/8 pass
- Python hygiene integration cases: 4/4 pass
- Changed PowerShell parser checks: 6 files, zero errors
- Mutation fixtures ran only in OS temporary Git repositories

## retired-numbered-case Strict-Mode Tests

Nine cases passed: null, empty, scalar one, multiple, missing status column,
invalid status, embedded null, expected valid fixture, and repository
immutability. Strict mode remains `Latest`.

An isolated static script run returned exit 1 for V003, V006, and V007 because
the authoritative sample remains absent. No Count-property exception occurred.
`-LiveKubectl` was not executed.

## Actual Repository Validation

- Mode: `ReadOnlyIsolated`
- Scenarios evaluated: 50
- PASS: 15
- WARN: 5
- FAIL: 30
- Integration failures: 0
- Exit: 1
- Report generation: skipped

The 30 failures are existing scenario artifact/evidence gaps. This action does
not weaken them or claim scenario completion.

## Working-Tree Before/After Comparison

- Before: `31f3bec9267cd697347c92b3baa5a7c44d03fa9cdb715af3fd30a4142eaac132`
- After: `31f3bec9267cd697347c92b3baa5a7c44d03fa9cdb715af3fd30a4142eaac132`
- Repository unchanged: `true`

## Existing Validator Results

- Zero Trust: 34 PASS / 0 WARN / 0 FAIL
- Synchronization: 5 PASS / 0 FAIL
- Generated report check: PASS
- Combined Zero Trust wrapper: PASS
- Architecture: 28 PASS / 0 WARN / 0 FAIL
- Repository structure: PASS
- Scenario quality: PASS with zero warnings
- Full unit suite: 66/66 PASS

## Security and Runtime Hygiene

No likely real secret was introduced. No runtime file is tracked.
`.runtime/zero-trust/` remains ignored with 50 protected files. No live service,
kubectl, ACL, monitoring, identity, deployment, remediation, or scheduled job
operation was run.

## Scenario Lock

retired numbered scenario framework remain exactly present. successor numbered scenario is absent. No scenario content,
identifier, semantics, evidence record, or status was regenerated or changed.

## Remaining Limitations

- Aggregate validation correctly remains exit 1 because 30 scenario validators fail existing criteria.
- retired-numbered-case lacks its tracked authoritative sample and remains `NOT_STARTED` / not runtime validated.
- Child validators still write reports internally; read-only aggregate mode confines those writes to a disposable temporary copy.
- The immutability fingerprint covers Git candidates; protected ignored runtime is checked separately by ignore/tracking metadata.

## Exactly One Next Action

`P1-RUN-BASE` — complete the minimum Phase 1 operational runbook baseline.

- Objective: identify and validate the minimum repository-local operator runbooks required for the current Phase 1 package boundary without claiming runtime execution.
- Rationale: the mandatory validator-hygiene blocker is cleared; runbook authority already exists, the work needs no live infrastructure, minimizes rework, and does not conflict with protected monitoring or identity work.
- Prerequisites: revalidate P1-HYG-001, select only the minimum Phase 1 procedures, preserve design/runtime evidence separation, and obtain separate authorization.
- Authorized files: selected `docs/runbooks/` records, their index/template, narrowly required runbook validators/tests, tracking notes, and `docs/zero-trust/recovery/P1-RUN-BASE/`.
- Protected files: `.runtime/**`, scenario/evidence content, ZT package and maturity states, monitoring/identity configuration, target-architecture semantics, credentials, and deployment files.
- Expected outputs: an explicit minimum runbook set, status/evidence/rollback rules, local validator coverage, and a bounded completion report.
- Validation: run runbook/architecture, Zero Trust, repository structure, scenario lock, full unit, secret/runtime, and working-tree immutability checks.
- Stop conditions: any live action, package-state promotion, protected-file change, secret/runtime tracking, scenario expansion, or requirement for deployment/remediation.

The action is selected only and was not executed.

## Changed Files

- `README.md`
- `retired aggregate validator available in Git history`
- `tools/validate-kubernetes-node-readiness.ps1`
- `retired aggregate safety module available in Git history`
- `retired parser module available in Git history`
- `tests/powershell/test-repository-validation-safety.ps1`
- `tests/powershell/test-s021-node-status-parser.ps1`
- `tests/test_repository_validation_hygiene.py`
- `docs/zero-trust/recovery/P1-HYG-001/README.md`
- `docs/zero-trust/recovery/P1-HYG-001/defect-analysis.yaml`
- `docs/zero-trust/recovery/P1-HYG-001/regression-results.yaml`
- `docs/zero-trust/recovery/P1-HYG-001/validation-report.md`

## Git Integrity

Status: `PASS`. The post-record inventory contains 13 tracked modifications,
105 untracked files, zero staged files, and zero tracked runtime files. The
recorded final implementation fingerprint is
`73b30e2b542c2361c7e487236d343c8f21e2613ee6d73e4abb46c6758446c25d`.
It covers every Git candidate except the four self-referential P1-HYG-001
records; those four records are parsed and counted separately.
No source repository file was staged, committed, pushed, reset, restored,
stashed, checked out, or cleaned.
