$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$scenarioRoot = Join-Path $repositoryRoot "scenarios"
$evidenceRoot = Join-Path $repositoryRoot "evidence"
$matrixPath = Join-Path $repositoryRoot "docs\evidence-status-matrix.md"
$s010EvidenceRoot = Join-Path $evidenceRoot "L1-foundation\S010-evidence-directory-structure-validation"
$logDirectory = Join-Path $s010EvidenceRoot "logs"
$configDirectory = Join-Path $s010EvidenceRoot "configs"
$logPath = Join-Path $logDirectory "evidence-directory-structure-validation.log"
$summaryPath = Join-Path $configDirectory "evidence-directory-structure-summary.md"

$requiredFiles = @("commands.md", "validation.md")
$requiredDirectories = @("logs", "screenshots", "configs")
$allowedEvidenceStatuses = @("NOT_READY", "PARTIAL", "READY", "REVIEWED")
$expectedIds = 1..50 | ForEach-Object { "S{0:D3}" -f $_ }

New-Item -ItemType Directory -Force -Path $logDirectory, $configDirectory | Out-Null

$results = [System.Collections.Generic.List[object]]::new()
$outputLines = [System.Collections.Generic.List[string]]::new()
$criticalFailures = 0

function Add-ValidationResult {
    param(
        [string] $Id,
        [string] $Description,
        [ValidateSet("PASS", "WARN", "FAIL")]
        [string] $Result,
        [string] $Detail
    )

    if ($Result -eq "FAIL") {
        $script:criticalFailures++
    }

    $line = "[$Result] $Id ${Description}: $Detail"
    Write-Host $line
    $script:outputLines.Add($line) | Out-Null
    $script:results.Add([pscustomobject]@{
        Id          = $Id
        Description = $Description
        Result      = $Result
        Detail      = $Detail
    }) | Out-Null
}

$scenarioDirectories = @(
    Get-ChildItem -LiteralPath $scenarioRoot -Directory -Recurse -Force -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -match '^S\d{3}-' }
)
$scenarioIds = @($scenarioDirectories | ForEach-Object { [regex]::Match($_.Name, '^S\d{3}').Value })
$missingScenarioIds = @($expectedIds | Where-Object { $_ -notin $scenarioIds })
$duplicateScenarioIds = @(
    $scenarioIds | Group-Object | Where-Object Count -gt 1 | ForEach-Object Name
)
if ($scenarioDirectories.Count -eq 50 -and $missingScenarioIds.Count -eq 0 -and $duplicateScenarioIds.Count -eq 0) {
    Add-ValidationResult "V001" "Scenario directory set" "PASS" "Exactly 50 unique scenario directories contain S001 through S050."
}
else {
    Add-ValidationResult "V001" "Scenario directory set" "FAIL" "Scenario count, ID coverage, or uniqueness is invalid."
}

$evidenceDirectories = @(
    Get-ChildItem -LiteralPath $evidenceRoot -Directory -Recurse -Force -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -match '^S\d{3}-' }
)
$evidenceIds = @($evidenceDirectories | ForEach-Object { [regex]::Match($_.Name, '^S\d{3}').Value })
$missingEvidenceIds = @($expectedIds | Where-Object { $_ -notin $evidenceIds })
$duplicateEvidenceIds = @(
    $evidenceIds | Group-Object | Where-Object Count -gt 1 | ForEach-Object Name
)
if ($evidenceDirectories.Count -eq 50 -and $missingEvidenceIds.Count -eq 0 -and $duplicateEvidenceIds.Count -eq 0) {
    Add-ValidationResult "V002" "Evidence directory set" "PASS" "Exactly 50 unique evidence directories contain S001 through S050."
}
else {
    Add-ValidationResult "V002" "Evidence directory set" "FAIL" "Evidence count, ID coverage, or uniqueness is invalid."
}

