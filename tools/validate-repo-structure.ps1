$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$failures = [System.Collections.Generic.List[string]]::new()

$requiredFiles = @(
    "README.md",
    "AGENTS.md",
    "docs/scope-lock.md",
    "docs/excluded-scope.md",
    "docs/evidence-model.md",
    "docs/progress-tracker.md",
    "docs/zero-trust/package-flow.yaml",
    "docs/zero-trust/final-roadmap.yaml",
    "docs/zero-trust/final-execution-plan.yaml",
    "docs/zero-trust/maturity-target.yaml",
    "docs/zero-trust/package-status.yaml",
    "docs/zero-trust/package-acceptance-cases.yaml",
    "schemas/zero-trust-package-flow.schema.json",
    "schemas/zt-roadmap.schema.json",
    "schemas/zt-execution-plan.schema.json",
    "schemas/zt-maturity-target.schema.json",
    "schemas/zt-package-status.schema.json",
    "schemas/zt-package-acceptance-cases.schema.json",
    "tools/validate_scenario_retirement.py",
    "tools/validate_zero_trust.py",
    "tools/check_zero_trust_sync.py",
    "tools/validate_phase1_runbook_baseline.py",
    "docs/runbooks/phase-1/runbook-manifest.yaml"
)

$packageIds = @("zt-fnd-001", "zt-net-001", "zt-vis-001", "zt-id-001", "zt-cv-001", "zt-rv-001", "zt-sch-001", "zt-arc-001")
foreach ($packageId in $packageIds) {
    $requiredFiles += "docs/zero-trust/packages/$packageId-package.yaml"
}

$retiredPaths = @(
    "scenarios",
    "evidence/L1-foundation",
    "evidence/L2-security-baseline",
    "evidence/L3-service-operations",
    "evidence/L4-failure-recovery",
    "evidence/L5-governance-intelligent-ops",
    "runbooks",
    "tools/validate-all-scenarios.ps1",
    "tools/validate-scenario-quality.ps1",
    "tools/generate-final-evidence-report.ps1"
)

Push-Location $repositoryRoot
try {
    foreach ($path in $requiredFiles) {
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
            $failures.Add("required file missing: $path") | Out-Null
        }
    }
    foreach ($path in $retiredPaths) {
        if (Test-Path -LiteralPath $path) {
            $failures.Add("retired authority remains: $path") | Out-Null
        }
    }

    $flow = Get-Content -LiteralPath "docs/zero-trust/package-flow.yaml" -Raw | ConvertFrom-Json
    $expectedFlow = @("ZT-FND-001", "ZT-NET-001", "ZT-VIS-001", "ZT-ID-001", "ZT-CV-001", "ZT-RV-001", "ZT-SCH-001", "P1-ACC-001")
    if (@(Compare-Object -ReferenceObject $expectedFlow -DifferenceObject @($flow.phase_1_sequence) -SyncWindow 0).Count -ne 0) {
        $failures.Add("canonical package flow differs") | Out-Null
    }
    if ($flow.phase_1_acceptance.completion_status -ne "NOT_COMPLETE" -or $flow.phase_1_acceptance.scope_boundary -ne "ZT-SCH-001") {
        $failures.Add("Phase 1 acceptance boundary differs") | Out-Null
    }

    $trackedRuntime = @(git ls-files .runtime)
    if ($LASTEXITCODE -ne 0) {
        $failures.Add("git ls-files .runtime failed") | Out-Null
    }
    elseif ($trackedRuntime.Count -ne 0) {
        $failures.Add("tracked runtime files found: $($trackedRuntime -join ', ')") | Out-Null
    }
}
finally {
    Pop-Location
}

if ($failures.Count -gt 0) {
    foreach ($failure in $failures) {
        Write-Host "[FAIL] $failure"
    }
    Write-Host "Repository structure summary: failed=$($failures.Count)"
    exit 1
}

Write-Host "[PASS] Required package authorities, schemas, validators, evidence contracts, and runbooks are present."
Write-Host "[PASS] Retired numbered-scenario authorities and tracked runtime are absent."
Write-Host "Repository structure summary: failed=0"
exit 0
