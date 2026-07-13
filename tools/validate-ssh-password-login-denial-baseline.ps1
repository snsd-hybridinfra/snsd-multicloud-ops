$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$baselineRoot = Join-Path $repositoryRoot "security-baseline"
$baselinePath = Join-Path $baselineRoot "ssh-password-login-denial-baseline.md"
$configPath = Join-Path $baselineRoot "sshd_config.password-denial.example"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L2-security-baseline\S012-password-login-denial-validation"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "password-login-denial-validation.log"
$summaryPath = Join-Path $configDirectory "password-login-denial-summary.md"

$requiredSettings = [ordered]@{
    V004 = "PasswordAuthentication no"
    V005 = "ChallengeResponseAuthentication no"
    V006 = "KbdInteractiveAuthentication no"
    V007 = "PubkeyAuthentication yes"
    V008 = "AuthenticationMethods publickey"
}
$requiredBaselineStatements = @(
    "No password values are stored in inventory or repository files",
    "SSH key authentication remains the approved administrative login method",
    "Password login is denied",
    "Emergency access is handled outside this repository",
    "approved operational process",
    "Evidence Collection Model",
    "<admin-user>", "<bastion-host>", "<target-host>", "<ssh-config-path>",
    "<approved-break-glass-process>", "<evidence-path>"
)

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

$baselineExists = Test-Path -LiteralPath $baselinePath -PathType Leaf
if ($baselineExists) {
    Add-ValidationResult "V001" "Password denial baseline" "PASS" "ssh-password-login-denial-baseline.md exists."
}
else {
    Add-ValidationResult "V001" "Password denial baseline" "FAIL" "ssh-password-login-denial-baseline.md is missing."
}

$configExists = Test-Path -LiteralPath $configPath -PathType Leaf
if ($configExists) {
    Add-ValidationResult "V002" "SSHD password-denial example" "PASS" "sshd_config.password-denial.example exists."
}
else {
    Add-ValidationResult "V002" "SSHD password-denial example" "FAIL" "sshd_config.password-denial.example is missing."
}

$baselineContent = if ($baselineExists) { Get-Content -LiteralPath $baselinePath -Raw } else { "" }
$configContent = if ($configExists) { Get-Content -LiteralPath $configPath -Raw } else { "" }

if ($configContent -match "NON-PRODUCTION EXAMPLE") {
    Add-ValidationResult "V003" "Non-production marker" "PASS" "The SSHD example is marked as non-production."
}
else {
    Add-ValidationResult "V003" "Non-production marker" "FAIL" "The non-production example marker is missing."
}

foreach ($entry in $requiredSettings.GetEnumerator()) {
    $description = ($entry.Value -split ' ')[0] + " setting"
    if ($configContent -match ('(?im)^\s*' + [regex]::Escape($entry.Value) + '\s*$')) {
        Add-ValidationResult $entry.Key $description "PASS" "$($entry.Value) is present."
    }
    else {
        Add-ValidationResult $entry.Key $description "FAIL" "$($entry.Value) is missing."
    }
}

$missingBaselineStatements = @(
    $requiredBaselineStatements |
        Where-Object { $baselineContent -notmatch [regex]::Escape($_) }
)
if ($missingBaselineStatements.Count -eq 0) {
    Add-ValidationResult "V009" "Password denial policy statements" "PASS" "All required denial, storage, break-glass, placeholder, and evidence statements exist."
}
else {
    Add-ValidationResult "V009" "Password denial policy statements" "FAIL" ("Missing statements: " + ($missingBaselineStatements -join ", "))
}

$combinedContent = @($baselineContent, $configContent) -join "`n"
$passwordValuePatterns = @(
    '(?im)^\s*PasswordAuthentication\s+(?:yes|true|on)\s*$',
    '(?im)^\s*(?:ansible_password|ssh_password|password)\s*[:=]\s*(?!no\b|disabled\b|<)[^\s#][^\r\n]*',
    '(?i)\bsshpass\s+-p\s+',
    '(?i)://[^\s/:]+:[^\s/@]+@'
)
$passwordValueHit = $false
foreach ($pattern in $passwordValuePatterns) {
    if ($combinedContent -match $pattern) {
        $passwordValueHit = $true
        break
    }
}
if (-not $passwordValueHit) {
    Add-ValidationResult "V010" "Password value safety" "PASS" "No enabled password authentication, password assignment, sshpass value, or embedded credential was detected."
}
else {
    Add-ValidationResult "V010" "Password value safety" "FAIL" "A forbidden password-like value or enabled password authentication was detected."
}

