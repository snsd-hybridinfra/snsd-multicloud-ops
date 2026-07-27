# P1-HYG-001

`P1-HYG-001` is the repository-hygiene action **Repository-Safe Scenario
Validation and retired-numbered-case Strict-Mode Regression Repair**. It is not a Zero Trust
capability, maturity capability, implementation package, scenario, or runtime
evidence record.

The repair makes `retired aggregate validator available in Git history` read-only by default. The
wrapper runs the existing child validators in an operating-system temporary
copy, does not copy `.git` or `.runtime`, removes the temporary copy, and
compares the source repository's tracked, untracked, staged, timestamp, size,
and SHA-256 state before and after. Explicit report generation remains
available only through the mutating `-GenerateReports` switch and was not run
by this action.

retired-numbered-case now uses a strict-mode parser that preserves zero, one, and multiple
results as explicit collections and rejects malformed rows without converting
them to empty success. No live `kubectl` action was executed. The missing retired-numbered-case
sample remains a meaningful scenario failure and is not replaced with synthetic
repository evidence.

Authoritative records:

- `defect-analysis.yaml` — validator discovery, exact root causes, repair, and protected boundaries.
- `regression-results.yaml` — baseline, targeted regression, actual aggregate validation, and final integrity.
- `validation-report.md` — human-readable execution and limitation report.

Current Phase 1 remains `PARTIAL / PARTIALLY_VALIDATED / NOT_COMPLETE`. No ZT
package state or maturity value changed.
