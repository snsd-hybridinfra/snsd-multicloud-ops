param(
    [switch] $LiveKubectl
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$baselinePath = Join-Path $repositoryRoot "kubernetes\ingress\ingress-routing-validation.md"
$commandReferencePath = Join-Path $repositoryRoot "kubernetes\ingress\ingress-routing-commands.example.md"
$ingressRoot = Join-Path $repositoryRoot "kubernetes\ingress\sample-service"
$manifestPath = Join-Path $ingressRoot "ingress.example.yaml"
$readmePath = Join-Path $ingressRoot "README.md"
$servicePath = Join-Path $repositoryRoot "kubernetes\workloads\sample-service\service.example.yaml"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L3-service-operations\S023-ingress-routing-validation"
$getIngressSamplePath = Join-Path $evidenceRoot "logs\kubectl-get-ingress.sample.txt"
$describeIngressSamplePath = Join-Path $evidenceRoot "logs\kubectl-describe-ingress.sample.txt"
$endpointSamplePath = Join-Path $evidenceRoot "logs\kubectl-get-endpoints.sample.txt"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "ingress-routing-validation.log"
$summaryPath = Join-Path $configDirectory "ingress-routing-summary.md"
$validationMode = if ($LiveKubectl) { "LiveKubectl" } else { "Static" }

$requiredCommands = @(
    'kubectl apply --dry-run=client -f kubernetes/ingress/sample-service/ingress.example.yaml',
    'kubectl get ingress -n snsd-example',
    'kubectl describe ingress <ingress-name> -n <namespace>',
    'kubectl get svc -n snsd-example',
    'kubectl get endpoints -n snsd-example',
    'kubectl get pods -n snsd-example -l app=<app-label-placeholder>',
    'curl -H "Host: <host-placeholder>" http://<ingress-address-placeholder>/'
)
$requiredBaselineTerms = @(
    'Client -> Ingress Controller -> Ingress Rule -> Service -> Pod',
    '`Ingress` object', 'Service backend reference', 'namespace alignment',
    '<namespace>', '<ingress-name>', '<ingress-class>', '<host-placeholder>',
    '<path-placeholder>', '<service-name>', '<service-port>', '<pod-selector>',
    '<tls-secret-placeholder>', '<evidence-path>', 'Static manifest validation', 'LiveKubectl'
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

function Get-TableRows {
    param([string[]] $Lines, [string] $HeaderPattern)
    $rows = [System.Collections.Generic.List[string]]::new()
    foreach ($line in $Lines) {
        $trimmed = $line.Trim()
        if (-not $trimmed -or $trimmed -cmatch '^(?:SAMPLE /|NON-PRODUCTION |#)' -or $trimmed -match $HeaderPattern) { continue }
        $rows.Add($trimmed) | Out-Null
    }
    return @($rows.ToArray())
}

$baselineExists = Test-Path -LiteralPath $baselinePath -PathType Leaf
$commandReferenceExists = Test-Path -LiteralPath $commandReferencePath -PathType Leaf
Add-ValidationResult "V001" "Ingress documentation" $(if ($baselineExists -and $commandReferenceExists) { "PASS" } else { "FAIL" }) $(if ($baselineExists -and $commandReferenceExists) { "Baseline and command reference exist." } else { "Baseline or command reference is missing." })

$manifestExists = Test-Path -LiteralPath $manifestPath -PathType Leaf
$readmeExists = Test-Path -LiteralPath $readmePath -PathType Leaf
Add-ValidationResult "V002" "Ingress example files" $(if ($manifestExists -and $readmeExists) { "PASS" } else { "FAIL" }) $(if ($manifestExists -and $readmeExists) { "Ingress manifest and README exist." } else { "Ingress manifest or README is missing." })

$samplePaths = @($getIngressSamplePath, $describeIngressSamplePath, $endpointSamplePath)
$missingSamples = @($samplePaths | Where-Object { -not (Test-Path -LiteralPath $_ -PathType Leaf) })
Add-ValidationResult "V003" "Ingress sample evidence" $(if ($missingSamples.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingSamples.Count -eq 0) { "Ingress list, describe, and endpoint samples exist." } else { "One or more sample evidence files are missing." })

$baselineContent = if ($baselineExists) { Get-Content -LiteralPath $baselinePath -Raw } else { "" }
$commandContent = if ($commandReferenceExists) { Get-Content -LiteralPath $commandReferencePath -Raw } else { "" }
$manifestContent = if ($manifestExists) { Get-Content -LiteralPath $manifestPath -Raw } else { "" }
$readmeContent = if ($readmeExists) { Get-Content -LiteralPath $readmePath -Raw } else { "" }
$serviceContent = if (Test-Path -LiteralPath $servicePath) { Get-Content -LiteralPath $servicePath -Raw } else { "" }
$getIngressContent = if (Test-Path -LiteralPath $getIngressSamplePath) { Get-Content -LiteralPath $getIngressSamplePath -Raw } else { "" }
$describeContent = if (Test-Path -LiteralPath $describeIngressSamplePath) { Get-Content -LiteralPath $describeIngressSamplePath -Raw } else { "" }
$endpointContent = if (Test-Path -LiteralPath $endpointSamplePath) { Get-Content -LiteralPath $endpointSamplePath -Raw } else { "" }
$combinedContent = @($baselineContent, $commandContent, $manifestContent, $readmeContent, $getIngressContent, $describeContent, $endpointContent) -join "`n"

$missingCommands = @($requiredCommands | Where-Object { $commandContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V004" "Required command examples" $(if ($missingCommands.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingCommands.Count -eq 0) { "All kubectl and manual curl examples are documented." } else { "Required command examples are missing." })

$missingBaselineTerms = @($requiredBaselineTerms | Where-Object { $baselineContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V005" "Routing model and placeholders" $(if ($missingBaselineTerms.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingBaselineTerms.Count -eq 0) { "Request path, objects, alignment, placeholders, evidence, and modes are documented." } else { "Required routing model terms are missing." })

$objectReady = $manifestContent -match '(?im)^kind:\s*Ingress\s*$' -and
    $manifestContent -match '(?im)^\s*name:\s*sample-service-ingress-placeholder\s*$' -and
    $manifestContent -match '(?im)^\s*namespace:\s*snsd-example\s*$' -and
    $manifestContent -match '(?im)^\s*ingressClassName:\s*nginx\s*$' -and
    $manifestContent -match 'NON-PRODUCTION EXAMPLE'
Add-ValidationResult "V006" "Ingress object and scope" $(if ($objectReady) { "PASS" } else { "FAIL" }) $(if ($objectReady) { "Ingress name, namespace, class, and example marker are correct." } else { "Ingress kind, name, namespace, class, or marker is invalid." })

$routeReady = $manifestContent -match '(?im)^\s*-\s*host:\s*app\.example\.internal\s*$' -and
    $manifestContent -match '(?im)^\s*-\s*path:\s*/\s*$' -and
    $manifestContent -match '(?im)^\s*pathType:\s*Prefix\s*$'
Add-ValidationResult "V007" "Host and path routing" $(if ($routeReady) { "PASS" } else { "FAIL" }) $(if ($routeReady) { "Approved example host, root path, and Prefix pathType exist." } else { "Host, path, or pathType is missing or invalid." })

$backendReady = $manifestContent -match '(?im)^\s*name:\s*sample-service-placeholder\s*$' -and
    $manifestContent -match '(?im)^\s*number:\s*80\s*$' -and
    $serviceContent -match '(?im)^\s*name:\s*sample-service-placeholder\s*$' -and
    $serviceContent -match '(?im)^\s*port:\s*80\s*$' -and
    $serviceContent -match '(?im)^\s*namespace:\s*snsd-example\s*$'
Add-ValidationResult "V008" "Backend Service reference" $(if ($backendReady) { "PASS" } else { "FAIL" }) $(if ($backendReady) { "Ingress and Service align on namespace, name, and port 80." } else { "Backend Service name, port, or namespace alignment is missing." })

$wildcardHostHit = $manifestContent -match '(?im)^\s*-?\s*host:\s*["'']?\*["'']?\s*$'
$secretResourceHit = $manifestContent -match '(?im)^kind:\s*Secret\s*$'
$tlsMaterialHit = $combinedContent -match '-----BEGIN (?:CERTIFICATE|(?:[A-Z ]+ )?PRIVATE KEY)-----' -or $manifestContent -match '(?im)^\s*(?:tls\.crt|tls\.key|data|stringData):\s*\S+'
$manifestSafe = -not $wildcardHostHit -and -not $secretResourceHit -and -not $tlsMaterialHit
Add-ValidationResult "V009" "Ingress and TLS safety" $(if ($manifestSafe) { "PASS" } else { "FAIL" }) $(if ($manifestSafe) { "No wildcard host, Secret resource, certificate, key, or TLS data exists." } else { "Unsafe wildcard, Secret, or TLS material was detected." })

[array] $ingressRows = if (Test-Path -LiteralPath $getIngressSamplePath) { @(Get-TableRows -Lines (Get-Content -LiteralPath $getIngressSamplePath) -HeaderPattern '^NAME\s+CLASS') } else { @() }
$activeIngressRows = @($ingressRows)
$activeDescribe = $describeContent
$activeServiceRows = @('sample-service-placeholder static-service-reference')
$activeEndpointRows = if (Test-Path -LiteralPath $endpointSamplePath) { @(Get-TableRows -Lines (Get-Content -LiteralPath $endpointSamplePath) -HeaderPattern '^NAME\s+ENDPOINTS') } else { @() }
$liveCommandsPassed = $true
$liveDetail = "Live kubectl was not requested; static evidence is authoritative for this run."

if ($LiveKubectl) {
    $kubectlCommand = Get-Command "kubectl" -CommandType Application -ErrorAction SilentlyContinue
    if ($null -eq $kubectlCommand) {
        $liveCommandsPassed = $false
        $activeIngressRows = @(); $activeDescribe = ""; $activeServiceRows = @(); $activeEndpointRows = @()
        $liveDetail = "LiveKubectl was requested but kubectl is unavailable."
    }
    else {
        $ingressArguments = @("get", "ingress", "-n", "snsd-example")
        $describeArguments = @("describe", "ingress", "sample-service-ingress-placeholder", "-n", "snsd-example")
        $serviceArguments = @("get", "svc", "-n", "snsd-example")
        $endpointArguments = @("get", "endpoints", "-n", "snsd-example")
        $ingressOutput = @(& $kubectlCommand.Source @ingressArguments 2>&1); $ingressExit = $LASTEXITCODE
        $describeOutput = @(& $kubectlCommand.Source @describeArguments 2>&1); $describeExit = $LASTEXITCODE
        $serviceOutput = @(& $kubectlCommand.Source @serviceArguments 2>&1); $serviceExit = $LASTEXITCODE
        $endpointOutput = @(& $kubectlCommand.Source @endpointArguments 2>&1); $endpointExit = $LASTEXITCODE
        if (@(@($ingressExit, $describeExit, $serviceExit, $endpointExit) | Where-Object { $_ -ne 0 }).Count -gt 0) {
            $liveCommandsPassed = $false
            $activeIngressRows = @(); $activeDescribe = ""; $activeServiceRows = @(); $activeEndpointRows = @()
            $liveDetail = "A read-only kubectl command failed; raw error output was not stored."
        }
        else {
            $activeIngressRows = @(Get-TableRows -Lines @($ingressOutput | ForEach-Object { [string]$_ }) -HeaderPattern '^NAME\s+CLASS')
            $activeDescribe = @($describeOutput | ForEach-Object { [string]$_ }) -join "`n"
            $activeServiceRows = @(Get-TableRows -Lines @($serviceOutput | ForEach-Object { [string]$_ }) -HeaderPattern '^NAME\s+TYPE')
            $activeEndpointRows = @(Get-TableRows -Lines @($endpointOutput | ForEach-Object { [string]$_ }) -HeaderPattern '^NAME\s+ENDPOINTS')
            $liveCommandsPassed = $activeIngressRows.Count -gt 0 -and $activeServiceRows.Count -gt 0 -and $activeEndpointRows.Count -gt 0
            $liveDetail = if ($liveCommandsPassed) { "Four read-only queries returned parseable resource rows; raw rows were not stored." } else { "Live queries returned incomplete routing resources." }
        }
    }
}

$ingressEvidenceReady = $activeIngressRows.Count -gt 0 -and @($activeIngressRows | Where-Object { $_ -match 'app\.example\.internal' -and $_ -match '(?:^|\s)80(?:\s|$)' }).Count -gt 0
Add-ValidationResult "V010" "Ingress list evidence" $(if ($ingressEvidenceReady) { "PASS" } else { "FAIL" }) $(if ($ingressEvidenceReady) { "Ingress evidence contains the approved host and port 80." } else { "Ingress host or port evidence is missing." })

$describeReady = $activeDescribe -match 'sample-service-placeholder:80' -and $activeDescribe -match 'app\.example\.internal'
$serviceReady = @($activeServiceRows | Where-Object { $_ -match 'sample-service-placeholder' }).Count -gt 0
Add-ValidationResult "V011" "Ingress backend evidence" $(if ($describeReady -and $serviceReady) { "PASS" } else { "FAIL" }) $(if ($describeReady -and $serviceReady) { "Ingress describe and Service evidence contain the expected backend." } else { "Backend describe or Service evidence is missing." })

$usableEndpoints = @($activeEndpointRows | Where-Object { $_ -match 'sample-service-placeholder' -and $_ -notmatch '(?i)<none>|\bnone\b|missing' -and $_ -match ':80(?:\s|$)' })
$endpointReady = $usableEndpoints.Count -gt 0
Add-ValidationResult "V012" "Endpoint evidence" $(if ($endpointReady) { "PASS" } else { "FAIL" }) $(if ($endpointReady) { "Backend endpoint evidence contains at least one target on port 80." } else { "Backend endpoint evidence is empty or missing." })

$placeholderAddressPresent = @($activeIngressRows | Where-Object { $_ -match '<ingress-address-placeholder>' }).Count -gt 0
$addressResult = if (-not $LiveKubectl -and $placeholderAddressPresent) { "WARN" } else { "PASS" }
$addressDetail = if ($addressResult -eq "WARN") { "Static ingress ADDRESS is a placeholder; live address was intentionally not validated." } else { "Ingress address evidence is available for the selected mode." }
Add-ValidationResult "V013" "Ingress address awareness" $addressResult $addressDetail

$forbiddenFiles = @(Get-ChildItem -LiteralPath $repositoryRoot -File -Recurse -Force -ErrorAction SilentlyContinue | Where-Object {
    $_.FullName -notmatch '[\\/]\.git[\\/]' -and
    ($_.Name -match '(?i)(^|\.)kubeconfig($|\.)|service[-_]?account.*token|\.crt$|\.cer$|\.pem$|\.key$|\.p12$|\.pfx$')
})
Add-ValidationResult "V014" "Kubernetes and TLS credential files" $(if ($forbiddenFiles.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($forbiddenFiles.Count -eq 0) { "No kubeconfig, token, certificate, or private-key file exists." } else { "A forbidden credential or TLS file was detected." })

$endpointUrlHit = $combinedContent -match '(?i)https?://(?!<)[^\s]+'
$ipMatches = @([regex]::Matches($combinedContent, '(?<![A-Za-z0-9<])((?:\d{1,3}\.){3}\d{1,3})(?:/\d{1,2})?(?![A-Za-z0-9>])'))
$domainMatches = @([regex]::Matches($combinedContent, '(?i)(?<![A-Za-z0-9<.-])(?:[a-z0-9-]+\.)+[a-z]{2,}(?![A-Za-z0-9>.-])') | ForEach-Object { $_.Value.ToLowerInvariant() })
$unexpectedDomains = @($domainMatches | Where-Object {
    $_ -ne 'app.example.internal' -and
    $_ -ne 'networking.k8s.io' -and
    $_ -notmatch '\.example\.(?:yaml|md)$' -and
    $_ -notmatch '\.namespace\.yaml$'
} | Sort-Object -Unique)
$secretHit = $combinedContent -match '-----BEGIN (?:CERTIFICATE|(?:[A-Z ]+ )?PRIVATE KEY)-----' -or
    $combinedContent -match '(?im)^\s*(?:token|password|secret|client-certificate-data|client-key-data)\s*[:=]\s*(?!["'']?<)\S+'
$contentSafe = -not $endpointUrlHit -and $ipMatches.Count -eq 0 -and $unexpectedDomains.Count -eq 0 -and -not $secretHit
Add-ValidationResult "V015" "Routing content safety" $(if ($contentSafe) { "PASS" } else { "FAIL" }) $(if ($contentSafe) { "No real endpoint, numeric address, unexpected domain, token, certificate, key, password, or secret exists." } else { "Sensitive or non-placeholder routing content was detected." })

$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$requiredArgumentSets = @(
    '\$ingressArguments\s*=\s*@\("get",\s*"ingress",\s*"-n",\s*"snsd-example"\)',
    '\$describeArguments\s*=\s*@\("describe",\s*"ingress",\s*"sample-service-ingress-placeholder",\s*"-n",\s*"snsd-example"\)',
    '\$serviceArguments\s*=\s*@\("get",\s*"svc",\s*"-n",\s*"snsd-example"\)',
    '\$endpointArguments\s*=\s*@\("get",\s*"endpoints",\s*"-n",\s*"snsd-example"\)'
)
$missingArgumentSets = @($requiredArgumentSets | Where-Object { $scriptContent -notmatch $_ })
$prohibitedInvocation = $scriptContent -match '(?im)^\s*(?:&\s*)?kubectl\s+(?:apply|delete|patch|edit|replace|scale|rollout|cordon|drain|taint)\b' -or $scriptContent -match '(?im)^\s*(?:&\s*)?curl\b'
$executionSafe = $missingArgumentSets.Count -eq 0 -and -not $prohibitedInvocation
Add-ValidationResult "V016" "Execution safety boundary" $(if ($executionSafe) { "PASS" } else { "FAIL" }) $(if ($executionSafe) { "Live mode contains four guarded read-only kubectl argument sets and no automatic curl." } else { "Read-only live boundaries are incomplete or a mutation/curl invocation exists." })

Add-ValidationResult "V017" "Validation mode" $(if ($liveCommandsPassed) { "PASS" } else { "FAIL" }) $(if ($LiveKubectl) { $liveDetail } else { "Static mode completed without invoking kubectl or curl." })

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Kubernetes ingress routing ($validationMode): $criticalFailures critical failure(s), $warningCount warning(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S023 Kubernetes Ingress Routing Validation"
    "Generated: $timestamp"
    "Validation mode: $validationMode"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No kubeconfig path, token, certificate, TLS key, endpoint, numeric address, raw live resource row, or secret was stored."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$requiredFilesPassed = $baselineExists -and $commandReferenceExists -and $manifestExists -and $readmeExists -and $missingSamples.Count -eq 0
$manifestCheckPassed = $objectReady -and $routeReady -and $manifestSafe
$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# Kubernetes Ingress Routing Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S023-ingress-routing-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Validation mode: **$validationMode**") | Out-Null
$summaryLines.Add("- Required file check result: **$(if ($requiredFilesPassed) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Ingress manifest check result: **$(if ($manifestCheckPassed) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Backend service reference check result: **$(if ($backendReady -and $describeReady -and $serviceReady) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Endpoint evidence parsing result: **$(if ($endpointReady) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Secret-safety check result: **$(if ($forbiddenFiles.Count -eq 0 -and $contentSafe) { 'PASS' } else { 'FAIL' })**") | Out-Null
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
$summaryLines.Add("Static mode invokes neither kubectl nor curl. LiveKubectl runs only read-only resource queries and stores routing judgments rather than raw cluster details.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) { exit 1 }
exit 0
