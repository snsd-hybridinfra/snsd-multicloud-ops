$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$script:CriticalFailures = [System.Collections.Generic.List[string]]::new()
$script:Warnings = [System.Collections.Generic.List[string]]::new()

function Write-Pass {
    param([string] $Message)
    Write-Host "[PASS] $Message"
}

function Add-CriticalFailure {
    param([string] $Message)
    $script:CriticalFailures.Add($Message) | Out-Null
    Write-Host "[FAIL] $Message"
}

function Add-Warning {
    param([string] $Message)
    $script:Warnings.Add($Message) | Out-Null
    Write-Host "[WARN] $Message"
}

function Get-ScenarioId {
    param([string] $Name)
    return ([regex]::Match($Name, "^S\d{3}")).Value
}

function Get-RelativePath {
    param(
        [string] $BasePath,
        [string] $FullPath
    )

    return $FullPath.Substring($BasePath.Length + 1)
}

function Test-ExpectedIdSet {
    param(
        [string[]] $ActualIds,
        [string[]] $ExpectedIds,
        [string] $Label
    )

    $duplicates = @(
        $ActualIds |
            Group-Object |
            Where-Object { $_.Count -gt 1 } |
            ForEach-Object { $_.Name }
    )
    $missing = @($ExpectedIds | Where-Object { $_ -notin $ActualIds })
    $unexpected = @($ActualIds | Where-Object { $_ -notin $ExpectedIds } | Sort-Object -Unique)

    if ($ActualIds.Count -ne 50) {
        Add-CriticalFailure "$Label count is $($ActualIds.Count); expected 50."
    }
    else {
        Write-Pass "$Label count is 50."
    }

    if ($duplicates.Count -gt 0) {
        Add-CriticalFailure "$Label contains duplicate IDs: $($duplicates -join ', ')."
    }
    else {
        Write-Pass "$Label has no duplicate IDs."
    }

    if ($missing.Count -gt 0) {
        Add-CriticalFailure "$Label is missing IDs: $($missing -join ', ')."
    }
    else {
        Write-Pass "$Label contains S001 through S050."
    }

    if ($unexpected.Count -gt 0) {
        Add-CriticalFailure "$Label contains unexpected IDs: $($unexpected -join ', ')."
    }
}

$rootMarkers = @(
    "README.md",
    "AGENTS.md",
    "docs",
    "scenarios",
    "evidence",
    "tools"
)

$missingRootMarkers = @(
    $rootMarkers |
        Where-Object { -not (Test-Path -LiteralPath $_) }
)

if ($missingRootMarkers.Count -gt 0) {
    Write-Host "[FAIL] Script must be run from the repository root."
    foreach ($marker in $missingRootMarkers) {
        Write-Host "  - Missing root marker: $marker"
    }
    exit 1
}

$expectedIds = @(1..50 | ForEach-Object { "S{0:D3}" -f $_ })
$expectedLevelById = @{}

1..10 | ForEach-Object {
    $expectedLevelById[("S{0:D3}" -f $_)] = "L1-foundation"
}
11..20 | ForEach-Object {
    $expectedLevelById[("S{0:D3}" -f $_)] = "L2-security-baseline"
}
21..30 | ForEach-Object {
    $expectedLevelById[("S{0:D3}" -f $_)] = "L3-service-operations"
}
31..40 | ForEach-Object {
    $expectedLevelById[("S{0:D3}" -f $_)] = "L4-failure-recovery"
}
41..50 | ForEach-Object {
    $expectedLevelById[("S{0:D3}" -f $_)] = "L5-governance-intelligent-ops"
}

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

$requiredEvidenceFiles = @(
    "commands.md",
    "validation.md",
    "logs/.gitkeep",
    "screenshots/.gitkeep",
    "configs/.gitkeep"
)

$requiredEvidenceDirectories = @(
    "logs",
    "screenshots",
    "configs"
)

$requiredReadmeFields = @(
    "Scenario ID",
    "Scenario Name",
    "Level",
    "Category",
    "Objective Summary",
    "Scope Summary",
    "Related Components",
    "Validation Summary",
    "Evidence Output Summary",
    "Status"
)

