$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$baselineRoot = Join-Path $repositoryRoot "security-baseline"
$baselinePath = Join-Path $baselineRoot "aws-security-group-least-privilege-baseline.md"
$matrixPath = Join-Path $baselineRoot "aws-security-group-rule-matrix.example.md"
$terraformRoot = Join-Path $repositoryRoot "terraform"
$moduleRoot = Join-Path $terraformRoot "modules\aws-network"
$environmentRoot = Join-Path $terraformRoot "envs\aws-network-validation"
$moduleMainPath = Join-Path $moduleRoot "main.tf"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L2-security-baseline\S014-aws-security-group-least-privilege-validation"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "aws-security-group-least-privilege-validation.log"
$summaryPath = Join-Path $configDirectory "aws-security-group-least-privilege-summary.md"

$requiredGroups = @(
    "aws-public-web-sg", "aws-bastion-sg", "aws-private-service-sg",
    "aws-database-sg", "aws-monitoring-sg"
)
$requiredStatements = @(
    'Default deny inbound principle', 'Explicit allow only for required service ports',
    'No public SSH from `0.0.0.0/0`', 'No public RDP from `0.0.0.0/0`',
    'No public database access from `0.0.0.0/0`',
    'HTTP/HTTPS public exposure is allowed only', 'Internal service access must use',
    'Egress must be documented and justified', 'Evidence Collection Model',
    '<aws-vpc-cidr>', '<management-cidr>', '<bastion-security-group-id>',
    '<public-web-security-group>', '<private-service-security-group>',
    '<database-security-group>', '<evidence-path>'
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
        [ValidateSet("PASS", "WARN", "FAIL")]
        [string] $Result,
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
Add-ValidationResult "V002" "Security Group rule matrix" $(if ($matrixExists) { "PASS" } else { "FAIL" }) $(if ($matrixExists) { "Rule matrix exists." } else { "Rule matrix is missing." })

$baselineContent = if ($baselineExists) { Get-Content -LiteralPath $baselinePath -Raw } else { "" }
$matrixContent = if ($matrixExists) { Get-Content -LiteralPath $matrixPath -Raw } else { "" }
$missingGroups = @($requiredGroups | Where-Object { $matrixContent -notmatch [regex]::Escape($_) })
if ($missingGroups.Count -eq 0) {
    Add-ValidationResult "V003" "Required Security Group placeholders" "PASS" "All five placeholder groups are documented."
}
else {
    Add-ValidationResult "V003" "Required Security Group placeholders" "FAIL" ("Missing groups: " + ($missingGroups -join ", "))
}

$missingStatements = @($requiredStatements | Where-Object { $baselineContent -notmatch [regex]::Escape($_) })
if ($missingStatements.Count -eq 0) {
    Add-ValidationResult "V004" "Least privilege statements" "PASS" "All required inbound, internal, egress, placeholder, and evidence statements exist."
}
else {
    Add-ValidationResult "V004" "Least privilege statements" "FAIL" ("Missing statements: " + ($missingStatements -join ", "))
}

$moduleExists = Test-Path -LiteralPath $moduleRoot -PathType Container
$moduleMainContent = if (Test-Path -LiteralPath $moduleMainPath -PathType Leaf) { Get-Content -LiteralPath $moduleMainPath -Raw } else { "" }
if ($moduleExists -and $moduleMainContent -match 'resource\s+"aws_security_group"') {
    Add-ValidationResult "V005" "Terraform Security Group placeholder" "PASS" "The AWS network module contains an aws_security_group resource placeholder."
}
else {
    Add-ValidationResult "V005" "Terraform Security Group placeholder" "FAIL" "The AWS module or aws_security_group placeholder is missing."
}

$terraformFiles = @(Get-ChildItem -LiteralPath $terraformRoot -File -Recurse -Force -ErrorAction SilentlyContinue)
$unsafeTerraformFiles = @(
    $terraformFiles | Where-Object {
        $_.Name -match '(?i)\.tfstate($|\.)' -or
        $_.Name -match '(?i)(^|\.)terraform\.tfvars$' -or
        $_.Name -match '(?i)\.auto\.tfvars($|\.json$)'
    }
)
if ($unsafeTerraformFiles.Count -eq 0) {
    Add-ValidationResult "V006" "Terraform state and variables" "PASS" "No tfstate, real tfvars, or auto tfvars file exists."
}
else {
    Add-ValidationResult "V006" "Terraform state and variables" "FAIL" "A forbidden Terraform artifact was detected."
}

$awsTargetFiles = @(
    Get-ChildItem -LiteralPath $moduleRoot, $environmentRoot -File -Recurse -Force -ErrorAction SilentlyContinue
)
$combinedContent = @($baselineContent, $matrixContent, ($awsTargetFiles | ForEach-Object { Get-Content -LiteralPath $_.FullName -Raw })) -join "`n"
$credentialPatterns = @(
    "-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----",
    '(?im)^\s*(?:aws_access_key_id|aws_secret_access_key|access_key|secret_key|account_id|credential|password|token)\s*[:=]',
    "\b(?:AKIA|ASIA)[A-Z0-9]{16}\b",
    "\b\d{12}\b",
    "(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b"
)
$credentialHit = $false
foreach ($pattern in $credentialPatterns) { if ($combinedContent -match $pattern) { $credentialHit = $true; break } }
if (-not $credentialHit) {
    Add-ValidationResult "V007" "AWS credential and account safety" "PASS" "No credential, key, account ID, access key, UUID, password value, or token value was detected."
}
else {
    Add-ValidationResult "V007" "AWS credential and account safety" "FAIL" "A forbidden credential-like or account-specific pattern was detected."
}

$ipMatches = @([regex]::Matches($combinedContent, '(?<![A-Za-z0-9<])((?:\d{1,3}\.){3}\d{1,3})(?:/\d{1,2})?(?![A-Za-z0-9>])'))
$realPublicIps = [System.Collections.Generic.List[string]]::new()
foreach ($match in $ipMatches) {
    $ip = $match.Groups[1].Value
    $octets = @($ip.Split('.') | ForEach-Object { [int]$_ })
    $allowed = $ip -eq "0.0.0.0" -or $octets[0] -eq 10 -or ($octets[0] -eq 172 -and $octets[1] -ge 16 -and $octets[1] -le 31) -or ($octets[0] -eq 192 -and $octets[1] -eq 168)
    if (-not $allowed) { $realPublicIps.Add($match.Value) | Out-Null }
}
if ($realPublicIps.Count -eq 0) {
    Add-ValidationResult "V008" "Public IP safety" "PASS" "No real-looking public IP address is present."
}
else {
    Add-ValidationResult "V008" "Public IP safety" "FAIL" ("Unexpected addresses: " + ($realPublicIps -join ", "))
}

$matrixRows = @($matrixContent -split "`r?`n" | Where-Object { $_ -match '^\|\s*aws-[^|]+\|' })
$parsedRows = @(
    foreach ($row in $matrixRows) {
        $cells = @($row.Split('|') | ForEach-Object { $_.Trim().Trim('`') })
        if ($cells.Count -ge 11) {
            [pscustomobject]@{ Group = $cells[1]; Direction = $cells[2]; Protocol = $cells[3]; Port = $cells[4]; Source = $cells[5]; Purpose = $cells[6]; Exposure = $cells[7]; Judgment = $cells[8] }
        }
    }
)
$dangerousRows = @(
    $parsedRows | Where-Object {
        $_.Direction -eq "ingress" -and $_.Source -eq "0.0.0.0/0" -and $_.Port -match '^\d+$' -and [int]$_.Port -in $dangerousPublicInboundPorts
    }
)
if ($dangerousRows.Count -eq 0) {
    Add-ValidationResult "V009" "Dangerous public inbound rules" "PASS" "No dangerous port permits inbound 0.0.0.0/0."
}
else {
    Add-ValidationResult "V009" "Dangerous public inbound rules" "FAIL" "A dangerous public inbound rule was detected."
}

$publicWebRows = @($parsedRows | Where-Object { $_.Direction -eq "ingress" -and $_.Source -eq "0.0.0.0/0" })
$invalidPublicWebRows = @($publicWebRows | Where-Object { $_.Group -ne "aws-public-web-sg" -or $_.Port -notin @("80", "443") -or $_.Exposure -notmatch "public-web" })
$publicWebPorts = @($publicWebRows | ForEach-Object Port | Sort-Object -Unique)
if ($invalidPublicWebRows.Count -eq 0 -and "80" -in $publicWebPorts -and "443" -in $publicWebPorts) {
    Add-ValidationResult "V010" "Public web exception" "PASS" "Only HTTP and HTTPS on aws-public-web-sg use public inbound exposure."
}
else {
    Add-ValidationResult "V010" "Public web exception" "FAIL" "The public HTTP/HTTPS exception is missing or overbroad."
}

$justifiedEgressRows = @($parsedRows | Where-Object { $_.Direction -eq "egress" -and $_.Purpose -match '(?i)Justified' -and $_.Judgment -eq "REVIEW_REQUIRED" })
if ($baselineContent -match 'Egress must be documented and justified' -and $justifiedEgressRows.Count -ge 1) {
    Add-ValidationResult "V011" "Egress justification" "PASS" "Egress policy and a review-required example are documented."
}
else {
    Add-ValidationResult "V011" "Egress justification" "FAIL" "Egress justification documentation is incomplete."
}

if ($combinedContent -notmatch '(?im)^\s*backend\s+"') {
    Add-ValidationResult "V012" "Remote backend" "PASS" "No Terraform backend block is configured."
}
else {
    Add-ValidationResult "V012" "Remote backend" "FAIL" "A backend block was detected."
}

$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$activeCommandPatterns = @(
    '(?im)^\s*(?:&\s*)?aws\b',
    '(?im)^\s*(?:&\s*)?terraform\s+(?:init|plan|apply|destroy)\b',
    '(?im)^\s*(?:Invoke-WebRequest|Invoke-RestMethod|Test-NetConnection)\b'
)
$activeCommandHit = $false
foreach ($pattern in $activeCommandPatterns) { if ($scriptContent -match $pattern) { $activeCommandHit = $true; break } }
if (-not $activeCommandHit) {
    Add-ValidationResult "V013" "Execution safety boundary" "PASS" "The validator contains no AWS, Terraform mutation, or network execution command."
}
else {
    Add-ValidationResult "V013" "Execution safety boundary" "FAIL" "A prohibited live execution command was detected."
}

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Repository-side AWS Security Group least privilege baseline: $criticalFailures critical failure(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S014 AWS Security Group Least Privilege Validation"
    "Generated: $timestamp"
    "Scope: repository baseline, rule matrix, and Terraform placeholder only"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No AWS authentication, AWS CLI, Terraform init, plan, apply, cloud query, state creation, or resource modification was performed."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# AWS Security Group Least Privilege Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S014-aws-security-group-least-privilege-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Overall result: **$overallResult**") | Out-Null
$summaryLines.Add("- Scope: local baseline, matrix, Terraform placeholder, and safety checks") | Out-Null
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
$summaryLines.Add("The validator inspected repository files only. It did not authenticate to AWS, query live Security Groups, run AWS CLI, initialize Terraform, create a plan, apply changes, or access cloud resources.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) { exit 1 }
exit 0
