# Source-integrity review

Reviewed locally on 2026-10-02 against
`17da9e90e530dcc3db26584b770f146db1c2f4f9` in the authoritative repository.
This is a local investigation record, not package acceptance or runtime evidence.
Neither approved hashes nor historical evidence have been changed.

## Open findings

| Source | Current and HEAD SHA-256 | Referenced SHA-256 | Authority |
| --- | --- | --- | --- |
| `.gitignore` | `4ec6247437b8c8f8ac198f3d446e918e7199cb06532b6371f78e6a4deb8c056a` | `21ee2ee499cce6c5bb6da851599b455e3d2f917b6a6c44a99b245c34ca2edeb3` | `docs/zero-trust/system-configuration-authority.yaml` and `docs/evidence/zero-trust/zt-sys-001-integrity-validation.yaml` |
| `ansible/playbooks/zt-vis-002-alert-validation.yml` | `dd54365efbe93e7f6828e36c76413f194a8ab609db8763a283ea952c5240170d` | `64cc1c23181bfdbdd5669c7359845180b19d79d83b100e0b2575022a0a789946` | `docs/evidence/zero-trust/zt-vis-002-alert-validation.sanitized.json` |

Both working-tree files are byte-identical to HEAD. The failures therefore
predate the current runner changes. Normalizing current CRLF to LF does not
change their hashes; current checkout line endings do not explain the mismatch.

## Git history findings

Commit `ac83dc4792286324f4e1e13f866f4a13871a8321` established the financial
Hybrid-Ready baseline. It added an explicit exception for the reviewed
OpenStack dependency lock and ignore rules for container supply-chain and
Mini-Ona runtime directories. Removing those rules merely to match an old
checksum would weaken runtime-file protection. The five reachable historical
`.gitignore` revisions were hashed; none matches the referenced approved hash.
The immediately preceding source has SHA-256
`6f5178a333e2ae98d7c6a4575f2f7c2057fcedeb7a31357e9d040121b87d93ea`,
which also differs from that authority.

The alert-validation playbook first appears in the same baseline commit in
this repository's reachable history. Its recorded runtime validation occurred
on 2026-08-25, before that import commit. The recorded source bytes have not
been located here. The current playbook retains four default-deny authorization
gates and an unconditional temporary-validator cleanup path. Those static
properties cannot validate the historical execution against different bytes.

## Required resolution

For `ZT-SYS-001`, the configuration owner must identify the approved source or
review the current ignore-rule changes and produce a new bounded local
integrity-validation record. Keep the 2026-07-22 evidence unchanged and keep
any new local claim separate from host/runtime validation. Review must also
verify ignore behavior, secret/state exclusions, rollback and ownership.

For `ZT-VIS-002`, locate the exact source used by the recorded execution or
perform a separately authorized validation using the reviewed current source.
The authorization must cover validation, temporary rule mutation, notification
delivery and cleanup. A successful local hash or syntax check cannot refresh
that runtime evidence. Preserve the open clock, retention, restore and package
status gates.

Both root-suite checks remain fail-closed until matching authority and evidence
exist. No hash replacement, validator relaxation, package-status promotion or
live execution is authorized by this review document.
