$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$terraformRoot = Join-Path $repositoryRoot "terraform"
$providerRoot = Join-Path $terraformRoot "envs\provider-validation"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L1-foundation\S006-terraform-provider-validation"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "terraform-provider-validation.log"
$summaryPath = Join-Path $configDirectory "terraform-provider-baseline-summary.md"

$requiredFiles = @("versions.tf", "providers.tf", "README.md")
$providerSources = [ordered]@{
    aws       = "hashicorp/aws"
    azurerm   = "hashicorp/azurerm"
    openstack = "terraform-provider-openstack/openstack"
}

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

if (Test-Path -LiteralPath $providerRoot -PathType Container) {
    Add-ValidationResult "V001" "Provider directory" "PASS" "The provider-validation directory exists."
}
else {
    Add-ValidationResult "V001" "Provider directory" "FAIL" "The provider-validation directory is missing."
}

$missingFiles = @(
    $requiredFiles |
        Where-Object { -not (Test-Path -LiteralPath (Join-Path $providerRoot $_) -PathType Leaf) }
)
if ($missingFiles.Count -eq 0) {
    Add-ValidationResult "V002" "Required files" "PASS" "versions.tf, providers.tf, and README.md exist."
}
else {
    Add-ValidationResult "V002" "Required files" "FAIL" ("Missing: " + ($missingFiles -join ", "))
}

$versionsPath = Join-Path $providerRoot "versions.tf"
$providersPath = Join-Path $providerRoot "providers.tf"
$readmePath = Join-Path $providerRoot "README.md"
$versionsContent = if (Test-Path -LiteralPath $versionsPath -PathType Leaf) { Get-Content -LiteralPath $versionsPath -Raw } else { "" }
$providersContent = if (Test-Path -LiteralPath $providersPath -PathType Leaf) { Get-Content -LiteralPath $providersPath -Raw } else { "" }
$readmeContent = if (Test-Path -LiteralPath $readmePath -PathType Leaf) { Get-Content -LiteralPath $readmePath -Raw } else { "" }
$combinedContent = @($versionsContent, $providersContent) -join "`n"

if ($versionsContent -match '(?s)terraform\s*\{.*required_version\s*=') {
    Add-ValidationResult "V003" "Terraform version constraint" "PASS" "A required_version constraint is declared."
}
else {
    Add-ValidationResult "V003" "Terraform version constraint" "FAIL" "The required_version constraint is missing."
}

if ($versionsContent -match '(?s)required_providers\s*\{') {
    Add-ValidationResult "V004" "Required providers block" "PASS" "The required_providers block exists."
}
else {
    Add-ValidationResult "V004" "Required providers block" "FAIL" "The required_providers block is missing."
}

$sourceCheckId = 5
foreach ($providerName in $providerSources.Keys) {
    $expectedSource = [regex]::Escape($providerSources[$providerName])
    $providerBlockPattern = '(?s)\b' + [regex]::Escape($providerName) + '\s*=\s*\{.*?source\s*=\s*"' + $expectedSource + '".*?\}'
    $checkId = "V{0:D3}" -f $sourceCheckId
    if ($versionsContent -match $providerBlockPattern) {
        Add-ValidationResult $checkId "$providerName provider source" "PASS" "The expected $providerName provider source is declared."
    }
    else {
        Add-ValidationResult $checkId "$providerName provider source" "FAIL" "The expected $providerName provider source is missing."
    }
    $sourceCheckId++
}

$missingVersionConstraints = @()
foreach ($providerName in $providerSources.Keys) {
    $providerVersionPattern = '(?s)\b' + [regex]::Escape($providerName) + '\s*=\s*\{.*?version\s*=\s*"[^"]+".*?\}'
    if ($versionsContent -notmatch $providerVersionPattern) {
        $missingVersionConstraints += $providerName
    }
}
if ($missingVersionConstraints.Count -eq 0) {
    Add-ValidationResult "V008" "Provider version constraints" "PASS" "All three providers have explicit version constraints."
}
else {
    Add-ValidationResult "V008" "Provider version constraints" "FAIL" ("Missing version constraints: " + ($missingVersionConstraints -join ", "))
}

$missingProviderBlocks = @(
    $providerSources.Keys |
        Where-Object { $providersContent -notmatch ('provider\s+"' + [regex]::Escape($_) + '"\s*\{') }
)
if ($missingProviderBlocks.Count -eq 0) {
    Add-ValidationResult "V009" "Provider blocks" "PASS" "Empty or non-authenticating AWS, AzureRM, and OpenStack provider blocks exist."
}
else {
    Add-ValidationResult "V009" "Provider blocks" "FAIL" ("Missing provider blocks: " + ($missingProviderBlocks -join ", "))
}

