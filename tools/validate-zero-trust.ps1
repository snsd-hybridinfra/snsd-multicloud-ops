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
    @{ Name = "Project definition"; Script = "tools/validate_zt_project_definition.py"; Arguments = @("--strict") },
    @{ Name = "Final roadmap"; Script = "tools/validate_zt_roadmap.py"; Arguments = @("--strict") },
    @{ Name = "Final execution plan"; Script = "tools/validate_zt_execution_plan.py"; Arguments = @("--strict") },
    @{ Name = "Dependency graph"; Script = "tools/validate_zt_dependency_graph.py"; Arguments = @("--strict") },
    @{ Name = "Milestones and gates"; Script = "tools/validate_zt_milestones.py"; Arguments = @("--strict") },
    @{ Name = "Risk register"; Script = "tools/validate_zt_risk_register.py"; Arguments = @("--strict") },
    @{ Name = "Evidence plan"; Script = "tools/validate_zt_evidence_plan.py"; Arguments = @("--strict") },
    @{ Name = "Maturity target"; Script = "tools/validate_zt_maturity_target.py"; Arguments = @("--strict") },
    @{ Name = "KISA mapping"; Script = "tools/validate_zt_kisa_mapping.py"; Arguments = @("--strict") },
    @{ Name = "Package acceptance cases"; Script = "tools/validate_zt_package_acceptance_cases.py"; Arguments = @("--strict") },
    @{ Name = "Status truth"; Script = "tools/validate_zt_status_truth.py"; Arguments = @("--strict") },
    @{ Name = "Phase 1 acceptance"; Script = "tools/validate_phase1_acceptance.py"; Arguments = @() },
    @{ Name = "Phase 2 entry"; Script = "tools/validate_phase2_entry.py"; Arguments = @() },
    @{ Name = "Phase 2 visibility artifacts"; Script = "tools/validate_p2_vis_001_artifacts.py"; Arguments = @() },
    @{ Name = "Zero Trust governance"; Script = "tools/validate_zero_trust.py"; Arguments = @() },
    @{ Name = "Zero Trust synchronization"; Script = "tools/check_zero_trust_sync.py"; Arguments = @() },
    @{ Name = "Zero Trust generated report"; Script = "tools/generate_zero_trust_reports.py"; Arguments = @("--check") },
    @{ Name = "Numbered scenario retirement"; Script = "tools/validate_scenario_retirement.py"; Arguments = @() },
    @{ Name = "Advanced target architecture"; Script = "tools/validate_advanced_target_architecture.py"; Arguments = @("--strict") },
    @{ Name = "Phase 1 package runbooks"; Script = "tools/validate_phase1_runbook_baseline.py"; Arguments = @() }
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
