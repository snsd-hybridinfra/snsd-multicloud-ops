$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$topologyPath = Join-Path $repositoryRoot "eve-ng\topology\on-prem-routing-topology.md"
$routerConfigRoot = Join-Path $repositoryRoot "eve-ng\router-configs"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L1-foundation\S002-eve-ng-on-prem-routing-validation"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "eve-ng-routing-baseline-validation.log"
$summaryPath = Join-Path $configDirectory "eve-ng-routing-baseline-summary.md"

$requiredConfigs = @(
    "mgmt-router-01.example.cfg",
    "transit-router-01.example.cfg",
    "internal-router-01.example.cfg",
    "monitoring-router-01.example.cfg"
)
$requiredZones = @(
    "Management Zone",
    "Bastion Zone",
    "Transit Zone",
    "Internal Server Zone",
    "Monitoring Zone"
)
$requiredDevices = @(
    "mgmt-router-01",
    "transit-router-01",
    "internal-router-01",
    "monitoring-router-01",
    "bastion-host-01"
)
$requiredCidrTokens = @(
    "<management-cidr>",
    "<bastion-cidr>",
    "<transit-cidr>",
    "<internal-server-cidr>",
    "<monitoring-cidr>"
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

$topologyExists = Test-Path -LiteralPath $topologyPath -PathType Leaf
if ($topologyExists) {
    Add-ValidationResult "V001" "Topology document" "PASS" "Required topology document exists."
    $topologyContent = Get-Content -LiteralPath $topologyPath -Raw
}
else {
    Add-ValidationResult "V001" "Topology document" "FAIL" "Required topology document is missing."
    $topologyContent = ""
}

$missingConfigs = @(
    $requiredConfigs |
        Where-Object { -not (Test-Path -LiteralPath (Join-Path $routerConfigRoot $_) -PathType Leaf) }
)
if ($missingConfigs.Count -eq 0) {
    Add-ValidationResult "V002" "Router example configs" "PASS" "All four required example configs exist."
}
else {
    Add-ValidationResult "V002" "Router example configs" "FAIL" ("Missing: " + ($missingConfigs -join ", "))
}

$missingZones = @($requiredZones | Where-Object { $topologyContent -notmatch [regex]::Escape($_) })
if ($missingZones.Count -eq 0) {
    Add-ValidationResult "V003" "Required zones" "PASS" "All required zones are documented."
}
else {
    Add-ValidationResult "V003" "Required zones" "FAIL" ("Missing: " + ($missingZones -join ", "))
}

$missingDevices = @($requiredDevices | Where-Object { $topologyContent -notmatch [regex]::Escape($_) })
if ($missingDevices.Count -eq 0) {
    Add-ValidationResult "V004" "Placeholder devices" "PASS" "All required placeholder devices are documented."
}
else {
    Add-ValidationResult "V004" "Placeholder devices" "FAIL" ("Missing: " + ($missingDevices -join ", "))
}

$missingCidrTokens = @($requiredCidrTokens | Where-Object { $topologyContent -notmatch [regex]::Escape($_) })
if ($missingCidrTokens.Count -eq 0) {
    Add-ValidationResult "V005" "CIDR placeholders" "PASS" "All required CIDR placeholder tokens are documented."
}
else {
    Add-ValidationResult "V005" "CIDR placeholders" "FAIL" ("Missing: " + ($missingCidrTokens -join ", "))
}

$availableConfigPaths = @(
    $requiredConfigs |
        ForEach-Object { Join-Path $routerConfigRoot $_ } |
        Where-Object { Test-Path -LiteralPath $_ -PathType Leaf }
)
$structureIssues = [System.Collections.Generic.List[string]]::new()
$secretIssues = [System.Collections.Generic.List[string]]::new()
$addressIssues = [System.Collections.Generic.List[string]]::new()

$secretPatterns = @(
    "-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----",
    "(?im)^\s*(?:password|secret|enable\s+secret)\s+(?:=|\S)",
    "(?im)^\s*username\s+\S+\s+(?:password|secret)\b",
    "(?im)^\s*(?:token|api[_-]?key|access[_-]?key)\s*[:=]"
)

foreach ($configPath in $availableConfigPaths) {
    $configName = Split-Path -Leaf $configPath
    $configContent = Get-Content -LiteralPath $configPath -Raw

    if (
        $configContent -notmatch [regex]::Escape("NON-PRODUCTION EXAMPLE") -or
        $configContent -notmatch "(?im)^interface\s+<[^>]+>" -or
        $configContent -notmatch "(?im)^ip route\s+<[^>]+>\s+<[^>]+>"
    ) {
        $structureIssues.Add($configName) | Out-Null
    }

    foreach ($pattern in $secretPatterns) {
        if ($configContent -match $pattern) {
            $secretIssues.Add($configName) | Out-Null
            break
        }
    }

    if ($configContent -match "\b(?:\d{1,3}\.){3}\d{1,3}\b") {
        $addressIssues.Add($configName) | Out-Null
    }
}

if ($structureIssues.Count -eq 0 -and $availableConfigPaths.Count -eq $requiredConfigs.Count) {
    Add-ValidationResult "V006" "Example config structure" "PASS" "All configs are marked non-production and contain placeholder interfaces and routes."
}
else {
    Add-ValidationResult "V006" "Example config structure" "FAIL" ("Invalid or unavailable configs: " + (($structureIssues | Sort-Object -Unique) -join ", "))
}

if ($secretIssues.Count -eq 0) {
    Add-ValidationResult "V007" "Secret-like content" "PASS" "No private-key or credential assignment pattern was detected."
}
else {
    Add-ValidationResult "V007" "Secret-like content" "FAIL" ("Detected in: " + (($secretIssues | Sort-Object -Unique) -join ", "))
}

if ($addressIssues.Count -eq 0) {
    Add-ValidationResult "V008" "Literal IP addresses" "PASS" "No IPv4 literal was detected in example configs."
}
else {
    Add-ValidationResult "V008" "Literal IP addresses" "FAIL" ("Detected in: " + (($addressIssues | Sort-Object -Unique) -join ", "))
}

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Repository-side EVE-NG routing baseline: $criticalFailures critical failure(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S002 EVE-NG On-Prem Routing Baseline Validation"
    "Generated: $timestamp"
    "Scope: repository topology and example config files only"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No router, EVE-NG API, cloud, credential, kubeconfig, or tfstate access was performed."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# EVE-NG Routing Baseline Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S002-eve-ng-on-prem-routing-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Overall result: **$overallResult**") | Out-Null
$summaryLines.Add("- Scope: repository topology and non-production example configs") | Out-Null
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
$summaryLines.Add("The validation read only repository documentation and example configuration files. It did not authenticate to EVE-NG, use its API, connect to routers, read credentials, contact cloud providers, inspect kubeconfig, or access tfstate.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) {
    exit 1
}

exit 0
