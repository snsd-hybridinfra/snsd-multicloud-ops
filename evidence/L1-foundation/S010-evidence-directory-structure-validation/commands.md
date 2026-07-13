# Commands

Scenario: S010-evidence-directory-structure-validation

Level: L1-foundation

## Run Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-evidence-directory-structure.ps1
```

## Inspect Generated Evidence

```powershell
Get-Content evidence\L1-foundation\S010-evidence-directory-structure-validation\logs\evidence-directory-structure-validation.log
Get-Content evidence\L1-foundation\S010-evidence-directory-structure-validation\configs\evidence-directory-structure-summary.md
```

## Rerun Repository Structure Validation

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-repo-structure.ps1
```

## Safety Notes

No planned command executes scenario implementations, processes secrets, or contacts external systems. The validator enumerates repository paths and status rows only.
