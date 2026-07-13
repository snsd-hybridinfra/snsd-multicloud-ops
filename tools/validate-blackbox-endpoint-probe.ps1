param(
    [switch]$LiveBlackbox,
    [string]$BlackboxExporterUrl,
    [string]$TargetUrl
)

$ErrorActionPreference="Stop"; Set-StrictMode -Version Latest
$repositoryRoot=Split-Path -Parent $PSScriptRoot
$exporterRoot=Join-Path $repositoryRoot "observability\exporters"
$baselinePath=Join-Path $exporterRoot "blackbox-endpoint-probe-validation.md"
$configPath=Join-Path $exporterRoot "blackbox-exporter.example.yml"
$scrapePath=Join-Path $repositoryRoot "observability\prometheus\blackbox-endpoint-probe-scrape.example.yml"
$matrixPath=Join-Path $exporterRoot "blackbox-endpoint-probe-rule-matrix.example.md"
$commandPath=Join-Path $exporterRoot "blackbox-endpoint-probe-commands.example.md"
$evidenceRoot=Join-Path $repositoryRoot "evidence\L3-service-operations\S030-blackbox-endpoint-probe-validation"
$successPath=Join-Path $evidenceRoot "logs\blackbox-probe-success.sample.txt"
$warningPath=Join-Path $evidenceRoot "logs\blackbox-probe-warning.sample.txt"
$failurePath=Join-Path $evidenceRoot "logs\blackbox-probe-failure.sample.txt"
$queryPath=Join-Path $evidenceRoot "logs\prometheus-probe-query.sample.json"
$logDirectory=Join-Path $evidenceRoot "logs"; $configDirectory=Join-Path $evidenceRoot "configs"
$logPath=Join-Path $logDirectory "blackbox-endpoint-probe-validation.log"
$summaryPath=Join-Path $configDirectory "blackbox-endpoint-probe-summary.md"
$validationMode=if($LiveBlackbox){"LiveBlackbox"}else{"Static"}

New-Item -ItemType Directory -Force -Path $logDirectory,$configDirectory|Out-Null
$results=[System.Collections.Generic.List[object]]::new(); $outputLines=[System.Collections.Generic.List[string]]::new(); $criticalFailures=0; $warningCount=0
function Add-ValidationResult{param([string]$Id,[string]$Description,[ValidateSet("PASS","WARN","FAIL")][string]$Result,[string]$Detail);if($Result-eq"FAIL"){$script:criticalFailures++};if($Result-eq"WARN"){$script:warningCount++};$line="[$Result] $Id ${Description}: $Detail";Write-Host $line;$script:outputLines.Add($line)|Out-Null;$script:results.Add([pscustomobject]@{Id=$Id;Description=$Description;Result=$Result;Detail=$Detail})|Out-Null}
function Read-Artifact{param([string]$Path);if(Test-Path -LiteralPath $Path -PathType Leaf){return Get-Content -LiteralPath $Path -Raw};return ""}
function Get-ProbeMetrics{param([string]$Content);$s=[regex]::Match($Content,'(?im)^probe_success[ \t]+([01](?:\.0+)?)\s*$');$h=[regex]::Match($Content,'(?im)^probe_http_status_code[ \t]+(\d+(?:\.0+)?)\s*$');$d=[regex]::Match($Content,'(?im)^probe_duration_seconds[ \t]+(\d+(?:\.\d+)?)\s*$');return [pscustomobject]@{Marked=$Content-match'SAMPLE / NON-PRODUCTION';SuccessFound=$s.Success;Success=if($s.Success){[double]$s.Groups[1].Value}else{$null};HttpFound=$h.Success;Http=if($h.Success){[double]$h.Groups[1].Value}else{$null};DurationFound=$d.Success;Duration=if($d.Success){[double]$d.Groups[1].Value}else{$null}}}
function Convert-SafeJson{param([string]$Content);try{return $Content|ConvertFrom-Json -ErrorAction Stop}catch{return $null}}

