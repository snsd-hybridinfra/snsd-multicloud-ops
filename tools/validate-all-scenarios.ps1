[CmdletBinding()]
param(
    [switch] $GenerateReports
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$sourceRepositoryRoot = Split-Path -Parent $PSScriptRoot
$stateModulePath = Join-Path $PSScriptRoot "modules\RepositoryValidationSafety.psm1"
Import-Module -Name $stateModulePath -Force

$repositoryStateBefore = Get-RepositoryStateSnapshot -RepositoryRoot $sourceRepositoryRoot
$temporaryContainer = $null
$executionError = $null
$cleanupError = $null
$validationExitCode = 2

try {
    if ($GenerateReports) {
        $repositoryRoot = $sourceRepositoryRoot
        $validationToolsRoot = $PSScriptRoot
        $validationMode = "GenerateReports"
    }
    else {
        $temporaryContainer = Join-Path ([System.IO.Path]::GetTempPath()) ("snsd-scenario-validation-" + [guid]::NewGuid().ToString('N'))
        $repositoryRoot = Join-Path $temporaryContainer "repository"
        New-Item -ItemType Directory -Force -Path $repositoryRoot | Out-Null
        foreach ($item in Get-ChildItem -LiteralPath $sourceRepositoryRoot -Force) {
            if ($item.Name -in @('.git', '.runtime')) {
                continue
            }
            Copy-Item -LiteralPath $item.FullName -Destination $repositoryRoot -Recurse -Force
        }
        $validationToolsRoot = Join-Path $repositoryRoot "tools"
        $validationMode = "ReadOnlyIsolated"
    }

$evidenceRoot = Join-Path $repositoryRoot "evidence\L5-governance-intelligent-ops\S050-final-evidence-report-generation-validation"
$logPath = Join-Path $evidenceRoot "logs\repo-wide-validation.log"
$summaryPath = Join-Path $evidenceRoot "configs\repo-wide-validation-summary.md"
$powerShellExecutable = (Get-Process -Id $PID).Path

$expectedScenarioPaths = @(
    "L1-foundation/S001-control-plane-toolchain-validation",
    "L1-foundation/S002-eve-ng-on-prem-routing-validation",
    "L1-foundation/S003-aws-network-provisioning-validation",
    "L1-foundation/S004-azure-network-provisioning-validation",
    "L1-foundation/S005-openstack-network-provisioning-validation",
    "L1-foundation/S006-terraform-provider-validation",
    "L1-foundation/S007-multi-cloud-inventory-validation",
    "L1-foundation/S008-bastion-reachability-validation",
    "L1-foundation/S009-dns-hostname-resolution-validation",
    "L1-foundation/S010-evidence-directory-structure-validation",
    "L2-security-baseline/S011-ssh-key-authentication-validation",
    "L2-security-baseline/S012-password-login-denial-validation",
    "L2-security-baseline/S013-root-login-denial-validation",
    "L2-security-baseline/S014-aws-security-group-least-privilege-validation",
    "L2-security-baseline/S015-azure-nsg-least-privilege-validation",
    "L2-security-baseline/S016-openstack-security-group-validation",
    "L2-security-baseline/S017-mariadb-access-control-validation",
    "L2-security-baseline/S018-kubernetes-rbac-validation",
    "L2-security-baseline/S019-nginx-security-header-validation",
    "L2-security-baseline/S020-grafana-anonymous-access-denial-validation",
    "L3-service-operations/S021-kubernetes-node-readiness-validation",
    "L3-service-operations/S022-kubernetes-workload-deployment-validation",
    "L3-service-operations/S023-ingress-routing-validation",
    "L3-service-operations/S024-nginx-reverse-proxy-validation",
    "L3-service-operations/S025-load-balancing-health-check-validation",
    "L3-service-operations/S026-mariadb-primary-replica-replication-validation",
    "L3-service-operations/S027-db-replication-lag-validation",
    "L3-service-operations/S028-prometheus-target-discovery-validation",
    "L3-service-operations/S029-grafana-dashboard-validation",
    "L3-service-operations/S030-blackbox-endpoint-probe-validation",
    "L4-failure-recovery/S031-web-pod-failure-recovery-validation",
    "L4-failure-recovery/S032-api-service-failure-validation",
    "L4-failure-recovery/S033-db-replica-failure-validation",
    "L4-failure-recovery/S034-db-primary-stop-runbook-validation",
    "L4-failure-recovery/S035-load-balancer-failure-validation",
    "L4-failure-recovery/S036-prometheus-target-down-validation",
    "L4-failure-recovery/S037-security-rule-misconfiguration-validation",
    "L4-failure-recovery/S038-backup-creation-validation",
    "L4-failure-recovery/S039-restore-execution-validation",
    "L4-failure-recovery/S040-service-health-after-recovery-validation",
    "L5-governance-intelligent-ops/S041-terraform-drift-detection-validation",
    "L5-governance-intelligent-ops/S042-terraform-drift-remediation-validation",
    "L5-governance-intelligent-ops/S043-policy-as-code-validation",
    "L5-governance-intelligent-ops/S044-kubernetes-manifest-policy-validation",
    "L5-governance-intelligent-ops/S045-cost-guardrail-validation",
    "L5-governance-intelligent-ops/S046-resource-cleanup-validation",
    "L5-governance-intelligent-ops/S047-ml-metric-dataset-collection-validation",
    "L5-governance-intelligent-ops/S048-ml-anomaly-detection-validation",
    "L5-governance-intelligent-ops/S049-ml-anomaly-report-generation-validation",
    "L5-governance-intelligent-ops/S050-final-evidence-report-generation-validation"
)

$requiredScenarioFiles = @(
    "README.md", "objective.md", "scope.md", "architecture.md", "prerequisites.md",
    "execution-plan.md", "validation-plan.md", "expected-result.md", "failure-condition.md",
    "rollback-plan.md", "evidence-map.md"
)
$requiredEvidenceFiles = @("commands.md", "validation.md")
$requiredEvidenceDirectories = @("logs", "screenshots", "configs")
$scenarioStatuses = @("NOT_STARTED", "PLANNED", "IN_PROGRESS", "IMPLEMENTED", "VALIDATED", "PARTIAL", "BLOCKED", "DEPRECATED")
$evidenceStatuses = @("NOT_READY", "PARTIAL", "READY", "REVIEWED")
$integrationResults = [System.Collections.Generic.List[object]]::new()
$validatorResults = [System.Collections.Generic.List[object]]::new()
$logLines = [System.Collections.Generic.List[string]]::new()

function Add-IntegrationResult {
    param([string]$Name, [bool]$Passed, [string]$Detail)
    $integrationResults.Add([pscustomobject]@{
        Name = $Name
        Status = if ($Passed) { "PASS" } else { "FAIL" }
        Detail = $Detail
    }) | Out-Null
}

function Get-ScenarioText {
    param([string]$ScenarioId)
    $directory = Get-ChildItem -Path (Join-Path $repositoryRoot "scenarios") -Recurse -Directory |
        Where-Object { $_.Name -like "$ScenarioId-*" } |
        Select-Object -First 1
    if ($null -eq $directory) { return "" }
    return ((Get-ChildItem -LiteralPath $directory.FullName -File | ForEach-Object {
        Get-Content -LiteralPath $_.FullName -Raw
    }) -join "`n")
}

$actualScenarioPaths = @(Get-ChildItem -Path (Join-Path $repositoryRoot "scenarios") -Recurse -Directory |
    Where-Object { $_.Name -match '^S\d{3}-' } |
    ForEach-Object { $_.FullName.Substring((Join-Path $repositoryRoot "scenarios").Length + 1).Replace('\', '/') } |
    Sort-Object)
$actualEvidencePaths = @(Get-ChildItem -Path (Join-Path $repositoryRoot "evidence") -Recurse -Directory |
    Where-Object { $_.Name -match '^S\d{3}-' } |
    ForEach-Object { $_.FullName.Substring((Join-Path $repositoryRoot "evidence").Length + 1).Replace('\', '/') } |
    Sort-Object)
$expectedSorted = @($expectedScenarioPaths | Sort-Object)

Add-IntegrationResult "ScenarioCoverage" (($actualScenarioPaths.Count -eq 50) -and (@(Compare-Object $expectedSorted $actualScenarioPaths).Count -eq 0)) "Expected locked S001-S050 scenario paths exist exactly once."
Add-IntegrationResult "EvidenceCoverage" (($actualEvidencePaths.Count -eq 50) -and (@(Compare-Object $expectedSorted $actualEvidencePaths).Count -eq 0)) "Evidence paths mirror the locked scenario paths."

$missingScenarioFiles = [System.Collections.Generic.List[string]]::new()
$missingEvidenceItems = [System.Collections.Generic.List[string]]::new()
foreach ($relativePath in $expectedScenarioPaths) {
    $scenarioPath = Join-Path (Join-Path $repositoryRoot "scenarios") $relativePath
    $scenarioEvidencePath = Join-Path (Join-Path $repositoryRoot "evidence") $relativePath
    foreach ($fileName in $requiredScenarioFiles) {
        if (-not (Test-Path -LiteralPath (Join-Path $scenarioPath $fileName) -PathType Leaf)) {
            $missingScenarioFiles.Add("$relativePath/$fileName") | Out-Null
        }
    }
    foreach ($fileName in $requiredEvidenceFiles) {
        if (-not (Test-Path -LiteralPath (Join-Path $scenarioEvidencePath $fileName) -PathType Leaf)) {
            $missingEvidenceItems.Add("$relativePath/$fileName") | Out-Null
        }
    }
    foreach ($directoryName in $requiredEvidenceDirectories) {
        if (-not (Test-Path -LiteralPath (Join-Path $scenarioEvidencePath $directoryName) -PathType Container)) {
            $missingEvidenceItems.Add("$relativePath/$directoryName/") | Out-Null
        }
    }
}
Add-IntegrationResult "ScenarioRequiredDocs" ($missingScenarioFiles.Count -eq 0) $(if ($missingScenarioFiles.Count -eq 0) { "All scenarios contain the 11 required documents." } else { $missingScenarioFiles -join ", " })
Add-IntegrationResult "EvidenceRequiredItems" ($missingEvidenceItems.Count -eq 0) $(if ($missingEvidenceItems.Count -eq 0) { "All evidence directories contain commands, validation, logs, screenshots, and configs." } else { $missingEvidenceItems -join ", " })

$scenarioMatrix = Get-Content -LiteralPath (Join-Path $repositoryRoot "docs\scenario-status-matrix.md") -Raw
$evidenceMatrix = Get-Content -LiteralPath (Join-Path $repositoryRoot "docs\evidence-status-matrix.md") -Raw
$invalidScenarioRows = @([regex]::Matches($scenarioMatrix, '(?m)^\|\s*S\d{3}\s*\|.*?\|\s*([A-Z_]+)\s*\|') | Where-Object { $_.Groups[1].Value -notin $scenarioStatuses })
$invalidEvidenceRows = @([regex]::Matches($evidenceMatrix, '(?m)^\|\s*S\d{3}\s*\|.*?\|\s*([A-Z_]+)\s*\|') | Where-Object { $_.Groups[1].Value -notin $evidenceStatuses })
Add-IntegrationResult "ScenarioStatusModel" ($invalidScenarioRows.Count -eq 0) "Scenario matrix uses only canonical scenario statuses."
Add-IntegrationResult "EvidenceStatusModel" ($invalidEvidenceRows.Count -eq 0) "Evidence matrix uses only canonical readiness statuses."

$crossReferences = @(
    @("S041", @("S042")),
    @("S042", @("S043", "S045")),
    @("S043", @("S044", "S045", "S046")),
    @("S044", @("S043", "S018")),
    @("S045", @("S046", "S050")),
    @("S046", @("S045", "S050")),
    @("S047", @("S048", "S049")),
    @("S048", @("S047", "S049")),
    @("S049", @("S050"))
)
$missingReferences = [System.Collections.Generic.List[string]]::new()
foreach ($mapping in $crossReferences) {
    $sourceText = Get-ScenarioText $mapping[0]
    foreach ($target in $mapping[1]) {
        if ($sourceText -notmatch [regex]::Escape($target)) {
            $missingReferences.Add("$($mapping[0])->$target") | Out-Null
        }
    }
}
$s050Text = Get-ScenarioText "S050"
if ($s050Text -notmatch 'S001' -or $s050Text -notmatch 'S050') {
    $missingReferences.Add("S050->S001-S050") | Out-Null
}
Add-IntegrationResult "CrossScenarioReferences" ($missingReferences.Count -eq 0) $(if ($missingReferences.Count -eq 0) { "Required ownership and hand-off references are present." } else { $missingReferences -join ", " })

$baseValidatorNames = @("validate-repo-structure.ps1", "validate-scenario-quality.ps1")
$repositoryValidatorNames = @("validate-all-scenarios.ps1", "validate-zero-trust.ps1")
$excludedValidatorNames = $repositoryValidatorNames + $baseValidatorNames
$scenarioValidators = @(Get-ChildItem -LiteralPath $validationToolsRoot -File -Filter "validate-*.ps1" |
    Where-Object { $_.Name -notin $excludedValidatorNames } |
    Sort-Object Name)
Add-IntegrationResult "ValidatorCoverage" ($scenarioValidators.Count -eq 50) "Discovered $($scenarioValidators.Count) scenario-specific local validators."

$validators = @($baseValidatorNames | ForEach-Object { Get-Item -LiteralPath (Join-Path $validationToolsRoot $_) }) + $scenarioValidators
$previousStaticMode = $env:SNSD_REPO_WIDE_STATIC_ONLY
$env:SNSD_REPO_WIDE_STATIC_ONLY = "1"

Push-Location $repositoryRoot
try {
    foreach ($validator in $validators) {
        $logLines.Add("=== $($validator.Name) ===") | Out-Null
        $output = @(& $powerShellExecutable -NoProfile -ExecutionPolicy Bypass -File $validator.FullName 2>&1)
        $exitCode = $LASTEXITCODE
        foreach ($line in $output) { $logLines.Add([string]$line) | Out-Null }
        $warningCount = @($output | Where-Object { [string]$_ -match '^\[WARN\]' }).Count
        $status = if ($exitCode -ne 0) { "FAIL" } elseif ($warningCount -gt 0) { "PASS_WITH_WARNINGS" } else { "PASS" }
        $validatorResults.Add([pscustomobject]@{
            Validator = $validator.Name
            Status = $status
            ExitCode = $exitCode
            Warnings = $warningCount
        }) | Out-Null
        Write-Host ("[{0}] {1} (exit={2}, warnings={3})" -f $status, $validator.Name, $exitCode, $warningCount)
    }
}
finally {
    Pop-Location
    if ($null -eq $previousStaticMode) {
        Remove-Item Env:SNSD_REPO_WIDE_STATIC_ONLY -ErrorAction SilentlyContinue
    }
    else {
        $env:SNSD_REPO_WIDE_STATIC_ONLY = $previousStaticMode
    }
}

$integrationFailures = @($integrationResults | Where-Object Status -eq "FAIL").Count
$validatorFailures = @($validatorResults | Where-Object Status -eq "FAIL").Count
$warningTotal = ($validatorResults | Measure-Object -Property Warnings -Sum).Sum
$finalStatus = if (($integrationFailures + $validatorFailures) -eq 0) { "PASS" } else { "FAIL" }
$validatorPassCount = @($validatorResults | Where-Object Status -eq "PASS").Count
$validatorWarnCount = @($validatorResults | Where-Object Status -eq "PASS_WITH_WARNINGS").Count
$scenarioValidatorNames = @($scenarioValidators | ForEach-Object Name)
$scenarioResults = @($validatorResults | Where-Object { $_.Validator -in $scenarioValidatorNames })
$scenarioPassCount = @($scenarioResults | Where-Object Status -eq "PASS").Count
$scenarioWarnCount = @($scenarioResults | Where-Object Status -eq "PASS_WITH_WARNINGS").Count
$scenarioFailCount = @($scenarioResults | Where-Object Status -eq "FAIL").Count

if ($GenerateReports) {
    $generatedAt = Get-Date -Format "yyyy-MM-ddTHH:mm:ssK"
    New-Item -ItemType Directory -Force -Path (Split-Path $logPath), (Split-Path $summaryPath) | Out-Null

    $logHeader = @(
        "SNSD REPOSITORY-WIDE LOCAL VALIDATION",
        "Generated: $generatedAt",
        "Mode: StaticOnlyGenerateReports",
        "No Terraform, kubectl, cloud CLI, monitoring query, or external service was invoked by this wrapper.",
        ""
    )
    Set-Content -LiteralPath $logPath -Value @($logHeader + $logLines) -Encoding UTF8

    $summaryLines = [System.Collections.Generic.List[string]]::new()
    $summaryLines.Add("# Repository-Wide Validation Summary") | Out-Null
    $summaryLines.Add("") | Out-Null
    $summaryLines.Add("- Generated: $generatedAt") | Out-Null
    $summaryLines.Add("- Mode: **StaticOnlyGenerateReports**") | Out-Null
    $summaryLines.Add("- Final result: **$finalStatus**") | Out-Null
    $summaryLines.Add("- Integration failures: **$integrationFailures**") | Out-Null
    $summaryLines.Add("- Validator failures: **$validatorFailures**") | Out-Null
    $summaryLines.Add("- Non-blocking validator warnings: **$warningTotal**") | Out-Null
    $summaryLines.Add("- Scenario results: **PASS=$scenarioPassCount WARN=$scenarioWarnCount FAIL=$scenarioFailCount**") | Out-Null
    $summaryLines.Add("") | Out-Null
    $summaryLines.Add("## Integration Checks") | Out-Null
    $summaryLines.Add("") | Out-Null
    $summaryLines.Add("| Check | Status | Detail |") | Out-Null
    $summaryLines.Add("|---|---|---|") | Out-Null
    foreach ($result in $integrationResults) {
        $detail = $result.Detail.Replace('|', '\|')
        $summaryLines.Add("| $($result.Name) | $($result.Status) | $detail |") | Out-Null
    }
    $summaryLines.Add("") | Out-Null
    $summaryLines.Add("## Validator Results") | Out-Null
    $summaryLines.Add("") | Out-Null
    $summaryLines.Add("| Validator | Status | Exit Code | Warnings |") | Out-Null
    $summaryLines.Add("|---|---|---:|---:|") | Out-Null
    foreach ($result in $validatorResults) {
        $summaryLines.Add("| $($result.Validator) | $($result.Status) | $($result.ExitCode) | $($result.Warnings) |") | Out-Null
    }
    $summaryLines.Add("") | Out-Null
    $summaryLines.Add("This mutating mode writes reviewed local reports. It does not run Terraform, kubectl, cloud CLIs, live monitoring queries, or external infrastructure checks.") | Out-Null
    Set-Content -LiteralPath $summaryPath -Value $summaryLines -Encoding UTF8

    Write-Host "Log: $logPath"
    Write-Host "Summary: $summaryPath"
}
else {
    Write-Host "Report generation: SKIPPED (read-only isolated mode)."
}

Write-Host "Repository-wide validation mode: $validationMode"
Write-Host "Scenarios evaluated: $($scenarioValidators.Count)"
Write-Host "Scenario results: PASS=$scenarioPassCount WARN=$scenarioWarnCount FAIL=$scenarioFailCount"
Write-Host "Validator results: PASS=$validatorPassCount WARN=$validatorWarnCount FAIL=$validatorFailures"
Write-Host "Integration failures: $integrationFailures"
Write-Host "Repository-wide validation result: $finalStatus"
$validationExitCode = if ($finalStatus -eq "FAIL") { 1 } else { 0 }
}
catch {
    $executionError = $_
    $validationExitCode = 2
}
finally {
    if ($null -ne $temporaryContainer) {
        try {
            $resolvedTemporaryContainer = [System.IO.Path]::GetFullPath($temporaryContainer)
            $resolvedSystemTemp = [System.IO.Path]::GetFullPath([System.IO.Path]::GetTempPath())
            $temporaryName = Split-Path -Leaf $resolvedTemporaryContainer
            if (
                -not $resolvedTemporaryContainer.StartsWith($resolvedSystemTemp, [System.StringComparison]::OrdinalIgnoreCase) -or
                $temporaryName -notlike 'snsd-scenario-validation-*'
            ) {
                throw "Refusing to remove unexpected validation workspace: $resolvedTemporaryContainer"
            }
            Remove-Item -LiteralPath $resolvedTemporaryContainer -Recurse -Force
        }
        catch {
            $cleanupError = $_
        }
    }
}

$repositoryStateAfter = Get-RepositoryStateSnapshot -RepositoryRoot $sourceRepositoryRoot
$stateComparison = Compare-RepositoryStateSnapshot -Before $repositoryStateBefore -After $repositoryStateAfter
Write-Host "Repository state before: $($repositoryStateBefore.Fingerprint)"
Write-Host "Repository state after:  $($repositoryStateAfter.Fingerprint)"
Write-Host "Repository unchanged: $($stateComparison.Unchanged)"

if (-not $stateComparison.Unchanged) {
    foreach ($difference in $stateComparison.Differences) {
        Write-Host "[FAIL] Repository mutation: $($difference.Change) $($difference.Path)"
    }
    exit 2
}
if ($null -ne $cleanupError) {
    Write-Host "[FAIL] Temporary validation workspace cleanup failed: $($cleanupError.Exception.Message)"
    exit 2
}
if ($null -ne $executionError) {
    Write-Host "[FAIL] Repository-wide validator error: $($executionError.Exception.Message)"
    exit 2
}
exit $validationExitCode