$scenarioRelativePaths = @(
    $scenarioDirectories |
        ForEach-Object { $_.FullName.Substring($scenarioRoot.Length) -replace '^[\\/]+', '' }
)
$evidenceRelativePaths = @(
    $evidenceDirectories |
        ForEach-Object { $_.FullName.Substring($evidenceRoot.Length) -replace '^[\\/]+', '' }
)
$missingMirrors = @($scenarioRelativePaths | Where-Object { $_ -notin $evidenceRelativePaths })
$orphanEvidencePaths = @($evidenceRelativePaths | Where-Object { $_ -notin $scenarioRelativePaths })
if ($missingMirrors.Count -eq 0 -and $orphanEvidencePaths.Count -eq 0) {
    Add-ValidationResult "V003" "Scenario and evidence path mirroring" "PASS" "All scenario and evidence paths mirror one-to-one."
}
else {
    Add-ValidationResult "V003" "Scenario and evidence path mirroring" "FAIL" "A missing mirror or orphan evidence path was detected."
}

$missingRequiredFiles = [System.Collections.Generic.List[string]]::new()
foreach ($directory in $evidenceDirectories) {
    foreach ($fileName in $requiredFiles) {
        if (-not (Test-Path -LiteralPath (Join-Path $directory.FullName $fileName) -PathType Leaf)) {
            $missingRequiredFiles.Add("$($directory.Name)/$fileName") | Out-Null
        }
    }
}
if ($missingRequiredFiles.Count -eq 0) {
    Add-ValidationResult "V004" "Required evidence files" "PASS" "All evidence directories contain commands.md and validation.md."
}
else {
    Add-ValidationResult "V004" "Required evidence files" "FAIL" ("Missing files: " + ($missingRequiredFiles -join ", "))
}

$missingRequiredDirectories = [System.Collections.Generic.List[string]]::new()
foreach ($directory in $evidenceDirectories) {
    foreach ($directoryName in $requiredDirectories) {
        if (-not (Test-Path -LiteralPath (Join-Path $directory.FullName $directoryName) -PathType Container)) {
            $missingRequiredDirectories.Add("$($directory.Name)/$directoryName") | Out-Null
        }
    }
}
if ($missingRequiredDirectories.Count -eq 0) {
    Add-ValidationResult "V005" "Required evidence subdirectories" "PASS" "All evidence directories contain logs, screenshots, and configs."
}
else {
    Add-ValidationResult "V005" "Required evidence subdirectories" "FAIL" ("Missing directories: " + ($missingRequiredDirectories -join ", "))
}

$evidenceFiles = @(Get-ChildItem -LiteralPath $evidenceRoot -File -Recurse -Force -ErrorAction SilentlyContinue)
$forbiddenSensitiveFiles = @(
    $evidenceFiles |
        Where-Object {
            $_.Name -match '(?i)\.tfstate(?:\.backup)?$' -or
            $_.Name -match '(?i)^terraform\.tfvars$' -or
            $_.Name -match '(?i)\.(?:pem|key|p12|pfx|sql|dump|bak|zip|7z|tar|gz)$' -or
            $_.Name -match '(?i)^id_(?:rsa|ed25519)$' -or
            $_.Name -match '(?i)^(?:kubeconfig|config\.kube)$' -or
            $_.Name -match '(?i)^clouds\.ya?ml$' -or
            $_.Name -match '(?i)openrc' -or
            $_.Name -match '(?i)^(?:credentials?|secrets?)(?:\.|$)' -or
            ($_.Extension -eq ".crt" -and (Get-Content -LiteralPath $_.FullName -Raw -ErrorAction SilentlyContinue) -match 'PRIVATE KEY')
        }
)
if ($forbiddenSensitiveFiles.Count -eq 0) {
    Add-ValidationResult "V006" "Sensitive evidence files" "PASS" "No forbidden state, key, credential, dump, certificate-private-material, or archive file exists."
}
else {
    Add-ValidationResult "V006" "Sensitive evidence files" "FAIL" ("Forbidden files: " + (($forbiddenSensitiveFiles | ForEach-Object FullName) -join ", "))
}