$baselinePaths=@($baselinePath,$configPath,$scrapePath,$matrixPath,$commandPath);$missingBaseline=@($baselinePaths|Where-Object{-not(Test-Path -LiteralPath $_ -PathType Leaf)})
Add-ValidationResult "V001" "Required probe baseline files" $(if($missingBaseline.Count-eq 0){"PASS"}else{"FAIL"}) $(if($missingBaseline.Count-eq 0){"Baseline, exporter config, scrape config, matrix, and commands exist."}else{"One or more baseline files are missing."})
$baselineContent=Read-Artifact $baselinePath;$configContent=Read-Artifact $configPath;$scrapeContent=Read-Artifact $scrapePath;$matrixContent=Read-Artifact $matrixPath;$commandContent=Read-Artifact $commandPath;$successContent=Read-Artifact $successPath;$warningContent=Read-Artifact $warningPath;$failureContent=Read-Artifact $failurePath;$queryContent=Read-Artifact $queryPath
$combinedContent=@($baselineContent,$configContent,$scrapeContent,$matrixContent,$commandContent,$successContent,$warningContent,$failureContent,$queryContent)-join"`n"

$modulesReady=$configContent-match'NON-PRODUCTION EXAMPLE' -and $configContent-match'(?im)^\s*http_2xx_placeholder:\s*$' -and $configContent-match'(?im)^\s*tcp_connect_placeholder:\s*$' -and $configContent-match'(?im)^\s*prober:\s*http\s*$' -and $configContent-match'(?im)^\s*prober:\s*tcp\s*$' -and $configContent-match'valid_status_codes:\s*\[200,\s*204\]' -and $configContent-match'valid_http_versions' -and $configContent-match'(?im)^\s*method:\s*GET\s*$' -and $configContent-match'preferred_ip_protocol:\s*ip4' -and @([regex]::Matches($configContent,'(?im)^\s*timeout:\s*5s\s*$')).Count-ge 2
Add-ValidationResult "V002" "Blackbox module definitions" $(if($modulesReady){"PASS"}else{"FAIL"}) $(if($modulesReady){"HTTP 2xx and TCP connect modules contain required safe settings."}else{"Required module settings are incomplete."})

$scrapeReady=$scrapeContent-match'NON-PRODUCTION EXAMPLE' -and $scrapeContent-match'job_name:\s*blackbox-endpoint-probe-placeholder' -and $scrapeContent-match'metrics_path:\s*/probe' -and $scrapeContent-match'module:\s*\[http_2xx_placeholder\]' -and $scrapeContent-match'http://<endpoint-url-placeholder>' -and $scrapeContent-match'__param_target' -and $scrapeContent-match'<blackbox-exporter-placeholder>:9115'
Add-ValidationResult "V003" "Prometheus Blackbox scrape placeholder" $(if($scrapeReady){"PASS"}else{"FAIL"}) $(if($scrapeReady){"Probe path, module, symbolic target, relabeling, and exporter placeholder exist."}else{"Scrape placeholder model is incomplete."})

$metricTerms=@('probe_success','probe_http_status_code','probe_duration_seconds','probe_dns_lookup_time_seconds','probe_connect_duration_seconds','<probe-timeout-seconds>','<probe-duration-threshold-seconds>')
$missingMetricTerms=@($metricTerms|Where-Object{$baselineContent-notmatch[regex]::Escape($_)-and$matrixContent-notmatch[regex]::Escape($_)})
$thresholdReady=$baselineContent-match'probe_duration_seconds <= 2\.0' -and $baselineContent-match'greater than 2\.0 and at most 5\.0' -and $baselineContent-match'greater than 5\.0'
Add-ValidationResult "V004" "Probe metrics and threshold model" $(if($missingMetricTerms.Count-eq 0-and$thresholdReady){"PASS"}else{"FAIL"}) $(if($missingMetricTerms.Count-eq 0-and$thresholdReady){"Probe metrics and normal/warning/failure thresholds are documented."}else{"Probe metric or threshold documentation is incomplete."})

$matrixAreas=@('Probe success','HTTP status','Probe duration','DNS lookup duration placeholder','Connect duration placeholder','HTTP timeout','TCP connect failure','Endpoint missing','Endpoint intentionally disabled placeholder');$missingAreas=@($matrixAreas|Where-Object{$matrixContent-notmatch[regex]::Escape($_)});$matrixReady=$missingAreas.Count-eq 0-and$matrixContent-match'Probe Area'-and$matrixContent-match'Operational Judgment'-and$matrixContent-match'Evidence Reference'
Add-ValidationResult "V005" "Probe rule matrix" $(if($matrixReady){"PASS"}else{"FAIL"}) $(if($matrixReady){"All nine probe areas and required columns are documented."}else{"Probe rule matrix is incomplete."})

