# P1-REC-001 — Recovered Working Tree Stabilization and Adoption Decision

P1-REC-001 is a recovery-governance action. It is not a Korean Zero Trust capability, maturity capability, implementation package, or scenario.

## Outcome

The audited P1-0 baseline was reproduced at `593f1f2c270a6338043d57cda5a4cea1d43f9342` on `main`. Three pre-write scans produced the same SHA-256 candidate fingerprint, `ad2d9d792391bd569b455df22a3db6d4b404776a60e3a13cab98832800bbb974`; no concurrent writer or Git operation state was detected.

| Item | Result |
|---|---:|
| Tracked modified candidates | 11 |
| Untracked candidates | 84 |
| Prior-work untracked files | 82 |
| P1-0 audit artifacts | 2 |
| Total hash-addressed candidates | 95 |
| Ignored Zero Trust runtime files (metadata only) | 50 |
| Tracked runtime files | 0 |
| Candidate files changed during audit | 0 |

## Decision boundary

- The 11 tracked deltas remain pending same-path merge review.
- 49 recovered ZT-ARC-001/ADR/profile/schema/validator artifacts are candidates for adoption only after normalization and explicit approval.
- `docs/architecture.md` plus all 32 `docs/runbooks/` files remain nonauthoritative because tracked architecture documents and `runbooks/` take precedence.
- ZT-FND-001 remains the bounded runtime-validated tracked authority.
- ZT-NET-001 remains partially runtime validated; its ACL enforcement gap is unchanged.
- ZT-VIS-001 remains partially runtime validated and is not equivalent to deployed Grafana/Loki/Alloy.
- ZT-SCH-001 remains design-only.
- ZT-VIS-002 remains protected ignored runtime work with Docker readiness traces only.
- ZT-ARC-001 remains design-only, locally validated, untracked, and nonauthoritative.

## Records

- [Immutable snapshot](recovery-snapshot.yaml)
- [File dispositions](file-disposition.yaml)
- [Future adoption sequence](adoption-plan.md)
- [Protected paths](protected-files.yaml)
- [Validation report](validation-report.md)

No source candidate was changed, normalized, moved, deleted, staged, committed, or pushed. No service or infrastructure state changed.