$scenarioRoot = (Resolve-Path -LiteralPath "scenarios").Path
$evidenceRoot = (Resolve-Path -LiteralPath "evidence").Path

$scenarioDirectories = @(
    Get-ChildItem -LiteralPath "scenarios" -Directory -Recurse |
        Where-Object { $_.Name -match "^S\d{3}-.+" }
)
$evidenceDirectories = @(
    Get-ChildItem -LiteralPath "evidence" -Directory -Recurse |
        Where-Object { $_.Name -match "^S\d{3}-.+" }
)

$scenarioIds = @($scenarioDirectories | ForEach-Object { Get-ScenarioId -Name $_.Name })
$evidenceIds = @($evidenceDirectories | ForEach-Object { Get-ScenarioId -Name $_.Name })

Write-Host ""
Write-Host "Scenario and evidence structure:"
Test-ExpectedIdSet -ActualIds $scenarioIds -ExpectedIds $expectedIds -Label "Scenario directories"
Test-ExpectedIdSet -ActualIds $evidenceIds -ExpectedIds $expectedIds -Label "Evidence directories"

$levelErrors = [System.Collections.Generic.List[string]]::new()
foreach ($directory in $scenarioDirectories) {
    $id = Get-ScenarioId -Name $directory.Name
    $expectedLevel = $expectedLevelById[$id]
    if ($directory.Parent.Name -ne $expectedLevel) {
        $levelErrors.Add("$id is under $($directory.Parent.Name); expected $expectedLevel") | Out-Null
    }
}

if ($levelErrors.Count -eq 0) {
    Write-Pass "All scenarios are under the correct level directories."
}
else {
    foreach ($errorMessage in $levelErrors) {
        Add-CriticalFailure $errorMessage
    }
}

$scenarioRelativePaths = @(
    $scenarioDirectories |
        ForEach-Object { Get-RelativePath -BasePath $scenarioRoot -FullPath $_.FullName }
)
$evidenceRelativePaths = @(
    $evidenceDirectories |
        ForEach-Object { Get-RelativePath -BasePath $evidenceRoot -FullPath $_.FullName }
)

$missingEvidencePairs = @(
    $scenarioRelativePaths |
        Where-Object { $_ -notin $evidenceRelativePaths }
)
$orphanEvidencePairs = @(
    $evidenceRelativePaths |
        Where-Object { $_ -notin $scenarioRelativePaths }
)

if ($missingEvidencePairs.Count -eq 0 -and $orphanEvidencePairs.Count -eq 0) {
    Write-Pass "All scenario and evidence paths are mirrored one-to-one."
}
else {
    foreach ($path in $missingEvidencePairs) {
        Add-CriticalFailure "Matching evidence directory is missing for $path."
    }
    foreach ($path in $orphanEvidencePairs) {
        Add-CriticalFailure "Evidence directory has no matching scenario: $path."
    }
}

$scenarioFileIssues = [System.Collections.Generic.List[string]]::new()
$scenarioContentIssues = [System.Collections.Generic.List[string]]::new()
$evidencePathIssues = [System.Collections.Generic.List[string]]::new()
$evidenceMappingIssues = [System.Collections.Generic.List[string]]::new()

