param(
    [switch] $LiveHttp,
    [string] $TargetUrl
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$trafficRoot = Join-Path $repositoryRoot "traffic-management"
$baselinePath = Join-Path $trafficRoot "nginx-reverse-proxy-validation.md"
$configPath = Join-Path $trafficRoot "nginx-reverse-proxy.example.conf"
$matrixPath = Join-Path $trafficRoot "nginx-reverse-proxy-rule-matrix.example.md"
$commandPath = Join-Path $trafficRoot "nginx-reverse-proxy-commands.example.md"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L3-service-operations\S024-nginx-reverse-proxy-validation"
$configTestSamplePath = Join-Path $evidenceRoot "logs\nginx-config-test.sample.txt"
$httpSamplePath = Join-Path $evidenceRoot "logs\reverse-proxy-http-response.sample.txt"
$accessSamplePath = Join-Path $evidenceRoot "logs\nginx-access-log.sample.txt"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "nginx-reverse-proxy-validation.log"
$summaryPath = Join-Path $configDirectory "nginx-reverse-proxy-summary.md"
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
    if (Test-Path -LiteralPath $Path -PathType Leaf) {
        return Get-Content -LiteralPath $Path -Raw
    }
    return ""
}

$requiredPaths = @($baselinePath, $configPath, $matrixPath, $commandPath)
$missingRequired = @($requiredPaths | Where-Object { -not (Test-Path -LiteralPath $_ -PathType Leaf) })
Add-ValidationResult "V001" "Required baseline files" $(if ($missingRequired.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingRequired.Count -eq 0) { "Baseline, config example, rule matrix, and command reference exist." } else { "One or more required baseline files are missing." })

$samplePaths = @($configTestSamplePath, $httpSamplePath, $accessSamplePath)
$missingSamples = @($samplePaths | Where-Object { -not (Test-Path -LiteralPath $_ -PathType Leaf) })
Add-ValidationResult "V002" "Sample evidence files" $(if ($missingSamples.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingSamples.Count -eq 0) { "Config test, HTTP response, and access log samples exist." } else { "One or more sample evidence files are missing." })

$baselineContent = Read-Artifact $baselinePath
$configContent = Read-Artifact $configPath
$matrixContent = Read-Artifact $matrixPath
$commandContent = Read-Artifact $commandPath
$configTestContent = Read-Artifact $configTestSamplePath
$httpSampleContent = Read-Artifact $httpSamplePath
$accessSampleContent = Read-Artifact $accessSamplePath
$combinedContent = @($baselineContent, $configContent, $matrixContent, $commandContent, $configTestContent, $httpSampleContent, $accessSampleContent) -join "`n"

