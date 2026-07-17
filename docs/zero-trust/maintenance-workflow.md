# Zero Trust Maintenance Workflow

Use this order for every taxonomy, mapping, assessment, or evidence-governance change.

1. **Update machine-readable catalog.** Review the local authoritative PDF and update [`capability-catalog.yaml`](capability-catalog.yaml). Preserve JSON-compatible YAML 1.2 and source citations.
2. **Validate schema.** Run `python tools/validate_zero_trust.py --verbose`. A canonical taxonomy change also requires a reviewed fingerprint update.
3. **Update scenario mappings.** Reconcile [`scenario-capability-matrix.md`](scenario-capability-matrix.md), [`control-coverage-matrix.md`](control-coverage-matrix.md), and [`evidence-coverage-matrix.md`](evidence-coverage-matrix.md). Mapping alone is not implementation.
4. **Update evidence records.** Add only sanitized, resolvable references with the correct authority and level. Keep live execution under an existing S001-S050 evidence path.
5. **Run baseline reassessment.** Update [`current-baseline-assessment.yaml`](current-baseline-assessment.yaml) per capability. Do not derive maturity from scenario completion or one lab test.
6. **Run report synchronization check.** Use `python tools/generate_zero_trust_reports.py --check`. If stale, review the target and then use `--write`; the command may edit only the explicit generated marker block.
7. **Run full repository validation.** Run `powershell -ExecutionPolicy Bypass -File tools/validate-zero-trust.ps1`, `python -m unittest discover -s tests -v`, and `powershell -ExecutionPolicy Bypass -File tools/validate-repo-structure.ps1`.
8. **Review the Git diff.** Run `git diff --check`, `git status --short`, and `git diff --stat`. Check for scenario drift, generated prose outside markers, and sensitive values.
9. **Obtain approval.** Human review is required for taxonomy corrections, maturity exceptions, schema changes, fingerprint changes, new dependencies, CI integration, or changes to scenario scope.
10. **Commit only after validation.** Do not commit or push when any required check fails. Keep live infrastructure execution and credentials outside this workflow.

## Synchronization Rule

When layers disagree, correct them in authority order: external PDF, capability catalog, baseline assessment, then Markdown views. Never treat a generated or manually maintained Markdown matrix as machine-readable authority.

## Runtime Boundary

The validators require no SSH, remote OpenStack or EVE-NG access, credentials, network access, or cloud account data. Live runtime collection remains separately approved and must be sanitized before it can support an assessment record.
