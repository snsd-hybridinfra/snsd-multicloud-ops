# P1-REC-001 Validation Report

## 1. Recovery Baseline

- Branch: `main`
- HEAD: `593f1f2c270a6338043d57cda5a4cea1d43f9342`
- origin/main: `593f1f2c270a6338043d57cda5a4cea1d43f9342`
- Phase 1 state preserved: `PARTIALLY_VALIDATED`
- Intended boundary preserved: `ZT-SCH-001`, `BOUNDARY_CONFIRMED_WITH_GAPS`

## 2. Baseline Drift Check

The P1-0 counts matched exactly before writing: 11 tracked modifications, 84 untracked files, 82 prior-work recovery files, two P1-0 audit files, 50 ignored Zero Trust runtime files, zero staged files, and zero tracked runtime files. No merge, rebase, cherry-pick, revert, bisect, conflict, or concurrent-writer state was found.

## 3. Snapshot Integrity

All 95 tracked/untracked candidates were hashed with SHA-256. Three pre-write scans, including a 15-second separated pair, produced the same fingerprint:

`ad2d9d792391bd569b455df22a3db6d4b404776a60e3a13cab98832800bbb974`

Changed during audit: 0. Unreadable: 0. Missing: 0. Zero-byte candidates: 0. Runtime files were metadata-only and intentionally not read or hashed.

## 4. Working Tree Classification

| Proposed disposition | Count |
|---|---:|
| Merge into existing authoritative file | 11 |
| Adopt after normalization | 49 |
| Retain as nonauthoritative reference | 33 |
| P1-0 audit artifact | 2 |
| Total candidates | 95 |
| Keep ignored runtime | 50 |

Every candidate has exactly one primary disposition in `file-disposition.yaml`.

## 5. Package and ID Conflict Analysis

| ID | Result |
|---|---|
| ZT-FND-001 | Existing tracked authority; bounded runtime-validated state protected. |
| ZT-NET-001 | Existing tracked authority; partially runtime validated; ACL enforcement gap preserved. |
| ZT-VIS-001 | Existing tracked authority; partially runtime validated; no Grafana/Loki/Alloy or persistent-store equivalence. |
| ZT-ID-001 | No package; tracked Phase 1 candidate conflicts with recovered Phase 2 planning and requires an ordering decision. |
| ZT-DEV-001 / ZT-APP-001 / ZT-DATA-001 / ZT-SYS-001 / ZT-AUTO-001 / ZT-CV-001 / ZT-RV-001 | No package or validation authority; candidate references do not establish implementation. |
| ZT-SCH-001 | Recovered boundary reference only; remains design-only and not validated. |
| ZT-VIS-002 | No tracked package; four protected Docker-readiness runtime files; not validated. |
| ZT-ARC-001 | Coherent recovered design package, local static checks passed, but it is untracked and nonauthoritative pending normalization. |

Recovered future IDs remain unapproved design references. `ZT-REC-001` is distinct from `P1-REC-001` but requires wording review to avoid confusion.

## 6. Authority Resolution

Existing tracked authority wins. The 11 tracked files require same-path merge review. `docs/architecture.md` does not replace tracked architecture documents. The 32 `docs/runbooks/` files do not replace `runbooks/`. ZT-ARC-001 cannot self-promote through local validation or newer timestamps.

## 7. Monitoring Protection

Four `.runtime/zero-trust/zt-vis-002/` files are protected active work. 19 recovered candidate files contain monitoring design references and are protected from overwriting active configuration. No Compose/service configuration, Grafana/Loki/Alloy deployment, ingestion, dashboard, or persistent storage was claimed.

## 8. Identity Planning Protection

49 recovered candidates contain identity-related planning references. They remain design/planning only. No Keycloak, MariaDB, Nginx, OIDC, MFA, RBAC, client-secret, or authentication-flow runtime validation was found or claimed.

## 9. Evidence-Claim Review

The recovered architecture validator confirmed design-only and unassessed boundaries. Words such as Advanced, Optimal, validated, PASS, operational, and deployment occur in scoped design, validator, negative-test, or prohibition contexts. Adoption after normalization must downgrade any wording that implies current architecture authority. No candidate was accepted as runtime evidence.

## 10. Secret and Sensitivity Review

