$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$baselinePath = Join-Path $repositoryRoot "security-baseline\grafana-anonymous-access-denial-baseline.md"
$matrixPath = Join-Path $repositoryRoot "security-baseline\grafana-access-control-rule-matrix.example.md"
$configPath = Join-Path $repositoryRoot "observability\grafana\grafana.ini.anonymous-denial.example"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L2-security-baseline\S020-grafana-anonymous-access-denial-validation"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "grafana-anonymous-access-denial-validation.log"
$summaryPath = Join-Path $configDirectory "grafana-anonymous-access-denial-summary.md"

$requiredBaselineTerms = @(
    'Anonymous access must be disabled',
    'Grafana dashboards must require authenticated access',
    'authenticated user, team, or role model',
    'Anonymous Viewer role must not be enabled',
    'Grafana admin password must not be stored',
    'Grafana API tokens must not be stored',
    'Datasource credentials must not be stored',
    'Public dashboard exposure requires separate justification',
    'Evidence Collection Model',
    '<grafana-host>', '<grafana-url-placeholder>', '<authenticated-viewer-role>',
    '<grafana-admin-user-placeholder>', '<grafana-config-path>', '<evidence-path>'
)
$requiredMatrixEntries = @(
    'Anonymous access', 'Anonymous org role', 'Admin password storage',
    'API token storage', 'Datasource credential storage',
    'Public dashboard exposure', 'Authenticated viewer access', 'Dashboard sharing control'
)

New-Item -ItemType Directory -Force -Path $logDirectory, $configDirectory | Out-Null
$results = [System.Collections.Generic.List[object]]::new()
$outputLines = [System.Collections.Generic.List[string]]::new()
$criticalFailures = 0

function Add-ValidationResult {
    param(
        [string] $Id,
        [string] $Description,
        [ValidateSet("PASS", "WARN", "FAIL")] [string] $Result,
        [string] $Detail
    )
    if ($Result -eq "FAIL") { $script:criticalFailures++ }
    $line = "[$Result] $Id ${Description}: $Detail"
    Write-Host $line
    $script:outputLines.Add($line) | Out-Null
    $script:results.Add([pscustomobject]@{ Id = $Id; Description = $Description; Result = $Result; Detail = $Detail }) | Out-Null
}

$baselineExists = Test-Path -LiteralPath $baselinePath -PathType Leaf
Add-ValidationResult "V001" "Anonymous access denial baseline" $(if ($baselineExists) { "PASS" } else { "FAIL" }) $(if ($baselineExists) { "Baseline document exists." } else { "Baseline document is missing." })

$matrixExists = Test-Path -LiteralPath $matrixPath -PathType Leaf
Add-ValidationResult "V002" "Access-control rule matrix" $(if ($matrixExists) { "PASS" } else { "FAIL" }) $(if ($matrixExists) { "Rule matrix exists." } else { "Rule matrix is missing." })

$configExists = Test-Path -LiteralPath $configPath -PathType Leaf
Add-ValidationResult "V003" "Grafana config example" $(if ($configExists) { "PASS" } else { "FAIL" }) $(if ($configExists) { "Non-production config example exists." } else { "Config example is missing." })

$baselineContent = if ($baselineExists) { Get-Content -LiteralPath $baselinePath -Raw } else { "" }
$matrixContent = if ($matrixExists) { Get-Content -LiteralPath $matrixPath -Raw } else { "" }
$configContent = if ($configExists) { Get-Content -LiteralPath $configPath -Raw } else { "" }
$combinedContent = @($baselineContent, $matrixContent, $configContent) -join "`n"

$anonymousSectionMatch = [regex]::Match($configContent, '(?ims)^\s*\[auth\.anonymous\]\s*$\s*(.*?)(?=^\s*\[|\z)')
$anonymousSectionExists = $anonymousSectionMatch.Success
$anonymousSection = if ($anonymousSectionExists) { $anonymousSectionMatch.Groups[1].Value } else { "" }
Add-ValidationResult "V004" "Anonymous configuration section" $(if ($anonymousSectionExists) { "PASS" } else { "FAIL" }) $(if ($anonymousSectionExists) { "[auth.anonymous] section exists." } else { "[auth.anonymous] section is missing." })

$anonymousDisabled = $anonymousSection -match '(?im)^\s*enabled\s*=\s*false\s*$'
Add-ValidationResult "V005" "Anonymous access disabled" $(if ($anonymousDisabled) { "PASS" } else { "FAIL" }) $(if ($anonymousDisabled) { "Anonymous enabled is explicitly false." } else { "Anonymous enabled=false is missing from the section." })

$anonymousEnablementHit = $anonymousSection -match '(?im)^\s*enabled\s*=\s*true\s*$' -or $combinedContent -match '(?i)GF_AUTH_ANONYMOUS_ENABLED\s*=\s*true'
Add-ValidationResult "V006" "Anonymous enablement denial" $(if (-not $anonymousEnablementHit) { "PASS" } else { "FAIL" }) $(if (-not $anonymousEnablementHit) { "No config or environment enablement is present." } else { "Anonymous access enablement was detected." })

$missingBaselineTerms = @($requiredBaselineTerms | Where-Object { $baselineContent -notmatch [regex]::Escape($_) })
$viewerDenied = $baselineContent -match 'Anonymous Viewer role must not be enabled' -and $anonymousSection -match '(?im)^\s*org_role\s*=\s*Viewer\s*$' -and $anonymousDisabled
$baselineReady = $missingBaselineTerms.Count -eq 0 -and $viewerDenied
Add-ValidationResult "V007" "Baseline denial documentation" $(if ($baselineReady) { "PASS" } else { "FAIL" }) $(if ($baselineReady) { "Authentication, Viewer denial, credential prohibitions, placeholders, and evidence model are documented." } else { "Required baseline denial documentation is incomplete." })

