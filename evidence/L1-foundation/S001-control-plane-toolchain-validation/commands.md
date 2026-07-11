# Commands

Scenario: S001-control-plane-toolchain-validation

Level: L1-foundation

Target: local control plane workstation

## Run Validation

From the repository root:

```powershell
powershell -ExecutionPolicy Bypass -File tools\validate-control-plane-toolchain.ps1
```

## Inspect Generated Log

```powershell
Get-Content evidence\L1-foundation\S001-control-plane-toolchain-validation\logs\control-plane-toolchain-validation.log
```

## Inspect Generated Summary

```powershell
Get-Content evidence\L1-foundation\S001-control-plane-toolchain-validation\configs\control-plane-toolchain-summary.md
```

## Safety Notes

- These are local discovery and version-only checks.
- No planned infrastructure action, authentication, remote cluster connection, registry access, credential read, kubeconfig read, or tfstate access occurs.
- The generated files contain no environment-variable dump or account-specific input.