$repositoryFiles = @(Get-ChildItem -LiteralPath $repositoryRoot -File -Recurse -ErrorAction SilentlyContinue)
$privateKeyFiles = @(
    $repositoryFiles |
        Where-Object {
            $_.Name -match '(?i)\.(?:pem|key|p12|pfx)$' -or
            $_.Name -match '(?i)^id_(?:rsa|ed25519|ecdsa)$'
        }
)
$privateKeyContentFiles = @(
    $repositoryFiles |
        Where-Object {
            $_.Extension -in @(".md", ".txt", ".example", ".yml", ".yaml", ".conf", ".config") -and
            (Get-Content -LiteralPath $_.FullName -Raw -ErrorAction SilentlyContinue) -match '-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----'
        }
)
if ($privateKeyFiles.Count -eq 0 -and $privateKeyContentFiles.Count -eq 0) {
    Add-ValidationResult "V011" "Private key safety" "PASS" "No private-key filename or private-key material exists in the repository."
}
else {
    Add-ValidationResult "V011" "Private key safety" "FAIL" "A private-key file or private-key material was detected."
}

$authorizedKeysFiles = @($repositoryFiles | Where-Object { $_.Name -eq "authorized_keys" })
if ($authorizedKeysFiles.Count -eq 0) {
    Add-ValidationResult "V012" "Authorized keys safety" "PASS" "No authorized_keys file exists in the repository."
}
else {
    Add-ValidationResult "V012" "Authorized keys safety" "FAIL" "An authorized_keys file was detected."
}

$sensitivePatterns = @(
    '(?im)^\s*(?:token|access_key|secret_key|account_id|subscription_id|tenant_id|credential|private_key)\s*[:=]',
    '(?i)(?:ssh-rsa|ssh-ed25519|ecdsa-sha2-nistp\d+)\s+[A-Za-z0-9+/]{40,}',
    "\b(?:AKIA|ASIA)[A-Z0-9]{16}\b",
    "(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b",
    "\b\d{12}\b",
    '(?<![A-Za-z0-9<])(?:\d{1,3}\.){3}\d{1,3}(?![A-Za-z0-9>])'
)
$sensitiveHit = $false
foreach ($pattern in $sensitivePatterns) {
    if ($combinedContent -match $pattern) {
        $sensitiveHit = $true
        break
    }
}
if (-not $sensitiveHit) {
    Add-ValidationResult "V013" "Secret and account content" "PASS" "No key material, credential assignment, numeric IP, account ID, UUID, or token value was detected."
}
else {
    Add-ValidationResult "V013" "Secret and account content" "FAIL" "A forbidden secret-like or account-specific pattern was detected."
}

$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$activeCommandPatterns = @(
    '(?im)^\s*(?:&\s*)?ssh\b',
    '(?im)^\s*(?:systemctl|service|Restart-Service|Set-Service)\b',
    '(?im)^\s*(?:sshd|sshpass|ssh-keygen|ssh-copy-id)\b',
    '(?im)^\s*(?:Test-NetConnection|Invoke-WebRequest|Invoke-RestMethod)\b',
    '(?im)^\s*(?:ansible|aws|az|openstack|kubectl)\s+'
)
$activeCommandHit = $false
foreach ($pattern in $activeCommandPatterns) {
    if ($scriptContent -match $pattern) {
        $activeCommandHit = $true
        break
    }
}
if (-not $activeCommandHit) {
    Add-ValidationResult "V014" "Execution safety boundary" "PASS" "The validator contains no SSH modification, restart, password attempt, connection, network, Ansible, cloud, or Kubernetes command."
}
else {
    Add-ValidationResult "V014" "Execution safety boundary" "FAIL" "A prohibited live execution command was detected in the validator."
}

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Repository-side SSH password-login denial baseline: $criticalFailures critical failure(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S012 Password Login Denial Validation"
    "Generated: $timestamp"
    "Scope: repository SSH password-denial baseline only"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No sshd configuration was changed, no service was restarted, no host connection or password attempt was performed, and no key or credential was read."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# Password Login Denial Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S012-password-login-denial-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Overall result: **$overallResult**") | Out-Null
$summaryLines.Add("- Scope: local password-denial baseline, secret-safety, and execution-boundary checks") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("| Check ID | Check | Result | Detail |") | Out-Null
$summaryLines.Add("|---|---|---|---|") | Out-Null
foreach ($result in $results) {
    $safeDetail = $result.Detail.Replace("|", "\|")
    $summaryLines.Add("| $($result.Id) | $($result.Description) | $($result.Result) | $safeDetail |") | Out-Null
}
$summaryLines.Add("") | Out-Null
$summaryLines.Add("## Safety Boundary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("The validator inspected repository files only. It did not modify sshd configuration, restart SSH, attempt password authentication, connect to hosts, read keys or credentials, or require live network access.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) {
    exit 1
}

exit 0
