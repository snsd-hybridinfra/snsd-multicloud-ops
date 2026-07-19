# Repository-Safe Validation

```json runbook-metadata
{
  "runbook_id": "RB-P1-002",
  "title": "Repository-Safe Validation",
  "phase": "PHASE_1",
  "related_packages": ["P1-HYG-001"],
  "owner_domain": "VALIDATION_HYGIENE",
  "supported_target_types": ["REPOSITORY_LOCAL", "ISOLATED_TEMPORARY_COPY"],
  "procedure_status": "IMPLEMENTED",
  "validation_status": "VALIDATED_LOCAL",
  "runtime_required": false,
  "live_execution_permitted": false,
  "required_authority": "CODEX_REPOSITORY_READ_ONLY",
  "evidence_authority": "CODEX_EXECUTED_LOCAL",
  "last_reviewed": "2026-07-19",
  "limitations": ["Scenario failures remain authoritative content gaps; the wrapper does not convert them to passes."]
}
```

## Purpose

Run the repaired aggregate scenario validation without changing the source
repository and interpret wrapper health separately from scenario outcomes.

## Scope

Default read-only aggregate behavior, temporary isolation, exit semantics,
immutability checks, and the repaired S021 strict-mode parser boundary.

## Related Phase

Phase 1 repository hygiene only; no package or scenario state is promoted.

## Related Package or Governance Action

P1-HYG-001.

## Supported Target Types

Source repository plus an OS temporary isolated copy without `.git` or
protected `.runtime` content.

## Current Procedure Status

`IMPLEMENTED` by the repaired aggregate wrapper and repository safety module.

## Current Validation Status

`VALIDATED_LOCAL`; no live S021 or Kubernetes runtime validation is included.

## Evidence Authority

`CODEX_EXECUTED_LOCAL` for wrapper, parser, test, and aggregate result facts.

## Required Authority

No extra approval for the default read-only invocation. Report generation and
all live options require a separate authorized action and are excluded here.

## User-Performed Physical or Approval Steps

None for default mode. The user must separately approve any future live target
or source-tree report generation.

## Codex or Automation-Managed Steps

Snapshot source state, create the isolated copy, discover exactly 50 scenario
validators, execute static behavior there, compare the source snapshot, and
report scenario versus integration failures separately.

## Prerequisites

RB-P1-001 is ready; PowerShell and Python are available; the P1-HYG modules and
tests exist; S001-S050 remain locked.

## Inputs

Repository root, default aggregate script, source snapshot, scenario validator
set, and temporary directory supplied by the operating system.

## Secret Inputs

None. `.runtime/zero-trust/`, credentials, kubeconfig, and live target data are
not copied or read by default mode.

## Service Impact

None. Default mode performs static validation in an isolated disposable copy.

## Security Impact

The isolation prevents repository-writing child validators from altering the
source tree and prevents protected runtime content from entering the copy.

## Preflight Checks

Confirm default mode, no report-generation flag, no live S021 option, exactly
50 scenario validators, source inventory captured, and OS temporary path not
inside the repository.

## Procedure

1. Capture the source repository snapshot.
2. Run the default aggregate command exactly as classified below.

```json command-metadata
{
  "command": "powershell -ExecutionPolicy Bypass -File tools/validate-all-scenarios.ps1",
  "command_status": "AVAILABLE_READ_ONLY",
  "execution_owner": "CODEX_OR_AUTOMATION",
  "approval_required": false,
  "runtime_target": "ISOLATED_TEMPORARY_COPY",
  "expected_effect": "Evaluate all 50 scenario validators in an isolated copy and skip source report generation.",
  "evidence_output": "Console summary with scenario counts, integration failures, mode, and exit code.",
  "rollback_reference": "RB-P1-002 Rollback; source snapshot must remain unchanged."
}
```

3. Treat report generation as explicit and unavailable in this action; do not
   invoke the generation flag.

```json command-metadata
{
  "command": "powershell -ExecutionPolicy Bypass -File tools/validate-all-scenarios.ps1 -GenerateReports",
  "command_status": "PROHIBITED_IN_CURRENT_PHASE",
  "execution_owner": "CODEX_OR_AUTOMATION",
  "approval_required": true,
  "runtime_target": "SOURCE_REPOSITORY",
  "expected_effect": "Would explicitly generate aggregate reports in the source repository; not authorized by P1-RUN-BASE.",
  "evidence_output": "None in this action.",
  "rollback_reference": "RB-P1-002 Rollback; use a separate reviewed generation action.",
  "executable": false
}
```

Live S021 collection is also prohibited in this action.

```json command-metadata
{
  "command": "powershell -ExecutionPolicy Bypass -File tools/validate-kubernetes-node-readiness.ps1 -LiveKubectl",
  "command_status": "PROHIBITED_IN_CURRENT_PHASE",
  "execution_owner": "CODEX_OR_AUTOMATION",
  "approval_required": true,
  "runtime_target": "KUBERNETES_RUNTIME",
  "expected_effect": "Would request live read-only Kubernetes node collection; no approved runtime or evidence target exists.",
  "evidence_output": "None in this action.",
  "rollback_reference": "S021 rollback plan; no live action is permitted.",
  "executable": false
}
```

4. Interpret exit `0` as scenario criteria satisfied, exit `1` as content or
   scenario validation failure with a healthy wrapper, and exit `2` as wrapper,
   isolation, configuration, parsing, or immutability failure.
5. Confirm source before/after equality and remove only the disposable copy by
   its OS-temporary lifecycle.

## Expected Output

Mode `ReadOnlyIsolated`, 50 evaluated scenarios, separate PASS/WARN/FAIL and
integration-failure counts, report generation skipped, source unchanged, and
an exit code. The current bounded baseline is 15 PASS, 5 WARN, 30 FAIL, zero
integration failures, exit `1`.

## Validation

Run targeted guard and S021 parser tests, then the default aggregate. The S021
zero/scalar/multiple cases must not produce a Count-property exception.

## Pass Criteria

Wrapper integration succeeds; exactly 50 validators run; source state is
unchanged; no live S021 action occurs. Exit `1` is an acceptable runbook result
when it reports the existing 30 scenario gaps and zero integration failures.

## Stop Conditions

Source-tree write, report generation without approval, temporary path inside
the repository, copied `.git` or `.runtime`, validator count other than 50,
live S021 request, Count-property defect, integration failure, or immutability
failure.

## Failure Handling

Classify scenario failure separately from validator defect. Preserve the
scenario failures; diagnose wrapper or parser defects without weakening any
scenario criterion.

## Rollback

The source is expected to be unchanged. On mutation, stop, report exact paths,
retain the before/after comparison, and do not reset, clean, restore, or stash.

## Evidence

Record sanitized counts, mode, exit code, integration failures, source
fingerprints, and the explicit fact that report generation and live S021 were
not invoked.

## Escalation

Escalate wrapper exit `2`, repository mutation, discovery drift, unsafe temp
scope, or a request to generate reports or contact a live cluster.

## Known Limitations

Child validators still write within the isolated copy. S021 lacks authoritative
tracked sample evidence and remains `NOT_STARTED` / not runtime validated.

## Related Architecture

`docs/zero-trust/governance.md` and P1-HYG-001 recovery records.

## Related Runbooks

RB-P1-001 for entry gating and RB-P1-003 for any sanitized retained result.
