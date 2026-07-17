# Zero Trust Governance

## Source-of-Truth Hierarchy

The governance layers are authoritative in this order:

1. The local **제로트러스트 가이드라인 2.0** PDF is the external authority for Korean terminology, numbering, functions, source pages, and maturity characteristics.
2. [`capability-catalog.yaml`](capability-catalog.yaml) is the repository authority for the normalized capability taxonomy.
3. [`current-baseline-assessment.yaml`](current-baseline-assessment.yaml) is the repository authority for the current capability assessment.
4. Markdown matrices and summaries are human-readable views. They must not override either machine-readable authority.

The two YAML files use the JSON-compatible YAML 1.2 subset. This deliberate constraint permits dependency-free, deterministic validation with the Python standard library. A change to general YAML syntax requires an approved dependency decision first.

## Capability Governance

- Keep exactly the 52 source capabilities across six core pillars and two cross-cutting domains.
- Preserve official Korean display names and source numbering. English slugs are stable repository identifiers, not replacement source terminology.
- Change canonical identifiers, names, relationships, pages, or table references only after reviewing the local authoritative PDF.
- Update the canonical taxonomy fingerprint in `tools/validate_zero_trust.py` only in the same reviewed change as the source-backed catalog correction.
- Do not invent aliases, IDs, pillars, functions, or source relationships.

## Maturity Governance

- Assess maturity per capability, never as one repository-wide or organization-wide score.
- Keep `current_maturity` and `target_maturity` separate from implementation and validation status.
- `OPTIMAL` requires `CONTINUOUS` evidence or an explicit reviewed exception.
- `ADVANCED` cannot rely on `NONE` evidence.
- One disposable-lab test cannot establish enterprise maturity.
- Ambiguous exceptions must contain `REVIEW_REQUIRED`; otherwise inconsistent assignments fail validation.

## Evidence Governance

- Evidence authority, evidence level, implementation state, and validation state are independent fields.
- Runtime authority requires sanitized, resolvable execution evidence. Design artifacts are not runtime evidence.
- `CODEX_EXECUTED_LIVE_RUNTIME` requires a recorded live command and result under an existing evidence path.
- Do not reference or commit raw logs, credentials, tokens, private keys, `clouds.yaml`, `passwords.yml`, account values, MAC inventories, or unnecessary UUID collections.
- Validator output redacts sensitive matches and reports only path, line, detector, and a masked preview.

## Scenario Mapping Governance

- S001-S050 are the only current scenario IDs.
- Scenario names in Zero Trust matrices must match the actual scenario directory names.
- Scenario ranges beyond S050 may appear only as clearly labeled future roadmap ranges in [`implementation-roadmap.md`](implementation-roadmap.md).
- Mapping means traceable alignment. It does not mean implementation, validation, compliance, or maturity.
- Do not rewrite scenario documents from the Zero Trust report generator.

## Prohibited Claims

Affirmative claims of full compliance, certification, complete Zero Trust implementation, enterprise-wide validation, production readiness, complete micro-segmentation, all-capability implementation, or repository-wide Optimal maturity are prohibited. The validator permits these phrases only in an explicit prohibition, exclusion, boundary statement, or controlled test fixture.

Preferred wording includes “aligned with,” “mapped to,” “validated within the stated environment,” “partially validated,” “conceptual alignment,” and “gap identified.”

## Validation Commands

Run from the repository root:

```powershell
python tools/validate_zero_trust.py --verbose
python tools/check_zero_trust_sync.py
python tools/generate_zero_trust_reports.py --check
powershell -ExecutionPolicy Bypass -File tools/validate-zero-trust.ps1
powershell -ExecutionPolicy Bypass -File tools/validate-repo-structure.ps1
python -m unittest discover -s tests -v
```

All commands above are read-only. The report generator writes only when explicitly invoked with `--write`, and then only inside the reviewed marker pair in `current-baseline-assessment.md`.

## Failure Interpretation

- Exit `0`: required checks passed.
- Exit `1`: content, synchronization, policy, reference, or safety validation failed.
- Exit `2`: validator configuration or parsing failed, or Python is unavailable to the PowerShell wrapper.
- `WARN`: a documented review condition exists. `--strict` promotes warnings to failures.

Fix the authoritative YAML first when YAML and Markdown disagree. Do not weaken a rule or edit a generated view merely to hide a contradiction.

## Exception Process

1. Record the capability and failed rule.
2. Cite the authoritative source and bounded evidence.
3. Add `REVIEW_REQUIRED` and an explicit expiry or resolution condition.
4. Obtain human approval before changing an enum, fingerprint, schema, or maturity rule.
5. Remove the exception when adequate evidence or a corrected assessment is available.

Exceptions cannot authorize secrets, new scenarios, source-inconsistent capability IDs, or unsupported maturity claims.

## Change Review

Review catalog, baseline, matrix, generated-block, and validator changes together. Run the full command set, inspect `git diff`, and commit only after the source, schema, synchronization, security, and repository checks pass. Live OpenStack, EVE-NG, router, or other infrastructure validation remains a separately authorized manual workflow.

No GitHub Actions workflow currently exists. A future workflow should run the standard-library Python tests, `tools/validate-zero-trust.ps1`, and the existing repository validators without secrets or network access; adding that workflow requires a separate impact review.
