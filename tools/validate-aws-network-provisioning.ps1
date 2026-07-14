$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$terraformRoot = Join-Path $repositoryRoot "terraform"
$moduleRoot = Join-Path $terraformRoot "modules\aws-network"
$environmentRoot = Join-Path $terraformRoot "envs\aws-network-validation"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L1-foundation\S003-aws-network-provisioning-validation"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "aws-network-provisioning-validation.log"
$summaryPath = Join-Path $configDirectory "aws-network-provisioning-summary.md"

$requiredModuleFiles = @("main.tf", "variables.tf", "outputs.tf", "README.md")
$requiredEnvironmentFiles = @("main.tf", "variables.tf", "outputs.tf", "terraform.tfvars.example", "README.md")
$requiredResourcePatterns = @(
    'resource\s+"aws_vpc"',
    'resource\s+"aws_subnet"',
    'resource\s+"aws_route_table"',
    'resource\s+"aws_internet_gateway"',
    'resource\s+"aws_security_group"'
)
$allowedExampleCidrs = @(
    "10.10.0.0/16",
    "10.10.1.0/24",
    "10.10.11.0/24",
    "0.0.0.0/0"
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
        Id = $Id
        Description = $Description
        Result = $Result
        Detail = $Detail
    }) | Out-Null
}

$missingModuleFiles = @(
    $requiredModuleFiles |
        Where-Object { -not (Test-Path -LiteralPath (Join-Path $moduleRoot $_) -PathType Leaf) }
)
if ($missingModuleFiles.Count -eq 0) {
    Add-ValidationResult "V001" "Module files" "PASS" "All required AWS network module files exist."
}
else {
    Add-ValidationResult "V001" "Module files" "FAIL" ("Missing: " + ($missingModuleFiles -join ", "))
}

$missingEnvironmentFiles = @(
    $requiredEnvironmentFiles |
        Where-Object { -not (Test-Path -LiteralPath (Join-Path $environmentRoot $_) -PathType Leaf) }
)
if ($missingEnvironmentFiles.Count -eq 0) {
    Add-ValidationResult "V002" "Environment files" "PASS" "All required AWS network validation environment files exist."
}
else {
    Add-ValidationResult "V002" "Environment files" "FAIL" ("Missing: " + ($missingEnvironmentFiles -join ", "))
}

$examplePath = Join-Path $environmentRoot "terraform.tfvars.example"
if (Test-Path -LiteralPath $examplePath -PathType Leaf) {
    Add-ValidationResult "V003" "Example variable file" "PASS" "terraform.tfvars.example exists."
}
else {
    Add-ValidationResult "V003" "Example variable file" "FAIL" "terraform.tfvars.example is missing."
}

$terraformFiles = @(
    Get-ChildItem -LiteralPath $terraformRoot -File -Recurse -Force -ErrorAction SilentlyContinue
)
$unsafeGeneratedFiles = @(
    $terraformFiles |
        Where-Object {
            $_.Name -match "(?i)\.tfstate($|\.)" -or
            $_.Name -match "(?i)(^|\.)terraform\.tfvars$" -or
            $_.Name -match "(?i)\.auto\.tfvars($|\.json$)"
        }
)
if ($unsafeGeneratedFiles.Count -eq 0) {
    Add-ValidationResult "V004" "State and real variable files" "PASS" "No tfstate or real tfvars file exists."
}
else {
    Add-ValidationResult "V004" "State and real variable files" "FAIL" ("Unsafe files: " + (($unsafeGeneratedFiles | ForEach-Object Name) -join ", "))
}

$moduleMainPath = Join-Path $moduleRoot "main.tf"
$moduleMainContent = if (Test-Path -LiteralPath $moduleMainPath -PathType Leaf) {
    Get-Content -LiteralPath $moduleMainPath -Raw
}
else {
    ""
}
$missingResourcePatterns = @(
    $requiredResourcePatterns |
        Where-Object { $moduleMainContent -notmatch $_ }
)
if ($missingResourcePatterns.Count -eq 0) {
    Add-ValidationResult "V005" "AWS network resources" "PASS" "All required AWS network resource placeholders are defined."
}
else {
    Add-ValidationResult "V005" "AWS network resources" "FAIL" ("Missing resource patterns: " + ($missingResourcePatterns -join ", "))
}