The repository validator reported no private keys, tokens, credential assignments, MAC inventories, or UUID collections. The candidate-only scan found five policy/reference/negative-test files and no likely real value. No likely real tracked secret was found. The ignored rendered OpenStack maintenance file retains a protected cloud-profile reference; its content was not copied, printed, read, or hashed.

## 11. Scenario Lock

Exactly 50 scenario IDs, retired-numbered-case through retired-numbered-case, remain present. No successor numbered scenario scenario exists and no renumbering occurred. successor numbered scenario text appears only in negative tests or explicit prohibition statements. No recovered file proposes successor numbered scenario as approved.

## 12. Syntax and Schema Validation

| Check | Result |
|---|---|
| Candidate UTF-8/Markdown/JSON-compatible YAML/JSON/Python syntax | 95/95 pass |
| Conflict markers | 0 |
| Zero-byte candidates | 0 |
| Zero Trust validator | 34 pass, 0 warn, 0 fail |
| Zero Trust synchronization | 5 pass, 0 fail |
| Generated report check | pass; check mode only |
| Combined Zero Trust wrapper | pass |
| Repository structure | pass |
| Recovered architecture validator | 28 pass, 0 warn, 0 fail |
| Full unit tests | 61 pass |

Terraform formatting, Compose configuration, and Mermaid external parsing were skipped because no recovery candidate required a safe executable check beyond the recovered validator. Ignored runtime PowerShell scripts were not parsed because their protected content boundary was metadata-only. The mutating aggregate scenario validator and retired-numbered-case validation were not run.

## 13. Disposition Summary

The disposition is conservative: 11 reviewed merges, 49 normalization candidates, 33 nonauthoritative references, two audit artifacts, and 50 ignored runtime records. No file is a deletion candidate; no deletion was executed.

## 14. User Decisions Required

- P1REC-D001: approve/reject the 11 tracked deltas by hunk.
- P1REC-D002: approve ZT-ARC-001 and its 49-file design set for normalization.
- P1REC-D003: decide whether the 33 architecture/runbook references remain nonauthoritative or receive selective merges.
- P1REC-D004: resolve ZT-ID-001 versus ZT-VIS-002 phase/order ownership.

## 15. Safe Adoption Sequence

Use Groups 0 through 7 in `adoption-plan.md`. Recovery governance comes first, then reviewed tracked merges, protected monitoring isolation, target architecture, future-phase design, and finally any nonauthoritative-content decision. No step may bypass a hash or approval gate.

## 16. Exactly One Next Action

```yaml
action_id: P1-REC-002
objective: Apply the approved non-destructive recovery adoption plan.
rationale: Stable classification is complete, but four human authority decisions remain.
prerequisites:
  - P1REC-D001 through P1REC-D004 approved.
  - Candidate fingerprint and Git baseline unchanged.
  - Protected runtime, package, evidence, monitoring, and identity paths preserved.
authorized_files:
  - Only explicitly approved candidate and recovery-governance files.
protected_files:
  - Every path in protected-files.yaml.
expected_outputs:
  - A single reviewable, non-destructive adoption patch.
  - Updated hash and validation record.
validation:
  - Repeat all read-only checks recorded in section 12.
stop_conditions:
  - Hash or baseline drift.
  - Concurrent writer or Git operation.
  - Likely real tracked secret or tracked runtime file.
  - Missing approval or monitoring-owner conflict.
```

This action was selected but not executed.

## 17. Changed Files

- `docs/zero-trust/recovery/P1-REC-001/README.md`
- `docs/zero-trust/recovery/P1-REC-001/recovery-snapshot.yaml`
- `docs/zero-trust/recovery/P1-REC-001/file-disposition.yaml`
- `docs/zero-trust/recovery/P1-REC-001/adoption-plan.md`
- `docs/zero-trust/recovery/P1-REC-001/protected-files.yaml`
- `docs/zero-trust/recovery/P1-REC-001/validation-report.md`

## 18. Limitations

- Runtime contents were deliberately excluded from reading and hashing.
- No service, infrastructure, deployment, scheduler, identity, or monitoring state was queried or changed.
- Local schema/test success does not establish package authority, runtime validation, evidence authority, or maturity.
- No source candidate was edited, normalized, moved, deleted, staged, committed, or pushed.
