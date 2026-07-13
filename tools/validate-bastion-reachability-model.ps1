$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$inventoryRoot = Join-Path $repositoryRoot "ansible\inventories"
$mapPath = Join-Path $inventoryRoot "bastion-reachability-map.example.md"
$policyPath = Join-Path $inventoryRoot "bastion-ssh-access-policy.example.md"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L1-foundation\S008-bastion-reachability-validation"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "bastion-reachability-validation.log"
$summaryPath = Join-Path $configDirectory "bastion-reachability-summary.md"

$requiredPaths = @(
    "control-plane-01 -> bastion-host-01",
    "bastion-host-01 -> internal-server-zone",
    "bastion-host-01 -> monitoring-zone",
    "bastion-host-01 -> database-nodes",
    "bastion-host-01 -> kubernetes-nodes",
    "bastion-host-01 -> on-prem-network-devices placeholder",
    "bastion-host-01 -> cloud-service-nodes placeholder"
)
$requiredTargets = @(
    "bastion-host-01", "db-primary-01", "db-replica-01", "monitoring-node-01",
    "k8s-node-01", "aws-service-node-01", "azure-service-node-01", "openstack-service-node-01"
)
$requiredAddressTokens = @(
    "<bastion-host-ip>", "<internal-server-cidr>", "<monitoring-cidr>",
    "<database-cidr>", "<kubernetes-node-cidr>", "<aws-service-node-ip>",
    "<azure-service-node-ip>", "<openstack-service-node-ip>"
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

$mapExists = Test-Path -LiteralPath $mapPath -PathType Leaf
if ($mapExists) {
    Add-ValidationResult "V001" "Reachability map file" "PASS" "bastion-reachability-map.example.md exists."
}
else {
    Add-ValidationResult "V001" "Reachability map file" "FAIL" "bastion-reachability-map.example.md is missing."
}

$policyExists = Test-Path -LiteralPath $policyPath -PathType Leaf
if ($policyExists) {
    Add-ValidationResult "V002" "SSH access policy file" "PASS" "bastion-ssh-access-policy.example.md exists."
}
else {
    Add-ValidationResult "V002" "SSH access policy file" "FAIL" "bastion-ssh-access-policy.example.md is missing."
}

$mapContent = if ($mapExists) { Get-Content -LiteralPath $mapPath -Raw } else { "" }
$policyContent = if ($policyExists) { Get-Content -LiteralPath $policyPath -Raw } else { "" }
$combinedContent = @($mapContent, $policyContent) -join "`n"

$missingPaths = @($requiredPaths | Where-Object { $mapContent -notmatch [regex]::Escape($_) })
if ($missingPaths.Count -eq 0) {
    Add-ValidationResult "V003" "Required access paths" "PASS" "All seven placeholder access paths are documented."
}
else {
    Add-ValidationResult "V003" "Required access paths" "FAIL" ("Missing paths: " + ($missingPaths -join ", "))
}

$missingTargets = @($requiredTargets | Where-Object { $mapContent -notmatch ('`' + [regex]::Escape($_) + '`') })
if ($missingTargets.Count -eq 0) {
    Add-ValidationResult "V004" "Required targets" "PASS" "All eight required target aliases are documented."
}
else {
    Add-ValidationResult "V004" "Required targets" "FAIL" ("Missing targets: " + ($missingTargets -join ", "))
}

$missingAddressTokens = @($requiredAddressTokens | Where-Object { $mapContent -notmatch [regex]::Escape($_) })
if ($missingAddressTokens.Count -eq 0) {
    Add-ValidationResult "V005" "Required address placeholders" "PASS" "All eight required address tokens are documented."
}
else {
    Add-ValidationResult "V005" "Required address placeholders" "FAIL" ("Missing tokens: " + ($missingAddressTokens -join ", "))
}

if ($policyContent -match '(?i)Bastion-only administrative access model') {
    Add-ValidationResult "V006" "Bastion-only administration" "PASS" "The bastion-only administrative access model is documented."
}
else {
    Add-ValidationResult "V006" "Bastion-only administration" "FAIL" "The bastion-only administrative access statement is missing."
}

if ($policyContent -match '(?i)No direct public SSH to internal servers') {
    Add-ValidationResult "V007" "Direct public SSH denial" "PASS" "Direct public SSH to internal servers is explicitly denied."
}
else {
    Add-ValidationResult "V007" "Direct public SSH denial" "FAIL" "The direct public SSH denial statement is missing."
}

if ($policyContent -match '(?i)SSH key authentication required') {
    Add-ValidationResult "V008" "SSH key authentication policy" "PASS" "SSH key authentication is required by policy."
}
else {
    Add-ValidationResult "V008" "SSH key authentication policy" "FAIL" "The SSH key authentication requirement is missing."
}

if ($policyContent -match '(?i)Password login denied') {
    Add-ValidationResult "V009" "Password login denial policy" "PASS" "Password login denial is documented."
}
else {
    Add-ValidationResult "V009" "Password login denial policy" "FAIL" "The password login denial statement is missing."
}

if ($policyContent -match '(?i)Root login denied') {
    Add-ValidationResult "V010" "Root login denial policy" "PASS" "Root login denial is documented."
}
else {
    Add-ValidationResult "V010" "Root login denial policy" "FAIL" "The root login denial statement is missing."
}

$numericIpMatches = @([regex]::Matches($combinedContent, '(?<![A-Za-z0-9<])(?:\d{1,3}\.){3}\d{1,3}(?![A-Za-z0-9>])'))
if ($numericIpMatches.Count -eq 0) {
    Add-ValidationResult "V011" "Numeric IP safety" "PASS" "No numeric IP address is present."
}
else {
    Add-ValidationResult "V011" "Numeric IP safety" "FAIL" "A numeric IP address was detected."
}

$sensitivePatterns = @(
    "-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----",
    '(?im)^\s*(?:ansible_user|ansible_password|ansible_ssh_private_key_file|private_key_file|password|token|access_key|secret_key|account_id|subscription_id|tenant_id|credential)\s*[:=]',
    '(?i)(?:[A-Z]:\\|/home/|/Users/|~[/\\])[^\r\n]*(?:id_rsa|id_ed25519|\.pem|\.key)',
    "\b(?:AKIA|ASIA)[A-Z0-9]{16}\b",
    "(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b",
    "\b\d{12}\b"
)
$sensitiveHit = $false
foreach ($pattern in $sensitivePatterns) {
    if ($combinedContent -match $pattern) {
        $sensitiveHit = $true
        break
    }
}
if (-not $sensitiveHit) {
    Add-ValidationResult "V012" "Sensitive and account content" "PASS" "No credential assignment, key path, access key, account ID, UUID, password value, or token value was detected."
}
else {
    Add-ValidationResult "V012" "Sensitive and account content" "FAIL" "A forbidden secret-like or account-specific pattern was detected."
}

$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$activeCommandPatterns = @(
    '(?im)^\s*(?:&\s*)?ssh\b',
    '(?im)^\s*(?:&\s*)?ansible(?:-playbook)?\b',
    '(?im)^\s*Test-NetConnection\b',
    '(?im)^\s*(?:Invoke-WebRequest|Invoke-RestMethod)\b',
    '(?im)^\s*(?:aws|az|openstack|kubectl)\s+'
)
$activeCommandHit = $false
foreach ($pattern in $activeCommandPatterns) {
    if ($scriptContent -match $pattern) {
        $activeCommandHit = $true
        break
    }
}
if (-not $activeCommandHit) {
    Add-ValidationResult "V013" "Execution safety boundary" "PASS" "The validator contains no SSH, Ansible, network, cloud, or Kubernetes execution command."
}
else {
    Add-ValidationResult "V013" "Execution safety boundary" "FAIL" "A prohibited live execution command was detected in the validator."
}

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Repository-side bastion reachability model: $criticalFailures critical failure(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S008 Bastion Reachability Validation"
    "Generated: $timestamp"
    "Scope: repository reachability and access-policy model only"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No SSH, Ansible execution, host connection, private-key read, credential read, DNS lookup, cloud query, Kubernetes access, EVE-NG access, or network request was performed."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# Bastion Reachability Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S008-bastion-reachability-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Overall result: **$overallResult**") | Out-Null
$summaryLines.Add("- Scope: local reachability-map, SSH-policy, and safety checks") | Out-Null
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
$summaryLines.Add("The validator inspected repository text only. It did not connect to hosts, execute SSH or Ansible, read keys or credentials, resolve names, test ports, or query cloud, Kubernetes, OpenStack, or EVE-NG systems.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) {
    exit 1
}

exit 0
