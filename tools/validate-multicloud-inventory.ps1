$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$inventoryRoot = Join-Path $repositoryRoot "ansible\inventories"
$inventoryPath = Join-Path $inventoryRoot "multicloud-inventory.example.yml"
$schemaPath = Join-Path $inventoryRoot "multicloud-inventory-schema.md"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L1-foundation\S007-multi-cloud-inventory-validation"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "multicloud-inventory-validation.log"
$summaryPath = Join-Path $configDirectory "multicloud-inventory-summary.md"

$requiredGroups = @(
    "control_plane", "on_prem", "aws", "azure", "openstack", "bastion",
    "internal_servers", "monitoring", "kubernetes_nodes", "database_nodes"
)
$requiredHosts = @(
    "control-plane-01", "bastion-host-01", "onprem-router-placeholder",
    "aws-service-node-01", "azure-service-node-01", "openstack-service-node-01",
    "k8s-node-01", "db-primary-01", "db-replica-01", "monitoring-node-01"
)
$requiredSchemaFields = @(
    "inventory_group", "host_alias", "provider_or_zone", "component_type",
    "environment", "management_path_placeholder", "validation_scope", "evidence_reference"
)
$requiredProviderValues = @("on-prem", "aws", "azure", "openstack", "control-plane")
$requiredComponentValues = @("bastion", "network", "compute", "kubernetes", "database", "monitoring", "service")

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

$inventoryExists = Test-Path -LiteralPath $inventoryPath -PathType Leaf
if ($inventoryExists) {
    Add-ValidationResult "V001" "Example inventory file" "PASS" "multicloud-inventory.example.yml exists."
}
else {
    Add-ValidationResult "V001" "Example inventory file" "FAIL" "multicloud-inventory.example.yml is missing."
}

$schemaExists = Test-Path -LiteralPath $schemaPath -PathType Leaf
if ($schemaExists) {
    Add-ValidationResult "V002" "Inventory schema file" "PASS" "multicloud-inventory-schema.md exists."
}
else {
    Add-ValidationResult "V002" "Inventory schema file" "FAIL" "multicloud-inventory-schema.md is missing."
}

$inventoryContent = if ($inventoryExists) { Get-Content -LiteralPath $inventoryPath -Raw } else { "" }
$schemaContent = if ($schemaExists) { Get-Content -LiteralPath $schemaPath -Raw } else { "" }

if ($inventoryContent -match "NON-PRODUCTION EXAMPLE") {
    Add-ValidationResult "V003" "Non-production marker" "PASS" "The inventory is explicitly marked as a non-production example."
}
else {
    Add-ValidationResult "V003" "Non-production marker" "FAIL" "The non-production example marker is missing."
}

$missingGroups = @(
    $requiredGroups |
        Where-Object { $inventoryContent -notmatch ('(?m)^\s{4}' + [regex]::Escape($_) + ':\s*$') }
)
if ($missingGroups.Count -eq 0) {
    Add-ValidationResult "V004" "Required groups" "PASS" "All ten required inventory groups exist."
}
else {
    Add-ValidationResult "V004" "Required groups" "FAIL" ("Missing groups: " + ($missingGroups -join ", "))
}

$missingHosts = @(
    $requiredHosts |
        Where-Object { $inventoryContent -notmatch ('(?m)^\s+' + [regex]::Escape($_) + ':\s*$') }
)
if ($missingHosts.Count -eq 0) {
    Add-ValidationResult "V005" "Required placeholder hosts" "PASS" "All ten required placeholder hosts exist."
}
else {
    Add-ValidationResult "V005" "Required placeholder hosts" "FAIL" ("Missing hosts: " + ($missingHosts -join ", "))
}

$missingSchemaFields = @(
    $requiredSchemaFields |
        Where-Object { $schemaContent -notmatch ('`' + [regex]::Escape($_) + '`') }
)
if ($missingSchemaFields.Count -eq 0) {
    Add-ValidationResult "V006" "Required schema fields" "PASS" "All required inventory schema fields are documented."
}
else {
    Add-ValidationResult "V006" "Required schema fields" "FAIL" ("Missing fields: " + ($missingSchemaFields -join ", "))
}

$missingProviderValues = @(
    $requiredProviderValues |
        Where-Object { $schemaContent -notmatch ('`' + [regex]::Escape($_) + '`') }
)
if ($missingProviderValues.Count -eq 0) {
    Add-ValidationResult "V007" "Provider or zone values" "PASS" "All allowed provider_or_zone values are documented."
}
else {
    Add-ValidationResult "V007" "Provider or zone values" "FAIL" ("Missing values: " + ($missingProviderValues -join ", "))
}

