# Authoritative Operational Runbook Framework

`docs/runbooks/` is the authoritative operational runbook root. The minimum
Phase 1 operator baseline is under [`phase-1/`](phase-1/) and is governed by
[`phase-1/runbook-manifest.yaml`](phase-1/runbook-manifest.yaml). Its seven
runbooks describe only the current Phase 1 boundary; their local document
validation does not promote package implementation, runtime validation,
evidence authority, completion, or maturity.

The numbered `00-` through `28-` documents remain future-phase
`DESIGN_SPECIFICATION` records supporting ZT-ARC-001. Planned `platform.ps1`
and `platform.sh` commands in those records are contracts, not available
executables.

Raw runtime output belongs under ignored `.runtime/zero-trust/`. Only reviewed,
sanitized evidence with an allowed authority may be tracked. Physical/manual
prerequisites remain user actions; repository, validator, and documentation
work remains automation-managed; live, mutating, destructive, or
service-affecting actions require the authority stated by the applicable
runbook.

The tracked root `runbooks/` directory is a secondary collection of
scenario-specific validation references. It is not authoritative for Phase 1
operations and cannot override this framework, package records, scenario
records, or Zero Trust governance authorities.

Use [`RUNBOOK_INDEX.md`](RUNBOOK_INDEX.md) for ownership and status. Use
[`RUNBOOK_TEMPLATE.md`](RUNBOOK_TEMPLATE.md) for new reviewed runbooks; a new
scenario ID or package state still requires its own authorization.
