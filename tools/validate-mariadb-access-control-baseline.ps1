$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$baselineRoot = Join-Path $repositoryRoot "security-baseline"
$baselinePath = Join-Path $baselineRoot "mariadb-access-control-baseline.md"
$matrixPath = Join-Path $baselineRoot "mariadb-grant-matrix.example.md"
$sqlPath = Join-Path $baselineRoot "mariadb-access-control.example.sql"
$inventoryRoot = Join-Path $repositoryRoot "ansible\inventories"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L2-security-baseline\S017-mariadb-access-control-validation"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "mariadb-access-control-validation.log"
$summaryPath = Join-Path $configDirectory "mariadb-access-control-summary.md"

$requiredAccounts = @(
    '<application-db-user>', '<replication-db-user>',
    '<monitoring-db-user>', '<admin-db-user>'
)
$requiredStatements = @(
    'Least Privilege Database Access Principle',
    'The root account must not be used by applications',
    'Remote root login must be denied',
    'Wildcard host `%` must be avoided',
    'Passwords must not be stored in repository',
    'read-only metadata/status access only',
    'separated from the application',
    '<db-primary-host>', '<db-replica-host>', '<application-database>',
    '<internal-service-cidr>', '<database-cidr>', '<evidence-path>'
)
$dangerousPrivileges = @('SUPER', 'FILE', 'PROCESS', 'SHUTDOWN', 'RELOAD', 'CREATE USER', 'GRANT OPTION', 'ALL PRIVILEGES')

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
Add-ValidationResult "V001" "Access-control baseline" $(if ($baselineExists) { "PASS" } else { "FAIL" }) $(if ($baselineExists) { "Baseline document exists." } else { "Baseline document is missing." })

$matrixExists = Test-Path -LiteralPath $matrixPath -PathType Leaf
Add-ValidationResult "V002" "Grant matrix" $(if ($matrixExists) { "PASS" } else { "FAIL" }) $(if ($matrixExists) { "Grant matrix exists." } else { "Grant matrix is missing." })

$sqlExists = Test-Path -LiteralPath $sqlPath -PathType Leaf
Add-ValidationResult "V003" "SQL baseline example" $(if ($sqlExists) { "PASS" } else { "FAIL" }) $(if ($sqlExists) { "Non-production SQL example exists." } else { "SQL example is missing." })

$baselineContent = if ($baselineExists) { Get-Content -LiteralPath $baselinePath -Raw } else { "" }
$matrixContent = if ($matrixExists) { Get-Content -LiteralPath $matrixPath -Raw } else { "" }
$sqlContent = if ($sqlExists) { Get-Content -LiteralPath $sqlPath -Raw } else { "" }
$combinedPolicyContent = @($baselineContent, $matrixContent, $sqlContent) -join "`n"

