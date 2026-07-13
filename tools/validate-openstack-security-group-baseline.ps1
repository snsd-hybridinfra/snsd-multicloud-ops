$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$baselineRoot = Join-Path $repositoryRoot "security-baseline"
$baselinePath = Join-Path $baselineRoot "openstack-security-group-baseline.md"
$matrixPath = Join-Path $baselineRoot "openstack-security-group-rule-matrix.example.md"
$terraformRoot = Join-Path $repositoryRoot "terraform"
$moduleRoot = Join-Path $terraformRoot "modules\openstack-network"
$environmentRoot = Join-Path $terraformRoot "envs\openstack-network-validation"
$moduleMainPath = Join-Path $moduleRoot "main.tf"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L2-security-baseline\S016-openstack-security-group-validation"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "openstack-security-group-validation.log"
$summaryPath = Join-Path $configDirectory "openstack-security-group-summary.md"

$requiredGroups = @(
    "openstack-public-web-sg", "openstack-bastion-sg", "openstack-private-service-sg",
    "openstack-database-sg", "openstack-monitoring-sg"
)
$requiredStatements = @(
    'Default deny inbound principle', 'Explicit allow only for required service ports',
    'No public SSH from `0.0.0.0/0`', 'No public database access from `0.0.0.0/0`',
    'No public monitoring/admin access from `0.0.0.0/0`',
    'HTTP/HTTPS public exposure is allowed only', 'Internal service access must use',
    'Egress must be documented and justified', 'Evidence Collection Model',
    '<openstack-private-network-cidr>', '<management-cidr>', '<bastion-security-group>',
    '<public-web-security-group>', '<private-service-security-group>',
    '<database-security-group>', '<monitoring-security-group>', '<evidence-path>'
)
$dangerousPublicInboundPorts = @(22, 3306, 5432, 6379, 9200, 5601, 9090, 3000)

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
Add-ValidationResult "V001" "Security Group baseline" $(if ($baselineExists) { "PASS" } else { "FAIL" }) $(if ($baselineExists) { "Baseline document exists." } else { "Baseline document is missing." })

$matrixExists = Test-Path -LiteralPath $matrixPath -PathType Leaf
Add-ValidationResult "V002" "Security Group rule matrix" $(if ($matrixExists) { "PASS" } else { "FAIL" }) $(if ($matrixExists) { "Rule matrix exists." } else { "Rule matrix is missing." })

