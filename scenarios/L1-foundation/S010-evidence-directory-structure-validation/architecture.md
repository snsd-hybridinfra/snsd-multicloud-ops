# Architecture

## Relevant Components

- `scenarios/`: source scenario documentation grouped by validation level.
- `evidence/`: matching evidence directories grouped by validation level.
- `commands.md`: command or action record for each scenario.
- `validation.md`: validation result table for each scenario.
- `logs/`: text log placeholder directory.
- `screenshots/`: screenshot placeholder directory.
- `configs/`: sanitized configuration or summary placeholder directory.
- `docs/evidence-status-matrix.md`: cross-scenario evidence status tracker.
- `tools/validate-repo-structure.ps1`: repository structure validation script.

## Logical Flow

1. Each scenario directory maps to one evidence directory at the same level and with the same scenario name.
2. Each evidence directory contains the required files and placeholder subdirectories.
3. Evidence files map validation checks to supporting artifacts.
4. Evidence status is tracked in `docs/evidence-status-matrix.md`.
5. The repository validation script checks structural completeness.

## Out-of-Scope Components

Live evidence capture, binary artifact generation, infrastructure execution, sensitive file storage, and implementation-specific validation are not part of S010.
