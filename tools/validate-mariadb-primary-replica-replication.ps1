$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$runbookPath = Join-Path $repositoryRoot "runbooks\mariadb-primary-replica-replication-validation.md"
$commandPath = Join-Path $repositoryRoot "runbooks\mariadb-replication-commands.example.md"
$playbookPath = Join-Path $repositoryRoot "ansible\playbooks\mariadb-replication-status-check.example.yml"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L3-service-operations\S026-mariadb-primary-replica-replication-validation"
$replicaSamplePath = Join-Path $evidenceRoot "logs\show-replica-status.sample.txt"
$masterSamplePath = Join-Path $evidenceRoot "logs\show-master-status.sample.txt"
$notesSamplePath = Join-Path $evidenceRoot "logs\replication-validation-notes.sample.txt"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "mariadb-primary-replica-replication-validation.log"
$summaryPath = Join-Path $configDirectory "mariadb-primary-replica-replication-summary.md"

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

$requiredPaths = @($runbookPath, $commandPath, $playbookPath, $replicaSamplePath, $masterSamplePath, $notesSamplePath)
$missingRequired = @($requiredPaths | Where-Object { -not (Test-Path -LiteralPath $_ -PathType Leaf) })
Add-ValidationResult "V001" "Required documentation and evidence" $(if ($missingRequired.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingRequired.Count -eq 0) { "Runbook, commands, playbook, and three samples exist." } else { "One or more required files are missing." })

$runbookContent = Read-Artifact $runbookPath
$commandContent = Read-Artifact $commandPath
$playbookContent = Read-Artifact $playbookPath
$replicaContent = Read-Artifact $replicaSamplePath
$masterContent = Read-Artifact $masterSamplePath
$notesContent = Read-Artifact $notesSamplePath
$combinedContent = @($runbookContent, $commandContent, $playbookContent, $replicaContent, $masterContent, $notesContent) -join "`n"

