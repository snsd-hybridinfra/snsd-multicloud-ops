$ErrorActionPreference = "Stop"

function Write-Pass {
    param([string] $Message)
    Write-Host "[PASS] $Message"
}

function Write-Fail {
    param([string] $Message)
    Write-Host "[FAIL] $Message"
}

function Add-MissingPath {
    param(
        [System.Collections.Generic.List[string]] $Missing,
        [string] $Path,
        [string] $Type
    )

    $Missing.Add("$Type missing: $Path") | Out-Null
}

function Test-FileContains {
    param(
        [System.Collections.Generic.List[string]] $Missing,
        [string] $Path,
        [string[]] $RequiredText,
        [string] $Description
    )

    if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
        Write-Fail "Tracking validation skipped; file missing: $Path"
        $Missing.Add("tracking validation skipped; file missing: $Path") | Out-Null
        return
    }

    $content = Get-Content -LiteralPath $Path -Raw
    $missingText = @()

    foreach ($text in $RequiredText) {
        if ($content -notlike "*$text*") {
            $missingText += $text
        }
    }

    if ($missingText.Count -eq 0) {
        Write-Pass "Tracking document validation passed: $Description"
    }
    else {
        Write-Fail "Tracking document validation failed: $Description"
        foreach ($text in $missingText) {
            $Missing.Add("content missing in ${Path}: $text") | Out-Null
        }
    }
}

$repoRootMarkers = @("README.md", "AGENTS.md", ".gitignore", "docs", "scenarios", "evidence", "tools")
$rootMarkerFailures = @()

foreach ($marker in $repoRootMarkers) {
    if (-not (Test-Path -LiteralPath $marker)) {
        $rootMarkerFailures += $marker
    }
}

if ($rootMarkerFailures.Count -gt 0) {
    Write-Fail "Script must be run from the repository root."
    Write-Host "Missing repository root markers:"
    foreach ($marker in $rootMarkerFailures) {
        Write-Host "  - $marker"
    }
    exit 1
}

$missing = [System.Collections.Generic.List[string]]::new()

$requiredTopLevelFiles = @(
    "README.md",
    "AGENTS.md",
    ".gitignore"
)

$requiredDocs = @(
    "docs/scope-lock.md",
    "docs/excluded-scope.md",
    "docs/scenario-model.md",
    "docs/evidence-model.md",
    "docs/naming-rules.md",
    "docs/codex-workflow.md",
    "docs/scenario-template.md",
    "docs/progress-tracker.md",
    "docs/scenario-status-matrix.md",
    "docs/evidence-status-matrix.md",
    "docs/validation-checklist.md",
    "docs/implementation-log.md",
    "docs/risk-register.md"
)

$requiredTopLevelDirs = @(
    "docs",
    "scenarios",
    "evidence",
    "terraform",
    "ansible",
    "kubernetes",
    "eve-ng",
    "observability",
    "ml-security",
    "security-baseline",
    "traffic-management",
    "policy",
    "runbooks",
    "cost-governance",
    "tools"
)

$requiredScenarioLevels = @(
    "scenarios/L1-foundation",
    "scenarios/L2-security-baseline",
    "scenarios/L3-service-operations",
    "scenarios/L4-failure-recovery",
    "scenarios/L5-governance-intelligent-ops"
)

$requiredEvidenceLevels = @(
    "evidence/L1-foundation",
    "evidence/L2-security-baseline",
    "evidence/L3-service-operations",
    "evidence/L4-failure-recovery",
    "evidence/L5-governance-intelligent-ops"
)

$requiredScenarioFiles = @(
    "README.md",
    "objective.md",
    "scope.md",
    "architecture.md",
    "prerequisites.md",
    "execution-plan.md",
    "validation-plan.md",
    "expected-result.md",
    "failure-condition.md",
    "rollback-plan.md",
    "evidence-map.md"
)

$requiredEvidencePaths = @(
    "commands.md",
    "validation.md",
    "logs/.gitkeep",
    "screenshots/.gitkeep",
    "configs/.gitkeep"
)

foreach ($path in $requiredTopLevelFiles) {
    if (Test-Path -LiteralPath $path -PathType Leaf) {
        Write-Pass "Required file exists: $path"
    }
    else {
        Write-Fail "Required file missing: $path"
        Add-MissingPath -Missing $missing -Path $path -Type "file"
    }
}

foreach ($path in $requiredDocs) {
    if (Test-Path -LiteralPath $path -PathType Leaf) {
        Write-Pass "Required doc exists: $path"
    }
    else {
        Write-Fail "Required doc missing: $path"
        Add-MissingPath -Missing $missing -Path $path -Type "file"
    }
}