foreach ($scenarioDirectory in $scenarioDirectories | Sort-Object Name) {
    $scenarioId = Get-ScenarioId -Name $scenarioDirectory.Name

    foreach ($requiredFile in $requiredScenarioFiles) {
        $requiredPath = Join-Path -Path $scenarioDirectory.FullName -ChildPath $requiredFile
        if (-not (Test-Path -LiteralPath $requiredPath -PathType Leaf)) {
            $scenarioFileIssues.Add("$scenarioId missing $requiredFile") | Out-Null
        }
    }

    if (@($requiredScenarioFiles | Where-Object {
        -not (Test-Path -LiteralPath (Join-Path $scenarioDirectory.FullName $_) -PathType Leaf)
    }).Count -gt 0) {
        continue
    }

    $readmePath = Join-Path $scenarioDirectory.FullName "README.md"
    $scopePath = Join-Path $scenarioDirectory.FullName "scope.md"
    $validationPlanPath = Join-Path $scenarioDirectory.FullName "validation-plan.md"
    $evidenceMapPath = Join-Path $scenarioDirectory.FullName "evidence-map.md"

    $readmeContent = Get-Content -LiteralPath $readmePath -Raw
    $scopeContent = Get-Content -LiteralPath $scopePath -Raw
    $validationPlanLines = @(Get-Content -LiteralPath $validationPlanPath)
    $evidenceMapLines = @(Get-Content -LiteralPath $evidenceMapPath)

    $missingReadmeFields = @(
        $requiredReadmeFields |
            Where-Object { $readmeContent -notmatch [regex]::Escape($_) }
    )
    if ($missingReadmeFields.Count -gt 0) {
        $scenarioContentIssues.Add(
            "$scenarioId README missing fields: $($missingReadmeFields -join ', ')"
        ) | Out-Null
    }

    if ($scopeContent -notmatch "(?im)^## Included\s*$") {
        $scenarioContentIssues.Add("$scenarioId scope.md missing Included section") | Out-Null
    }
    if ($scopeContent -notmatch "(?im)^## Excluded\s*$") {
        $scenarioContentIssues.Add("$scenarioId scope.md missing Excluded section") | Out-Null
    }

    $validationRows = @(
        $validationPlanLines |
            Where-Object { $_ -match "^\|\s*[A-Z]{1,3}\d{3}\s*\|" }
    )
    $evidenceRows = @(
        $evidenceMapLines |
            Where-Object {
                $_ -match "^\|" -and
                $_ -notmatch "^\|\s*(Validation Item|Validation Check|---)"
            }
    )

    if ($validationRows.Count -eq 0) {
        $scenarioContentIssues.Add("$scenarioId validation-plan.md has no check rows") | Out-Null
    }

    $validationCheckIds = @()
    foreach ($validationRow in $validationRows) {
        $validationCells = @($validationRow.Trim().Trim("|") -split "\|")
        if ($validationCells.Count -lt 2) {
            $evidenceMappingIssues.Add("$scenarioId has an unreadable validation row") | Out-Null
            continue
        }

        $checkId = $validationCells[0].Trim()
        $validationItem = $validationCells[1].Trim()
        $validationCheckIds += $checkId
        $mapped = $false

        foreach ($evidenceRow in $evidenceRows) {
            $evidenceCells = @($evidenceRow.Trim().Trim("|") -split "\|")
            if ($evidenceCells.Count -lt 1) {
                continue
            }

            $mapItem = $evidenceCells[0].Trim()
            $mapItemWithoutId = ($mapItem -replace "^[A-Z]{1,3}\d{3}\s+", "").Trim()
            if (
                $mapItem -match ("^" + [regex]::Escape($checkId) + "(\s|$)") -or
                $mapItemWithoutId.Equals($validationItem, [System.StringComparison]::OrdinalIgnoreCase)
            ) {
                $mapped = $true
                break
            }
        }

        if (-not $mapped) {
            $evidenceMappingIssues.Add(
                "$scenarioId $checkId is not mapped by ID or validation-item name"
            ) | Out-Null
        }
    }

    $duplicateCheckIds = @(
        $validationCheckIds |
            Group-Object |
            Where-Object { $_.Count -gt 1 } |
            ForEach-Object { $_.Name }
    )
    if ($duplicateCheckIds.Count -gt 0) {
        $evidenceMappingIssues.Add(
            "$scenarioId has duplicate validation IDs: $($duplicateCheckIds -join ', ')"
        ) | Out-Null
    }

    $relativeScenarioPath = Get-RelativePath -BasePath $scenarioRoot -FullPath $scenarioDirectory.FullName
    $matchingEvidenceDirectory = Join-Path $evidenceRoot $relativeScenarioPath

    foreach ($requiredFile in $requiredEvidenceFiles) {
        $requiredPath = Join-Path -Path $matchingEvidenceDirectory -ChildPath $requiredFile
        if (-not (Test-Path -LiteralPath $requiredPath -PathType Leaf)) {
            $evidencePathIssues.Add("$scenarioId evidence missing $requiredFile") | Out-Null
        }
    }
    foreach ($requiredDirectory in $requiredEvidenceDirectories) {
        $requiredPath = Join-Path -Path $matchingEvidenceDirectory -ChildPath $requiredDirectory
        if (-not (Test-Path -LiteralPath $requiredPath -PathType Container)) {
            $evidencePathIssues.Add("$scenarioId evidence missing $requiredDirectory/") | Out-Null
        }
    }

    $commandsPath = Join-Path $matchingEvidenceDirectory "commands.md"
    $validationPath = Join-Path $matchingEvidenceDirectory "validation.md"
    if (Test-Path -LiteralPath $commandsPath -PathType Leaf) {
        $commandsContent = Get-Content -LiteralPath $commandsPath -Raw
        if ($commandsContent -notmatch "(?i)TODO|NOT_RUN|planned") {
            $scenarioContentIssues.Add(
                "$scenarioId commands.md does not identify planned or not-run output"
            ) | Out-Null
        }
    }
    if (Test-Path -LiteralPath $validationPath -PathType Leaf) {
        $validationContent = Get-Content -LiteralPath $validationPath -Raw
        if (
            $validationContent -notmatch "(?i)Actual Result" -or
            $validationContent -notmatch "(?i)Status"
        ) {
            $scenarioContentIssues.Add(
                "$scenarioId validation.md is missing result or status fields"
            ) | Out-Null
        }
    }
}