$missingAccounts = @($requiredAccounts | Where-Object { $combinedPolicyContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V004" "Required account placeholders" $(if ($missingAccounts.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingAccounts.Count -eq 0) { "All four account placeholders are documented." } else { "Missing accounts: " + ($missingAccounts -join ", ") })

$missingStatements = @($requiredStatements | Where-Object { $baselineContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V005" "Least privilege statements" $(if ($missingStatements.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingStatements.Count -eq 0) { "Least privilege, root denial, password, host, separation, and evidence statements exist." } else { "Missing statements: " + ($missingStatements -join ", ") })

$matrixReady = $matrixContent -match 'SELECT, INSERT, UPDATE, DELETE' -and
    $matrixContent -match 'REPLICATION SLAVE, REPLICATION CLIENT' -and
    $matrixContent -match 'SELECT and read-only status-related access' -and
    $matrixContent -match 'Remote root login is denied' -and
    $matrixContent -match '<database-client-subnet>'
Add-ValidationResult "V006" "Grant matrix role separation" $(if ($matrixReady) { "PASS" } else { "FAIL" }) $(if ($matrixReady) { "Application, replication, monitoring, administration, root, and host-scope expectations exist." } else { "Grant matrix expectations are incomplete." })

$sqlStatements = @($sqlContent -split ';' | ForEach-Object { ($_ -replace '(?m)^\s*--.*$', '').Trim() } | Where-Object { $_ })
$applicationGrants = @($sqlStatements | Where-Object { $_ -match '(?is)^GRANT\s+' -and $_ -match [regex]::Escape("TO '<application-db-user>'") })
$applicationReady = $applicationGrants.Count -eq 1 -and $applicationGrants[0] -match '(?i)GRANT\s+SELECT\s*,\s*INSERT\s*,\s*UPDATE\s*,\s*DELETE\s+ON\s+`?<application-database>`?\.\*'
Add-ValidationResult "V007" "Application grant" $(if ($applicationReady) { "PASS" } else { "FAIL" }) $(if ($applicationReady) { "Application account receives only required DML on the application database placeholder." } else { "Application grant is missing or not limited to required DML." })

$replicationGrants = @($sqlStatements | Where-Object { $_ -match '(?is)^GRANT\s+' -and $_ -match [regex]::Escape("TO '<replication-db-user>'") })
$replicationReady = $replicationGrants.Count -eq 1 -and $replicationGrants[0] -match '(?i)GRANT\s+REPLICATION SLAVE\s*,\s*REPLICATION CLIENT\s+ON\s+\*\.\*'
Add-ValidationResult "V008" "Replication grant" $(if ($replicationReady) { "PASS" } else { "FAIL" }) $(if ($replicationReady) { "Replication account receives replication privileges only." } else { "Replication grant is missing or overbroad." })

$monitoringGrants = @($sqlStatements | Where-Object { $_ -match '(?is)^GRANT\s+' -and $_ -match [regex]::Escape("TO '<monitoring-db-user>'") })
$monitoringReady = $monitoringGrants.Count -eq 1 -and $monitoringGrants[0] -match '(?i)GRANT\s+SELECT\s+ON\s+`?performance_schema`?\.\*'
Add-ValidationResult "V009" "Monitoring grant" $(if ($monitoringReady) { "PASS" } else { "FAIL" }) $(if ($monitoringReady) { "Monitoring account receives limited read-only metadata access." } else { "Monitoring grant is missing or overbroad." })

$restrictedGrants = @($applicationGrants + $monitoringGrants)
$dangerousAssignments = [System.Collections.Generic.List[string]]::new()
foreach ($grant in $restrictedGrants) {
    foreach ($privilege in $dangerousPrivileges) {
        if ($grant -match "(?i)\b$([regex]::Escape($privilege))\b") { $dangerousAssignments.Add($privilege) | Out-Null }
    }
}
Add-ValidationResult "V010" "Dangerous application or monitoring privileges" $(if ($dangerousAssignments.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($dangerousAssignments.Count -eq 0) { "No dangerous privilege is assigned to application or monitoring accounts." } else { "Dangerous assignments: " + (($dangerousAssignments | Sort-Object -Unique) -join ", ") })

$identifiedValues = @([regex]::Matches($sqlContent, "(?is)IDENTIFIED\s+BY\s+'([^']*)'") | ForEach-Object { $_.Groups[1].Value })
$unsafePasswordValues = @($identifiedValues | Where-Object { $_ -notmatch '^<[^>]+>$' })
$connectionStringHit = $combinedPolicyContent -match '(?i)\b(?:mysql|mariadb)://[^\s<]+'
$secretAssignmentHit = $combinedPolicyContent -match '(?im)^\s*(?:password|passwd|secret|token|credential)\s*[:=]\s*(?!["'']?<)\S+'
$passwordSafe = $unsafePasswordValues.Count -eq 0 -and -not $connectionStringHit -and -not $secretAssignmentHit
Add-ValidationResult "V011" "Password and connection safety" $(if ($passwordSafe) { "PASS" } else { "FAIL" }) $(if ($passwordSafe) { "Only an angle-bracket password placeholder is used; no connection string or secret assignment exists." } else { "A real-looking password, connection string, or secret assignment was detected." })

$dumpFiles = @(Get-ChildItem -LiteralPath $repositoryRoot -File -Recurse -Force -ErrorAction SilentlyContinue | Where-Object {
    $_.FullName -notmatch '[\\/]\.git[\\/]' -and
    $_.FullName -ne $sqlPath -and
    ($_.Extension -match '(?i)^\.(sql|dump|bak)$' -or $_.Name -match '(?i)(dump|backup|export).*(\.gz|\.zip|\.sql)$')
})
Add-ValidationResult "V012" "Database dump safety" $(if ($dumpFiles.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($dumpFiles.Count -eq 0) { "No database dump or export file exists." } else { "A database dump-like file was detected." })

$inventoryContent = @((Get-ChildItem -LiteralPath $inventoryRoot -File -Recurse -Force -ErrorAction SilentlyContinue | ForEach-Object { Get-Content -LiteralPath $_.FullName -Raw })) -join "`n"
$safetyContent = @($combinedPolicyContent, $inventoryContent) -join "`n"
$sensitivePatterns = @(
    '-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----',
    '(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b'
)
$sensitiveHit = $false
foreach ($pattern in $sensitivePatterns) { if ($safetyContent -match $pattern) { $sensitiveHit = $true; break } }
$ipMatches = @([regex]::Matches($safetyContent, '(?<![A-Za-z0-9<])((?:\d{1,3}\.){3}\d{1,3})(?:/\d{1,2})?(?![A-Za-z0-9>])'))
$realPublicIps = [System.Collections.Generic.List[string]]::new()
foreach ($match in $ipMatches) {
    $ip = $match.Groups[1].Value
    $octets = @($ip.Split('.') | ForEach-Object { [int]$_ })
    $documentationRange = ($octets[0] -eq 192 -and $octets[1] -eq 0 -and $octets[2] -eq 2) -or ($octets[0] -eq 198 -and $octets[1] -eq 51 -and $octets[2] -eq 100) -or ($octets[0] -eq 203 -and $octets[1] -eq 0 -and $octets[2] -eq 113)
    $allowed = $ip -eq "0.0.0.0" -or $octets[0] -eq 10 -or ($octets[0] -eq 172 -and $octets[1] -ge 16 -and $octets[1] -le 31) -or ($octets[0] -eq 192 -and $octets[1] -eq 168) -or $documentationRange
    if (-not $allowed) { $realPublicIps.Add($match.Value) | Out-Null }
}
$accountSafe = -not $sensitiveHit -and $realPublicIps.Count -eq 0
Add-ValidationResult "V013" "Account and address safety" $(if ($accountSafe) { "PASS" } else { "FAIL" }) $(if ($accountSafe) { "No private key, account identifier, UUID, or real-looking public IP is present." } else { "Sensitive or account-specific content was detected." })

$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$activeCommandPatterns = @(
    '(?im)^\s*(?:&\s*)?(?:mysql|mariadb|mysqldump)\b',
    '(?im)^\s*(?:Invoke-WebRequest|Invoke-RestMethod|Test-NetConnection)\b',
    '(?im)^\s*(?:&\s*)?ansible(?:-playbook)?\b'
)
$activeCommandHit = $false
foreach ($pattern in $activeCommandPatterns) { if ($scriptContent -match $pattern) { $activeCommandHit = $true; break } }
Add-ValidationResult "V014" "Execution safety boundary" $(if (-not $activeCommandHit) { "PASS" } else { "FAIL" }) $(if (-not $activeCommandHit) { "The validator contains no database client, SQL execution, host connection, or network command." } else { "A prohibited live execution command was detected." })

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Repository-side MariaDB access-control baseline: $criticalFailures critical failure(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S017 MariaDB Access Control Validation"
    "Generated: $timestamp"
    "Scope: repository baseline, grant matrix, SQL example, inventory placeholders, and safety checks only"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No MariaDB connection, database client, SQL execution, credential read, user creation, grant change, dump operation, or network access was performed."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# MariaDB Access Control Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S017-mariadb-access-control-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Overall result: **$overallResult**") | Out-Null
$summaryLines.Add("- Scope: local policy, matrix, SQL example, inventory placeholders, and safety checks") | Out-Null
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
$summaryLines.Add("This validation read repository files only. It did not connect to MariaDB, execute SQL, read credentials, create or alter users, generate dumps, or contact external systems.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) { exit 1 }
exit 0
