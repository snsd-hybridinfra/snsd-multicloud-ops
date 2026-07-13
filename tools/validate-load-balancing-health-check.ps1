param(
    [switch] $LiveHttp,
    [string] $LoadBalancerHealthUrl,
    [string[]] $BackendHealthUrls
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$trafficRoot = Join-Path $repositoryRoot "traffic-management"
$baselinePath = Join-Path $trafficRoot "load-balancing-health-check-validation.md"
$matrixPath = Join-Path $trafficRoot "load-balancing-health-check-rule-matrix.example.md"
$configPath = Join-Path $trafficRoot "nginx-upstream-health-check.example.conf"
$commandPath = Join-Path $trafficRoot "load-balancing-health-check-commands.example.md"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L3-service-operations\S025-load-balancing-health-check-validation"
$loadBalancerSamplePath = Join-Path $evidenceRoot "logs\load-balancer-health-response.sample.txt"
$backendSamplePath = Join-Path $evidenceRoot "logs\backend-health-response.sample.txt"
$accessSamplePath = Join-Path $evidenceRoot "logs\load-balancer-access-log.sample.txt"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "load-balancing-health-check-validation.log"
$summaryPath = Join-Path $configDirectory "load-balancing-health-check-summary.md"
$validationMode = if ($LiveHttp) { "LiveHttp" } else { "Static" }

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

function Invoke-SafeHead {
    param([string] $Url, [System.Net.Http.HttpClient] $Client)
    $uri = $null
    $valid = [System.Uri]::TryCreate($Url, [System.UriKind]::Absolute, [ref] $uri) -and
        $uri.Scheme -in @("http", "https") -and [string]::IsNullOrEmpty($uri.UserInfo)
    if (-not $valid) { return [pscustomobject]@{ State = "FAIL"; Code = "INVALID_TARGET" } }
    $request = $null
    $response = $null
    try {
        $request = [System.Net.Http.HttpRequestMessage]::new([System.Net.Http.HttpMethod]::Head, $uri)
        $response = $Client.SendAsync($request).GetAwaiter().GetResult()
        $code = [int] $response.StatusCode
        if ($code -in @(200, 204)) { return [pscustomobject]@{ State = "PASS"; Code = [string]$code } }
        if ($code -in @(401, 403)) { return [pscustomobject]@{ State = "WARN"; Code = [string]$code } }
        return [pscustomobject]@{ State = "FAIL"; Code = [string]$code }
    }
    catch {
        return [pscustomobject]@{ State = "FAIL"; Code = "REQUEST_FAILED" }
    }
    finally {
        if ($null -ne $response) { $response.Dispose() }
        if ($null -ne $request) { $request.Dispose() }
    }
}

$requiredPaths = @($baselinePath, $matrixPath, $configPath, $commandPath)
$missingRequired = @($requiredPaths | Where-Object { -not (Test-Path -LiteralPath $_ -PathType Leaf) })
Add-ValidationResult "V001" "Required baseline files" $(if ($missingRequired.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingRequired.Count -eq 0) { "Baseline, rule matrix, upstream example, and command reference exist." } else { "One or more required baseline files are missing." })

$samplePaths = @($loadBalancerSamplePath, $backendSamplePath, $accessSamplePath)
$missingSamples = @($samplePaths | Where-Object { -not (Test-Path -LiteralPath $_ -PathType Leaf) })
Add-ValidationResult "V002" "Sample evidence files" $(if ($missingSamples.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingSamples.Count -eq 0) { "Load-balancer, backend, and access-log samples exist." } else { "One or more required samples are missing." })

$baselineContent = Read-Artifact $baselinePath
$matrixContent = Read-Artifact $matrixPath
$configContent = Read-Artifact $configPath
$commandContent = Read-Artifact $commandPath
$loadBalancerContent = Read-Artifact $loadBalancerSamplePath
$backendContent = Read-Artifact $backendSamplePath
$accessContent = Read-Artifact $accessSamplePath
$combinedContent = @($baselineContent, $matrixContent, $configContent, $commandContent, $loadBalancerContent, $backendContent, $accessContent) -join "`n"

$baselineTerms = @(
    'Client -> Load Balancing Layer -> Healthy Backend Service', '<load-balancer>', '<backend-pool>',
    '<backend-service-a>', '<backend-service-b>', '<backend-health-path>', '<expected-status-code>',
    '<health-check-interval>', '<health-check-timeout>', '<unhealthy-threshold>', '<evidence-path>',
    'Manual recovery / failover relationship', 'Static validation', 'Optional live HTTP health check validation'
)
$missingBaselineTerms = @($baselineTerms | Where-Object { $baselineContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V003" "Health-check baseline" $(if ($missingBaselineTerms.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingBaselineTerms.Count -eq 0) { "Path, pool, health settings, evidence, manual recovery, and validation modes are documented." } else { "Required health-check baseline terms are missing." })

$poolReady = $configContent -match '(?im)^upstream\s+<backend-pool-placeholder>\s*\{' -and
    $configContent -match '(?im)^\s*server\s+<backend-service-a-placeholder>\s*;' -and
    $configContent -match '(?im)^\s*server\s+<backend-service-b-placeholder>\s*;' -and
    $configContent -match 'NON-PRODUCTION EXAMPLE'
Add-ValidationResult "V004" "Backend pool definition" $(if ($poolReady) { "PASS" } else { "FAIL" }) $(if ($poolReady) { "The symbolic pool contains both backend placeholders." } else { "The upstream pool, backend members, or example marker is missing." })

$healthEndpointReady = $configContent -match '(?im)^\s*location\s+/health\s*\{' -and
    $configContent -match '(?im)^\s*proxy_pass\s+http://<backend-pool-placeholder>\s*;' -and
    $baselineContent -match [regex]::Escape('<expected-status-code>')
Add-ValidationResult "V005" "Health endpoint and expected status" $(if ($healthEndpointReady) { "PASS" } else { "FAIL" }) $(if ($healthEndpointReady) { "The /health route, pool proxy, and expected status placeholder are defined." } else { "Health route, pool proxy, or expected status is missing." })

$passiveHandlingReady = $configContent -match '(?im)^\s*proxy_next_upstream\s+.+;' -and
    $configContent -match '(?im)^\s*proxy_next_upstream_tries\s+\d+\s*;' -and
    $configContent -match '(?im)^\s*proxy_connect_timeout\s+\S+\s*;' -and
    $configContent -match '(?im)^\s*proxy_read_timeout\s+\S+\s*;' -and
    $configContent -match '(?im)^\s*proxy_send_timeout\s+\S+\s*;' -and
    $baselineContent -match [regex]::Escape('<unhealthy-threshold>')
Add-ValidationResult "V006" "Timeout retry and unhealthy handling" $(if ($passiveHandlingReady) { "PASS" } else { "FAIL" }) $(if ($passiveHandlingReady) { "Passive retry, retry count, three timeouts, and unhealthy threshold are defined." } else { "Timeout, retry, or unhealthy handling is incomplete." })

$matrixControls = @(
    'backend pool definition', 'backend health path', 'expected HTTP status code', 'health check interval',
    'timeout', 'retry / unhealthy threshold', 'healthy backend count', 'unhealthy backend detection',
    'backend exclusion behavior', 'manual recovery / failover reference'
)
$missingControls = @($matrixControls | Where-Object { $matrixContent -notmatch [regex]::Escape($_) })
$matrixHeadersReady = $matrixContent -match 'Health Check Control' -and $matrixContent -match 'Approved Placeholder Value' -and $matrixContent -match 'Evidence Reference'
Add-ValidationResult "V007" "Health-check rule matrix" $(if ($matrixHeadersReady -and $missingControls.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($matrixHeadersReady -and $missingControls.Count -eq 0) { "All ten controls and required columns are documented." } else { "The health-check matrix is incomplete." })

$requiredCommands = @(
    'curl -I http://<load-balancer-placeholder>/<backend-health-path-placeholder>',
    'curl http://<backend-service-a-placeholder>/<backend-health-path-placeholder>',
    'curl http://<backend-service-b-placeholder>/<backend-health-path-placeholder>',
    'tail -n 100 <load-balancer-access-log-placeholder>',
    'tail -n 100 <load-balancer-error-log-placeholder>'
)
$missingCommands = @($requiredCommands | Where-Object { $commandContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V008" "Safe command reference" $(if ($missingCommands.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingCommands.Count -eq 0) { "All five symbolic command examples exist." } else { "A required command example is missing." })

$failurePattern = '(?i)\b(?:500|502|503|504)\b|connection refused|timed?\s*out|unhealthy|no healthy upstream'
$loadBalancerSampleReady = $loadBalancerContent -match 'SAMPLE / NON-PRODUCTION' -and
    $loadBalancerContent -match '(?im)^HTTP/1\.1\s+200\s+OK\s*$' -and $loadBalancerContent -notmatch $failurePattern
Add-ValidationResult "V009" "Load-balancer health evidence" $(if ($loadBalancerSampleReady) { "PASS" } else { "FAIL" }) $(if ($loadBalancerSampleReady) { "The marked sample contains 200 OK and no failure indicator." } else { "The load-balancer sample is missing, unhealthy, or unacceptable." })

$backendAReady = $backendContent -match '(?im)^backend-service-a-placeholder:\s*200\s+OK\s*$'
$backendBReady = $backendContent -match '(?im)^backend-service-b-placeholder:\s*200\s+OK\s*$'
$backendSampleReady = $backendContent -match 'SAMPLE / NON-PRODUCTION' -and $backendAReady -and $backendBReady -and $backendContent -notmatch $failurePattern
Add-ValidationResult "V010" "Backend health evidence" $(if ($backendSampleReady) { "PASS" } else { "FAIL" }) $(if ($backendSampleReady) { "Both symbolic backends are marked 200 OK with no failure indicator." } else { "Backend-specific evidence is missing or indicates an unhealthy member." })

$accessSampleReady = $accessContent -match 'SAMPLE / NON-PRODUCTION' -and
    $accessContent -match '"GET /health HTTP/1\.1"\s+200' -and $accessContent -match '<client-placeholder>'
Add-ValidationResult "V011" "Access-log health evidence" $(if ($accessSampleReady) { "PASS" } else { "FAIL" }) $(if ($accessSampleReady) { "The sanitized access sample contains a symbolic /health request and 200 status." } else { "The access sample is incomplete or unsanitized." })

$tlsHit = $combinedContent -match '-----BEGIN (?:CERTIFICATE|(?:[A-Z ]+ )?PRIVATE KEY)-----' -or
    $configContent -match '(?im)^\s*(?:ssl_certificate|ssl_certificate_key)\s+\S+'
Add-ValidationResult "V012" "TLS material safety" $(if (-not $tlsHit) { "PASS" } else { "FAIL" }) $(if (-not $tlsHit) { "No certificate, key, or TLS path/material exists." } else { "TLS certificate or private material/path was detected." })

$secretHit = $combinedContent -match '(?im)^\s*(?:password|token|secret|api[-_]?key|access[-_]?key|cookie|authorization)\s*[:=]\s*(?!["'']?<)\S+' -or
    $configContent -match '(?im)^\s*auth_basic(?:_user_file)?\b' -or
    $combinedContent -match '(?im)^\s*(?:Authorization|Cookie|Set-Cookie):\s*(?!<)\S+'
Add-ValidationResult "V013" "Credential and header safety" $(if (-not $secretHit) { "PASS" } else { "FAIL" }) $(if (-not $secretHit) { "No credential, token, cookie, authorization value, auth directive, or secret assignment exists." } else { "Sensitive or credential-like content was detected." })

$ipMatches = @([regex]::Matches($combinedContent, '(?<![A-Za-z0-9<])(?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?(?![A-Za-z0-9>])'))
$domainMatches = @([regex]::Matches($combinedContent, '(?i)(?<![A-Za-z0-9<.-])(?:[a-z0-9-]+\.)+[a-z]{2,}(?![A-Za-z0-9>.-])') | ForEach-Object { $_.Value.ToLowerInvariant() })
$unexpectedDomains = @($domainMatches | Where-Object { $_ -notmatch '\.(?:md|conf|txt|ps1)$' } | Sort-Object -Unique)
$nonPlaceholderUrls = @([regex]::Matches($combinedContent, '(?i)https?://(?!<)[^\s;`]+'))
$addressSafe = $ipMatches.Count -eq 0 -and $unexpectedDomains.Count -eq 0 -and $nonPlaceholderUrls.Count -eq 0
Add-ValidationResult "V014" "Address and domain safety" $(if ($addressSafe) { "PASS" } else { "FAIL" }) $(if ($addressSafe) { "No numeric address, real domain, or concrete URL exists." } else { "A numeric address, real domain, or concrete URL was detected." })

$scopeSafe = $baselineContent -match '(?i)does not claim Nginx Plus active health checking' -and
    $configContent -match '(?i)active health checks.*out of scope' -and
    $configContent -notmatch '(?im)^\s*health_check\s*;'
Add-ValidationResult "V015" "Active-health and failover boundary" $(if ($scopeSafe) { "PASS" } else { "FAIL" }) $(if ($scopeSafe) { "Passive evidence scope is explicit and no active-health directive is claimed." } else { "Active-health scope is ambiguous or an unsupported directive exists." })

$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$executionSafe = $scriptContent -notmatch '(?im)^\s*(?:&\s*)?nginx(?:\.exe)?\s+' -and
    $scriptContent -notmatch '(?im)^\s*(?:&\s*)?curl(?:\.exe)?\s+' -and
    $scriptContent -notmatch '(?i)nginx\s+-s\s+reload' -and
    $scriptContent -match 'if \(\$LiveHttp\)' -and $scriptContent -match 'HttpMethod\]::Head' -and
    $scriptContent -match 'UseCookies\s*=\s*\$false'
Add-ValidationResult "V016" "Execution safety boundary" $(if ($executionSafe) { "PASS" } else { "FAIL" }) $(if ($executionSafe) { "Nginx and curl are never invoked; guarded live mode uses cookie-free HEAD requests." } else { "Execution safety guards are incomplete." })

$liveResult = "PASS"
$liveDetail = "Static mode completed without running Nginx, curl, failover, or a network request."
$sanitizedStatuses = @("NOT_RUN")
if ($LiveHttp) {
    $hasLoadBalancer = -not [string]::IsNullOrWhiteSpace($LoadBalancerHealthUrl)
    $backendTargets = @($BackendHealthUrls | Where-Object { -not [string]::IsNullOrWhiteSpace($_) })
    if (-not $hasLoadBalancer -or $backendTargets.Count -eq 0) {
        $liveResult = "FAIL"
        $liveDetail = "LiveHttp requires LoadBalancerHealthUrl and at least one BackendHealthUrls value; no request was sent."
        $sanitizedStatuses = @("MISSING_TARGETS")
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
            $liveChecks = [System.Collections.Generic.List[object]]::new()
            $liveChecks.Add((Invoke-SafeHead -Url $LoadBalancerHealthUrl -Client $client)) | Out-Null
            foreach ($backendUrl in $backendTargets) { $liveChecks.Add((Invoke-SafeHead -Url $backendUrl -Client $client)) | Out-Null }
            $sanitizedStatuses = @($liveChecks | ForEach-Object { $_.Code })
            $failed = @($liveChecks | Where-Object { $_.State -eq "FAIL" }).Count
            $warned = @($liveChecks | Where-Object { $_.State -eq "WARN" }).Count
            if ($failed -gt 0) {
                $liveResult = "FAIL"
                $liveDetail = "One or more indexed live health checks failed; targets and response content were not stored."
            }
            elseif ($warned -gt 0) {
                $liveResult = "WARN"
                $liveDetail = "One or more indexed health checks returned 401/403; targets and response content were not stored."
            }
            else {
                $liveDetail = "Load-balancer and backend HEAD checks returned accepted statuses; targets and response content were not stored."
            }
        }
        catch {
            $liveResult = "FAIL"
            $liveDetail = "Live health validation failed before completion; targets and exception details were not stored."
            $sanitizedStatuses = @("REQUEST_FAILED")
        }
        finally {
            if ($null -ne $client) { $client.Dispose() }
            if ($null -ne $handler) { $handler.Dispose() }
        }
    }
}
Add-ValidationResult "V017" "Validation mode and live health result" $liveResult $liveDetail

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Load balancing health check ($validationMode): $criticalFailures critical failure(s), $warningCount warning(s)."
Write-Host $overallLine

$indexedStatus = for ($i = 0; $i -lt $sanitizedStatuses.Count; $i++) { "check-$($i + 1)=$($sanitizedStatuses[$i])" }
$logLines = @(
    "SNSD Multi-Cloud Ops - S025 Load Balancing Health Check Validation"
    "Generated: $timestamp"
    "Validation mode: $validationMode"
    "Sanitized live statuses: $($indexedStatus -join ', ')"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No target URL, header, body, cookie, authorization value, credential, address, domain, certificate, or key was stored."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$requiredFileCheck = $missingRequired.Count -eq 0 -and $missingSamples.Count -eq 0
$evidenceParsing = $loadBalancerSampleReady -and $backendSampleReady -and $accessSampleReady
$secretSafety = -not $tlsHit -and -not $secretHit -and $addressSafe
$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# Load Balancing Health Check Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S025-load-balancing-health-check-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Validation mode: **$validationMode**") | Out-Null
$summaryLines.Add("- Required file check result: **$(if ($requiredFileCheck) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Backend pool definition check result: **$(if ($poolReady) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Health endpoint check result: **$(if ($healthEndpointReady) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Timeout / retry / unhealthy threshold check result: **$(if ($passiveHandlingReady) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Evidence parsing result: **$(if ($evidenceParsing) { 'PASS' } else { 'FAIL' })**") | Out-Null
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
$summaryLines.Add("Static mode performs repository-side validation only. LiveHttp requires explicit load-balancer and backend URLs, sends HEAD requests without cookies or authorization, stores indexed statuses only, and never performs failover.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) { exit 1 }
exit 0