if ($scenarioFileIssues.Count -eq 0) {
    Write-Pass "All 50 scenarios contain the 11 required files."
}
else {
    foreach ($issue in $scenarioFileIssues) {
        Add-CriticalFailure $issue
    }
}

if ($evidencePathIssues.Count -eq 0) {
    Write-Pass "All 50 evidence directories contain required files and subdirectories."
}
else {
    foreach ($issue in $evidencePathIssues) {
        Add-CriticalFailure $issue
    }
}

if ($scenarioContentIssues.Count -eq 0) {
    Write-Pass "Scenario metadata, scope sections, and evidence placeholders pass quality checks."
}
else {
    foreach ($issue in $scenarioContentIssues) {
        Add-CriticalFailure $issue
    }
}

if ($evidenceMappingIssues.Count -eq 0) {
    Write-Pass "Every validation item maps to evidence by check ID or item name."
}
else {
    foreach ($issue in $evidenceMappingIssues) {
        Add-CriticalFailure $issue
    }
}

Write-Host ""
Write-Host "Tracking consistency:"

$scenarioMatrixPath = "docs/scenario-status-matrix.md"
$evidenceMatrixPath = "docs/evidence-status-matrix.md"
$progressTrackerPath = "docs/progress-tracker.md"

if (
    -not (Test-Path -LiteralPath $scenarioMatrixPath -PathType Leaf) -or
    -not (Test-Path -LiteralPath $evidenceMatrixPath -PathType Leaf) -or
    -not (Test-Path -LiteralPath $progressTrackerPath -PathType Leaf)
) {
    Add-CriticalFailure "One or more required tracking files are missing."
}
else {
    $scenarioMatrixRows = @(
        Get-Content -LiteralPath $scenarioMatrixPath |
            Where-Object { $_ -match "^\|\s*S\d{3}\s*\|" }
    )
    $scenarioMatrixIds = @(
        $scenarioMatrixRows |
            ForEach-Object { ([regex]::Match($_, "S\d{3}")).Value }
    )
    $evidenceMatrixRows = @(
        Get-Content -LiteralPath $evidenceMatrixPath |
            Where-Object { $_ -match "^\|\s*S\d{3}\s*\|" }
    )
    $evidenceMatrixIds = @(
        $evidenceMatrixRows |
            ForEach-Object { ([regex]::Match($_, "S\d{3}")).Value }
    )

    Test-ExpectedIdSet -ActualIds $scenarioMatrixIds -ExpectedIds $expectedIds -Label "Scenario status matrix"
    Test-ExpectedIdSet -ActualIds $evidenceMatrixIds -ExpectedIds $expectedIds -Label "Evidence status matrix"

    $progressContent = Get-Content -LiteralPath $progressTrackerPath -Raw
    $missingLevels = @(
        @("L1", "L2", "L3", "L4", "L5") |
            Where-Object { $progressContent -notmatch ("\|\s*" + $_ + "\s*\|") }
    )
    if ($missingLevels.Count -eq 0 -and $progressContent -match "\|\s*Total\s*\|\s*All Levels\s*\|\s*50/50\s*\|") {
        Write-Pass "Progress tracker contains L1 through L5 and a 50/50 total."
    }
    else {
        Add-CriticalFailure "Progress tracker is missing a level or the 50/50 total."
    }
}