$matrixExists = Test-Path -LiteralPath $matrixPath -PathType Leaf
$matrixLines = if ($matrixExists) { @(Get-Content -LiteralPath $matrixPath) } else { @() }
$matrixRows = @($matrixLines | Where-Object { $_ -match '^\|\s*S\d{3}\s*\|' })
$matrixIds = @($matrixRows | ForEach-Object { [regex]::Match($_, 'S\d{3}').Value })
$matrixMissingIds = @($expectedIds | Where-Object { $_ -notin $matrixIds })
if ($matrixExists -and $matrixRows.Count -eq 50 -and $matrixMissingIds.Count -eq 0) {
    Add-ValidationResult "V007" "Evidence matrix ID coverage" "PASS" "The evidence status matrix contains S001 through S050."
}
else {
    Add-ValidationResult "V007" "Evidence matrix ID coverage" "FAIL" "The matrix is missing, has an invalid row count, or lacks required IDs."
}

$matrixDuplicateIds = @($matrixIds | Group-Object | Where-Object Count -gt 1 | ForEach-Object Name)
if ($matrixDuplicateIds.Count -eq 0) {
    Add-ValidationResult "V008" "Evidence matrix ID uniqueness" "PASS" "The evidence status matrix contains no duplicate scenario ID."
}
else {
    Add-ValidationResult "V008" "Evidence matrix ID uniqueness" "FAIL" ("Duplicate IDs: " + ($matrixDuplicateIds -join ", "))
}

$invalidStatusCells = [System.Collections.Generic.List[string]]::new()
foreach ($row in $matrixRows) {
    $cells = @($row.Split('|') | ForEach-Object { $_.Trim() })
    $scenarioId = $cells[1]
    foreach ($statusValue in $cells[3..8]) {
        if ($statusValue -notin $allowedEvidenceStatuses) {
            $invalidStatusCells.Add("${scenarioId}:$statusValue") | Out-Null
        }
    }
}
if ($invalidStatusCells.Count -eq 0) {
    Add-ValidationResult "V009" "Evidence readiness status values" "PASS" "All matrix status cells use NOT_READY, PARTIAL, READY, or REVIEWED."
}
else {
    Add-ValidationResult "V009" "Evidence readiness status values" "FAIL" ("Invalid status cells: " + ($invalidStatusCells -join ", "))
}

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Repository evidence directory structure: $criticalFailures critical failure(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S010 Evidence Directory Structure Validation"
    "Generated: $timestamp"
    "Scope: scenario/evidence structure and readiness status only"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "This validation did not inspect cloud systems, execute scenario implementations, process secrets, or judge scenario-specific technical success."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

function Format-SummaryList {
    param([object[]] $Items)
    if ($Items.Count -eq 0) { return "None" }
    return ($Items -join ", ")
}

$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# Evidence Directory Structure Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S010-evidence-directory-structure-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Final judgment: **$overallResult**") | Out-Null
$summaryLines.Add("- Scenario directory count: $($scenarioDirectories.Count)") | Out-Null
$summaryLines.Add("- Evidence directory count: $($evidenceDirectories.Count)") | Out-Null
$summaryLines.Add("- Missing evidence directories: $(Format-SummaryList $missingMirrors)") | Out-Null
$summaryLines.Add("- Missing required evidence files: $(Format-SummaryList @($missingRequiredFiles))") | Out-Null
$summaryLines.Add("- Missing required evidence subdirectories: $(Format-SummaryList @($missingRequiredDirectories))") | Out-Null
$summaryLines.Add("- Sensitive file findings: $(Format-SummaryList @($forbiddenSensitiveFiles | ForEach-Object FullName))") | Out-Null
$summaryLines.Add("- Evidence status matrix consistency: $(if ($results | Where-Object { $_.Id -in @('V007', 'V008', 'V009') -and $_.Result -eq 'FAIL' }) { 'FAIL' } else { 'PASS' })") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("| Check ID | Check | Result | Detail |") | Out-Null
$summaryLines.Add("|---|---|---|---|") | Out-Null
foreach ($result in $results) {
    $safeDetail = $result.Detail.Replace("|", "\|")
    $summaryLines.Add("| $($result.Id) | $($result.Description) | $($result.Result) | $safeDetail |") | Out-Null
}
$summaryLines.Add("") | Out-Null
$summaryLines.Add("## Boundary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("S010 validates evidence structure and readiness governance only. It does not replace scenario-specific validation or the final evidence report in S050.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) {
    exit 1
}

exit 0
