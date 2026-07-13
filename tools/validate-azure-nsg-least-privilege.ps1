$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$baselineRoot = Join-Path $repositoryRoot "security-baseline"
$baselinePath = Join-Path $baselineRoot "azure-nsg-least-privilege-baseline.md"
$matrixPath = Join-Path $baselineRoot "azure-nsg-rule-matrix.example.md"
$terraformRoot = Join-Path $repositoryRoot "terraform"
$moduleRoot = Join-Path $terraformRoot "modules\azure-network"
$environmentRoot = Join-Path $terraformRoot "envs\azure-network-validation"
$moduleMainPath = Join-Path $moduleRoot "main.tf"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L2-security-baseline\S015-azure-nsg-least-privilege-validation"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "azure-nsg-least-privilege-validation.log"
$summaryPath = Join-Path $configDirectory "azure-nsg-least-privilege-summary.md"

$requiredGroups = @(
    "azure-public-web-nsg", "azure-bastion-nsg", "azure-private-service-nsg",
    "azure-database-nsg", "azure-monitoring-nsg"
)
$requiredStatements = @(
    'Default deny inbound principle', 'Explicit allow only for required service ports',
    'No public SSH from `0.0.0.0/0` or `Internet`',
    'No public RDP from `0.0.0.0/0` or `Internet`',
    'No public database access from `0.0.0.0/0` or `Internet`',
    'HTTP/HTTPS public exposure is allowed only', 'Internal service access must use',
    'Egress must be documented and justified', 'Evidence Collection Model',
    '<azure-vnet-cidr>', '<management-cidr>', '<bastion-subnet-cidr>',
    '<public-web-nsg>', '<private-service-nsg>', '<database-nsg>',
    '<monitoring-nsg>', '<evidence-path>'
)
$dangerousPublicInboundPorts = @(22, 3389, 3306, 5432, 6379, 9200, 5601, 9090, 3000)

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
Add-ValidationResult "V001" "Least privilege baseline" $(if ($baselineExists) { "PASS" } else { "FAIL" }) $(if ($baselineExists) { "Baseline document exists." } else { "Baseline document is missing." })

$matrixExists = Test-Path -LiteralPath $matrixPath -PathType Leaf
Add-ValidationResult "V002" "NSG rule matrix" $(if ($matrixExists) { "PASS" } else { "FAIL" }) $(if ($matrixExists) { "Rule matrix exists." } else { "Rule matrix is missing." })