foreach ($path in $requiredTopLevelDirs) {
    if (Test-Path -LiteralPath $path -PathType Container) {
        Write-Pass "Required directory exists: $path"
    }
    else {
        Write-Fail "Required directory missing: $path"
        Add-MissingPath -Missing $missing -Path $path -Type "directory"
    }
}

foreach ($path in $requiredScenarioLevels) {
    if (Test-Path -LiteralPath $path -PathType Container) {
        Write-Pass "Scenario level exists: $path"
    }
    else {
        Write-Fail "Scenario level missing: $path"
        Add-MissingPath -Missing $missing -Path $path -Type "directory"
    }
}

foreach ($path in $requiredEvidenceLevels) {
    if (Test-Path -LiteralPath $path -PathType Container) {
        Write-Pass "Evidence level exists: $path"
    }
    else {
        Write-Fail "Evidence level missing: $path"
        Add-MissingPath -Missing $missing -Path $path -Type "directory"
    }
}

$scenarioDirs = @()
if (Test-Path -LiteralPath "scenarios" -PathType Container) {
    $scenarioDirs = @(Get-ChildItem -LiteralPath "scenarios" -Directory -Recurse | Where-Object { $_.Name -match "^S\d{3}-.+" })
}

$evidenceDirs = @()
if (Test-Path -LiteralPath "evidence" -PathType Container) {
    $evidenceDirs = @(Get-ChildItem -LiteralPath "evidence" -Directory -Recurse | Where-Object { $_.Name -match "^S\d{3}-.+" })
}

Write-Host "Scenario directory count: $($scenarioDirs.Count)"
Write-Host "Evidence directory count: $($evidenceDirs.Count)"

if ($scenarioDirs.Count -eq 50) {
    Write-Pass "Scenario directory count is 50."
}
else {
    Write-Fail "Scenario directory count is $($scenarioDirs.Count); expected 50."
    $missing.Add("count mismatch: scenarios expected 50, found $($scenarioDirs.Count)") | Out-Null
}

if ($evidenceDirs.Count -eq 50) {
    Write-Pass "Evidence directory count is 50."
}
else {
    Write-Fail "Evidence directory count is $($evidenceDirs.Count); expected 50."
    $missing.Add("count mismatch: evidence expected 50, found $($evidenceDirs.Count)") | Out-Null
}

foreach ($dir in $scenarioDirs) {
    foreach ($file in $requiredScenarioFiles) {
        $path = Join-Path -Path $dir.FullName -ChildPath $file
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
            $relativePath = Join-Path -Path $dir.FullName.Substring((Get-Location).Path.Length + 1) -ChildPath $file
            Write-Fail "Scenario file missing: $relativePath"
            Add-MissingPath -Missing $missing -Path $relativePath -Type "file"
        }
    }
}

foreach ($dir in $evidenceDirs) {
    foreach ($item in $requiredEvidencePaths) {
        $path = Join-Path -Path $dir.FullName -ChildPath $item
        if (-not (Test-Path -LiteralPath $path)) {
            $relativePath = Join-Path -Path $dir.FullName.Substring((Get-Location).Path.Length + 1) -ChildPath $item
            Write-Fail "Evidence path missing: $relativePath"
            Add-MissingPath -Missing $missing -Path $relativePath -Type "path"
        }
    }
}

Write-Host "Tracking document validation result:"

Test-FileContains `
    -Missing $missing `
    -Path "docs/scenario-status-matrix.md" `
    -RequiredText @("S001", "S050") `
    -Description "scenario status matrix contains S001 and S050"

Test-FileContains `
    -Missing $missing `
    -Path "docs/evidence-status-matrix.md" `
    -RequiredText @("S001", "S050") `
    -Description "evidence status matrix contains S001 and S050"

Test-FileContains `
    -Missing $missing `
    -Path "docs/progress-tracker.md" `
    -RequiredText @("L1", "L2", "L3", "L4", "L5") `
    -Description "progress tracker contains L1 through L5"

Test-FileContains `
    -Missing $missing `
    -Path "docs/risk-register.md" `
    -RequiredText @("OneDrive sync conflict") `
    -Description "risk register contains OneDrive sync conflict"

Test-FileContains `
    -Missing $missing `
    -Path "AGENTS.md" `
    -RequiredText @("Tracking File Update Rule") `
    -Description "AGENTS.md contains Tracking File Update Rule"

if ($missing.Count -eq 0) {
    Write-Pass "Repository structure validation passed."
    exit 0
}

Write-Fail "Repository structure validation failed."
Write-Host "Missing paths and validation errors:"
foreach ($item in $missing) {
    Write-Host "  - $item"
}

exit 1