$targetFiles = @(
    $terraformFiles |
        Where-Object { $_.FullName.StartsWith($moduleRoot) -or $_.FullName.StartsWith($environmentRoot) }
)
$combinedContent = ($targetFiles | ForEach-Object { Get-Content -LiteralPath $_.FullName -Raw }) -join "`n"
if ($combinedContent -notmatch '(?im)^\s*backend\s+"') {
    Add-ValidationResult "V006" "Remote backend" "PASS" "No Terraform backend block is defined."
}
else {
    Add-ValidationResult "V006" "Remote backend" "FAIL" "A backend block was detected."
}

$credentialPatterns = @(
    "-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----",
    "(?i)\b(?:aws_access_key_id|aws_secret_access_key|access_key|secret_key)\s*=",
    "\b\d{12}\b"
)
$credentialHit = $false
foreach ($pattern in $credentialPatterns) {
    if ($combinedContent -match $pattern) {
        $credentialHit = $true
        break
    }
}
if (-not $credentialHit) {
    Add-ValidationResult "V007" "Credential-like content" "PASS" "No credential, private-key, or account-ID pattern was detected."
}
else {
    Add-ValidationResult "V007" "Credential-like content" "FAIL" "A forbidden credential-like pattern was detected."
}

$exampleContent = if (Test-Path -LiteralPath $examplePath -PathType Leaf) {
    Get-Content -LiteralPath $examplePath -Raw
}
else {
    ""
}
$exampleCidrs = @(
    [regex]::Matches($exampleContent, "\b(?:\d{1,3}\.){3}\d{1,3}/\d{1,2}\b") |
        ForEach-Object Value |
        Sort-Object -Unique
)
$unexpectedCidrs = @($exampleCidrs | Where-Object { $_ -notin $allowedExampleCidrs })
if ($unexpectedCidrs.Count -eq 0 -and $exampleContent -match "NON-PRODUCTION EXAMPLE") {
    Add-ValidationResult "V008" "Example values" "PASS" "Only approved non-production example CIDRs are present."
}
else {
    Add-ValidationResult "V008" "Example values" "FAIL" ("Unexpected CIDRs or missing example marker: " + ($unexpectedCidrs -join ", "))
}

$repoWideStaticOnly = $env:SNSD_REPO_WIDE_STATIC_ONLY -eq "1"
$terraformCommand = Get-Command -Name "terraform" -ErrorAction SilentlyContinue | Select-Object -First 1
if ($repoWideStaticOnly) {
    Add-ValidationResult "V009" "Terraform formatting" "WARN" "Skipped by repository-wide static-only validation mode."
}
elseif ($null -eq $terraformCommand) {
    Add-ValidationResult "V009" "Terraform formatting" "WARN" "Terraform is unavailable; fmt check was skipped."
}
else {
    $previousErrorActionPreference = $ErrorActionPreference
    try {
        $ErrorActionPreference = "Continue"
        $formatOutput = @(& terraform fmt -check -recursive $moduleRoot $environmentRoot 2>&1)
        $formatExitCode = $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = $previousErrorActionPreference
    }

    if ($formatExitCode -eq 0) {
        Add-ValidationResult "V009" "Terraform formatting" "PASS" "terraform fmt -check passed."
    }
    else {
        Add-ValidationResult "V009" "Terraform formatting" "WARN" "terraform fmt -check reported formatting differences."
    }
}

Add-ValidationResult "V010" "Terraform validate" "WARN" "Skipped because terraform init and provider download are prohibited in S003."

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Repository-side AWS network provisioning definitions: $criticalFailures critical failure(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S003 AWS Network Provisioning Validation"
    "Generated: $timestamp"
    "Scope: repository Terraform definitions only"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No Terraform init, validate, plan, apply, destroy, AWS authentication, credential read, backend access, or cloud API call was performed."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# AWS Network Provisioning Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S003-aws-network-provisioning-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Overall result: **$overallResult**") | Out-Null
$summaryLines.Add("- Scope: local Terraform definition and safety checks") | Out-Null
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
$summaryLines.Add("The validator inspected repository files and optionally ran terraform fmt -check. It did not initialize Terraform, validate providers, create a plan, apply changes, authenticate to AWS, read credentials, or contact cloud APIs.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) {
    exit 1
}

exit 0
