# Architecture

## Canonical Path

`evidence/<level>/<scenario-id-scenario-name>/`

Each directory contains:

- `commands.md`
- `validation.md`
- `logs/`
- `screenshots/`
- `configs/`

## Validation Components

- `scenarios/`: source path set.
- `evidence/`: mirrored evidence path set.
- `docs/evidence-status-matrix.md`: readiness tracking.
- `validate-evidence-directory-structure.ps1`: repository-only structure and safety validator.

## Validation Flow

The validator enumerates scenario and evidence directories, compares relative paths, checks required content, scans evidence filenames for forbidden artifacts, validates matrix IDs and statuses, then writes S010 evidence. It does not execute scenario logic or inspect external systems.
