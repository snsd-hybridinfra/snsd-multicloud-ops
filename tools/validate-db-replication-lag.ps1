$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$runbookPath = Join-Path $repositoryRoot "runbooks\db-replication-lag-validation.md"
$matrixPath = Join-Path $repositoryRoot "runbooks\db-replication-lag-threshold-matrix.example.md"
$metricsPath = Join-Path $repositoryRoot "observability\prometheus\db-replication-lag-metrics.example.md"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L3-service-operations\S027-db-replication-lag-validation"
$normalPath = Join-Path $evidenceRoot "logs\replication-lag-normal.sample.txt"
$warningPath = Join-Path $evidenceRoot "logs\replication-lag-warning.sample.txt"
$criticalPath = Join-Path $evidenceRoot "logs\replication-lag-critical.sample.txt"
$nullPath = Join-Path $evidenceRoot "logs\replication-lag-null.sample.txt"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "db-replication-lag-validation.log"
$summaryPath = Join-Path $configDirectory "db-replication-lag-summary.md"

New-Item -ItemType Directory -Force -Path $logDirectory, $configDirectory | Out-Null
$results = [System.Collections.Generic.List[object]]::new()
$outputLines = [System.Collections.Generic.List[string]]::new()
$criticalFailures = 0
$warningCount = 0

function Add-ValidationResult {
    param(
        [string] $Id,
        [string] $Description,
        [ValidateSet("PASS", "WARN", "FAIL")] [string] $Result,
        [string] $Detail
    )
    if ($Result -eq "FAIL") { $script:criticalFailures++ }
    if ($Result -eq "WARN") { $script:warningCount++ }
    $line = "[$Result] $Id ${Description}: $Detail"
    Write-Host $line
    $script:outputLines.Add($line) | Out-Null
    $script:results.Add([pscustomobject]@{ Id = $Id; Description = $Description; Result = $Result; Detail = $Detail }) | Out-Null
}

function Read-Artifact {
    param([string] $Path)
    if (Test-Path -LiteralPath $Path -PathType Leaf) { return Get-Content -LiteralPath $Path -Raw }
    return ""
}

function Get-LagEvidence {
    param([string] $Content)
    $io = [regex]::Match($Content, '(?im)^(Replica|Slave)_IO_Running:[ \t]*(Yes|No)[ \t]*$')
    $sql = [regex]::Match($Content, '(?im)^(Replica|Slave)_SQL_Running:[ \t]*(Yes|No)[ \t]*$')
    $lag = [regex]::Match($Content, '(?im)^Seconds_Behind_(Master|Source):[ \t]*(NULL|\d+)[ \t]*$')
    $ioError = [regex]::Match($Content, '(?im)^Last_IO_Error:[ \t]*(.*)$')
    $sqlError = [regex]::Match($Content, '(?im)^Last_SQL_Error:[ \t]*(.*)$')
    $lagValue = $null
    if ($lag.Success -and $lag.Groups[2].Value -ne "NULL") { $lagValue = [int]$lag.Groups[2].Value }
    return [pscustomobject]@{
        Marked = $Content -match 'SAMPLE / NON-PRODUCTION'
        IOFound = $io.Success
        IOState = if ($io.Success) { $io.Groups[2].Value } else { "MISSING" }
        SQLFound = $sql.Success
        SQLState = if ($sql.Success) { $sql.Groups[2].Value } else { "MISSING" }
        LagFound = $lag.Success
        LagNull = $lag.Success -and $lag.Groups[2].Value -eq "NULL"
        LagValue = $lagValue
        IOErrorFound = $ioError.Success
        IOError = if ($ioError.Success) { $ioError.Groups[1].Value.Trim() } else { "MISSING" }
        SQLErrorFound = $sqlError.Success
        SQLError = if ($sqlError.Success) { $sqlError.Groups[1].Value.Trim() } else { "MISSING" }
        Legacy = ($io.Success -and $io.Groups[1].Value -eq "Slave") -or ($sql.Success -and $sql.Groups[1].Value -eq "Slave")
        Modern = ($io.Success -and $io.Groups[1].Value -eq "Replica") -or ($sql.Success -and $sql.Groups[1].Value -eq "Replica")
    }
}