$baselineContent = if ($baselineExists) { Get-Content -LiteralPath $baselinePath -Raw } else { "" }
$matrixContent = if ($matrixExists) { Get-Content -LiteralPath $matrixPath -Raw } else { "" }
$missingGroups = @($requiredGroups | Where-Object { $matrixContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V003" "Required NSG placeholders" $(if ($missingGroups.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingGroups.Count -eq 0) { "All five placeholder NSGs are documented." } else { "Missing NSGs: " + ($missingGroups -join ", ") })

$missingStatements = @($requiredStatements | Where-Object { $baselineContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V004" "Least privilege statements" $(if ($missingStatements.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingStatements.Count -eq 0) { "All required inbound, internal, egress, placeholder, and evidence statements exist." } else { "Missing statements: " + ($missingStatements -join ", ") })

$moduleMainContent = if (Test-Path -LiteralPath $moduleMainPath -PathType Leaf) { Get-Content -LiteralPath $moduleMainPath -Raw } else { "" }
$terraformPlaceholderReady = (Test-Path -LiteralPath $moduleRoot -PathType Container) -and
    $moduleMainContent -match 'resource\s+"azurerm_network_security_group"' -and
    $moduleMainContent -match 'resource\s+"azurerm_subnet_network_security_group_association"' -and
    ($moduleMainContent -match 'resource\s+"azurerm_network_security_rule"' -or $baselineContent -match 'azurerm_network_security_rule.*future implementation placeholder')
Add-ValidationResult "V005" "Terraform NSG placeholder" $(if ($terraformPlaceholderReady) { "PASS" } else { "FAIL" }) $(if ($terraformPlaceholderReady) { "NSG and association resources exist; individual rule intent is safely documented." } else { "The Azure NSG placeholder structure is incomplete." })

$terraformFiles = @(Get-ChildItem -LiteralPath $terraformRoot -File -Recurse -Force -ErrorAction SilentlyContinue)
$unsafeTerraformFiles = @($terraformFiles | Where-Object {
    $_.Name -match '(?i)\.tfstate($|\.)' -or
    $_.Name -match '(?i)(^|\.)terraform\.tfvars$' -or
    $_.Name -match '(?i)\.auto\.tfvars($|\.json$)'
})
Add-ValidationResult "V006" "Terraform state and variables" $(if ($unsafeTerraformFiles.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($unsafeTerraformFiles.Count -eq 0) { "No tfstate, real tfvars, or auto tfvars file exists." } else { "A forbidden Terraform artifact was detected." })

$azureTargetFiles = @(Get-ChildItem -LiteralPath $moduleRoot, $environmentRoot -File -Recurse -Force -ErrorAction SilentlyContinue)
$combinedContent = @($baselineContent, $matrixContent, ($azureTargetFiles | ForEach-Object { Get-Content -LiteralPath $_.FullName -Raw })) -join "`n"
$sensitivePatterns = @(
    '-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----',
    '(?im)^\s*(?:client_id|client_secret|tenant_id|subscription_id|access_key|secret_key|credential|password|token)\s*[:=]',
    '(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b'
)
$sensitiveHit = $false
foreach ($pattern in $sensitivePatterns) { if ($combinedContent -match $pattern) { $sensitiveHit = $true; break } }
Add-ValidationResult "V007" "Azure identity and secret safety" $(if (-not $sensitiveHit) { "PASS" } else { "FAIL" }) $(if (-not $sensitiveHit) { "No identity value, credential, key, password value, or token value was detected." } else { "A forbidden identity or secret-like pattern was detected." })

$ipMatches = @([regex]::Matches($combinedContent, '(?<![A-Za-z0-9<])((?:\d{1,3}\.){3}\d{1,3})(?:/\d{1,2})?(?![A-Za-z0-9>])'))
$realPublicIps = [System.Collections.Generic.List[string]]::new()
foreach ($match in $ipMatches) {
    $ip = $match.Groups[1].Value
    $octets = @($ip.Split('.') | ForEach-Object { [int]$_ })
    $allowed = $ip -eq "0.0.0.0" -or $octets[0] -eq 10 -or ($octets[0] -eq 172 -and $octets[1] -ge 16 -and $octets[1] -le 31) -or ($octets[0] -eq 192 -and $octets[1] -eq 168)
    if (-not $allowed) { $realPublicIps.Add($match.Value) | Out-Null }
}
Add-ValidationResult "V008" "Public IP safety" $(if ($realPublicIps.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($realPublicIps.Count -eq 0) { "No real-looking public IP address is present." } else { "Unexpected addresses: " + ($realPublicIps -join ", ") })

$matrixRows = @($matrixContent -split "`r?`n" | Where-Object { $_ -match '^\|\s*azure-[^|]+\|' })
$parsedRows = @(foreach ($row in $matrixRows) {
    $cells = @($row.Split('|') | ForEach-Object { $_.Trim().Trim('`') })
    if ($cells.Count -ge 12) {
        [pscustomobject]@{ Group = $cells[1]; Direction = $cells[2]; Protocol = $cells[3]; Port = $cells[4]; Source = $cells[5]; Priority = $cells[6]; Purpose = $cells[7]; Exposure = $cells[8]; Judgment = $cells[9] }
    }
})
$dangerousRows = @($parsedRows | Where-Object {
    $_.Direction -eq "inbound" -and $_.Source -in @("0.0.0.0/0", "Internet") -and $_.Port -match '^\d+$' -and [int]$_.Port -in $dangerousPublicInboundPorts
})
Add-ValidationResult "V009" "Dangerous public inbound rules" $(if ($dangerousRows.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($dangerousRows.Count -eq 0) { "No dangerous port permits public inbound access." } else { "A dangerous public inbound rule was detected." })

$publicRows = @($parsedRows | Where-Object { $_.Direction -eq "inbound" -and $_.Source -in @("0.0.0.0/0", "Internet") })
$invalidPublicRows = @($publicRows | Where-Object { $_.Group -ne "azure-public-web-nsg" -or $_.Port -notin @("80", "443") -or $_.Exposure -notmatch "public-web" })
$publicPorts = @($publicRows | ForEach-Object Port | Sort-Object -Unique)
$publicWebValid = $invalidPublicRows.Count -eq 0 -and "80" -in $publicPorts -and "443" -in $publicPorts
Add-ValidationResult "V010" "Public web exception" $(if ($publicWebValid) { "PASS" } else { "FAIL" }) $(if ($publicWebValid) { "Only HTTP and HTTPS on azure-public-web-nsg use public inbound exposure." } else { "The public HTTP/HTTPS exception is missing or overbroad." })

$justifiedEgressRows = @($parsedRows | Where-Object { $_.Direction -eq "outbound" -and $_.Purpose -match '(?i)Justified' -and $_.Judgment -eq "REVIEW_REQUIRED" })
$egressValid = $baselineContent -match 'Egress must be documented and justified' -and $justifiedEgressRows.Count -ge 1
Add-ValidationResult "V011" "Egress justification" $(if ($egressValid) { "PASS" } else { "FAIL" }) $(if ($egressValid) { "Egress policy and a review-required example are documented." } else { "Egress justification documentation is incomplete." })

Add-ValidationResult "V012" "Remote backend" $(if ($combinedContent -notmatch '(?im)^\s*backend\s+"') { "PASS" } else { "FAIL" }) $(if ($combinedContent -notmatch '(?im)^\s*backend\s+"') { "No Terraform backend block is configured." } else { "A backend block was detected." })

$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$activeCommandPatterns = @(
    '(?im)^\s*(?:&\s*)?az\b',
    '(?im)^\s*(?:&\s*)?terraform\s+(?:init|plan|apply|destroy)\b',
    '(?im)^\s*(?:Invoke-WebRequest|Invoke-RestMethod|Test-NetConnection)\b'
)
$activeCommandHit = $false
foreach ($pattern in $activeCommandPatterns) { if ($scriptContent -match $pattern) { $activeCommandHit = $true; break } }
Add-ValidationResult "V013" "Execution safety boundary" $(if (-not $activeCommandHit) { "PASS" } else { "FAIL" }) $(if (-not $activeCommandHit) { "The validator contains no Azure CLI, Terraform mutation, or network execution command." } else { "A prohibited live execution command was detected." })

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Repository-side Azure NSG least privilege baseline: $criticalFailures critical failure(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S015 Azure NSG Least Privilege Validation"
    "Generated: $timestamp"
    "Scope: repository baseline, rule matrix, and Terraform placeholder only"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No Azure authentication, Azure CLI, Terraform init, plan, apply, cloud query, state creation, or resource modification was performed."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# Azure NSG Least Privilege Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S015-azure-nsg-least-privilege-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Overall result: **$overallResult**") | Out-Null
$summaryLines.Add("- Scope: local baseline, matrix, Terraform placeholder, and safety checks") | Out-Null
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
$summaryLines.Add("This validation read repository files only. It did not authenticate to Azure, invoke Azure CLI, query NSGs, run Terraform init/plan/apply, read credentials, or modify resources.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) { exit 1 }
exit 0
