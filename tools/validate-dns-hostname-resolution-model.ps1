$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$inventoryRoot = Join-Path $repositoryRoot "ansible\inventories"
$topologyRoot = Join-Path $repositoryRoot "eve-ng\topology"
$mapPath = Join-Path $inventoryRoot "hostname-resolution-map.example.md"
$policyPath = Join-Path $inventoryRoot "dns-resolution-policy.example.md"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L1-foundation\S009-dns-hostname-resolution-validation"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "dns-hostname-resolution-validation.log"
$summaryPath = Join-Path $configDirectory "dns-hostname-resolution-summary.md"

$requiredHosts = @(
    "control-plane-01", "bastion-host-01", "onprem-router-placeholder",
    "aws-service-node-01", "azure-service-node-01", "openstack-service-node-01",
    "k8s-node-01", "db-primary-01", "db-replica-01", "monitoring-node-01",
    "prometheus-placeholder", "grafana-placeholder"
)
$requiredDomains = @(
    "<internal-domain>", "<onprem-domain>", "<aws-domain-placeholder>",
    "<azure-domain-placeholder>", "<openstack-domain-placeholder>",
    "<kubernetes-domain-placeholder>"
)
$requiredAddressTokens = @(
    "<control-plane-ip>", "<bastion-host-ip>", "<aws-service-node-ip>",
    "<azure-service-node-ip>", "<openstack-service-node-ip>", "<db-primary-ip>",
    "<db-replica-ip>", "<monitoring-node-ip>"
)
$requiredPolicyStatements = @(
    "Bastion and management hostname resolution rule",
    "Database hostname resolution rule",
    "Kubernetes node hostname resolution rule",
    "Monitoring hostname resolution rule",
    "Cloud service node hostname placeholder rule",
    "Failure condition for unresolved hostnames",
    "Evidence capture model"
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
    Add-ValidationResult "V001" "Hostname map file" "PASS" "hostname-resolution-map.example.md exists."
}
else {
    Add-ValidationResult "V001" "Hostname map file" "FAIL" "hostname-resolution-map.example.md is missing."
}

$policyExists = Test-Path -LiteralPath $policyPath -PathType Leaf
if ($policyExists) {
    Add-ValidationResult "V002" "DNS policy file" "PASS" "dns-resolution-policy.example.md exists."
}
else {
    Add-ValidationResult "V002" "DNS policy file" "FAIL" "dns-resolution-policy.example.md is missing."
}

$mapContent = if ($mapExists) { Get-Content -LiteralPath $mapPath -Raw } else { "" }
$policyContent = if ($policyExists) { Get-Content -LiteralPath $policyPath -Raw } else { "" }
$combinedContent = @($mapContent, $policyContent) -join "`n"

if ($mapContent -match "NON-PRODUCTION EXAMPLE") {
    Add-ValidationResult "V003" "Non-production marker" "PASS" "The hostname map is explicitly marked as a non-production example."
}
else {
    Add-ValidationResult "V003" "Non-production marker" "FAIL" "The non-production marker is missing."
}

$missingHosts = @($requiredHosts | Where-Object { $mapContent -notmatch ('`' + [regex]::Escape($_) + '`') })
if ($missingHosts.Count -eq 0) {
    Add-ValidationResult "V004" "Required host aliases" "PASS" "All twelve required aliases are documented."
}
else {
    Add-ValidationResult "V004" "Required host aliases" "FAIL" ("Missing aliases: " + ($missingHosts -join ", "))
}

$missingDomains = @($requiredDomains | Where-Object { $combinedContent -notmatch [regex]::Escape($_) })
if ($missingDomains.Count -eq 0) {
    Add-ValidationResult "V005" "Required domain placeholders" "PASS" "All six required domain placeholders are documented."
}
else {
    Add-ValidationResult "V005" "Required domain placeholders" "FAIL" ("Missing domains: " + ($missingDomains -join ", "))
}

$missingAddressTokens = @($requiredAddressTokens | Where-Object { $mapContent -notmatch [regex]::Escape($_) })
if ($missingAddressTokens.Count -eq 0) {
    Add-ValidationResult "V006" "Required address placeholders" "PASS" "All eight required address tokens are documented."
}
else {
    Add-ValidationResult "V006" "Required address placeholders" "FAIL" ("Missing tokens: " + ($missingAddressTokens -join ", "))
}

if ($policyContent -match '(?i)Hostname Naming Convention') {
    Add-ValidationResult "V007" "Hostname naming convention" "PASS" "The hostname naming convention is documented."
}
else {
    Add-ValidationResult "V007" "Hostname naming convention" "FAIL" "The hostname naming convention is missing."
}