Write-Host ""
Write-Host "Scope and governance consistency:"

$scenarioModelPath = "docs/scenario-model.md"
$namingRulesPath = "docs/naming-rules.md"

if (-not (Test-Path -LiteralPath $scenarioModelPath -PathType Leaf)) {
    Add-CriticalFailure "Canonical scenario model is missing."
}
else {
    $scenarioModelContent = Get-Content -LiteralPath $scenarioModelPath -Raw
    $modelMissingIds = @(
        $expectedIds |
            Where-Object {
                $scenarioModelContent -notmatch (
                    "(?<!\d)" + [regex]::Escape($_) + "(?!\d)"
                )
            }
    )
    if ($modelMissingIds.Count -eq 0) {
        Write-Pass "Canonical scenario model contains S001 through S050."
    }
    else {
        Add-CriticalFailure (
            "Canonical scenario model does not define the implemented S001-S050 set " +
            "($($modelMissingIds.Count) IDs missing)."
        )
    }

    $trackingStatuses = @(
        "NOT_STARTED",
        "PLANNED",
        "IN_PROGRESS",
        "IMPLEMENTED",
        "VALIDATED",
        "PARTIAL",
        "BLOCKED",
        "DEPRECATED"
    )
    $missingModelStatuses = @(
        $trackingStatuses |
            Where-Object { $scenarioModelContent -notmatch [regex]::Escape($_) }
    )
    if ($missingModelStatuses.Count -gt 0) {
        Add-Warning (
            "Scenario model lifecycle statuses differ from tracking statuses: " +
            "$($missingModelStatuses -join ', ')."
        )
    }
}

if (-not (Test-Path -LiteralPath $namingRulesPath -PathType Leaf)) {
    Add-CriticalFailure "Naming rules document is missing."
}
else {
    $namingRulesContent = Get-Content -LiteralPath $namingRulesPath -Raw
    if (
        $namingRulesContent -match "S###" -or
        $namingRulesContent -match "S<three-digit-number>" -or
        $namingRulesContent -match "S\\d\{3\}"
    ) {
        Write-Pass "Naming rules define the S### scenario ID format."
    }
    else {
        Add-CriticalFailure "Naming rules do not define the implemented S### scenario ID format."
    }
}

if (Test-Path -LiteralPath "docs/scenario-template.md" -PathType Leaf) {
    $scenarioTemplateContent = Get-Content -LiteralPath "docs/scenario-template.md" -Raw
    if ($scenarioTemplateContent -notmatch "IMPLEMENTED") {
        Add-Warning "Scenario template omits the IMPLEMENTED tracking status."
    }
}

if (
    (Test-Path -LiteralPath "docs/evidence-model.md" -PathType Leaf) -and
    (Test-Path -LiteralPath "docs/evidence-status-matrix.md" -PathType Leaf)
) {
    $evidenceModelContent = Get-Content -LiteralPath "docs/evidence-model.md" -Raw
    $evidenceMatrixContent = Get-Content -LiteralPath "docs/evidence-status-matrix.md" -Raw
    if (
        $evidenceModelContent -match "## Evidence Status Model" -and
        $evidenceModelContent -match "\bPASS\b" -and
        $evidenceMatrixContent -match "\bNOT_READY\b"
    ) {
        Add-Warning (
            "Evidence model and evidence matrix use different status models " +
            "without distinct names for validation result and evidence readiness."
        )
    }
}