$requiredCommands=@('curl "http://<blackbox-exporter-placeholder>:9115/probe?target=<endpoint-url-placeholder>&module=http_2xx_placeholder"','query?query=probe_success','query?query=probe_http_status_code','query?query=probe_duration_seconds');$missingCommands=@($requiredCommands|Where-Object{$commandContent-notmatch[regex]::Escape($_)})
Add-ValidationResult "V006" "Probe command reference" $(if($missingCommands.Count-eq 0){"PASS"}else{"FAIL"}) $(if($missingCommands.Count-eq 0){"Exporter and three Prometheus query examples exist."}else{"Required command reference is missing."})

$samplePaths=@($successPath,$warningPath,$failurePath,$queryPath);$missingSamples=@($samplePaths|Where-Object{-not(Test-Path -LiteralPath $_ -PathType Leaf)})
Add-ValidationResult "V007" "Required probe samples" $(if($missingSamples.Count-eq 0){"PASS"}else{"FAIL"}) $(if($missingSamples.Count-eq 0){"Success, warning, failure, and query samples exist."}else{"One or more samples are missing."})

$success=Get-ProbeMetrics $successContent;$warning=Get-ProbeMetrics $warningContent;$failure=Get-ProbeMetrics $failureContent
$successReady=$success.Marked-and$success.Success-eq 1-and$success.Http-in@(200,204)-and$success.Duration-le 2.0
Add-ValidationResult "V008" "Healthy probe evidence" $(if($successReady){"PASS"}else{"FAIL"}) $(if($successReady){"probe_success=1, acceptable status, and normal duration were parsed."}else{"Healthy fixture is missing metrics or indicates failure."})
$warningReady=$warning.Marked-and$warning.Success-eq 1-and$warning.Http-in@(200,204)-and$warning.Duration-gt 2.0-and$warning.Duration-le 5.0
Add-ValidationResult "V009" "Warning duration evidence" $(if($warningReady){"WARN"}else{"FAIL"}) $(if($warningReady){"Expected warning fixture was classified above 2.0 through 5.0 seconds."}else{"Warning fixture is malformed or outside its expected range."})
$failureDetected=$failure.Marked-and$failure.Success-eq 0-and($failure.Http-eq 0-or$failure.Http-ge 500)-and($failureContent-match'(?i)timeout|connection-refused')
Add-ValidationResult "V010" "Failure negative fixture" $(if($failureDetected){"PASS"}else{"FAIL"}) $(if($failureDetected){"Failed probe and timeout/refusal placeholder were correctly rejected operationally."}else{"Failure detection fixture was not classified correctly."})

$queryJson=Convert-SafeJson $queryContent;$queryReady=$null-ne$queryJson-and$queryJson.sample_notice-eq'SAMPLE / NON-PRODUCTION'-and$queryJson.status-eq'success'-and$queryJson.endpoint-eq'<endpoint-name-placeholder>'-and[double]$queryJson.metrics.probe_success-eq 1-and[double]$queryJson.metrics.probe_http_status_code-in@(200,204)-and[double]$queryJson.metrics.probe_duration_seconds-le 2.0
Add-ValidationResult "V011" "Prometheus probe query sample" $(if($queryReady){"PASS"}else{"FAIL"}) $(if($queryReady){"Valid JSON contains all three required healthy probe metrics."}else{"Probe query JSON is invalid, incomplete, or unhealthy."})

$authHit=$combinedContent-match'(?im)^\s*(?:basic_auth|authorization|bearer_token|bearer_token_file|password|token|secret|cookie):' -or $combinedContent-match'(?im)^\s*(?:Authorization|Cookie|Set-Cookie):\s*(?!<)\S+' -or $combinedContent-match'-----BEGIN (?:CERTIFICATE|(?:[A-Z ]+ )?PRIVATE KEY)-----' -or $configContent-match'(?im)^\s*(?:key_file|cert_file):\s*\S+'
Add-ValidationResult "V012" "Credential token cookie and TLS safety" $(if(-not$authHit){"PASS"}else{"FAIL"}) $(if(-not$authHit){"No auth config, credential, token, cookie, authorization, certificate, or key exists."}else{"Sensitive probe content was detected."})

