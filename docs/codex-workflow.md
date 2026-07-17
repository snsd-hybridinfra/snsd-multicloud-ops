# Codex Workflow

Codex should work as a scoped repository collaborator, not as an autonomous deployment agent.

## Before Changing Files

1. Read `AGENTS.md`.
2. Read the relevant scope and scenario documents.
3. Confirm the change does not introduce excluded scope.
4. Prefer concise documentation and skeletal structure for foundation work.

## During Changes

- Keep changes scenario-based.
- Update naming, evidence, or scope docs when conventions change.
- Add ADRs for meaningful architecture or scope decisions.
- Avoid generated binaries and local machine artifacts.
- Do not create credentials, secrets, tfstate, kubeconfig files, or provider configuration.

## Validation

After changes, verify:

- required directories exist
- required docs are populated
- `.gitignore` blocks sensitive and local artifacts
- scenario IDs follow naming rules
- evidence paths match the evidence model

For Zero Trust governance changes, run:

```powershell
python tools/validate_zero_trust.py --verbose
python tools/check_zero_trust_sync.py
python tools/generate_zero_trust_reports.py --check
powershell -ExecutionPolicy Bypass -File tools/validate-zero-trust.ps1
python -m unittest discover -s tests -v
```

`capability-catalog.yaml` is the repository taxonomy authority,
`current-baseline-assessment.yaml` is the current-assessment authority, and
`capability-implementation-backlog.yaml` is the planning authority. Backlog
targets and waves never promote current status or maturity. Markdown views
must follow those files. These checks are local and read-only; they do not
authorize SSH, cloud access, live infrastructure validation, or report writes.
Use report `--write` only after reviewing the generated markers and diff.

Before deriving future scenario work, review the backlog dependency chain,
phase gate, verification plan, evidence authority, rollback, and
`docs/zero-trust/future-scenario-governance.md`. Use backlog identifiers until
scenario creation is explicitly approved; never allocate an identifier beyond
the locked S001-S050 set during planning.

## Restricted OpenStack Validation Endpoint

S005 has one operator-approved, non-interactive validation endpoint. Codex may
invoke exactly:

```powershell
ssh -o BatchMode=yes openstack-validator validate-all
```

The local alias resolves outside the repository and uses a dedicated private
key stored outside the repository. The remote key is forced through a
dispatcher that accepts only `validate-all`; an empty command, interactive
shell request, or any other command is rejected. Agent, port, and X11
forwarding, PTY allocation, and user SSH startup files are disabled for the
key. The restricted account may run through passwordless sudo only the
root-owned read-only validator script.

This authority permits current-state inspection only. It does not authorize
general shell access, direct credential reads, arbitrary `sudo`, direct
OpenStack or Docker commands, Kolla actions, resource mutation, service or
container restart, network reconfiguration, failure injection, or recovery
execution. The repository wrapper
`tools/openstack-validator/invoke-openstack-validation.ps1` accepts no remote
command parameter and preserves the validator exit status.

Only sanitized validator output may be retained. Target addresses, dynamic
addresses, UUIDs, tokens, MAC addresses, SSH key material, authentication
files, and raw session logs remain outside the repository.

## Handoff

Summaries should include changed files, validation performed, and any remaining risks or deferred work.