$missingComponentValues = @(
    $requiredComponentValues |
        Where-Object { $schemaContent -notmatch ('`' + [regex]::Escape($_) + '`') }
)
if ($missingComponentValues.Count -eq 0) {
    Add-ValidationResult "V008" "Component type values" "PASS" "All allowed component_type values are documented."
}
else {
    Add-ValidationResult "V008" "Component type values" "FAIL" ("Missing values: " + ($missingComponentValues -join ", "))
}

$ansibleHostMatches = @([regex]::Matches($inventoryContent, '(?im)^\s*ansible_host:\s*"([^"]+)"\s*$'))
$invalidHostValues = @(
    $ansibleHostMatches |
        ForEach-Object { $_.Groups[1].Value } |
        Where-Object { $_ -notmatch '^<[a-z0-9-]+-ip>$' }
)
$numericIpMatches = @([regex]::Matches($inventoryContent, '(?<![A-Za-z0-9<])(?:\d{1,3}\.){3}\d{1,3}(?![A-Za-z0-9>])'))
if ($ansibleHostMatches.Count -ge $requiredHosts.Count -and $invalidHostValues.Count -eq 0 -and $numericIpMatches.Count -eq 0) {
    Add-ValidationResult "V009" "Host address placeholders" "PASS" "All ansible_host values are placeholders and no numeric IP address is present."
}
else {
    Add-ValidationResult "V009" "Host address placeholders" "FAIL" "A missing, invalid, or numeric host address value was detected."
}

$sensitivePatterns = @(
    "-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----",
    '(?im)^\s*(?:ansible_user|ansible_password|ansible_ssh_private_key_file|private_key_file|password|token|access_key|secret_key|account_id|subscription_id|tenant_id)\s*:',
    "\b(?:AKIA|ASIA)[A-Z0-9]{16}\b",
    "(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b",
    "\b\d{12}\b"
)
$sensitiveHit = $false
foreach ($pattern in $sensitivePatterns) {
    if ($inventoryContent -match $pattern) {
        $sensitiveHit = $true
        break
    }
}
if (-not $sensitiveHit) {
    Add-ValidationResult "V010" "Sensitive inventory content" "PASS" "No credential, key path, access key, account ID, UUID, username, password, or token pattern was detected."
}
else {
    Add-ValidationResult "V010" "Sensitive inventory content" "FAIL" "A forbidden secret-like or account-specific pattern was detected."
}

$inventoryFiles = @(Get-ChildItem -LiteralPath $inventoryRoot -File -Recurse -Force -ErrorAction SilentlyContinue)
$forbiddenInventoryFiles = @(
    $inventoryFiles |
        Where-Object {
            $_.Name -match '(?i)^production\.ya?ml$' -or
            $_.Name -match '(?i)^inventory\.ya?ml$' -or
            $_.Name -match '(?i)^hosts\.ini$' -or
            $_.Name -match '(?i)^vault(?:[-_.].*)?$'
        }
)
if ($forbiddenInventoryFiles.Count -eq 0) {
    Add-ValidationResult "V011" "Live inventory artifacts" "PASS" "No production, live inventory, hosts.ini, or vault file exists."
}
else {
    Add-ValidationResult "V011" "Live inventory artifacts" "FAIL" ("Forbidden files: " + (($forbiddenInventoryFiles | ForEach-Object Name) -join ", "))
}

$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$activeCommandPatterns = @(
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
    Add-ValidationResult "V012" "Execution safety boundary" "PASS" "The validator contains no host, Ansible, cloud, Kubernetes, or network execution command."
}
else {
    Add-ValidationResult "V012" "Execution safety boundary" "FAIL" "A prohibited live execution command was detected in the validator."
}

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Repository-side multi-cloud inventory model: $criticalFailures critical failure(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S007 Multi-Cloud Inventory Validation"
    "Generated: $timestamp"
    "Scope: repository inventory model only"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No Ansible execution, host connection, private-key read, credential read, cloud query, Kubernetes access, EVE-NG access, or network request was performed."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# Multi-Cloud Inventory Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S007-multi-cloud-inventory-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Overall result: **$overallResult**") | Out-Null
$summaryLines.Add("- Scope: local inventory structure, schema, and safety checks") | Out-Null
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
$summaryLines.Add("The validator inspected repository text only. It did not connect to hosts, execute Ansible, read keys or credentials, resolve names, query cloud providers, or access Kubernetes, OpenStack, or EVE-NG.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) {
    exit 1
}

exit 0