$missingMatrixEntries = @($requiredMatrixEntries | Where-Object { $matrixContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V008" "Access-control matrix completeness" $(if ($missingMatrixEntries.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingMatrixEntries.Count -eq 0) { "All eight required control areas exist." } else { "Missing matrix entries: " + ($missingMatrixEntries -join ", ") })

$adminPasswordMatches = @([regex]::Matches($configContent, '(?im)^\s*admin_password\s*=\s*(.+?)\s*$'))
$adminPasswordSafe = $adminPasswordMatches.Count -eq 1 -and $adminPasswordMatches[0].Groups[1].Value.Trim() -match '^<[^>]+>$'
Add-ValidationResult "V009" "Admin password storage safety" $(if ($adminPasswordSafe) { "PASS" } else { "FAIL" }) $(if ($adminPasswordSafe) { "Admin password uses an external-management placeholder only." } else { "A missing or real-looking admin password value was detected." })

$grafanaTokenHit = $combinedContent -match '(?i)\bglsa_[A-Za-z0-9_-]{8,}\b' -or
    $combinedContent -match '(?im)^\s*(?:api[_-]?token|auth[_-]?token|bearer[_-]?token)\s*[:=]\s*(?!["'']?<)\S+'
Add-ValidationResult "V010" "Grafana API token safety" $(if (-not $grafanaTokenHit) { "PASS" } else { "FAIL" }) $(if (-not $grafanaTokenHit) { "No Grafana API token-like value exists." } else { "A Grafana token-like value was detected." })

$datasourceCredentialHit = $combinedContent -match '(?im)^\s*(?:basicAuthPassword|secureJsonData|datasource[_-]?(?:password|token|credential))\s*[:=]\s*(?!["'']?<)\S+'
Add-ValidationResult "V011" "Datasource credential safety" $(if (-not $datasourceCredentialHit) { "PASS" } else { "FAIL" }) $(if (-not $datasourceCredentialHit) { "No datasource credential-like value exists." } else { "A datasource credential-like value was detected." })

$urlHit = $combinedContent -match '(?i)https?://[^\s<]+'
$ipMatches = @([regex]::Matches($combinedContent, '(?<![A-Za-z0-9<])((?:\d{1,3}\.){3}\d{1,3})(?:/\d{1,2})?(?![A-Za-z0-9>])'))
$accountIdHit = $combinedContent -match '(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b' -or $combinedContent -match '\b\d{12}\b'
$locationSafe = -not $urlHit -and $ipMatches.Count -eq 0 -and -not $accountIdHit
Add-ValidationResult "V012" "URL, address, and account safety" $(if ($locationSafe) { "PASS" } else { "FAIL" }) $(if ($locationSafe) { "No URL, numeric address, account ID, or UUID exists." } else { "A real-looking URL, address, or identifier was detected." })

$privateMaterialHit = $combinedContent -match '-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----'
$genericSecretHit = $combinedContent -match '(?im)^\s*(?:password|passwd|secret|token|credential|api[_-]?key)\s*[:=]\s*(?!["'']?<)\S+'
$secretSafe = -not $privateMaterialHit -and -not $genericSecretHit
Add-ValidationResult "V013" "Generic secret safety" $(if ($secretSafe) { "PASS" } else { "FAIL" }) $(if ($secretSafe) { "No private material or non-placeholder secret assignment exists." } else { "Private material or a secret-like assignment was detected." })

$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$activeCommandPatterns = @(
    '(?im)^\s*(?:&\s*)?grafana(?:-server|-cli)?\b',
    '(?im)^\s*(?:&\s*)?(?:docker|podman)\b',
    '(?im)^\s*(?:&\s*)?curl\b',
    '(?im)^\s*(?:Invoke-WebRequest|Invoke-RestMethod|Test-NetConnection)\b',
    '(?im)^\s*(?:ssh|scp)\b'
)
$activeCommandHit = $false
foreach ($pattern in $activeCommandPatterns) { if ($scriptContent -match $pattern) { $activeCommandHit = $true; break } }
Add-ValidationResult "V014" "Execution safety boundary" $(if (-not $activeCommandHit) { "PASS" } else { "FAIL" }) $(if (-not $activeCommandHit) { "The validator contains no Grafana, container, curl, host, or network execution command." } else { "A prohibited live execution command was detected." })

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Repository-side Grafana anonymous access denial baseline: $criticalFailures critical failure(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S020 Grafana Anonymous Access Denial Validation"
    "Generated: $timestamp"
    "Scope: repository baseline, rule matrix, config example, and safety checks only"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No Grafana execution, container start, curl, host connection, environment-secret read, credential read, live login, or network operation was performed."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# Grafana Anonymous Access Denial Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S020-grafana-anonymous-access-denial-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Overall result: **$overallResult**") | Out-Null
$summaryLines.Add("- Scope: local policy, matrix, example config, and safety checks") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("| Check ID | Check | Result | Detail |") | Out-Null
$summaryLines.Add("|---|---|---|---|") | Out-Null
foreach ($result in $results) {
    $detail = $result.Detail.Replace("|", "\|")
    $summaryLines.Add("| $($result.Id) | $($result.Description) | $($result.Result) | $detail |") | Out-Null
}
$summaryLines.Add("") | Out-Null
$summaryLines.Add("## Safety Boundary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("This validation read repository files only. It did not run Grafana, start containers, curl endpoints, connect to hosts, read environment secrets or credentials, or validate live login behavior.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) { exit 1 }
exit 0