$requiredPaths = @($runbookPath, $matrixPath, $metricsPath, $normalPath, $warningPath, $criticalPath, $nullPath)
$missingRequired = @($requiredPaths | Where-Object { -not (Test-Path -LiteralPath $_ -PathType Leaf) })
Add-ValidationResult "V001" "Required baseline and sample files" $(if ($missingRequired.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingRequired.Count -eq 0) { "Three baseline artifacts and four lag fixtures exist." } else { "One or more required files are missing." })

$runbookContent = Read-Artifact $runbookPath
$matrixContent = Read-Artifact $matrixPath
$metricsContent = Read-Artifact $metricsPath
$normalContent = Read-Artifact $normalPath
$warningContent = Read-Artifact $warningPath
$criticalContent = Read-Artifact $criticalPath
$nullContent = Read-Artifact $nullPath
$combinedContent = @($runbookContent, $matrixContent, $metricsContent, $normalContent, $warningContent, $criticalContent, $nullContent) -join "`n"

$thresholdTerms = @(
    '<db-primary-host>', '<db-replica-host>', '<replication-channel>', '<normal-lag-threshold-seconds>',
    '<warning-lag-threshold-seconds>', '<critical-lag-threshold-seconds>', '<evidence-path>',
    '0 through 5 seconds', 'greater than 5 through 30 seconds', 'greater than 30 seconds or `NULL`',
    'Seconds_Behind_Master', 'Seconds_Behind_Source', 'replica IO', 'replica SQL', 'S026'
)
$matrixTerms = @(
    'Seconds_Behind_Master = 0', 'Seconds_Behind_Master between 1 and 5',
    'Seconds_Behind_Master greater than 5 and less than or equal to 30',
    'Seconds_Behind_Master greater than 30', 'Seconds_Behind_Master NULL',
    'IO thread not running', 'SQL thread not running', 'Last_IO_Error non-empty', 'Last_SQL_Error non-empty'
)
$missingThresholdTerms = @($thresholdTerms | Where-Object { $runbookContent -notmatch [regex]::Escape($_) })
$missingMatrixTerms = @($matrixTerms | Where-Object { $matrixContent -notmatch [regex]::Escape($_) })
$matrixHeaders = $matrixContent -match 'Lag Condition' -and $matrixContent -match 'Operational Judgment' -and $matrixContent -match 'Evidence Reference'
$thresholdModelReady = $missingThresholdTerms.Count -eq 0 -and $missingMatrixTerms.Count -eq 0 -and $matrixHeaders
Add-ValidationResult "V002" "Replication lag threshold model" $(if ($thresholdModelReady) { "PASS" } else { "FAIL" }) $(if ($thresholdModelReady) { "Normal, warning, critical, NULL, thread, and error judgments are complete." } else { "Threshold documentation or matrix coverage is incomplete." })

$metricNames = @(
    'mysql_slave_status_seconds_behind_master', 'mariadb_replication_lag_seconds',
    'mysql_slave_status_slave_io_running', 'mysql_slave_status_slave_sql_running'
)
$missingMetrics = @($metricNames | Where-Object { $metricsContent -notmatch [regex]::Escape($_) })
$metricsReady = $missingMetrics.Count -eq 0 -and $metricsContent -match 'NON-PRODUCTION METRIC EXAMPLES' -and
    $metricsContent -match 'S028' -and $metricsContent -match 'S029'
Add-ValidationResult "V003" "Prometheus metric placeholders" $(if ($metricsReady) { "PASS" } else { "FAIL" }) $(if ($metricsReady) { "Four metric names and S028/S029 boundaries are documented without a live target." } else { "Metric placeholders or ownership boundaries are incomplete." })

