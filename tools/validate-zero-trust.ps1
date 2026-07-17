$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$pythonCommand = Get-Command python -ErrorAction SilentlyContinue
if ($null -eq $pythonCommand) {
    $pythonCommand = Get-Command py -ErrorAction SilentlyContinue
}
if ($null -eq $pythonCommand) {
    Write-Host "[FAIL] Python 3 was not found on PATH."
    exit 2
}

$pythonExecutable = $pythonCommand.Source
$pythonPrefix = @()
if ($pythonCommand.Name -eq "py.exe" -or $pythonCommand.Name -eq "py") {
    $pythonPrefix = @("-3")
}

$stages = @(
    @{ Name = "Zero Trust governance"; Script = "tools/validate_zero_trust.py"; Arguments = @() },
    @{ Name = "Zero Trust synchronization"; Script = "tools/check_zero_trust_sync.py"; Arguments = @() },
    @{ Name = "Zero Trust generated report"; Script = "tools/generate_zero_trust_reports.py"; Arguments = @("--check") }
)

$failure = 0
Push-Location $repositoryRoot
try {
    foreach ($stage in $stages) {
        Write-Host ""
        Write-Host "=== $($stage.Name) ==="
        & $pythonExecutable @pythonPrefix $stage.Script @($stage.Arguments)
        $stageExit = $LASTEXITCODE
        if ($stageExit -ne 0 -and $failure -eq 0) {
            $failure = $stageExit
        }
    }
}
finally {
    Pop-Location
}

if ($failure -ne 0) {
    Write-Host "[FAIL] Zero Trust validation failed (exit=$failure)."
    exit $failure
}
Write-Host "[PASS] Zero Trust validation passed."
exit 0