$topologyTerms = @(
    '<db-primary-host>', '<db-replica-host>', '<replication-db-user>', '<replication-channel>',
    '<binlog-file-placeholder>', '<binlog-position-placeholder>', '<gtid-placeholder>', '<evidence-path>',
    'Replica IO thread', 'Replica SQL thread', 'S027', 'Static evidence validation', 'Real database validation'
)
$missingTopologyTerms = @($topologyTerms | Where-Object { $runbookContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V002" "Replication topology documentation" $(if ($missingTopologyTerms.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingTopologyTerms.Count -eq 0) { "Primary, replica, stream, account, thread, delay, evidence, and mode boundaries are documented." } else { "Required topology or validation-boundary terms are missing." })

$requiredSqlReferences = @('SHOW REPLICA STATUS\G', 'SHOW SLAVE STATUS\G', 'SHOW MASTER STATUS;', 'SHOW BINARY LOGS;', 'SELECT @@read_only;', 'SELECT @@server_id;')
$missingSqlReferences = @($requiredSqlReferences | Where-Object { $commandContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V003" "Replication command reference" $(if ($missingSqlReferences.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingSqlReferences.Count -eq 0) { "All six non-executed SQL references are documented." } else { "A required status command reference is missing." })

$playbookSafe = $playbookContent -match 'NON-PRODUCTION EXAMPLE' -and
    $playbookContent -match '(?im)^\s*hosts:\s*db_replica_placeholder\s*$' -and
    $playbookContent -match 'ansible\.builtin\.debug' -and
    $playbookContent -notmatch '(?im)^\s*(?:ansible\.builtin\.)?(?:command|shell|raw|mysql_query|mysql_user):' -and
    $playbookContent -notmatch '(?im)^\s*(?:become_password|password|login_password):\s*\S+'
Add-ValidationResult "V004" "Non-production Ansible placeholder" $(if ($playbookSafe) { "PASS" } else { "FAIL" }) $(if ($playbookSafe) { "The playbook targets only the placeholder group and uses debug without database execution." } else { "The playbook marker, host, safe task, or credential/execution boundary is invalid." })

$modernIo = $replicaContent -match '(?im)^Replica_IO_Running:\s*Yes\s*$'
$legacyIo = $replicaContent -match '(?im)^Slave_IO_Running:\s*Yes\s*$'
$ioNo = $replicaContent -match '(?im)^(?:Replica|Slave)_IO_Running:\s*No\s*$'
$ioHealthy = ($modernIo -or $legacyIo) -and -not $ioNo
Add-ValidationResult "V005" "Replica IO thread" $(if ($ioHealthy) { "PASS" } else { "FAIL" }) $(if ($ioHealthy) { "IO thread evidence is Yes." } else { "IO thread evidence is missing or unhealthy." })

$modernSql = $replicaContent -match '(?im)^Replica_SQL_Running:\s*Yes\s*$'
$legacySql = $replicaContent -match '(?im)^Slave_SQL_Running:\s*Yes\s*$'
$sqlNo = $replicaContent -match '(?im)^(?:Replica|Slave)_SQL_Running:\s*No\s*$'
$sqlHealthy = ($modernSql -or $legacySql) -and -not $sqlNo
Add-ValidationResult "V006" "Replica SQL thread" $(if ($sqlHealthy) { "PASS" } else { "FAIL" }) $(if ($sqlHealthy) { "SQL thread evidence is Yes." } else { "SQL thread evidence is missing or unhealthy." })

$delayMatch = [regex]::Match($replicaContent, '(?im)^Seconds_Behind_(?:Master|Source):\s*(NULL|\d+)\s*$')
$thresholdMatch = [regex]::Match($notesContent, '(?im)^Replication_Delay_Threshold_Seconds:\s*(\d+)\s*$')
$delayResult = "FAIL"
$delayDetail = "Delay or threshold evidence is missing."
$delayHealthy = $false
$delayValue = $null
$thresholdValue = $null
if ($delayMatch.Success -and $thresholdMatch.Success) {
    $thresholdValue = [int] $thresholdMatch.Groups[1].Value
    if ($delayMatch.Groups[1].Value -eq "NULL") {
        $delayDetail = "Replication delay is NULL."
    }
    else {
        $delayValue = [int] $delayMatch.Groups[1].Value
        if ($delayValue -gt $thresholdValue) {
            $delayDetail = "Replication delay exceeds the documented non-production threshold."
        }
        elseif ($delayValue -gt 0) {
            $delayResult = "WARN"
            $delayHealthy = $true
            $delayDetail = "Replication delay is nonzero but remains within the documented threshold."
        }
        else {
            $delayResult = "PASS"
            $delayHealthy = $true
            $delayDetail = "Replication delay is zero."
        }
    }
}
Add-ValidationResult "V007" "Replication delay" $delayResult $delayDetail

$ioErrorMatch = [regex]::Match($replicaContent, '(?im)^Last_IO_Error:[ \t]*(.*)$')
$sqlErrorMatch = [regex]::Match($replicaContent, '(?im)^Last_SQL_Error:[ \t]*(.*)$')
$errorFieldsHealthy = $ioErrorMatch.Success -and $sqlErrorMatch.Success -and
    [string]::IsNullOrWhiteSpace($ioErrorMatch.Groups[1].Value) -and
    [string]::IsNullOrWhiteSpace($sqlErrorMatch.Groups[1].Value)
Add-ValidationResult "V008" "Replication error fields" $(if ($errorFieldsHealthy) { "PASS" } else { "FAIL" }) $(if ($errorFieldsHealthy) { "IO and SQL error fields exist and are empty." } else { "An error field is missing or contains a non-empty value." })

$masterPlaceholdersReady = $masterContent -match 'SAMPLE / NON-PRODUCTION' -and
    $masterContent -match '(?im)^File:\s*<binlog-file-placeholder>\s*$' -and
    $masterContent -match '(?im)^Position:\s*<binlog-position-placeholder>\s*$' -and
    $masterContent -match '(?im)^Executed_Gtid_Set:\s*<gtid-placeholder>\s*$'
Add-ValidationResult "V009" "Master status placeholders" $(if ($masterPlaceholdersReady) { "PASS" } else { "FAIL" }) $(if ($masterPlaceholdersReady) { "Master/source file, position, and GTID are symbolic." } else { "Master status placeholders or sample marker are missing." })

$notesReady = $notesContent -match 'SAMPLE / NON-PRODUCTION' -and
    $notesContent -match '(?im)^Primary_Node:\s*<db-primary-host>\s*$' -and
    $notesContent -match '(?im)^Replica_Node:\s*<db-replica-host>\s*$' -and
    $notesContent -match '(?im)^Replication_User:\s*<replication-db-user>\s*$' -and
    $notesContent -match '(?im)^Replication_Channel:\s*<replication-channel>\s*$'
Add-ValidationResult "V010" "Sanitized replication notes" $(if ($notesReady) { "PASS" } else { "FAIL" }) $(if ($notesReady) { "Topology and account references use approved placeholders." } else { "The notes sample is unmarked or contains incomplete placeholders." })

$legacyOnly = ($legacyIo -or $legacySql) -and -not ($modernIo -or $modernSql)
Add-ValidationResult "V011" "Replication terminology" $(if ($legacyOnly) { "WARN" } else { "PASS" }) $(if ($legacyOnly) { "Legacy SHOW SLAVE STATUS fields are accepted for compatibility." } else { "Modern replica terminology is present." })

$credentialHit = $combinedContent -match '(?im)^\s*(?:password|passwd|login_password|token|secret|api[-_]?key)\s*[:=]\s*(?!["'']?<)\S+' -or
    $combinedContent -match '(?i)(?:mysql|mariadb)://[^\s<]+' -or
    $combinedContent -match '(?i)\b(?:mysql|mariadb)\s+[^\r\n]*(?:-u\s*\S+|-p\S+)'
Add-ValidationResult "V012" "Database credential and connection safety" $(if (-not $credentialHit) { "PASS" } else { "FAIL" }) $(if (-not $credentialHit) { "No database credential, connection string, or client credential flag exists." } else { "Database credential or connection content was detected." })

$dumpFiles = @(Get-ChildItem -LiteralPath $repositoryRoot -Recurse -File -Force -ErrorAction SilentlyContinue | Where-Object {
    $_.FullName -notmatch '[\\/]\.git[\\/]' -and
    $_.Name -notmatch '(?i)\.example\.sql$' -and
    ($_.Name -match '(?i)\.(?:dump|bak)$' -or $_.Name -match '(?i)(?:dump|backup|export).*\.(?:sql|gz)$' -or $_.Name -match '(?i)\.sql$')
})
Add-ValidationResult "V013" "Database dump file safety" $(if ($dumpFiles.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($dumpFiles.Count -eq 0) { "No database dump or production SQL export file exists; the marked policy example is excluded." } else { "A database dump or unapproved SQL export file was detected." })

$ipMatches = @([regex]::Matches($combinedContent, '(?<![A-Za-z0-9<])(?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?(?![A-Za-z0-9>])'))
$accountIdHit = $combinedContent -match '(?<!\d)\d{12}(?!\d)' -or $combinedContent -match '(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b'
$hostConnectionHit = $combinedContent -match '(?i)(?:host|server)\s*[:=]\s*(?!<|db_replica_placeholder)\S+\.(?:com|net|org|internal|local)\b'
$contentSafe = $ipMatches.Count -eq 0 -and -not $accountIdHit -and -not $hostConnectionHit
Add-ValidationResult "V014" "Address and account-specific safety" $(if ($contentSafe) { "PASS" } else { "FAIL" }) $(if ($contentSafe) { "No numeric database address, account identifier, UUID, or concrete host exists." } else { "Address or account-specific content was detected." })

$destructiveSqlHit = $commandContent -match '(?im)^\s*(?:STOP|START|RESET|CHANGE|ALTER|CREATE|DROP)\s+(?:SLAVE|REPLICA|MASTER|USER|DATABASE)\b'
$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$clientInvocationHit = $scriptContent -match '(?im)^\s*(?:&\s*)?(?:mysql|mariadb)(?:\.exe)?\s+'
$executionSafe = -not $destructiveSqlHit -and -not $clientInvocationHit -and
    $playbookContent -notmatch '(?im)^\s*(?:ansible\.builtin\.)?(?:command|shell|raw|mysql_query):'
Add-ValidationResult "V015" "Static execution boundary" $(if ($executionSafe) { "PASS" } else { "FAIL" }) $(if ($executionSafe) { "No database client, SQL execution task, or destructive replication command is invoked." } else { "A database execution or destructive replication path was detected." })

$sampleMarkersReady = $replicaContent -match 'SAMPLE / NON-PRODUCTION' -and $masterContent -match 'SAMPLE / NON-PRODUCTION' -and $notesContent -match 'SAMPLE / NON-PRODUCTION'
Add-ValidationResult "V016" "Validation mode" $(if ($sampleMarkersReady) { "PASS" } else { "FAIL" }) $(if ($sampleMarkersReady) { "StaticEvidence mode validated three marked samples without database access or SQL execution." } else { "A sample marker is missing." })

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] MariaDB primary-replica replication (StaticEvidence): $criticalFailures critical failure(s), $warningCount warning(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S026 MariaDB Primary-Replica Replication Validation"
    "Generated: $timestamp"
    "Validation mode: StaticEvidence"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No database connection, client, SQL execution, credential read, replication mutation, dump operation, host, account value, or network access was performed."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$requiredFileCheck = $missingRequired.Count -eq 0
$topologyReady = $missingTopologyTerms.Count -eq 0 -and $notesReady
$secretSafety = -not $credentialHit -and $dumpFiles.Count -eq 0 -and $contentSafe
$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# MariaDB Primary-Replica Replication Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S026-mariadb-primary-replica-replication-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Validation mode: **StaticEvidence**") | Out-Null
$summaryLines.Add("- Required file check result: **$(if ($requiredFileCheck) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Replication topology documentation result: **$(if ($topologyReady) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Replica IO thread result: **$(if ($ioHealthy) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Replica SQL thread result: **$(if ($sqlHealthy) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Replication delay result: **$delayResult**") | Out-Null
$summaryLines.Add("- Master status placeholder result: **$(if ($masterPlaceholdersReady) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Error field parsing result: **$(if ($errorFieldsHealthy) { 'PASS' } else { 'FAIL' })**") | Out-Null
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
$summaryLines.Add("## Safety Boundary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("This validator reads sanitized repository evidence only. It never connects to MariaDB, invokes a database client, executes SQL, reads credentials, mutates replication, or creates a dump.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) { exit 1 }
exit 0