$normal = Get-LagEvidence $normalContent
$warning = Get-LagEvidence $warningContent
$critical = Get-LagEvidence $criticalContent
$nullFixture = Get-LagEvidence $nullContent

$normalReady = $normal.Marked -and $normal.IOState -eq "Yes" -and $normal.SQLState -eq "Yes" -and
    $normal.LagFound -and -not $normal.LagNull -and $normal.LagValue -ge 0 -and $normal.LagValue -le 5 -and
    $normal.IOErrorFound -and [string]::IsNullOrEmpty($normal.IOError) -and
    $normal.SQLErrorFound -and [string]::IsNullOrEmpty($normal.SQLError)
Add-ValidationResult "V004" "Normal lag evidence" $(if ($normalReady) { "PASS" } else { "FAIL" }) $(if ($normalReady) { "Healthy threads and lag in the 0-5 second range were parsed." } else { "Normal fixture is missing, unhealthy, malformed, or outside its range." })

$warningReady = $warning.Marked -and $warning.IOState -eq "Yes" -and $warning.SQLState -eq "Yes" -and
    $warning.LagFound -and -not $warning.LagNull -and $warning.LagValue -gt 5 -and $warning.LagValue -le 30 -and
    $warning.IOErrorFound -and [string]::IsNullOrEmpty($warning.IOError) -and
    $warning.SQLErrorFound -and [string]::IsNullOrEmpty($warning.SQLError)
Add-ValidationResult "V005" "Warning lag evidence" $(if ($warningReady) { "WARN" } else { "FAIL" }) $(if ($warningReady) { "Expected warning fixture was correctly classified in the 6-30 second range." } else { "Warning fixture is missing, unhealthy, malformed, or outside its range." })

$criticalDetected = $critical.Marked -and $critical.IOState -eq "Yes" -and $critical.SQLState -eq "Yes" -and
    $critical.LagFound -and -not $critical.LagNull -and $critical.LagValue -gt 30 -and
    $critical.IOErrorFound -and [string]::IsNullOrEmpty($critical.IOError) -and
    $critical.SQLErrorFound -and [string]::IsNullOrEmpty($critical.SQLError)
Add-ValidationResult "V006" "Critical lag negative fixture" $(if ($criticalDetected) { "PASS" } else { "FAIL" }) $(if ($criticalDetected) { "Lag above 30 seconds was detected and classified as an expected CRITICAL fixture." } else { "Critical-lag detection fixture was not classified correctly." })

$nullFailureDetected = $nullFixture.Marked -and $nullFixture.LagFound -and $nullFixture.LagNull -and
    ($nullFixture.IOState -eq "No" -or $nullFixture.SQLState -eq "No") -and
    $nullFixture.IOErrorFound -and -not [string]::IsNullOrEmpty($nullFixture.IOError) -and
    $nullFixture.IOError -eq '<replication-io-error-placeholder>' -and $nullFixture.SQLErrorFound
Add-ValidationResult "V007" "NULL lag negative fixture" $(if ($nullFailureDetected) { "PASS" } else { "FAIL" }) $(if ($nullFailureDetected) { "NULL lag, unhealthy thread, and symbolic error were detected as an expected failure fixture." } else { "NULL/unhealthy/error detection fixture was not classified correctly." })

$threadParsingReady = $normal.IOState -eq "Yes" -and $normal.SQLState -eq "Yes" -and
    $warning.IOState -eq "Yes" -and $warning.SQLState -eq "Yes" -and
    $critical.IOState -eq "Yes" -and $critical.SQLState -eq "Yes" -and $nullFixture.IOState -eq "No"
Add-ValidationResult "V008" "Thread health parsing" $(if ($threadParsingReady) { "PASS" } else { "FAIL" }) $(if ($threadParsingReady) { "Healthy fixture threads and the negative fixture IO failure were distinguished." } else { "IO or SQL thread-state parsing is incomplete." })