$forbiddenPatterns = @(
    [pscustomobject]@{ Name = "production-grade HA"; Pattern = "production-grade\s+HA" },
    [pscustomobject]@{ Name = "automatic DR"; Pattern = "automatic\s+DR" },
    [pscustomobject]@{ Name = "automatic cross-cloud failover"; Pattern = "automatic\s+cross-cloud\s+failover" },
    [pscustomobject]@{ Name = "Wazuh"; Pattern = "\bWazuh\b" },
    [pscustomobject]@{ Name = "Elastic SIEM"; Pattern = "\bElastic\s+SIEM\b" },
    [pscustomobject]@{ Name = "EDR"; Pattern = "\bEDR\b" },
    [pscustomobject]@{ Name = "SOAR"; Pattern = "\bSOAR\b" },
    [pscustomobject]@{ Name = "threat hunting"; Pattern = "threat\s+hunting" },
    [pscustomobject]@{ Name = "malware detection"; Pattern = "malware\s+detection" },
    [pscustomobject]@{ Name = "packet payload"; Pattern = "packet\s+payload" },
    [pscustomobject]@{ Name = "deep learning"; Pattern = "deep[- ]learning" },
    [pscustomobject]@{ Name = "formal certification"; Pattern = "(ISO\s+27001|ISMS-P|SOC\s+2)\s+certified" },
    [pscustomobject]@{ Name = "Terraform Cloud"; Pattern = "\bTerraform\s+Cloud\b" },
    [pscustomobject]@{ Name = "Atlantis"; Pattern = "\bAtlantis\b" },
    [pscustomobject]@{ Name = "Spacelift"; Pattern = "\bSpacelift\b" },
    [pscustomobject]@{ Name = "Argo CD"; Pattern = "\bArgo\s+CD\b" },
    [pscustomobject]@{ Name = "Istio"; Pattern = "\bIstio\b" },
    [pscustomobject]@{ Name = "service mesh"; Pattern = "\bservice\s+mesh\b" },
    [pscustomobject]@{ Name = "real-time blocking"; Pattern = "real-time\s+(automated\s+)?blocking" }
)

$governanceFiles = @(
    "AGENTS.md",
    "docs/scope-lock.md",
    "docs/excluded-scope.md",
    "docs/scenario-model.md",
    "docs/evidence-model.md",
    "docs/naming-rules.md",
    "docs/progress-tracker.md",
    "docs/scenario-status-matrix.md",
    "docs/evidence-status-matrix.md",
    "docs/validation-checklist.md",
    "docs/implementation-log.md",
    "docs/risk-register.md"
) | Where-Object { Test-Path -LiteralPath $_ -PathType Leaf }

$claimScanFiles = @(
    Get-ChildItem -LiteralPath "scenarios", "evidence" -File -Recurse -Filter "*.md"
) + @(
    $governanceFiles | ForEach-Object { Get-Item -LiteralPath $_ }
)

$unsupportedClaims = [System.Collections.Generic.List[string]]::new()
$boundaryReferenceCount = 0
$safeContextPattern = (
    "(?i)(\b(no|not|without|exclude(?:d|s)?|" +
    "prohibit(?:ed|s)?|must\s+not|do\s+not|does\s+not|cannot|avoid|" +
    "unless|failure|unsupported)\b|out[_ -]?of[_ -]?scope)"
)

foreach ($file in $claimScanFiles) {
    $section = ""
    $lineNumber = 0
    foreach ($line in Get-Content -LiteralPath $file.FullName) {
        $lineNumber++
        if ($line -match "^\s*#{1,6}\s+(.+?)\s*$") {
            $section = $Matches[1]
        }

        foreach ($forbiddenPattern in $forbiddenPatterns) {
            if ($line -notmatch ("(?i)" + $forbiddenPattern.Pattern)) {
                continue
            }

            $isBoundaryContext = (
                $line -match $safeContextPattern -or
                $section -match "(?i)excluded|boundary|prohibited" -or
                $file.Name -match "(?i)^failure-condition\.md$|^rollback-plan\.md$"
            )

            if ($isBoundaryContext) {
                $boundaryReferenceCount++
            }
            else {
                $relativePath = Get-RelativePath -BasePath (Get-Location).Path -FullPath $file.FullName
                $unsupportedClaims.Add(
                    "$($forbiddenPattern.Name) at ${relativePath}:$lineNumber"
                ) | Out-Null
            }
        }
    }
}

