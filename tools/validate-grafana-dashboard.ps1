param(
    [switch] $LiveGrafana,
    [string] $GrafanaUrl,
    [string] $DashboardTitle = "SNSD Ops Overview Placeholder"
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$grafanaRoot = Join-Path $repositoryRoot "observability\grafana"
$baselinePath = Join-Path $grafanaRoot "grafana-dashboard-validation.md"
$datasourcePath = Join-Path $grafanaRoot "datasource.prometheus.example.yml"
$dashboardPath = Join-Path $grafanaRoot "dashboards\snsd-ops-overview.example.json"
$matrixPath = Join-Path $grafanaRoot "grafana-dashboard-rule-matrix.example.md"
$commandPath = Join-Path $grafanaRoot "grafana-dashboard-commands.example.md"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L3-service-operations\S029-grafana-dashboard-validation"
$searchSamplePath = Join-Path $evidenceRoot "logs\grafana-dashboard-search.sample.json"
$detailSamplePath = Join-Path $evidenceRoot "logs\grafana-dashboard-detail.sample.json"
$datasourceSamplePath = Join-Path $evidenceRoot "logs\grafana-datasource-list.sample.json"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "grafana-dashboard-validation.log"
$summaryPath = Join-Path $configDirectory "grafana-dashboard-summary.md"
$validationMode = if ($LiveGrafana) { "LiveGrafana" } else { "Static" }

$requiredPanels = @(
    "Prometheus Target Status", "Kubernetes Node Readiness", "Kubernetes Pod Readiness",
    "Nginx Reverse Proxy Health", "Load Balancer Health", "MariaDB Replication IO Thread",
    "MariaDB Replication SQL Thread", "MariaDB Replication Lag", "Blackbox Probe Success",
    "Service Availability Summary"
)
$requiredMetrics = @(
    "up", "kube_node_status_condition", "kube_pod_status_ready", "nginx_http_requests_total",
    "load_balancer_health_placeholder", "mysql_slave_status_slave_io_running",
    "mysql_slave_status_slave_sql_running", "mariadb_replication_lag_seconds", "probe_success"
)

New-Item -ItemType Directory -Force -Path $logDirectory, $configDirectory | Out-Null
$results = [System.Collections.Generic.List[object]]::new()
$outputLines = [System.Collections.Generic.List[string]]::new()
$criticalFailures = 0
$warningCount = 0

function Add-ValidationResult {
    param([string]$Id, [string]$Description, [ValidateSet("PASS","WARN","FAIL")][string]$Result, [string]$Detail)
    if ($Result -eq "FAIL") { $script:criticalFailures++ }
    if ($Result -eq "WARN") { $script:warningCount++ }
    $line = "[$Result] $Id ${Description}: $Detail"
    Write-Host $line
    $script:outputLines.Add($line) | Out-Null
    $script:results.Add([pscustomobject]@{ Id=$Id; Description=$Description; Result=$Result; Detail=$Detail }) | Out-Null
}

function Read-Artifact {
    param([string]$Path)
    if (Test-Path -LiteralPath $Path -PathType Leaf) { return Get-Content -LiteralPath $Path -Raw }
    return ""
}

function Convert-SafeJson {
    param([string]$Content)
    try { return $Content | ConvertFrom-Json -ErrorAction Stop } catch { return $null }
}

$requiredBaselinePaths = @($baselinePath,$datasourcePath,$dashboardPath,$matrixPath,$commandPath)
$missingBaseline = @($requiredBaselinePaths | Where-Object { -not (Test-Path -LiteralPath $_ -PathType Leaf) })
Add-ValidationResult "V001" "Required dashboard baseline files" $(if($missingBaseline.Count -eq 0){"PASS"}else{"FAIL"}) $(if($missingBaseline.Count -eq 0){"Baseline, datasource, dashboard, matrix, and commands exist."}else{"One or more baseline files are missing."})

$baselineContent = Read-Artifact $baselinePath
$datasourceContent = Read-Artifact $datasourcePath
$dashboardContent = Read-Artifact $dashboardPath
$matrixContent = Read-Artifact $matrixPath
$commandContent = Read-Artifact $commandPath
$searchContent = Read-Artifact $searchSamplePath
$detailContent = Read-Artifact $detailSamplePath
$datasourceSampleContent = Read-Artifact $datasourceSamplePath
$combinedContent = @($baselineContent,$datasourceContent,$dashboardContent,$matrixContent,$commandContent,$searchContent,$detailContent,$datasourceSampleContent) -join "`n"

$datasourceReady = $datasourceContent -match 'NON-PRODUCTION EXAMPLE' -and
    $datasourceContent -match '(?im)^apiVersion:\s*1\s*$' -and
    $datasourceContent -match '(?im)^datasources:\s*$' -and
    $datasourceContent -match '(?im)^\s*-\s*name:\s*Prometheus Placeholder\s*$' -and
    $datasourceContent -match '(?im)^\s*type:\s*prometheus\s*$' -and
    $datasourceContent -match '(?im)^\s*access:\s*proxy\s*$' -and
    $datasourceContent -match '(?im)^\s*url:\s*http://<prometheus-server-placeholder>:9090\s*$' -and
    $datasourceContent -match '(?im)^\s*isDefault:\s*true\s*$'
Add-ValidationResult "V002" "Prometheus datasource definition" $(if($datasourceReady){"PASS"}else{"FAIL"}) $(if($datasourceReady){"All required non-production datasource fields are present."}else{"Datasource fields or marker are incomplete."})

$dashboardJson = Convert-SafeJson $dashboardContent
$dashboardJsonReady = $null -ne $dashboardJson -and $dashboardJson.sample_notice -eq 'NON-PRODUCTION EXAMPLE' -and
    $dashboardJson.title -eq 'SNSD Ops Overview Placeholder' -and $dashboardJson.uid -eq '<dashboard-uid-placeholder>'
Add-ValidationResult "V003" "Dashboard JSON structure" $(if($dashboardJsonReady){"PASS"}else{"FAIL"}) $(if($dashboardJsonReady){"Dashboard JSON is parseable and uses placeholder title/UID."}else{"Dashboard JSON, marker, title, or UID is invalid."})

$dashboardPanelTitles = if($dashboardJsonReady){ @($dashboardJson.panels | ForEach-Object { [string]$_.title }) }else{ @() }
$missingPanels = @($requiredPanels | Where-Object { $_ -notin $dashboardPanelTitles })
$panelReady = $missingPanels.Count -eq 0 -and $dashboardPanelTitles.Count -eq 10
Add-ValidationResult "V004" "Required dashboard panels" $(if($panelReady){"PASS"}else{"FAIL"}) $(if($panelReady){"All ten required panels exist."}else{"One or more required panel titles are missing or duplicated."})

$missingMetrics = @($requiredMetrics | Where-Object { $dashboardContent -notmatch [regex]::Escape($_) })
$datasourceReferences = @('invalid')
if ($dashboardJsonReady) {
    [array]$datasourceReferences = @($dashboardJson.panels | Where-Object { $_.datasource.uid -ne '<prometheus-datasource-placeholder>' })
}
$queryReady = $missingMetrics.Count -eq 0 -and $datasourceReferences.Count -eq 0 -and $dashboardContent -match '<alert-readiness-placeholder>'
Add-ValidationResult "V005" "Panel datasource and query coverage" $(if($queryReady){"PASS"}else{"FAIL"}) $(if($queryReady){"All panels use the placeholder datasource and required metrics/alert placeholder exist."}else{"A datasource reference, metric, or alert-readiness placeholder is missing."})

$matrixAreas = @('Prometheus target status','Kubernetes node readiness','Kubernetes pod readiness','Nginx reverse proxy health','Load balancing health check','MariaDB replication thread status','MariaDB replication lag','Blackbox endpoint probe','Service availability summary')
$missingAreas = @($matrixAreas | Where-Object { $matrixContent -notmatch [regex]::Escape($_) })
$matrixReady = $missingAreas.Count -eq 0 -and $matrixContent -match 'Dashboard Area' -and $matrixContent -match 'Datasource Placeholder' -and $matrixContent -match 'Evidence Reference'
Add-ValidationResult "V006" "Dashboard rule matrix" $(if($matrixReady){"PASS"}else{"FAIL"}) $(if($matrixReady){"All nine dashboard areas and required columns are documented."}else{"The dashboard matrix is incomplete."})

$requiredCommands = @('curl http://<grafana-server-placeholder>/api/search','curl http://<grafana-server-placeholder>/api/dashboards/uid/<dashboard-uid-placeholder>','curl http://<grafana-server-placeholder>/api/datasources','grafana dashboard import')
$missingCommands = @($requiredCommands | Where-Object { $commandContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V007" "Dashboard command reference" $(if($missingCommands.Count -eq 0){"PASS"}else{"FAIL"}) $(if($missingCommands.Count -eq 0){"Three API and one manual import workflow references exist."}else{"A required command/workflow reference is missing."})

$samplePaths = @($searchSamplePath,$detailSamplePath,$datasourceSamplePath)
$missingSamples = @($samplePaths | Where-Object { -not(Test-Path -LiteralPath $_ -PathType Leaf) })
Add-ValidationResult "V008" "Required sample evidence" $(if($missingSamples.Count -eq 0){"PASS"}else{"FAIL"}) $(if($missingSamples.Count -eq 0){"Search, detail, and datasource samples exist."}else{"One or more sample files are missing."})

$searchJson = Convert-SafeJson $searchContent
$searchReady = $null -ne $searchJson -and $searchJson.sample_notice -eq 'SAMPLE / NON-PRODUCTION' -and @($searchJson.results | Where-Object { $_.title -eq 'SNSD Ops Overview Placeholder' }).Count -gt 0
Add-ValidationResult "V009" "Dashboard search evidence" $(if($searchReady){"PASS"}else{"FAIL"}) $(if($searchReady){"The required placeholder dashboard appears in valid sanitized search JSON."}else{"Dashboard search evidence is invalid or missing the required title."})

$detailJson = Convert-SafeJson $detailContent
$detailTitles = if($null -ne $detailJson){ @($detailJson.dashboard.panels | ForEach-Object { [string]$_.title }) }else{ @() }
$missingDetailPanels = @($requiredPanels | Where-Object { $_ -notin $detailTitles })
$detailReady = $null -ne $detailJson -and $detailJson.sample_notice -eq 'SAMPLE / NON-PRODUCTION' -and $detailJson.dashboard.title -eq 'SNSD Ops Overview Placeholder' -and $missingDetailPanels.Count -eq 0
Add-ValidationResult "V010" "Dashboard detail evidence" $(if($detailReady){"PASS"}else{"FAIL"}) $(if($detailReady){"Valid sanitized detail JSON contains all ten required panels."}else{"Dashboard detail evidence is invalid or incomplete."})

$datasourceJson = Convert-SafeJson $datasourceSampleContent
$datasourceSampleReady = $null -ne $datasourceJson -and $datasourceJson.sample_notice -eq 'SAMPLE / NON-PRODUCTION' -and @($datasourceJson.datasources | Where-Object { $_.name -eq 'Prometheus Placeholder' -and $_.type -eq 'prometheus' }).Count -gt 0
Add-ValidationResult "V011" "Datasource list evidence" $(if($datasourceSampleReady){"PASS"}else{"FAIL"}) $(if($datasourceSampleReady){"Valid sanitized evidence contains the Prometheus Placeholder datasource."}else{"Datasource evidence is invalid or missing the required datasource."})

$secretHit = $combinedContent -match '(?im)^\s*["'']?(?:password|basicAuthPassword|token|api[-_]?key|secret|cookie|authorization|secureJsonData)["'']?\s*[:=]\s*(?!["'']?<|\{\s*\})\S+' -or
    $combinedContent -match '(?im)^\s*(?:Authorization|Cookie|Set-Cookie):\s*(?!<)\S+' -or
    $combinedContent -match '-----BEGIN (?:CERTIFICATE|(?:[A-Z ]+ )?PRIVATE KEY)-----'
Add-ValidationResult "V012" "Credential token datasource and TLS safety" $(if(-not $secretHit){"PASS"}else{"FAIL"}) $(if(-not $secretHit){"No credential, token, cookie, authorization value, datasource secret, certificate, or key exists."}else{"Sensitive dashboard/datasource content was detected."})

$ipMatches = @([regex]::Matches($combinedContent,'(?<![A-Za-z0-9<])(?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?(?![A-Za-z0-9>])'))
$domainMatches = @([regex]::Matches($combinedContent,'(?i)(?<![A-Za-z0-9<.-])(?:[a-z0-9-]+\.)+[a-z]{2,}(?![A-Za-z0-9>.-])') | ForEach-Object {$_.Value.ToLowerInvariant()})
$unexpectedDomains = @($domainMatches | Where-Object { $_ -notmatch '\.(?:md|yml|yaml|json|txt|ps1)$' } | Sort-Object -Unique)
$concreteUrls = @([regex]::Matches($combinedContent,'(?i)https?://(?!<)[^\s"`]+'))
$endpointSafe = $ipMatches.Count -eq 0 -and $unexpectedDomains.Count -eq 0 -and $concreteUrls.Count -eq 0
Add-ValidationResult "V013" "Monitoring URL address and domain safety" $(if($endpointSafe){"PASS"}else{"FAIL"}) $(if($endpointSafe){"No real Grafana/Prometheus URL, cluster endpoint, address, or domain exists."}else{"Concrete monitoring endpoint content was detected."})

$uidMatches = @([regex]::Matches($combinedContent,'(?im)["'']uid["'']\s*[:=]\s*["'']([^"'']+)["'']') | ForEach-Object {$_.Groups[1].Value})
$realUids = @($uidMatches | Where-Object { $_ -notmatch '^<[^>]+>$' })
$identityHit = $combinedContent -match '(?im)["'']?(?:orgId|userId)["'']?\s*[:=]\s*\d+'
$identitySafe = $realUids.Count -eq 0 -and -not $identityHit
Add-ValidationResult "V014" "Dashboard UID and identity safety" $(if($identitySafe){"PASS"}else{"FAIL"}) $(if($identitySafe){"All UIDs are placeholders and no organization/user ID exists."}else{"A real-looking dashboard/datasource UID or identity ID was detected."})

$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$dashboardMutationPath = 'api/dashboards/' + 'db'
$executionSafe = $scriptContent -notmatch '(?im)^\s*(?:&\s*)?curl(?:\.exe)?\s+' -and $scriptContent -notmatch '(?im)^\s*(?:&\s*)?grafana(?:\.exe)?\s+' -and
    $scriptContent -match 'if \(\$LiveGrafana\)' -and $scriptContent -match 'UseCookies\s*=\s*\$false' -and
    $scriptContent -notmatch [regex]::Escape($dashboardMutationPath)
Add-ValidationResult "V015" "Execution safety boundary" $(if($executionSafe){"PASS"}else{"FAIL"}) $(if($executionSafe){"Static mode invokes no client/import; guarded live mode is cookie-free and read-only."}else{"Execution guardrails are incomplete or unsafe."})

$liveResult = "PASS"
$liveDetail = "Static mode completed without curl, Grafana query, import, mutation, or network access."
$sanitizedLive = @("NOT_RUN")
if($LiveGrafana){
    if([string]::IsNullOrWhiteSpace($GrafanaUrl)){
        $liveResult="FAIL"; $liveDetail="LiveGrafana requires GrafanaUrl; no request was sent."; $sanitizedLive=@("MISSING_URL")
    }else{
        $baseUri=$null
        $valid=[System.Uri]::TryCreate($GrafanaUrl,[System.UriKind]::Absolute,[ref]$baseUri) -and $baseUri.Scheme -in @('http','https') -and [string]::IsNullOrEmpty($baseUri.UserInfo)
        if(-not $valid){
            $liveResult="FAIL"; $liveDetail="GrafanaUrl must be absolute HTTP(S) without user information; no request was sent."; $sanitizedLive=@("INVALID_URL")
        }else{
            $handler=$null; $client=$null; $searchResponse=$null; $dsResponse=$null
            try{
                Add-Type -AssemblyName System.Net.Http
                $handler=[System.Net.Http.HttpClientHandler]::new(); $handler.UseCookies=$false; $handler.AllowAutoRedirect=$false
                $client=[System.Net.Http.HttpClient]::new($handler); $client.Timeout=[TimeSpan]::FromSeconds(10)
                $base=$baseUri.AbsoluteUri.TrimEnd('/')
                $searchResponse=$client.GetAsync("$base/api/search").GetAwaiter().GetResult()
                $dsResponse=$client.GetAsync("$base/api/datasources").GetAwaiter().GetResult()
                $codes=@([int]$searchResponse.StatusCode,[int]$dsResponse.StatusCode)
                if(@($codes | Where-Object { $_ -ge 500 }).Count -gt 0){
                    $liveResult="FAIL"; $liveDetail="Grafana returned a server error; URL and response were not stored."; $sanitizedLive=@("SERVER_ERROR")
                }elseif(@($codes | Where-Object { $_ -eq 401 -or $_ -eq 403 }).Count -gt 0){
                    $liveResult="WARN"; $liveDetail="Grafana requires authentication as expected by S020; no credentials were sent."; $sanitizedLive=@("AUTH_REQUIRED")
                }elseif(@($codes | Where-Object { $_ -ne 200 }).Count -gt 0){
                    $liveResult="WARN"; $liveDetail="Grafana is reachable but returned a non-success client status; no response was stored."; $sanitizedLive=@("CLIENT_STATUS")
                }else{
                    $searchLive=Convert-SafeJson ($searchResponse.Content.ReadAsStringAsync().GetAwaiter().GetResult())
                    $dsLive=Convert-SafeJson ($dsResponse.Content.ReadAsStringAsync().GetAwaiter().GetResult())
                    $dashboardFound=@($searchLive | Where-Object { $_.title -eq $DashboardTitle }).Count -gt 0
                    $prometheusFound=@($dsLive | Where-Object { $_.name -eq 'Prometheus Placeholder' -and $_.type -eq 'prometheus' }).Count -gt 0
                    $sanitizedLive=@("dashboard-title-match=$dashboardFound","panel-count=NOT_QUERIED","Prometheus Placeholder=$prometheusFound")
                    if($dashboardFound -and $prometheusFound){ $liveDetail="Dashboard and datasource are discoverable; only sanitized match judgments are retained." }
                    else{ $liveResult="WARN"; $liveDetail="Grafana is reachable but the placeholder dashboard or datasource is absent; raw response was not stored." }
                }
            }catch{
                $liveResult="FAIL"; $liveDetail="Live Grafana validation was unreachable or failed; URL, response, and exception details were not stored."; $sanitizedLive=@("REQUEST_FAILED")
            }finally{
                if($null -ne $searchResponse){$searchResponse.Dispose()}; if($null -ne $dsResponse){$dsResponse.Dispose()}; if($null -ne $client){$client.Dispose()}; if($null -ne $handler){$handler.Dispose()}
            }
        }
    }
}
Add-ValidationResult "V016" "Validation mode and live Grafana result" $liveResult $liveDetail

$timestamp=(Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult=if($criticalFailures -eq 0){"PASS"}else{"FAIL"}
$overallLine="[$overallResult] Grafana dashboard ($validationMode): $criticalFailures critical failure(s), $warningCount warning(s)."
Write-Host $overallLine

$logLines=@("SNSD Multi-Cloud Ops - S029 Grafana Dashboard Validation","Generated: $timestamp","Validation mode: $validationMode","Sanitized live findings: $($sanitizedLive -join ', ')","")+@($outputLines)+@("",$overallLine,"No Grafana/Prometheus URL, raw API response, credential, token, cookie, authorization value, datasource secret, UID, identity ID, address, domain, certificate, or key was stored.")
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$requiredFileCheck=$missingBaseline.Count-eq 0 -and $missingSamples.Count-eq 0
$sampleParsing=$searchReady -and $detailReady -and $datasourceSampleReady
$secretSafety=(-not $secretHit) -and $endpointSafe -and $identitySafe
$summaryLines=[System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# Grafana Dashboard Summary")|Out-Null; $summaryLines.Add("")|Out-Null
$summaryLines.Add("- Scenario: S029-grafana-dashboard-validation")|Out-Null; $summaryLines.Add("- Generated: $timestamp")|Out-Null
$summaryLines.Add("- Validation mode: **$validationMode**")|Out-Null
$summaryLines.Add("- Required file check result: **$(if($requiredFileCheck){'PASS'}else{'FAIL'})**")|Out-Null
$summaryLines.Add("- Datasource definition check result: **$(if($datasourceReady){'PASS'}else{'FAIL'})**")|Out-Null
$summaryLines.Add("- Dashboard JSON check result: **$(if($dashboardJsonReady){'PASS'}else{'FAIL'})**")|Out-Null
$summaryLines.Add("- Required panel check result: **$(if($panelReady){'PASS'}else{'FAIL'})**")|Out-Null
$summaryLines.Add("- Sample evidence parsing result: **$(if($sampleParsing){'PASS'}else{'FAIL'})**")|Out-Null
$summaryLines.Add("- Missing panel findings: **$(if($missingPanels.Count){$missingPanels -join ', '}else{'none'})**")|Out-Null
$summaryLines.Add("- Secret-safety check result: **$(if($secretSafety){'PASS'}else{'FAIL'})**")|Out-Null
$summaryLines.Add("- Final judgment: **$overallResult**")|Out-Null; $summaryLines.Add("")|Out-Null
$summaryLines.Add("| Check ID | Check | Result | Detail |")|Out-Null; $summaryLines.Add("|---|---|---|---|")|Out-Null
foreach($result in $results){$detail=$result.Detail.Replace("|","\|");$summaryLines.Add("| $($result.Id) | $($result.Description) | $($result.Result) | $detail |")|Out-Null}
$summaryLines.Add("")|Out-Null; $summaryLines.Add("## Safety Boundary")|Out-Null; $summaryLines.Add("")|Out-Null
$summaryLines.Add("Static mode parses repository artifacts only. LiveGrafana uses unauthenticated, cookie-free search/datasource requests and stores sanitized match judgments rather than raw responses.")|Out-Null
$summaryLines|Set-Content -LiteralPath $summaryPath -Encoding UTF8

if($criticalFailures-gt 0){exit 1}; exit 0