$errorParsingReady = [string]::IsNullOrEmpty($normal.IOError) -and [string]::IsNullOrEmpty($normal.SQLError) -and
    [string]::IsNullOrEmpty($warning.IOError) -and [string]::IsNullOrEmpty($warning.SQLError) -and
    [string]::IsNullOrEmpty($critical.IOError) -and [string]::IsNullOrEmpty($critical.SQLError) -and
    $nullFixture.IOError -eq '<replication-io-error-placeholder>' -and [string]::IsNullOrEmpty($nullFixture.SQLError)
Add-ValidationResult "V009" "Replication error parsing" $(if ($errorParsingReady) { "PASS" } else { "FAIL" }) $(if ($errorParsingReady) { "Positive fixtures have empty errors and the negative fixture has only the approved placeholder error." } else { "Error-field parsing found a missing, concrete, or unexpected value." })

$allFixtures = @($normal, $warning, $critical, $nullFixture)
$legacyOnly = @($allFixtures | Where-Object { $_.Legacy }).Count -gt 0 -and @($allFixtures | Where-Object { $_.Modern }).Count -eq 0
Add-ValidationResult "V010" "Replication terminology" $(if ($legacyOnly) { "WARN" } else { "PASS" }) $(if ($legacyOnly) { "Legacy Slave fields are accepted for compatibility." } else { "Modern Replica fields are present." })

$credentialHit = $combinedContent -match '(?im)^\s*(?:password|passwd|login_password|token|secret|api[-_]?key|access[-_]?key)\s*[:=]\s*(?!["'']?<)\S+' -or
    $combinedContent -match '(?i)(?:mysql|mariadb)://[^\s<]+' -or
    $combinedContent -match '(?i)\b(?:mysql|mariadb)\s+[^\r\n]*(?:-u\s*\S+|-p\S+)'
Add-ValidationResult "V011" "Database credential and connection safety" $(if (-not $credentialHit) { "PASS" } else { "FAIL" }) $(if (-not $credentialHit) { "No database credential, connection string, or client credential flag exists." } else { "Database credential or connection content was detected." })

