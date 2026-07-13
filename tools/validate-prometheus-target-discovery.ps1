param(
    [switch] $LivePrometheus,
    [string] $PrometheusUrl
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$prometheusRoot = Join-Path $repositoryRoot "observability\prometheus"
$baselinePath = Join-Path $prometheusRoot "prometheus-target-discovery-validation.md"
$configPath = Join-Path $prometheusRoot "prometheus.scrape-targets.example.yml"
$matrixPath = Join-Path $prometheusRoot "prometheus-target-discovery-rule-matrix.example.md"
$commandPath = Join-Path $prometheusRoot "prometheus-target-discovery-commands.example.md"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L3-service-operations\S028-prometheus-target-discovery-validation"
$targetsSamplePath = Join-Path $evidenceRoot "logs\prometheus-targets.sample.json"
$upSamplePath = Join-Path $evidenceRoot "logs\prometheus-up-query.sample.json"
$labelsSamplePath = Join-Path $evidenceRoot "logs\prometheus-job-labels.sample.txt"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "prometheus-target-discovery-validation.log"
$summaryPath = Join-Path $configDirectory "prometheus-target-discovery-summary.md"
$validationMode = if ($LivePrometheus) { "LivePrometheus" } else { "Static" }

$requiredJobs = @(
    "prometheus-self-placeholder",
    "node-exporter-placeholder",
    "mariadb-exporter-placeholder",
    "nginx-exporter-placeholder",
    "blackbox-exporter-placeholder",
    "kubernetes-service-discovery-placeholder"
)
$requiredTargets = @(
    "<prometheus-server>",
    "<node-exporter-target>",
    "<mariadb-exporter-target>",
    "<nginx-exporter-target>",
    "<blackbox-exporter-target>",
    "<kubernetes-service-discovery-placeholder>"
)

New-Item -ItemType Directory -Force -Path $logDirectory, $configDirectory | Out-Null
$results = [System.Collections.Generic.List[object]]::new()
$outputLines = [System.Collections.Generic.List[string]]::new()
$criticalFailures = 0
$warningCount = 0

function Add-ValidationResult {
    param(
        [string] $Id,
        [string] $Description,
        [ValidateSet("PASS", "WARN", "FAIL")] [string] $Result,
        [string] $Detail
    )
    if ($Result -eq "FAIL") { $script:criticalFailures++ }
    if ($Result -eq "WARN") { $script:warningCount++ }
    $line = "[$Result] $Id ${Description}: $Detail"
    Write-Host $line
    $script:outputLines.Add($line) | Out-Null
    $script:results.Add([pscustomobject]@{ Id = $Id; Description = $Description; Result = $Result; Detail = $Detail }) | Out-Null
}

function Read-Artifact {
    param([string] $Path)
    if (Test-Path -LiteralPath $Path -PathType Leaf) { return Get-Content -LiteralPath $Path -Raw }
    return ""
}

function Convert-SafeJson {
    param([string] $Content)
    try { return $Content | ConvertFrom-Json -ErrorAction Stop }
    catch { return $null }
}

$requiredBaselinePaths = @($baselinePath, $configPath, $matrixPath, $commandPath)
$missingBaseline = @($requiredBaselinePaths | Where-Object { -not (Test-Path -LiteralPath $_ -PathType Leaf) })
Add-ValidationResult "V001" "Required baseline files" $(if ($missingBaseline.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingBaseline.Count -eq 0) { "Baseline, scrape example, rule matrix, and command reference exist." } else { "One or more required baseline files are missing." })

$baselineContent = Read-Artifact $baselinePath
$configContent = Read-Artifact $configPath
$matrixContent = Read-Artifact $matrixPath
$commandContent = Read-Artifact $commandPath
$targetsContent = Read-Artifact $targetsSamplePath
$upContent = Read-Artifact $upSamplePath
$labelsContent = Read-Artifact $labelsSamplePath
$combinedContent = @($baselineContent, $configContent, $matrixContent, $commandContent, $targetsContent, $upContent, $labelsContent) -join "`n"

$missingJobsInConfig = @($requiredJobs | Where-Object { $configContent -notmatch "(?im)^\s*-\s*job_name:\s*$([regex]::Escape($_))\s*$" })
$jobDefinitionsReady = $missingJobsInConfig.Count -eq 0 -and $configContent -match 'NON-PRODUCTION EXAMPLE'
Add-ValidationResult "V002" "Scrape job definitions" $(if ($jobDefinitionsReady) { "PASS" } else { "FAIL" }) $(if ($jobDefinitionsReady) { "All six required symbolic scrape jobs are defined." } else { "A required scrape job or example marker is missing." })

$missingTargets = @($requiredTargets | Where-Object { $configContent -notmatch [regex]::Escape($_) })
$discoveryModelReady = $missingTargets.Count -eq 0 -and $configContent -match '(?im)^\s*kubernetes_sd_configs:\s*$' -and
    $configContent -match '(?im)^\s*-\s*role:\s*endpoints\s*$'
Add-ValidationResult "V003" "Target and Kubernetes discovery model" $(if ($discoveryModelReady) { "PASS" } else { "FAIL" }) $(if ($discoveryModelReady) { "Five static target placeholders and Kubernetes endpoint discovery are defined." } else { "A target placeholder or Kubernetes discovery field is missing." })

$missingMatrixJobs = @($requiredJobs | Where-Object { $matrixContent -notmatch [regex]::Escape($_) })
$matrixReady = $missingMatrixJobs.Count -eq 0 -and $matrixContent -match 'Scrape Job' -and
    $matrixContent -match 'Expected State' -and $matrixContent -match 'Required Labels' -and
    $matrixContent -match 'Authentication material must not be committed'
Add-ValidationResult "V004" "Target discovery rule matrix" $(if ($matrixReady) { "PASS" } else { "FAIL" }) $(if ($matrixReady) { "All required jobs, UP/DOWN rules, labels, and authentication boundary are documented." } else { "The target discovery matrix is incomplete." })

$requiredCommands = @(
    'curl http://<prometheus-server-placeholder>/api/v1/targets',
    'curl http://<prometheus-server-placeholder>/api/v1/query?query=up',
    'curl http://<prometheus-server-placeholder>/api/v1/label/job/values'
)
$missingCommands = @($requiredCommands | Where-Object { $commandContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V005" "Prometheus API command reference" $(if ($missingCommands.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingCommands.Count -eq 0) { "All three symbolic API command examples are documented." } else { "A required command example is missing." })

$authConfigHit = $configContent -match '(?im)^\s*(?:basic_auth|authorization|bearer_token|bearer_token_file|password|credentials):' -or
    $configContent -match '(?im)^\s*(?:tls_config|key_file|cert_file|ca_file):\s*\S+' -or
    $combinedContent -match '-----BEGIN (?:CERTIFICATE|(?:[A-Z ]+ )?PRIVATE KEY)-----'
Add-ValidationResult "V006" "Authentication and TLS config safety" $(if (-not $authConfigHit) { "PASS" } else { "FAIL" }) $(if (-not $authConfigHit) { "No basic auth, bearer token, authorization config, TLS path, certificate, or key exists." } else { "Authentication or TLS material/config was detected." })

$ipMatches = @([regex]::Matches($combinedContent, '(?<![A-Za-z0-9<])(?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?(?![A-Za-z0-9>])'))
$domainMatches = @([regex]::Matches($combinedContent, '(?i)(?<![A-Za-z0-9<.-])(?:[a-z0-9-]+\.)+[a-z]{2,}(?![A-Za-z0-9>.-])') | ForEach-Object { $_.Value.ToLowerInvariant() })
$unexpectedDomains = @($domainMatches | Where-Object { $_ -notmatch '\.(?:md|yml|yaml|json|txt|ps1)$' } | Sort-Object -Unique)
$concreteUrls = @([regex]::Matches($combinedContent, '(?i)https?://(?!<)[^\s"`]+'))
$endpointSafe = $ipMatches.Count -eq 0 -and $unexpectedDomains.Count -eq 0 -and $concreteUrls.Count -eq 0
Add-ValidationResult "V007" "Endpoint address and domain safety" $(if ($endpointSafe) { "PASS" } else { "FAIL" }) $(if ($endpointSafe) { "No real URL, numeric address, domain, or Kubernetes API endpoint exists." } else { "A concrete URL, address, domain, or endpoint was detected." })

$samplePaths = @($targetsSamplePath, $upSamplePath, $labelsSamplePath)
$missingSamples = @($samplePaths | Where-Object { -not (Test-Path -LiteralPath $_ -PathType Leaf) })
Add-ValidationResult "V008" "Required sample evidence" $(if ($missingSamples.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingSamples.Count -eq 0) { "Targets, up-query, and job-label samples exist." } else { "One or more required evidence samples are missing." })

$targetsJson = Convert-SafeJson $targetsContent
$targetsJsonReady = $null -ne $targetsJson -and $targetsJson.sample_notice -eq 'SAMPLE / NON-PRODUCTION' -and $targetsJson.status -eq 'success'
Add-ValidationResult "V009" "Targets JSON syntax" $(if ($targetsJsonReady) { "PASS" } else { "FAIL" }) $(if ($targetsJsonReady) { "The marked targets sample is valid success JSON." } else { "Targets evidence is invalid JSON or lacks its sample/success marker." })

$targetJobMap = @{}
if ($targetsJsonReady) {
    foreach ($target in @($targetsJson.data.activeTargets)) {
        if ($null -ne $target.labels -and $null -ne $target.labels.job) { $targetJobMap[[string]$target.labels.job] = [string]$target.health }
    }
}
$missingTargetJobs = @($requiredJobs | Where-Object { -not $targetJobMap.ContainsKey($_) })
$downTargetJobs = @($requiredJobs | Where-Object { $targetJobMap.ContainsKey($_) -and $targetJobMap[$_] -ne 'up' })
$targetEvidenceReady = $missingTargetJobs.Count -eq 0 -and $downTargetJobs.Count -eq 0
Add-ValidationResult "V010" "Target discovery and health evidence" $(if ($targetEvidenceReady) { "PASS" } else { "FAIL" }) $(if ($targetEvidenceReady) { "All six required jobs are discoverable with health up." } else { "A required target is missing or not up." })

$upJson = Convert-SafeJson $upContent
$upJsonReady = $null -ne $upJson -and $upJson.sample_notice -eq 'SAMPLE / NON-PRODUCTION' -and $upJson.status -eq 'success'
Add-ValidationResult "V011" "UP query JSON syntax" $(if ($upJsonReady) { "PASS" } else { "FAIL" }) $(if ($upJsonReady) { "The marked up-query sample is valid success JSON." } else { "UP evidence is invalid JSON or lacks its sample/success marker." })

$upJobMap = @{}
if ($upJsonReady) {
    foreach ($series in @($upJson.data.result)) {
        if ($null -ne $series.metric -and $null -ne $series.metric.job -and @($series.value).Count -ge 2) {
            $upJobMap[[string]$series.metric.job] = [string]$series.value[1]
        }
    }
}
$missingUpJobs = @($requiredJobs | Where-Object { -not $upJobMap.ContainsKey($_) })
$zeroUpJobs = @($requiredJobs | Where-Object { $upJobMap.ContainsKey($_) -and $upJobMap[$_] -ne '1' })
$upEvidenceReady = $missingUpJobs.Count -eq 0 -and $zeroUpJobs.Count -eq 0
Add-ValidationResult "V012" "UP query required job values" $(if ($upEvidenceReady) { "PASS" } else { "FAIL" }) $(if ($upEvidenceReady) { "All six required jobs report up value 1." } else { "A required up series is missing or not equal to 1." })

$labelLines = @($labelsContent -split '\r?\n' | ForEach-Object { $_.Trim() } | Where-Object { $_ -and $_ -ne 'SAMPLE / NON-PRODUCTION' })
$missingLabelJobs = @($requiredJobs | Where-Object { $_ -notin $labelLines })
$labelsReady = $labelsContent -match 'SAMPLE / NON-PRODUCTION' -and $missingLabelJobs.Count -eq 0
Add-ValidationResult "V013" "Job label evidence" $(if ($labelsReady) { "PASS" } else { "FAIL" }) $(if ($labelsReady) { "The sanitized label sample contains all required job values." } else { "A required job label or sample marker is missing." })

$secretAssignmentHit = $combinedContent -match '(?im)^\s*["'']?(?:password|token|secret|api[-_]?key|access[-_]?key|cookie|authorization|client-key-data|client-certificate-data)["'']?\s*[:=]\s*(?!["'']?<)\S+' -or
    $combinedContent -match '(?im)^\s*(?:Authorization|Cookie|Set-Cookie):\s*(?!<)\S+'
$accountIdHit = $combinedContent -match '(?<!\d)\d{12}(?!\d)' -or $combinedContent -match '(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b'
$contentSafe = -not $secretAssignmentHit -and -not $accountIdHit
Add-ValidationResult "V014" "Credential token and account safety" $(if ($contentSafe) { "PASS" } else { "FAIL" }) $(if ($contentSafe) { "No credential, token, cookie, authorization value, secret assignment, account ID, or UUID exists." } else { "Sensitive or account-specific content was detected." })

$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$reloadPath = '/' + '-/' + 'reload'
$executionSafe = $scriptContent -notmatch '(?im)^\s*(?:&\s*)?curl(?:\.exe)?\s+' -and
    $scriptContent -notmatch '(?im)^\s*(?:prometheus|promtool)(?:\.exe)?\s+' -and
    $scriptContent -match 'if \(\$LivePrometheus\)' -and
    $scriptContent -match 'UseCookies\s*=\s*\$false' -and
    $scriptContent -notmatch [regex]::Escape($reloadPath)
Add-ValidationResult "V015" "Execution safety boundary" $(if ($executionSafe) { "PASS" } else { "FAIL" }) $(if ($executionSafe) { "Static mode invokes no client; guarded live mode is cookie-free and contains no reload path." } else { "Execution guardrails are incomplete or unsafe." })

$liveResult = "PASS"
$liveDetail = "Static mode completed without curl, Prometheus query, process start/reload, or network access."
$liveMissing = @()
$liveDown = @()
$sanitizedLiveRows = @("NOT_RUN")
if ($LivePrometheus) {
    if ([string]::IsNullOrWhiteSpace($PrometheusUrl)) {
        $liveResult = "FAIL"
        $liveDetail = "LivePrometheus requires PrometheusUrl; no request was sent."
        $sanitizedLiveRows = @("MISSING_URL")
    }
    else {
        $baseUri = $null
        $validUri = [System.Uri]::TryCreate($PrometheusUrl, [System.UriKind]::Absolute, [ref]$baseUri) -and
            $baseUri.Scheme -in @('http', 'https') -and [string]::IsNullOrEmpty($baseUri.UserInfo)
        if (-not $validUri) {
            $liveResult = "FAIL"
            $liveDetail = "PrometheusUrl must be absolute HTTP(S) without user information; no request was sent."
            $sanitizedLiveRows = @("INVALID_URL")
        }
        else {
            $handler = $null
            $client = $null
            try {
                Add-Type -AssemblyName System.Net.Http
                $handler = [System.Net.Http.HttpClientHandler]::new()
                $handler.UseCookies = $false
                $handler.AllowAutoRedirect = $false
                $client = [System.Net.Http.HttpClient]::new($handler)
                $client.Timeout = [TimeSpan]::FromSeconds(10)
                $base = $baseUri.AbsoluteUri.TrimEnd('/')
                $liveTargetsText = $client.GetStringAsync("$base/api/v1/targets").GetAwaiter().GetResult()
                $liveUpText = $client.GetStringAsync("$base/api/v1/query?query=up").GetAwaiter().GetResult()
                $liveTargetsJson = Convert-SafeJson $liveTargetsText
                $liveUpJson = Convert-SafeJson $liveUpText
                if ($null -eq $liveTargetsJson -or $null -eq $liveUpJson -or $liveTargetsJson.status -ne 'success' -or $liveUpJson.status -ne 'success') {
                    throw "Invalid API response"
                }
                $liveTargetMap = @{}
                foreach ($target in @($liveTargetsJson.data.activeTargets)) {
                    if ($null -ne $target.labels -and $null -ne $target.labels.job -and [string]$target.labels.job -in $requiredJobs) {
                        $liveTargetMap[[string]$target.labels.job] = [string]$target.health
                    }
                }
                $liveUpMap = @{}
                foreach ($series in @($liveUpJson.data.result)) {
                    if ($null -ne $series.metric -and [string]$series.metric.job -in $requiredJobs -and @($series.value).Count -ge 2) {
                        $liveUpMap[[string]$series.metric.job] = [string]$series.value[1]
                    }
                }
                $liveMissing = @($requiredJobs | Where-Object { -not $liveTargetMap.ContainsKey($_) -or -not $liveUpMap.ContainsKey($_) })
                $liveDown = @($requiredJobs | Where-Object {
                    ($liveTargetMap.ContainsKey($_) -and $liveTargetMap[$_] -ne 'up') -or
                    ($liveUpMap.ContainsKey($_) -and $liveUpMap[$_] -ne '1')
                })
                $sanitizedLiveRows = @($requiredJobs | ForEach-Object {
                    if ($liveTargetMap.ContainsKey($_) -and $liveUpMap.ContainsKey($_)) { "$_=$($liveTargetMap[$_])/up:$($liveUpMap[$_])" } else { "$_=MISSING" }
                })
                if ($liveDown.Count -gt 0) {
                    $liveResult = "FAIL"
                    $liveDetail = "A required known job is down or reports up=0; raw API data was not stored."
                }
                elseif ($liveMissing.Count -gt 0) {
                    $liveResult = "WARN"
                    $liveDetail = "Prometheus APIs are reachable but the live lab lacks one or more placeholder jobs; raw API data was not stored."
                }
                else {
                    $liveDetail = "All required known jobs are present and healthy; only sanitized known-job judgments are retained."
                }
            }
            catch {
                $liveResult = "FAIL"
                $liveDetail = "Live Prometheus API validation failed; URL, response, and exception details were not stored."
                $sanitizedLiveRows = @("REQUEST_FAILED")
            }
            finally {
                if ($null -ne $client) { $client.Dispose() }
                if ($null -ne $handler) { $handler.Dispose() }
            }
        }
    }
}
Add-ValidationResult "V016" "Validation mode and live API result" $liveResult $liveDetail

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Prometheus target discovery ($validationMode): $criticalFailures critical failure(s), $warningCount warning(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S028 Prometheus Target Discovery Validation"
    "Generated: $timestamp"
    "Validation mode: $validationMode"
    "Sanitized known-job states: $($sanitizedLiveRows -join ', ')"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No Prometheus URL, scrape endpoint, raw label, raw API response, credential, token, cookie, authorization value, address, domain, certificate, or key was stored."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$requiredFileCheck = $missingBaseline.Count -eq 0 -and $missingSamples.Count -eq 0
$targetParsing = $targetsJsonReady -and $targetEvidenceReady -and $labelsReady
$upParsing = $upJsonReady -and $upEvidenceReady
$secretSafety = -not $authConfigHit -and $endpointSafe -and $contentSafe
$missingSummary = if ($LivePrometheus) { if ($liveMissing.Count) { $liveMissing -join ', ' } else { 'none' } } else { if ($missingTargetJobs.Count) { $missingTargetJobs -join ', ' } else { 'none' } }
$downSummary = if ($LivePrometheus) { if ($liveDown.Count) { $liveDown -join ', ' } else { 'none' } } else { if ($downTargetJobs.Count -or $zeroUpJobs.Count) { @($downTargetJobs + $zeroUpJobs | Sort-Object -Unique) -join ', ' } else { 'none' } }
$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# Prometheus Target Discovery Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S028-prometheus-target-discovery-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Validation mode: **$validationMode**") | Out-Null
$summaryLines.Add("- Required file check result: **$(if ($requiredFileCheck) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Scrape job definition check result: **$(if ($jobDefinitionsReady -and $discoveryModelReady) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Target discovery evidence parsing result: **$(if ($targetParsing) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- UP query evidence parsing result: **$(if ($upParsing) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Missing target findings: **$missingSummary**") | Out-Null
$summaryLines.Add("- Down target findings: **$downSummary**") | Out-Null
$summaryLines.Add("- Secret-safety check result: **$(if ($secretSafety) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Final judgment: **$overallResult**") | Out-Null
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
$summaryLines.Add("Static mode reads repository artifacts only. LivePrometheus requires an explicit URL, sends credential-free API GET requests, and stores only known job names and health judgments rather than raw API data.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) { exit 1 }
exit 0