$requiredBaselineTerms = @(
    'Client -> Nginx Reverse Proxy -> Backend Service', '<reverse-proxy-host>',
    '<public-service-domain>', '<backend-service>', '<backend-service-port>',
    '<backend-health-path>', '<upstream-name>', '<evidence-path>',
    'Static config validation', 'Optional live HTTP validation'
)
$missingBaselineTerms = @($requiredBaselineTerms | Where-Object { $baselineContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V003" "Reverse proxy baseline" $(if ($missingBaselineTerms.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingBaselineTerms.Count -eq 0) { "Purpose, request path, placeholders, evidence model, and validation modes are documented." } else { "Required baseline terms are missing." })

$proxyDirectivesReady = $configContent -match '(?im)^upstream\s+<upstream-name-placeholder>\s*\{' -and
    $configContent -match '(?im)^server\s*\{' -and
    $configContent -match '(?im)^\s*listen\s+80\s*;' -and
    $configContent -match '(?im)^\s*server_name\s+<public-service-domain-placeholder>\s*;' -and
    $configContent -match '(?im)^\s*location\s+/\s*\{' -and
    $configContent -match '(?im)^\s*proxy_pass\s+http://<upstream-name-placeholder>\s*;' -and
    $configContent -match 'NON-PRODUCTION EXAMPLE'
Add-ValidationResult "V004" "Reverse proxy directives" $(if ($proxyDirectivesReady) { "PASS" } else { "FAIL" }) $(if ($proxyDirectivesReady) { "Upstream, server, listener, symbolic server name, location, and proxy_pass are defined." } else { "A required reverse proxy directive or example marker is missing." })

$forwardedHeadersReady = $configContent -match '(?im)^\s*proxy_set_header\s+Host\s+\$host\s*;' -and
    $configContent -match '(?im)^\s*proxy_set_header\s+X-Real-IP\s+\$remote_addr\s*;' -and
    $configContent -match '(?im)^\s*proxy_set_header\s+X-Forwarded-For\s+\$proxy_add_x_forwarded_for\s*;' -and
    $configContent -match '(?im)^\s*proxy_set_header\s+X-Forwarded-Proto\s+\$scheme\s*;'
Add-ValidationResult "V005" "Forwarded headers" $(if ($forwardedHeadersReady) { "PASS" } else { "FAIL" }) $(if ($forwardedHeadersReady) { "Host and three forwarding headers use the approved variables." } else { "A required forwarded header is missing or has an unapproved value." })

$timeoutReady = $configContent -match '(?im)^\s*proxy_connect_timeout\s+\S+\s*;' -and
    $configContent -match '(?im)^\s*proxy_send_timeout\s+\S+\s*;' -and
    $configContent -match '(?im)^\s*proxy_read_timeout\s+\S+\s*;'
Add-ValidationResult "V006" "Proxy timeout baseline" $(if ($timeoutReady) { "PASS" } else { "FAIL" }) $(if ($timeoutReady) { "Connect, send, and read timeouts are explicit." } else { "A required proxy timeout directive is missing." })

$matrixControls = @(
    'upstream backend definition', 'server listen directive', 'server_name placeholder',
    'location routing', 'proxy_pass', 'Host forwarding', 'X-Real-IP forwarding',
    'X-Forwarded-For forwarding', 'X-Forwarded-Proto forwarding',
    'proxy_connect_timeout', 'proxy_send_timeout', 'proxy_read_timeout',
    'backend health path placeholder'
)
$missingMatrixControls = @($matrixControls | Where-Object { $matrixContent -notmatch [regex]::Escape($_) })
$matrixHeadersReady = $matrixContent -match 'Reverse Proxy Control' -and $matrixContent -match 'Approved Placeholder Value' -and $matrixContent -match 'Evidence Reference'
Add-ValidationResult "V007" "Reverse proxy rule matrix" $(if ($matrixHeadersReady -and $missingMatrixControls.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($matrixHeadersReady -and $missingMatrixControls.Count -eq 0) { "All thirteen required controls and matrix columns are documented." } else { "The rule matrix is incomplete." })

$requiredCommands = @(
    'nginx -t -c <nginx-config-placeholder>',
    'curl -I http://<reverse-proxy-host-placeholder>/',
    'curl http://<reverse-proxy-host-placeholder>/<backend-health-path-placeholder>',
    'tail -n 100 <nginx-access-log-placeholder>',
    'tail -n 100 <nginx-error-log-placeholder>'
)
$missingCommands = @($requiredCommands | Where-Object { $commandContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V008" "Safe command reference" $(if ($missingCommands.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingCommands.Count -eq 0) { "All five non-production command examples are documented." } else { "A required command example is missing." })

$configTestReady = $configTestContent -match '(?i)syntax is ok' -and $configTestContent -match '(?i)test is successful' -and $configTestContent -match 'SAMPLE / NON-PRODUCTION'
Add-ValidationResult "V009" "Config-test sample parsing" $(if ($configTestReady) { "PASS" } else { "FAIL" }) $(if ($configTestReady) { "The marked sample contains both Nginx success indicators." } else { "The config-test sample is absent, unmarked, or unsuccessful." })

$httpSampleReady = $httpSampleContent -match '(?im)^HTTP/1\.1\s+200\s+OK\s*$' -and $httpSampleContent -match 'SAMPLE / NON-PRODUCTION'
Add-ValidationResult "V010" "HTTP response sample parsing" $(if ($httpSampleReady) { "PASS" } else { "FAIL" }) $(if ($httpSampleReady) { "The marked sample contains HTTP 200 OK." } else { "The HTTP sample is absent, unmarked, or does not contain 200 OK." })

$accessSampleReady = $accessSampleContent -match 'SAMPLE / NON-PRODUCTION' -and
    $accessSampleContent -match '<client-placeholder>' -and
    $accessSampleContent -match '"GET /<backend-health-path-placeholder> HTTP/1\.1"\s+200'
Add-ValidationResult "V011" "Access-log sample parsing" $(if ($accessSampleReady) { "PASS" } else { "FAIL" }) $(if ($accessSampleReady) { "The marked sample contains symbolic client, request, and 200 status evidence." } else { "The access-log sample is incomplete or unmarked." })

$tlsMaterialHit = $combinedContent -match '-----BEGIN (?:CERTIFICATE|(?:[A-Z ]+ )?PRIVATE KEY)-----' -or
    $configContent -match '(?im)^\s*(?:ssl_certificate|ssl_certificate_key)\s+\S+' -or
    $configContent -match '(?im)^\s*(?:tls\.crt|tls\.key)\s*[:=]\s*\S+'
Add-ValidationResult "V012" "TLS material safety" $(if (-not $tlsMaterialHit) { "PASS" } else { "FAIL" }) $(if (-not $tlsMaterialHit) { "No certificate, private key, or TLS path/material exists." } else { "TLS certificate or private material/path was detected." })

$sensitiveAssignmentHit = $combinedContent -match '(?im)^\s*(?:password|token|secret|api[-_]?key|access[-_]?key|cookie|authorization)\s*[:=]\s*(?!["'']?<)\S+' -or
    $configContent -match '(?im)^\s*auth_basic(?:_user_file)?\b' -or
    $combinedContent -match '(?im)^\s*(?:Authorization|Cookie|Set-Cookie):\s*(?!<)\S+'
Add-ValidationResult "V013" "Credential and header safety" $(if (-not $sensitiveAssignmentHit) { "PASS" } else { "FAIL" }) $(if (-not $sensitiveAssignmentHit) { "No credential, token, cookie, authorization value, basic-auth directive, or secret assignment exists." } else { "Credential-like content or a sensitive header was detected." })

$ipMatches = @([regex]::Matches($combinedContent, '(?<![A-Za-z0-9<])(?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?(?![A-Za-z0-9>])'))
$domainMatches = @([regex]::Matches($combinedContent, '(?i)(?<![A-Za-z0-9<.-])(?:[a-z0-9-]+\.)+[a-z]{2,}(?![A-Za-z0-9>.-])') | ForEach-Object { $_.Value.ToLowerInvariant() })
$unexpectedDomains = @($domainMatches | Where-Object { $_ -notmatch '\.(?:md|conf|txt|ps1)$' } | Sort-Object -Unique)
$nonPlaceholderUrls = @([regex]::Matches($combinedContent, '(?i)https?://(?!<)[^\s;`]+'))
$addressSafe = $ipMatches.Count -eq 0 -and $unexpectedDomains.Count -eq 0 -and $nonPlaceholderUrls.Count -eq 0
Add-ValidationResult "V014" "Address and domain safety" $(if ($addressSafe) { "PASS" } else { "FAIL" }) $(if ($addressSafe) { "No numeric address, real domain, or non-placeholder URL exists." } else { "A numeric address, real domain, or non-placeholder URL was detected." })

$exampleSafe = $configContent -notmatch '(?im)^\s*proxy_pass\s+https?://(?:\*|\$request_uri|\$host)' -and
    $configContent -notmatch '(?im)^\s*resolver\s+' -and
    $configContent -notmatch '(?im)^\s*listen\s+443\b'
Add-ValidationResult "V015" "Proxy example safety" $(if ($exampleSafe) { "PASS" } else { "FAIL" }) $(if ($exampleSafe) { "No broad dynamic proxying, resolver, or TLS listener is defined." } else { "An unsafe broad proxy or out-of-scope TLS directive was detected." })

$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$executionSafe = $scriptContent -notmatch '(?im)^\s*(?:&\s*)?nginx(?:\.exe)?\s+' -and
    $scriptContent -notmatch '(?im)^\s*(?:&\s*)?curl(?:\.exe)?\s+' -and
    $scriptContent -notmatch '(?i)nginx\s+-s\s+reload' -and
    $scriptContent -match 'if \(\$LiveHttp\)' -and
    $scriptContent -match 'HttpMethod\]::Head' -and
    $scriptContent -match 'UseCookies\s*=\s*\$false'
Add-ValidationResult "V016" "Execution safety boundary" $(if ($executionSafe) { "PASS" } else { "FAIL" }) $(if ($executionSafe) { "Nginx and curl are never invoked; guarded LiveHttp uses a cookie-free HEAD request." } else { "Execution boundary checks failed." })

$liveResult = "PASS"
$liveDetail = "Static mode completed without running Nginx, curl, or a network request."
$sanitizedLiveStatus = "NOT_RUN"
if ($LiveHttp) {
    if ([string]::IsNullOrWhiteSpace($TargetUrl)) {
        $liveResult = "FAIL"
        $liveDetail = "LiveHttp requires -TargetUrl; no request was sent."
        $sanitizedLiveStatus = "MISSING_TARGET"
    }
    else {
        $targetUri = $null
        $uriValid = [System.Uri]::TryCreate($TargetUrl, [System.UriKind]::Absolute, [ref] $targetUri) -and
            $targetUri.Scheme -in @("http", "https") -and
            [string]::IsNullOrEmpty($targetUri.UserInfo)
        if (-not $uriValid) {
            $liveResult = "FAIL"
            $liveDetail = "TargetUrl must be an absolute HTTP(S) URL without embedded user information; no request was sent."
            $sanitizedLiveStatus = "INVALID_TARGET"
        }
        else {
            $handler = $null
            $client = $null
            $request = $null
            try {
                Add-Type -AssemblyName System.Net.Http
                $handler = [System.Net.Http.HttpClientHandler]::new()
                $handler.UseCookies = $false
                $handler.AllowAutoRedirect = $false
                $client = [System.Net.Http.HttpClient]::new($handler)
                $client.Timeout = [TimeSpan]::FromSeconds(10)
                $request = [System.Net.Http.HttpRequestMessage]::new([System.Net.Http.HttpMethod]::Head, $targetUri)
                $response = $client.SendAsync($request).GetAwaiter().GetResult()
                $statusCode = [int] $response.StatusCode
                $sanitizedLiveStatus = [string] $statusCode
                if ($statusCode -in @(200, 204, 301, 302)) {
                    $liveDetail = "Live HEAD returned an accepted status code; target and headers were not stored."
                }
                elseif ($statusCode -in @(401, 403)) {
                    $liveResult = "WARN"
                    $liveDetail = "Live HEAD returned an authentication-related status; target and headers were not stored."
                }
                else {
                    $liveResult = "FAIL"
                    $liveDetail = "Live HEAD returned an unaccepted status code; target and headers were not stored."
                }
                $response.Dispose()
            }
            catch {
                $liveResult = "FAIL"
                $liveDetail = "Live HEAD failed or timed out; target and exception details were not stored."
                $sanitizedLiveStatus = "REQUEST_FAILED"
            }
            finally {
                if ($null -ne $request) { $request.Dispose() }
                if ($null -ne $client) { $client.Dispose() }
                if ($null -ne $handler) { $handler.Dispose() }
            }
        }
    }
}
Add-ValidationResult "V017" "Validation mode and live result" $liveResult $liveDetail

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Nginx reverse proxy ($validationMode): $criticalFailures critical failure(s), $warningCount warning(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S024 Nginx Reverse Proxy Validation"
    "Generated: $timestamp"
    "Validation mode: $validationMode"
    "Sanitized live status: $sanitizedLiveStatus"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No target URL, response body, response header, cookie, authorization value, credential, address, domain, certificate, or key was stored."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$requiredFileCheck = $missingRequired.Count -eq 0 -and $missingSamples.Count -eq 0
$evidenceParsing = $configTestReady -and $httpSampleReady -and $accessSampleReady
$secretSafety = -not $tlsMaterialHit -and -not $sensitiveAssignmentHit -and $addressSafe
$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# Nginx Reverse Proxy Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S024-nginx-reverse-proxy-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Validation mode: **$validationMode**") | Out-Null
$summaryLines.Add("- Required file check result: **$(if ($requiredFileCheck) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Reverse proxy directive check result: **$(if ($proxyDirectivesReady) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Forwarded header check result: **$(if ($forwardedHeadersReady) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Timeout directive check result: **$(if ($timeoutReady) { 'PASS' } else { 'FAIL' })**") | Out-Null
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
$summaryLines.Add("Static mode performs repository-side validation only. LiveHttp requires explicit operator input, sends one HEAD request without cookies or authorization, and stores neither the target nor response content.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) { exit 1 }
exit 0