$ipMatches=@([regex]::Matches($combinedContent,'(?<![A-Za-z0-9<])(?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?(?![A-Za-z0-9>])'));$domains=@([regex]::Matches($combinedContent,'(?i)(?<![A-Za-z0-9<.-])(?:[a-z0-9-]+\.)+[a-z]{2,}(?![A-Za-z0-9>.-])')|ForEach-Object{$_.Value.ToLowerInvariant()});$unexpectedDomains=@($domains|Where-Object{$_-notmatch'\.(?:md|yml|yaml|json|txt|ps1)$'}|Sort-Object -Unique);$urls=@([regex]::Matches($combinedContent,'(?i)https?://(?!<)[^\s"`]+'));$endpointSafe=$ipMatches.Count-eq 0-and$unexpectedDomains.Count-eq 0-and$urls.Count-eq 0
Add-ValidationResult "V013" "Endpoint URL address and domain safety" $(if($endpointSafe){"PASS"}else{"FAIL"}) $(if($endpointSafe){"No real endpoint, Prometheus/Blackbox URL, address, or domain exists."}else{"Concrete endpoint content was detected."})

$accountHit=$combinedContent-match'(?<!\d)\d{12}(?!\d)'-or$combinedContent-match'(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b';Add-ValidationResult "V014" "Account and identifier safety" $(if(-not$accountHit){"PASS"}else{"FAIL"}) $(if(-not$accountHit){"No account ID or UUID exists."}else{"Account-specific identifier was detected."})

$scriptContent=Get-Content -LiteralPath $PSCommandPath -Raw;$reloadPath='/'+'-/'+'reload';$executionSafe=$scriptContent-notmatch'(?im)^\s*(?:&\s*)?curl(?:\.exe)?\s+' -and $scriptContent-match'if\(\$LiveBlackbox\)' -and $scriptContent-match'UseCookies\s*=\s*\$false' -and $scriptContent-notmatch[regex]::Escape($reloadPath)
Add-ValidationResult "V015" "Execution safety boundary" $(if($executionSafe){"PASS"}else{"FAIL"}) $(if($executionSafe){"Static mode invokes no client; live mode is explicit, cookie-free, and non-mutating."}else{"Execution guardrails are incomplete."})

$liveResult="PASS";$liveDetail="Static mode completed without curl, Prometheus/Blackbox query, reload, or network access.";$sanitizedLive=@("NOT_RUN")
if($LiveBlackbox){
 if([string]::IsNullOrWhiteSpace($BlackboxExporterUrl)-or[string]::IsNullOrWhiteSpace($TargetUrl)){$liveResult="FAIL";$liveDetail="LiveBlackbox requires exporter and target URLs; no request was sent.";$sanitizedLive=@("MISSING_URLS")}
 else{$exporterUri=$null;$targetUri=$null;$validExporter=[System.Uri]::TryCreate($BlackboxExporterUrl,[System.UriKind]::Absolute,[ref]$exporterUri)-and$exporterUri.Scheme-in@('http','https')-and[string]::IsNullOrEmpty($exporterUri.UserInfo);$validTarget=[System.Uri]::TryCreate($TargetUrl,[System.UriKind]::Absolute,[ref]$targetUri)-and$targetUri.Scheme-in@('http','https')-and[string]::IsNullOrEmpty($targetUri.UserInfo)
  if(-not($validExporter-and$validTarget)){$liveResult="FAIL";$liveDetail="Both URLs must be absolute HTTP(S) without user information; no request was sent.";$sanitizedLive=@("INVALID_URLS")}
  else{$handler=$null;$client=$null;$response=$null
   try{Add-Type -AssemblyName System.Net.Http;$handler=[System.Net.Http.HttpClientHandler]::new();$handler.UseCookies=$false;$handler.AllowAutoRedirect=$false;$client=[System.Net.Http.HttpClient]::new($handler);$client.Timeout=[TimeSpan]::FromSeconds(10);$probeUri=$exporterUri.AbsoluteUri.TrimEnd('/')+"/probe?target=$([System.Uri]::EscapeDataString($targetUri.AbsoluteUri))&module=http_2xx_placeholder";$response=$client.GetAsync($probeUri).GetAwaiter().GetResult();$code=[int]$response.StatusCode
    if($code-in@(401,403)){$liveResult="WARN";$liveDetail="Blackbox requires authentication; no credentials were sent.";$sanitizedLive=@("AUTH_REQUIRED")}
    elseif($code-ge 500){$liveResult="FAIL";$liveDetail="Blackbox returned 5xx; URLs and response were not stored.";$sanitizedLive=@("SERVER_ERROR")}
    elseif($code-ne 200){$liveResult="FAIL";$liveDetail="Blackbox returned an unacceptable HTTP status.";$sanitizedLive=@("HTTP_STATUS=$code")}
    else{$liveMetrics=Get-ProbeMetrics ($response.Content.ReadAsStringAsync().GetAwaiter().GetResult());$sanitizedLive=@("probe_success=$($liveMetrics.Success)","probe_http_status_code=$($liveMetrics.Http)","probe_duration_seconds=$($liveMetrics.Duration)");if($liveMetrics.Success-eq 1-and$liveMetrics.Http-in@(200,204)){$liveDetail="Live probe metrics are healthy; URLs/raw response were not stored."}else{$liveResult="FAIL";$liveDetail="Live probe metrics indicate failure; URLs/raw response were not stored."}}
   }catch{$liveResult="FAIL";$liveDetail="Live Blackbox validation failed; URLs, response, and exception were not stored.";$sanitizedLive=@("REQUEST_FAILED")}
   finally{if($null-ne$response){$response.Dispose()};if($null-ne$client){$client.Dispose()};if($null-ne$handler){$handler.Dispose()}}
  }
 }
}
Add-ValidationResult "V016" "Validation mode and live probe result" $liveResult $liveDetail