if ($unsupportedClaims.Count -eq 0) {
    Write-Pass (
        "No unsupported affirmative capability claims found; " +
        "$boundaryReferenceCount exclusion or boundary references reviewed."
    )
}
else {
    foreach ($claim in $unsupportedClaims) {
        Add-CriticalFailure "Unsupported claim candidate: $claim."
    }
}

Write-Host ""
Write-Host "Sensitive-file safety:"

$repositoryFiles = @(
    Get-ChildItem -LiteralPath "." -File -Recurse -Force |
        Where-Object { $_.FullName -notmatch "[\\/]\.git[\\/]" }
)

$riskyFileNamePattern = (
    "(?i)(^|\.)kubeconfig($|\.)|^id_(rsa|dsa|ecdsa|ed25519)(\.|$)|" +
    "\.tfstate($|\.)|\.tfvars($|\.)|\.pem$|\.key$|\.p12$|\.pfx$|" +
    "\.jks$|\.keystore$|\.env($|\.)|openrc|clouds\.ya?ml$|" +
    "credentials?|private[-_]?key|access[-_]?key|api[-_]?key|" +
    "\.sql$|\.dump$|\.bak$|\.tar$|\.gz$|\.zip$"
)

$riskyFiles = @(
    $repositoryFiles |
        Where-Object { $_.Name -match $riskyFileNamePattern }
)

if ($riskyFiles.Count -eq 0) {
    Write-Pass "No risky secret, state, configuration, archive, or database-dump filenames found."
}
else {
    foreach ($file in $riskyFiles) {
        $relativePath = Get-RelativePath -BasePath (Get-Location).Path -FullPath $file.FullName
        Add-CriticalFailure "Risky filename found: $relativePath."
    }
}

$textExtensions = @(
    ".md",
    ".ps1",
    ".txt",
    ".yml",
    ".yaml",
    ".json",
    ".conf",
    ".ini",
    ".tf"
)

$sensitiveContentPatterns = @(
    "-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----",
    "\b(?:AKIA|ASIA)[A-Z0-9]{16}\b",
    (
        "(?i)\b(?:password|passwd|api[_-]?key|access[_-]?key|secret|token)" +
        "\s*[:=]\s*['""]?(?!<|TODO|TBD|placeholder|NOT_|none|null)" +
        "[A-Za-z0-9/+_.=-]{8,}"
    ),
    "\b\d{12}\b",
    (
        "\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-" +
        "[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b"
    )
)

$sensitiveContentHits = [System.Collections.Generic.List[string]]::new()
foreach ($file in $repositoryFiles | Where-Object { $_.Extension -in $textExtensions }) {
    $lineNumber = 0
    foreach ($line in Get-Content -LiteralPath $file.FullName) {
        $lineNumber++
        foreach ($pattern in $sensitiveContentPatterns) {
            if ($line -match $pattern) {
                $relativePath = Get-RelativePath -BasePath (Get-Location).Path -FullPath $file.FullName
                $sensitiveContentHits.Add("${relativePath}:$lineNumber") | Out-Null
                break
            }
        }
    }
}

if ($sensitiveContentHits.Count -eq 0) {
    Write-Pass "No private-key, access-key, account-ID, UUID, or secret-assignment candidates found."
}
else {
    foreach ($hit in $sensitiveContentHits) {
        Add-CriticalFailure "Sensitive content candidate found at $hit."
    }
}

Write-Host ""
Write-Host "QA summary:"
Write-Host "  Scenario directories: $($scenarioDirectories.Count)"
Write-Host "  Evidence directories: $($evidenceDirectories.Count)"
Write-Host "  Critical failures: $($script:CriticalFailures.Count)"
Write-Host "  Warnings: $($script:Warnings.Count)"

if ($script:Warnings.Count -gt 0) {
    Write-Host "Warnings:"
    foreach ($warning in $script:Warnings) {
        Write-Host "  - $warning"
    }
}

if ($script:CriticalFailures.Count -eq 0) {
    Write-Pass "Scenario quality validation passed."
    exit 0
}

Write-Host "Critical failures:"
foreach ($failure in $script:CriticalFailures) {
    Write-Host "  - $failure"
}
Write-Host "[FAIL] Scenario quality validation failed."
exit 1