$baselineContent = if ($baselineExists) { Get-Content -LiteralPath $baselinePath -Raw } else { "" }
$matrixContent = if ($matrixExists) { Get-Content -LiteralPath $matrixPath -Raw } else { "" }
$missingGroups = @($requiredGroups | Where-Object { $matrixContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V003" "Required Security Group placeholders" $(if ($missingGroups.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingGroups.Count -eq 0) { "All five placeholder groups are documented." } else { "Missing groups: " + ($missingGroups -join ", ") })

$missingStatements = @($requiredStatements | Where-Object { $baselineContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V004" "Least privilege statements" $(if ($missingStatements.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingStatements.Count -eq 0) { "All required inbound, internal, egress, placeholder, and evidence statements exist." } else { "Missing statements: " + ($missingStatements -join ", ") })

$moduleMainContent = if (Test-Path -LiteralPath $moduleMainPath -PathType Leaf) { Get-Content -LiteralPath $moduleMainPath -Raw } else { "" }
$terraformPlaceholderReady = (Test-Path -LiteralPath $moduleRoot -PathType Container) -and
    $moduleMainContent -match 'resource\s+"openstack_networking_secgroup_v2"' -and
    $moduleMainContent -match 'resource\s+"openstack_networking_secgroup_rule_v2"' -and
    $moduleMainContent -match 'remote_ip_prefix\s*=\s*var\.management_cidr'
Add-ValidationResult "V005" "Terraform Security Group placeholders" $(if ($terraformPlaceholderReady) { "PASS" } else { "FAIL" }) $(if ($terraformPlaceholderReady) { "Security Group and management-scoped rule placeholders exist." } else { "The OpenStack Security Group placeholder structure is incomplete." })

$terraformFiles = @(Get-ChildItem -LiteralPath $terraformRoot -File -Recurse -Force -ErrorAction SilentlyContinue)
$unsafeTerraformFiles = @($terraformFiles | Where-Object {
    $_.Name -match '(?i)\.tfstate($|\.)' -or
    $_.Name -match '(?i)(^|\.)terraform\.tfvars$' -or
    $_.Name -match '(?i)\.auto\.tfvars($|\.json$)'
})
Add-ValidationResult "V006" "Terraform state and variables" $(if ($unsafeTerraformFiles.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($unsafeTerraformFiles.Count -eq 0) { "No tfstate, real tfvars, or auto tfvars file exists." } else { "A forbidden Terraform artifact was detected." })

$forbiddenConfigFiles = @(Get-ChildItem -LiteralPath $repositoryRoot -File -Recurse -Force -ErrorAction SilentlyContinue | Where-Object {
    $_.FullName -notmatch '[\\/]\.git[\\/]' -and ($_.Name -ieq 'clouds.yaml' -or $_.Name -match '(?i)(^|[-_.])openrc(?:\.sh)?$')
})
Add-ValidationResult "V007" "OpenStack configuration files" $(if ($forbiddenConfigFiles.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($forbiddenConfigFiles.Count -eq 0) { "No clouds.yaml or openrc file exists." } else { "A forbidden OpenStack configuration file was detected." })

$openstackTargetFiles = @(Get-ChildItem -LiteralPath $moduleRoot, $environmentRoot -File -Recurse -Force -ErrorAction SilentlyContinue)
$combinedContent = @($baselineContent, $matrixContent, ($openstackTargetFiles | ForEach-Object { Get-Content -LiteralPath $_.FullName -Raw })) -join "`n"
$sensitivePatterns = @(
    '-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----',
    '(?im)^\s*(?:auth_url|project_id|tenant_id|username|password|token|application_credential_id|application_credential_secret|credential|secret_key)\s*[:=]',
    '(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b'
)
$sensitiveHit = $false
foreach ($pattern in $sensitivePatterns) { if ($combinedContent -match $pattern) { $sensitiveHit = $true; break } }
Add-ValidationResult "V008" "OpenStack identity and secret safety" $(if (-not $sensitiveHit) { "PASS" } else { "FAIL" }) $(if (-not $sensitiveHit) { "No identity value, credential, key, password value, or token value was detected." } else { "A forbidden identity or secret-like pattern was detected." })

$ipMatches = @([regex]::Matches($combinedContent, '(?<![A-Za-z0-9<])((?:\d{1,3}\.){3}\d{1,3})(?:/\d{1,2})?(?![A-Za-z0-9>])'))
$realPublicIps = [System.Collections.Generic.List[string]]::new()
foreach ($match in $ipMatches) {
    $ip = $match.Groups[1].Value
    $octets = @($ip.Split('.') | ForEach-Object { [int]$_ })
    $documentationRange = ($octets[0] -eq 192 -and $octets[1] -eq 0 -and $octets[2] -eq 2) -or ($octets[0] -eq 198 -and $octets[1] -eq 51 -and $octets[2] -eq 100) -or ($octets[0] -eq 203 -and $octets[1] -eq 0 -and $octets[2] -eq 113)
    $allowed = $ip -eq "0.0.0.0" -or $octets[0] -eq 10 -or ($octets[0] -eq 172 -and $octets[1] -ge 16 -and $octets[1] -le 31) -or ($octets[0] -eq 192 -and $octets[1] -eq 168) -or $documentationRange
    if (-not $allowed) { $realPublicIps.Add($match.Value) | Out-Null }
}
Add-ValidationResult "V009" "Public IP safety" $(if ($realPublicIps.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($realPublicIps.Count -eq 0) { "No real-looking public IP address is present." } else { "Unexpected addresses: " + ($realPublicIps -join ", ") })

$matrixRows = @($matrixContent -split "`r?`n" | Where-Object { $_ -match '^\|\s*openstack-[^|]+\|' })
$parsedRows = @(foreach ($row in $matrixRows) {
    $cells = @($row.Split('|') | ForEach-Object { $_.Trim().Trim('`') })
    if ($cells.Count -ge 12) {
        [pscustomobject]@{ Group = $cells[1]; Direction = $cells[2]; Ethertype = $cells[3]; Protocol = $cells[4]; Port = $cells[5]; Remote = $cells[6]; Purpose = $cells[7]; Exposure = $cells[8]; Judgment = $cells[9] }
    }
})
$dangerousRows = @($parsedRows | Where-Object {
    $_.Direction -eq "ingress" -and $_.Remote -eq "0.0.0.0/0" -and $_.Port -match '^\d+$' -and [int]$_.Port -in $dangerousPublicInboundPorts
})
Add-ValidationResult "V010" "Dangerous public ingress rules" $(if ($dangerousRows.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($dangerousRows.Count -eq 0) { "No dangerous port permits ingress from 0.0.0.0/0." } else { "A dangerous public ingress rule was detected." })

$publicRows = @($parsedRows | Where-Object { $_.Direction -eq "ingress" -and $_.Remote -eq "0.0.0.0/0" })
$invalidPublicRows = @($publicRows | Where-Object { $_.Group -ne "openstack-public-web-sg" -or $_.Port -notin @("80", "443") -or $_.Exposure -notmatch "public-web" })
$publicPorts = @($publicRows | ForEach-Object Port | Sort-Object -Unique)
$publicWebValid = $invalidPublicRows.Count -eq 0 -and "80" -in $publicPorts -and "443" -in $publicPorts
Add-ValidationResult "V011" "Public web exception" $(if ($publicWebValid) { "PASS" } else { "FAIL" }) $(if ($publicWebValid) { "Only HTTP and HTTPS on openstack-public-web-sg use public ingress exposure." } else { "The public HTTP/HTTPS exception is missing or overbroad." })

$justifiedEgressRows = @($parsedRows | Where-Object { $_.Direction -eq "egress" -and $_.Purpose -match '(?i)Justified' -and $_.Judgment -eq "REVIEW_REQUIRED" })
$egressValid = $baselineContent -match 'Egress must be documented and justified' -and $justifiedEgressRows.Count -ge 1
Add-ValidationResult "V012" "Egress justification" $(if ($egressValid) { "PASS" } else { "FAIL" }) $(if ($egressValid) { "Egress policy and a review-required example are documented." } else { "Egress justification documentation is incomplete." })

Add-ValidationResult "V013" "Remote backend" $(if ($combinedContent -notmatch '(?im)^\s*backend\s+"') { "PASS" } else { "FAIL" }) $(if ($combinedContent -notmatch '(?im)^\s*backend\s+"') { "No Terraform backend block is configured." } else { "A backend block was detected." })

$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$activeCommandPatterns = @(
    '(?im)^\s*(?:&\s*)?openstack\b',
    '(?im)^\s*(?:&\s*)?terraform\s+(?:init|plan|apply|destroy)\b',
    '(?im)^\s*(?:Invoke-WebRequest|Invoke-RestMethod|Test-NetConnection)\b'
)
$activeCommandHit = $false
foreach ($pattern in $activeCommandPatterns) { if ($scriptContent -match $pattern) { $activeCommandHit = $true; break } }
Add-ValidationResult "V014" "Execution safety boundary" $(if (-not $activeCommandHit) { "PASS" } else { "FAIL" }) $(if (-not $activeCommandHit) { "The validator contains no OpenStack CLI, Terraform mutation, or network execution command." } else { "A prohibited live execution command was detected." })

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Repository-side OpenStack Security Group baseline: $criticalFailures critical failure(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S016 OpenStack Security Group Validation"
    "Generated: $timestamp"
    "Scope: repository baseline, rule matrix, and Terraform placeholders only"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No OpenStack authentication, OpenStack CLI, Terraform init, plan, apply, cloud query, state creation, or resource modification was performed."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# OpenStack Security Group Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S016-openstack-security-group-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Overall result: **$overallResult**") | Out-Null
$summaryLines.Add("- Scope: local baseline, matrix, Terraform placeholders, and safety checks") | Out-Null
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
$summaryLines.Add("This validation read repository files only. It did not authenticate to OpenStack, invoke OpenStack CLI, query Security Groups, run Terraform init/plan/apply, read credentials, or modify resources.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) { exit 1 }
exit 0