if ($policyContent -match '(?i)Zone and Domain Separation Model') {
    Add-ValidationResult "V008" "Zone separation model" "PASS" "The zone and domain separation model is documented."
}
else {
    Add-ValidationResult "V008" "Zone separation model" "FAIL" "The zone and domain separation model is missing."
}

if ($policyContent -match '(?i)Internal-only components have no dependency on public DNS') {
    Add-ValidationResult "V009" "Internal DNS boundary" "PASS" "The internal-only public-DNS independence boundary is documented."
}
else {
    Add-ValidationResult "V009" "Internal DNS boundary" "FAIL" "The internal-only DNS boundary is missing."
}

$missingPolicyStatements = @($requiredPolicyStatements | Where-Object { $policyContent -notmatch [regex]::Escape($_) })
if ($missingPolicyStatements.Count -eq 0) {
    Add-ValidationResult "V010" "Resolution policy rules" "PASS" "All seven required resolution, failure, and evidence statements exist."
}
else {
    Add-ValidationResult "V010" "Resolution policy rules" "FAIL" ("Missing statements: " + ($missingPolicyStatements -join ", "))
}

$numericIpMatches = @([regex]::Matches($combinedContent, '(?<![A-Za-z0-9<])(?:\d{1,3}\.){3}\d{1,3}(?![A-Za-z0-9>])'))
if ($numericIpMatches.Count -eq 0) {
    Add-ValidationResult "V011" "Numeric IP safety" "PASS" "No numeric public or private IP address is present."
}
else {
    Add-ValidationResult "V011" "Numeric IP safety" "FAIL" "A numeric IP address was detected."
}

$sensitivePatterns = @(
    "-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----",
    '(?im)^\s*(?:password|token|access_key|secret_key|account_id|subscription_id|tenant_id|credential|private_key)\s*[:=]',
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
    Add-ValidationResult "V012" "Sensitive and account content" "PASS" "No credential assignment, access key, account ID, UUID, password value, token value, or private key was detected."
}
else {
    Add-ValidationResult "V012" "Sensitive and account content" "FAIL" "A forbidden secret-like or account-specific pattern was detected."
}

$dnsModelFiles = @(
    Get-ChildItem -LiteralPath $inventoryRoot, $topologyRoot -File -Recurse -Force -ErrorAction SilentlyContinue
)
$forbiddenZoneFiles = @(
    $dnsModelFiles |
        Where-Object {
            $_.Name -match '(?i)\.zone$' -or
            $_.Name -match '(?i)^named\.conf' -or
            $_.Name -match '(?i)^zone[-_.]?export\.' -or
            $_.Name -match '(?i)^dns[-_.]?export\.'
        }
)
if ($forbiddenZoneFiles.Count -eq 0) {
    Add-ValidationResult "V013" "DNS zone export artifacts" "PASS" "No DNS zone or resolver export file exists in the model directories."
}
else {
    Add-ValidationResult "V013" "DNS zone export artifacts" "FAIL" ("Forbidden files: " + (($forbiddenZoneFiles | ForEach-Object Name) -join ", "))
}

$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$activeCommandPatterns = @(
    '(?im)^\s*(?:&\s*)?nslookup\b',
    '(?im)^\s*Resolve-DnsName\b',
    '(?im)^\s*(?:Test-NetConnection|ping)\b',
    '(?im)^\s*(?:Invoke-WebRequest|Invoke-RestMethod)\b',
    '(?im)^\s*(?:aws|az|openstack|kubectl|ssh|ansible)\s+'
)
$activeCommandHit = $false
foreach ($pattern in $activeCommandPatterns) {
    if ($scriptContent -match $pattern) {
        $activeCommandHit = $true
        break
    }
}
if (-not $activeCommandHit) {
    Add-ValidationResult "V014" "Execution safety boundary" "PASS" "The validator contains no DNS, host, network, cloud, SSH, Ansible, or Kubernetes execution command."
}
else {
    Add-ValidationResult "V014" "Execution safety boundary" "FAIL" "A prohibited live execution command was detected in the validator."
}

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Repository-side DNS and hostname model: $criticalFailures critical failure(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S009 DNS Hostname Resolution Validation"
    "Generated: $timestamp"
    "Scope: repository hostname map and DNS policy only"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No DNS query, host connection, resolver change, credential read, cloud authentication, cloud query, Kubernetes access, or live network request was performed."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# DNS Hostname Resolution Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S009-dns-hostname-resolution-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Overall result: **$overallResult**") | Out-Null
$summaryLines.Add("- Scope: local hostname-map, DNS-policy, and safety checks") | Out-Null
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
$summaryLines.Add("The validator inspected repository text only. It did not query DNS, connect to hosts, change resolvers, read credentials, authenticate to cloud providers, or access external networks.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) {
    exit 1
}

exit 0