$terraformFiles = @(Get-ChildItem -LiteralPath $terraformRoot -File -Recurse -Force -ErrorAction SilentlyContinue)
$unsafeFiles = @(
    $terraformFiles |
        Where-Object {
            $_.Name -match '(?i)\.tfstate($|\.)' -or
            $_.Name -match '(?i)(^|\.)terraform\.tfvars$' -or
            $_.Name -match '(?i)\.auto\.tfvars($|\.json$)'
        }
)
$terraformWorkDirectories = @(
    Get-ChildItem -LiteralPath $providerRoot -Directory -Recurse -Force -ErrorAction SilentlyContinue |
        Where-Object { $_.Name -eq ".terraform" }
)
if ($unsafeFiles.Count -eq 0 -and $terraformWorkDirectories.Count -eq 0) {
    Add-ValidationResult "V010" "Generated Terraform artifacts" "PASS" "No tfstate, real tfvars, auto tfvars, or .terraform directory exists."
}
else {
    Add-ValidationResult "V010" "Generated Terraform artifacts" "FAIL" "A forbidden Terraform state, variable, or work-directory artifact was detected."
}

if ($combinedContent -notmatch '(?im)^\s*backend\s+"') {
    Add-ValidationResult "V011" "Remote backend" "PASS" "No Terraform backend block is configured."
}
else {
    Add-ValidationResult "V011" "Remote backend" "FAIL" "A backend block was detected."
}

$credentialPatterns = @(
    "-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----",
    '(?im)^\s*(?:tenant_id|subscription_id|client_id|client_secret|access_key|secret_key|auth_url|username|password|project_id|token)\s*=',
    '(?im)^\s*application_credential(?:_id|_secret)?\s*=',
    "(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b",
    "\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"
)
$credentialHit = $false
foreach ($pattern in $credentialPatterns) {
    if ($combinedContent -match $pattern) {
        $credentialHit = $true
        break
    }
}
if (-not $credentialHit) {
    Add-ValidationResult "V012" "Credential and account content" "PASS" "No credential, private-key, access-key, UUID, or account-specific assignment was detected."
}
else {
    Add-ValidationResult "V012" "Credential and account content" "FAIL" "A forbidden credential-like or account-specific pattern was detected."
}

$requiredBoundaryPhrases = @(
    "secure local environment configuration outside the repository",
    "Provider authentication validation is not performed in S006",
    "Remote backend validation is out of scope for S006",
    "terraform init",
    "plan",
    "apply"
)
$missingBoundaryPhrases = @($requiredBoundaryPhrases | Where-Object { $readmeContent -notmatch [regex]::Escape($_) })
if ($missingBoundaryPhrases.Count -eq 0) {
    Add-ValidationResult "V013" "Safety boundary documentation" "PASS" "Provider authentication, backend, and real execution boundaries are documented."
}
else {
    Add-ValidationResult "V013" "Safety boundary documentation" "FAIL" ("Missing boundary text: " + ($missingBoundaryPhrases -join ", "))
}

$repoWideStaticOnly = $env:SNSD_REPO_WIDE_STATIC_ONLY -eq "1"
$terraformCommand = Get-Command -Name "terraform" -ErrorAction SilentlyContinue | Select-Object -First 1
if ($repoWideStaticOnly) {
    Add-ValidationResult "V014" "Terraform formatting" "WARN" "Skipped by repository-wide static-only validation mode."
}
elseif ($null -eq $terraformCommand) {
    Add-ValidationResult "V014" "Terraform formatting" "WARN" "Terraform is unavailable; fmt check was skipped."
}
else {
    $previousErrorActionPreference = $ErrorActionPreference
    try {
        $ErrorActionPreference = "Continue"
        $formatOutput = @(& terraform fmt -check $providerRoot 2>&1)
        $formatExitCode = $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = $previousErrorActionPreference
    }

    if ($formatExitCode -eq 0) {
        Add-ValidationResult "V014" "Terraform formatting" "PASS" "terraform fmt -check passed."
    }
    else {
        Add-ValidationResult "V014" "Terraform formatting" "WARN" ("terraform fmt -check reported formatting differences: " + ($formatOutput -join " "))
    }
}

Add-ValidationResult "V015" "Terraform provider validation" "WARN" "Skipped because terraform init, provider download, and authentication are prohibited in S006."

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Repository-side Terraform provider baseline: $criticalFailures critical failure(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S006 Terraform Provider Validation"
    "Generated: $timestamp"
    "Scope: repository provider definitions only"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No Terraform init, validate, plan, apply, cloud authentication, credential read, backend access, provider download, or cloud API call was performed."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# Terraform Provider Baseline Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S006-terraform-provider-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Overall result: **$overallResult**") | Out-Null
$summaryLines.Add("- Scope: local provider declaration and safety checks") | Out-Null
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
$summaryLines.Add("The validator inspected repository files and optionally ran terraform fmt -check. It did not initialize or validate providers, create a plan, apply changes, authenticate to any cloud, read credentials, create state, or contact external systems.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) {
    exit 1
}

exit 0