$timestamp=(Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK");$overallResult=if($criticalFailures-eq 0){"PASS"}else{"FAIL"};$overallLine="[$overallResult] Blackbox endpoint probe ($validationMode): $criticalFailures critical failure(s), $warningCount warning(s).";Write-Host $overallLine
@("SNSD Multi-Cloud Ops - S030 Blackbox Endpoint Probe Validation","Generated: $timestamp","Validation mode: $validationMode","Sanitized live metrics: $($sanitizedLive-join', ')","")+@($outputLines)+@("",$overallLine,"Failure sample is a negative fixture; no URL, endpoint, response, credential, token, cookie, authorization, address, domain, certificate, or key was stored.")|Set-Content -LiteralPath $logPath -Encoding UTF8
$requiredFileCheck=$missingBaseline.Count-eq 0-and$missingSamples.Count-eq 0;$secretSafety=-not$authHit-and$endpointSafe-and-not$accountHit
$summaryLines=[System.Collections.Generic.List[string]]::new();$summaryLines.Add("# Blackbox Endpoint Probe Summary")|Out-Null;$summaryLines.Add("")|Out-Null;$summaryLines.Add("- Scenario: S030-blackbox-endpoint-probe-validation")|Out-Null;$summaryLines.Add("- Generated: $timestamp")|Out-Null;$summaryLines.Add("- Validation mode: **$validationMode**")|Out-Null;$summaryLines.Add("- Required file check result: **$(if($requiredFileCheck){'PASS'}else{'FAIL'})**")|Out-Null;$summaryLines.Add("- Blackbox module check result: **$(if($modulesReady){'PASS'}else{'FAIL'})**")|Out-Null;$summaryLines.Add("- Prometheus scrape config placeholder check result: **$(if($scrapeReady){'PASS'}else{'FAIL'})**")|Out-Null;$summaryLines.Add("- Probe metric documentation check result: **$(if($thresholdReady-and$missingMetricTerms.Count-eq 0){'PASS'}else{'FAIL'})**")|Out-Null;$summaryLines.Add("- Success sample parsing result: **$(if($successReady){'HEALTHY'}else{'INVALID'})**")|Out-Null;$summaryLines.Add("- Warning sample parsing result: **$(if($warningReady){'WARNING'}else{'INVALID'})**")|Out-Null;$summaryLines.Add("- Failure sample parsing result: **$(if($failureDetected){'EXPECTED_FAILURE_DETECTED'}else{'INVALID'})**")|Out-Null;$summaryLines.Add("- Prometheus probe query sample parsing result: **$(if($queryReady){'PASS'}else{'FAIL'})**")|Out-Null;$summaryLines.Add("- Secret-safety check result: **$(if($secretSafety){'PASS'}else{'FAIL'})**")|Out-Null;$summaryLines.Add("- Final judgment: **$overallResult**")|Out-Null;$summaryLines.Add("")|Out-Null;$summaryLines.Add("| Check ID | Check | Result | Detail |")|Out-Null;$summaryLines.Add("|---|---|---|---|")|Out-Null;foreach($result in $results){$detail=$result.Detail.Replace("|","\|");$summaryLines.Add("| $($result.Id) | $($result.Description) | $($result.Result) | $detail |")|Out-Null};$summaryLines|Set-Content -LiteralPath $summaryPath -Encoding UTF8
if($criticalFailures-gt 0){exit 1};exit 0