$dumpFiles = @(Get-ChildItem -LiteralPath $repositoryRoot -Recurse -File -Force -ErrorAction SilentlyContinue | Where-Object {
    $_.FullName -notmatch '[\\/]\.git[\\/]' -and $_.Name -notmatch '(?i)\.example\.sql$' -and
    ($_.Name -match '(?i)\.(?:dump|bak)$' -or $_.Name -match '(?i)(?:dump|backup|export).*\.(?:sql|gz)$' -or $_.Name -match '(?i)\.sql$')
})
Add-ValidationResult "V012" "Database dump file safety" $(if ($dumpFiles.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($dumpFiles.Count -eq 0) { "No dump or production SQL export exists; the marked access-control example is excluded." } else { "A dump or unapproved SQL export was detected." })

$observabilityCredentialHit = $combinedContent -match '(?im)^\s*(?:prometheus|grafana)[-_]?(?:password|token|user|api[-_]?key)\s*[:=]\s*(?!["'']?<)\S+' -or
    $combinedContent -match '(?i)https?://[^\s<]+@[^\s<]+'
Add-ValidationResult "V013" "Observability credential safety" $(if (-not $observabilityCredentialHit) { "PASS" } else { "FAIL" }) $(if (-not $observabilityCredentialHit) { "No Prometheus/Grafana credential or credential-bearing URL exists." } else { "Observability credential content was detected." })

$ipMatches = @([regex]::Matches($combinedContent, '(?<![A-Za-z0-9<])(?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?(?![A-Za-z0-9>])'))
$accountIdHit = $combinedContent -match '(?<!\d)\d{12}(?!\d)' -or $combinedContent -match '(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b'
$concreteUrlHit = $combinedContent -match '(?i)https?://(?!<)[^\s]+'
$contentSafe = $ipMatches.Count -eq 0 -and -not $accountIdHit -and -not $concreteUrlHit
Add-ValidationResult "V014" "Address and account-specific safety" $(if ($contentSafe) { "PASS" } else { "FAIL" }) $(if ($contentSafe) { "No numeric address, account identifier, UUID, or concrete observability URL exists." } else { "Address or account-specific content was detected." })

$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$clientInvocation = $scriptContent -match '(?im)^\s*(?:&\s*)?(?:mysql|mariadb)(?:\.exe)?\s+'
$queryInvocation = $scriptContent -match '(?im)^\s*(?:Invoke-WebRequest|Invoke-RestMethod|curl|wget)\b'
$destructiveReference = $combinedContent -match '(?im)^\s*(?:STOP|START|RESET|CHANGE|ALTER|CREATE|DROP)\s+(?:SLAVE|REPLICA|MASTER|USER|DATABASE)\b'
$executionSafe = -not $clientInvocation -and -not $queryInvocation -and -not $destructiveReference
Add-ValidationResult "V015" "Static execution boundary" $(if ($executionSafe) { "PASS" } else { "FAIL" }) $(if ($executionSafe) { "No database client, SQL, Prometheus/Grafana query, or destructive replication path is invoked." } else { "An external query or destructive execution path was detected." })

$markersReady = @($allFixtures | Where-Object { -not $_.Marked }).Count -eq 0
Add-ValidationResult "V016" "Validation mode" $(if ($markersReady) { "PASS" } else { "FAIL" }) $(if ($markersReady) { "StaticEvidence mode parsed four marked fixtures without database or observability access." } else { "A sample marker is missing." })

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] DB replication lag (StaticEvidence): $criticalFailures critical failure(s), $warningCount warning(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S027 DB Replication Lag Validation"
    "Generated: $timestamp"
    "Validation mode: StaticEvidence"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "Critical and NULL samples are negative fixtures; their unsafe operational judgments were detected without external access."
    "No database, Prometheus, or Grafana connection/query; SQL execution; credential read; replication change; dump operation; or network access occurred."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$requiredFileCheck = $missingRequired.Count -eq 0
$threadParsingResult = $threadParsingReady
$errorParsingResult = $errorParsingReady
$secretSafety = -not $credentialHit -and $dumpFiles.Count -eq 0 -and -not $observabilityCredentialHit -and $contentSafe
$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# DB Replication Lag Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S027-db-replication-lag-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Validation mode: **StaticEvidence**") | Out-Null
$summaryLines.Add("- Required file check result: **$(if ($requiredFileCheck) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Threshold model check result: **$(if ($thresholdModelReady) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Normal lag evidence result: **$(if ($normalReady) { 'NORMAL' } else { 'INVALID' })**") | Out-Null
$summaryLines.Add("- Warning lag evidence result: **$(if ($warningReady) { 'WARNING' } else { 'INVALID' })**") | Out-Null
$summaryLines.Add("- Critical lag evidence result: **$(if ($criticalDetected) { 'EXPECTED_CRITICAL_DETECTED' } else { 'INVALID' })**") | Out-Null
$summaryLines.Add("- NULL lag evidence result: **$(if ($nullFailureDetected) { 'EXPECTED_NULL_FAILURE_DETECTED' } else { 'INVALID' })**") | Out-Null
$summaryLines.Add("- Thread health parsing result: **$(if ($threadParsingResult) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Error field parsing result: **$(if ($errorParsingResult) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Secret-safety check result: **$(if ($secretSafety) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Final judgment: **$overallResult**") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("| Check ID | Check | Result | Detail |") | Out-Null
$summaryLines.Add("|---|---|---|---|") | Out-Null
foreach ($result in $results) {
    $detail = $result.Detail.Replace("|", "\|")
    $summaryLines.Add("| $($result.Id) | $($result.Description) | $($result.Result) | $detail |") | Out-Null
}
$summaryLines.Add("") | Out-Null
$summaryLines.Add("## Fixture Interpretation") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("Normal and warning files are positive range fixtures. Critical and NULL files are negative fixtures that must be rejected operationally; detecting those states makes the validator check pass.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) { exit 1 }
exit 0
