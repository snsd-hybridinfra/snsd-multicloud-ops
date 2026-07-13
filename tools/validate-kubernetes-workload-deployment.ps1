param(
    [switch] $LiveKubectl
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$baselinePath = Join-Path $repositoryRoot "kubernetes\workloads\workload-deployment-validation.md"
$commandReferencePath = Join-Path $repositoryRoot "kubernetes\workloads\workload-deployment-commands.example.md"
$namespacePath = Join-Path $repositoryRoot "kubernetes\namespaces\snsd-example.namespace.yaml"
$workloadRoot = Join-Path $repositoryRoot "kubernetes\workloads\sample-service"
$deploymentPath = Join-Path $workloadRoot "deployment.example.yaml"
$servicePath = Join-Path $workloadRoot "service.example.yaml"
$workloadReadmePath = Join-Path $workloadRoot "README.md"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L3-service-operations\S022-kubernetes-workload-deployment-validation"
$deploymentSamplePath = Join-Path $evidenceRoot "logs\kubectl-get-deployments.sample.txt"
$podSamplePath = Join-Path $evidenceRoot "logs\kubectl-get-pods.sample.txt"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "kubernetes-workload-deployment-validation.log"
$summaryPath = Join-Path $configDirectory "kubernetes-workload-deployment-summary.md"
$validationMode = if ($LiveKubectl) { "LiveKubectl" } else { "Static" }

$requiredCommands = @(
    'kubectl apply --dry-run=client -f kubernetes/namespaces/snsd-example.namespace.yaml',
    'kubectl apply --dry-run=client -f kubernetes/workloads/sample-service/deployment.example.yaml',
    'kubectl apply --dry-run=client -f kubernetes/workloads/sample-service/service.example.yaml',
    'kubectl get deployments -n snsd-example',
    'kubectl get pods -n snsd-example',
    'kubectl describe deployment <deployment-name> -n <namespace>',
    'kubectl rollout status deployment/<deployment-name> -n <namespace>'
)
$requiredBaselineTerms = @(
    'Required workload object: `Deployment`', 'Required service object: `Service`',
    'namespace object', 'available replicas', 'pods to report Ready and Running',
    '<container-image-placeholder>', 'labels', 'selectors', 'readiness', 'liveness',
    'resource requests and limits', '<namespace>', '<deployment-name>', '<service-name>',
    '<container-name>', '<replica-count>', '<evidence-path>', 'Static manifest validation', 'LiveKubectl'
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

function Get-DeploymentEvidence {
    param([string[]] $Lines)
    $items = [System.Collections.Generic.List[object]]::new()
    foreach ($line in $Lines) {
        $trimmed = $line.Trim()
        if (-not $trimmed -or $trimmed -cmatch '^(?:SAMPLE /|NON-PRODUCTION |#)' -or $trimmed -match '^NAME\s+READY') { continue }
        $columns = @($trimmed -split '\s+')
        if ($columns.Count -ge 4) {
            $items.Add([pscustomobject]@{ Ready = $columns[1]; Available = $columns[3]; RawStatus = ($columns[1..3] -join ' ') }) | Out-Null
        }
    }
    return @($items.ToArray())
}

function Get-PodEvidence {
    param([string[]] $Lines)
    $items = [System.Collections.Generic.List[object]]::new()
    foreach ($line in $Lines) {
        $trimmed = $line.Trim()
        if (-not $trimmed -or $trimmed -cmatch '^(?:SAMPLE /|NON-PRODUCTION |#)' -or $trimmed -match '^NAME\s+READY') { continue }
        $columns = @($trimmed -split '\s+')
        if ($columns.Count -ge 4) {
            $restartValue = 0
            [void][int]::TryParse(($columns[3] -replace '[^0-9].*$', ''), [ref]$restartValue)
            $items.Add([pscustomobject]@{ Ready = $columns[1]; Status = $columns[2]; Restarts = $restartValue }) | Out-Null
        }
    }
    return @($items.ToArray())
}

$baselineExists = Test-Path -LiteralPath $baselinePath -PathType Leaf
$commandReferenceExists = Test-Path -LiteralPath $commandReferencePath -PathType Leaf
Add-ValidationResult "V001" "Workload documentation" $(if ($baselineExists -and $commandReferenceExists) { "PASS" } else { "FAIL" }) $(if ($baselineExists -and $commandReferenceExists) { "Baseline and command reference exist." } else { "Baseline or command reference is missing." })

$manifestPaths = @($namespacePath, $deploymentPath, $servicePath, $workloadReadmePath)
$missingManifests = @($manifestPaths | Where-Object { -not (Test-Path -LiteralPath $_ -PathType Leaf) })
Add-ValidationResult "V002" "Required workload files" $(if ($missingManifests.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingManifests.Count -eq 0) { "Namespace, Deployment, Service, and README files exist." } else { "One or more workload files are missing." })

$samplePaths = @($deploymentSamplePath, $podSamplePath)
$missingSamples = @($samplePaths | Where-Object { -not (Test-Path -LiteralPath $_ -PathType Leaf) })
Add-ValidationResult "V003" "Sample workload evidence" $(if ($missingSamples.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingSamples.Count -eq 0) { "Deployment and pod sample evidence exist." } else { "Deployment or pod sample evidence is missing." })

$baselineContent = if ($baselineExists) { Get-Content -LiteralPath $baselinePath -Raw } else { "" }
$commandContent = if ($commandReferenceExists) { Get-Content -LiteralPath $commandReferencePath -Raw } else { "" }
$namespaceContent = if (Test-Path -LiteralPath $namespacePath) { Get-Content -LiteralPath $namespacePath -Raw } else { "" }
$deploymentContent = if (Test-Path -LiteralPath $deploymentPath) { Get-Content -LiteralPath $deploymentPath -Raw } else { "" }
$serviceContent = if (Test-Path -LiteralPath $servicePath) { Get-Content -LiteralPath $servicePath -Raw } else { "" }
$deploymentSampleContent = if (Test-Path -LiteralPath $deploymentSamplePath) { Get-Content -LiteralPath $deploymentSamplePath -Raw } else { "" }
$podSampleContent = if (Test-Path -LiteralPath $podSamplePath) { Get-Content -LiteralPath $podSamplePath -Raw } else { "" }
$manifestContent = @($namespaceContent, $deploymentContent, $serviceContent) -join "`n"
$combinedContent = @($baselineContent, $commandContent, $manifestContent, $deploymentSampleContent, $podSampleContent) -join "`n"

$missingCommands = @($requiredCommands | Where-Object { $commandContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V004" "Required command examples" $(if ($missingCommands.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingCommands.Count -eq 0) { "All seven command examples are documented." } else { "Required command examples are missing." })

$missingBaselineTerms = @($requiredBaselineTerms | Where-Object { $baselineContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V005" "Deployment validation model" $(if ($missingBaselineTerms.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingBaselineTerms.Count -eq 0) { "Objects, replicas, readiness, image, labels, probes, resources, evidence, and modes are documented." } else { "Required deployment model terms are missing." })

$kindAndNamespaceReady = $namespaceContent -match '(?im)^kind:\s*Namespace\s*$' -and
    $namespaceContent -match '(?im)^\s*name:\s*snsd-example\s*$' -and
    $deploymentContent -match '(?im)^kind:\s*Deployment\s*$' -and
    $serviceContent -match '(?im)^kind:\s*Service\s*$' -and
    $deploymentContent -match '(?im)^\s*namespace:\s*snsd-example\s*$' -and
    $serviceContent -match '(?im)^\s*namespace:\s*snsd-example\s*$' -and
    @(@($namespaceContent, $deploymentContent, $serviceContent) | Where-Object { $_ -notmatch 'NON-PRODUCTION EXAMPLE' }).Count -eq 0
Add-ValidationResult "V006" "Manifest kinds and namespace" $(if ($kindAndNamespaceReady) { "PASS" } else { "FAIL" }) $(if ($kindAndNamespaceReady) { "Namespace, Deployment, and Service examples use snsd-example and are marked non-production." } else { "Manifest kind, namespace, or example marker is invalid." })

$deploymentLabels = @([regex]::Matches($deploymentContent, '(?im)^\s*app:\s*sample-service-placeholder\s*$')).Count
$serviceLabels = @([regex]::Matches($serviceContent, '(?im)^\s*app:\s*sample-service-placeholder\s*$')).Count
$labelsReady = $deploymentLabels -ge 3 -and $serviceLabels -ge 2 -and $deploymentContent -match '(?im)^\s*matchLabels:\s*$' -and $serviceContent -match '(?im)^\s*selector:\s*$'
Add-ValidationResult "V007" "Labels and selectors" $(if ($labelsReady) { "PASS" } else { "FAIL" }) $(if ($labelsReady) { "Deployment metadata/template/selector and Service selector labels are consistent." } else { "Label or selector consistency is incomplete." })

$runtimeReady = $deploymentContent -match '(?im)^\s*readinessProbe:\s*$' -and
    $deploymentContent -match '(?im)^\s*livenessProbe:\s*$' -and
    $deploymentContent -match '(?im)^\s*requests:\s*$' -and
    $deploymentContent -match '(?im)^\s*limits:\s*$' -and
    $deploymentContent -match '(?im)^\s*image:\s*nginx:stable-alpine\s*$' -and
    $deploymentContent -notmatch '(?im)^\s*image:\s*[^\s]+:latest\s*$'
Add-ValidationResult "V008" "Runtime readiness controls" $(if ($runtimeReady) { "PASS" } else { "FAIL" }) $(if ($runtimeReady) { "Readiness/liveness probes, requests/limits, and fixed image tag exist." } else { "Probe, resource, or image-tag requirements are incomplete." })

$unsafeManifestPatterns = @(
    '(?im)^\s*hostNetwork:\s*true\s*$',
    '(?im)^\s*privileged:\s*true\s*$',
    '(?im)^\s*hostPath:\s*$',
    '(?im)^kind:\s*Secret\s*$',
    '(?im)^\s*imagePullSecrets:\s*$',
    '(?im)^kind:\s*ClusterRoleBinding\s*$',
    '(?im)^\s*type:\s*NodePort\s*$'
)
$unsafeManifestHit = $false
foreach ($pattern in $unsafeManifestPatterns) { if ($manifestContent -match $pattern) { $unsafeManifestHit = $true; break } }
Add-ValidationResult "V009" "Unsafe manifest pattern denial" $(if (-not $unsafeManifestHit) { "PASS" } else { "FAIL" }) $(if (-not $unsafeManifestHit) { "No hostNetwork, privileged, hostPath, Secret, imagePullSecrets, ClusterRoleBinding, or NodePort pattern exists." } else { "An unsafe manifest pattern was detected." })

[array] $staticDeployments = if (Test-Path -LiteralPath $deploymentSamplePath) { @(Get-DeploymentEvidence -Lines (Get-Content -LiteralPath $deploymentSamplePath)) } else { @() }
[array] $staticPods = if (Test-Path -LiteralPath $podSamplePath) { @(Get-PodEvidence -Lines (Get-Content -LiteralPath $podSamplePath)) } else { @() }
[array] $activeDeployments = @($staticDeployments)
[array] $activePods = @($staticPods)
$liveCommandsPassed = $true
$liveDetail = "Live kubectl was not requested; static evidence is authoritative for this run."

if ($LiveKubectl) {
    $kubectlCommand = Get-Command "kubectl" -CommandType Application -ErrorAction SilentlyContinue
    if ($null -eq $kubectlCommand) {
        $liveCommandsPassed = $false
        $activeDeployments = @()
        $activePods = @()
        $liveDetail = "LiveKubectl was requested but kubectl is unavailable."
    }
    else {
        $deploymentArguments = @("get", "deployments", "-n", "snsd-example")
        $podArguments = @("get", "pods", "-n", "snsd-example")
        $deploymentOutput = @(& $kubectlCommand.Source @deploymentArguments 2>&1)
        $deploymentExitCode = $LASTEXITCODE
        $podOutput = @(& $kubectlCommand.Source @podArguments 2>&1)
        $podExitCode = $LASTEXITCODE
        if ($deploymentExitCode -ne 0 -or $podExitCode -ne 0) {
            $liveCommandsPassed = $false
            $activeDeployments = @()
            $activePods = @()
            $liveDetail = "A read-only kubectl command failed; raw error output was not stored."
        }
        else {
            $activeDeployments = @(Get-DeploymentEvidence -Lines @($deploymentOutput | ForEach-Object { [string]$_ }))
            $activePods = @(Get-PodEvidence -Lines @($podOutput | ForEach-Object { [string]$_ }))
            $liveCommandsPassed = $activeDeployments.Count -gt 0 -and $activePods.Count -gt 0
            $liveDetail = if ($liveCommandsPassed) { "Read-only kubectl returned $($activeDeployments.Count) deployment and $($activePods.Count) pod row(s); raw rows were not stored." } else { "kubectl returned no parseable deployment or pod rows." }
        }
    }
}

$failedDeploymentIndicators = @($activeDeployments | Where-Object { $_.RawStatus -match '(?i)(?:^|\s)0/\d+|unavailable|failed|crash|error' })
$notReadyDeployments = @($activeDeployments | Where-Object {
    if ($_.Ready -notmatch '^(\d+)/(\d+)$') { return $true }
    $ready = [int]$Matches[1]
    $desired = [int]$Matches[2]
    return $desired -le 0 -or $ready -ne $desired -or [int]$_.Available -lt $desired
})
$deploymentPassed = $activeDeployments.Count -gt 0 -and $failedDeploymentIndicators.Count -eq 0 -and $notReadyDeployments.Count -eq 0
Add-ValidationResult "V010" "Deployment evidence" $(if ($deploymentPassed) { "PASS" } else { "FAIL" }) $(if ($deploymentPassed) { "All $($activeDeployments.Count) deployment row(s) are fully ready and available." } else { "Deployment evidence is absent, failed, unavailable, or not fully ready." })

$failedPodStatuses = @('CrashLoopBackOff', 'ImagePullBackOff', 'ErrImagePull', 'Error', 'Failed', 'Pending', 'Unknown')
$failedPods = @($activePods | Where-Object { $_.Status -in $failedPodStatuses -or $_.Status -ne 'Running' })
$notReadyPods = @($activePods | Where-Object {
    if ($_.Ready -notmatch '^(\d+)/(\d+)$') { return $true }
    return [int]$Matches[2] -le 0 -or [int]$Matches[1] -ne [int]$Matches[2]
})
$podPassed = $activePods.Count -gt 0 -and $failedPods.Count -eq 0 -and $notReadyPods.Count -eq 0
Add-ValidationResult "V011" "Pod evidence" $(if ($podPassed) { "PASS" } else { "FAIL" }) $(if ($podPassed) { "All $($activePods.Count) pod row(s) are Running and fully ready." } else { "Pod evidence is absent, non-running, failed, or not fully ready." })

$restartCount = 0
foreach ($pod in $activePods) { $restartCount += [int]$pod.Restarts }
Add-ValidationResult "V012" "Pod restart awareness" $(if ($restartCount -eq 0) { "PASS" } else { "WARN" }) $(if ($restartCount -eq 0) { "No pod restart is present in evaluated evidence." } else { "$restartCount restart(s) require review unless expected." })

$forbiddenFiles = @(Get-ChildItem -LiteralPath $repositoryRoot -File -Recurse -Force -ErrorAction SilentlyContinue | Where-Object {
    $_.FullName -notmatch '[\\/]\.git[\\/]' -and
    ($_.Name -match '(?i)(^|\.)kubeconfig($|\.)|service[-_]?account.*token|\.crt$|\.cer$|\.pem$|\.key$|\.p12$|\.pfx$')
})
Add-ValidationResult "V013" "Kubernetes credential files" $(if ($forbiddenFiles.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($forbiddenFiles.Count -eq 0) { "No kubeconfig, service-account token, certificate, or private-key file exists." } else { "A forbidden Kubernetes credential file was detected." })

$endpointHit = $combinedContent -match '(?i)https?://[^\s<]+'
$secretHit = $combinedContent -match '-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----' -or
    $combinedContent -match '(?im)^\s*(?:token|password|secret|client-certificate-data|client-key-data)\s*[:=]\s*(?!["'']?<|false\s*$)\S+'
$ipMatches = @([regex]::Matches($combinedContent, '(?<![A-Za-z0-9<])((?:\d{1,3}\.){3}\d{1,3})(?:/\d{1,2})?(?![A-Za-z0-9>])'))
$contentSafe = -not $endpointHit -and -not $secretHit -and $ipMatches.Count -eq 0
Add-ValidationResult "V014" "Manifest and evidence sensitive-content safety" $(if ($contentSafe) { "PASS" } else { "FAIL" }) $(if ($contentSafe) { "No endpoint URL, numeric address, token, certificate data, key, password, or secret exists." } else { "Sensitive or account-specific content was detected." })

$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$deploymentInvocationReady = $scriptContent -match '\$deploymentArguments\s*=\s*@\("get",\s*"deployments",\s*"-n",\s*"snsd-example"\)'
$podInvocationReady = $scriptContent -match '\$podArguments\s*=\s*@\("get",\s*"pods",\s*"-n",\s*"snsd-example"\)'
$prohibitedInvocation = $scriptContent -match '(?im)^\s*(?:&\s*)?kubectl\s+(?:apply|delete|patch|edit|replace|scale|rollout|cordon|drain|taint)\b'
$executionSafe = $deploymentInvocationReady -and $podInvocationReady -and -not $prohibitedInvocation
Add-ValidationResult "V015" "Execution safety boundary" $(if ($executionSafe) { "PASS" } else { "FAIL" }) $(if ($executionSafe) { "Live argument sets contain only read-only deployment and pod listings guarded by LiveKubectl." } else { "Read-only live boundaries are missing or a mutation invocation exists." })

Add-ValidationResult "V016" "Validation mode" $(if ($liveCommandsPassed) { "PASS" } else { "FAIL" }) $(if ($LiveKubectl) { $liveDetail } else { "Static mode completed without invoking kubectl." })

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Kubernetes workload deployment ($validationMode): $criticalFailures critical failure(s), $warningCount warning(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S022 Kubernetes Workload Deployment Validation"
    "Generated: $timestamp"
    "Validation mode: $validationMode"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No kubeconfig path, token, certificate, endpoint, address, raw live workload row, or secret was stored."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$requiredFilesPassed = $baselineExists -and $commandReferenceExists -and $missingManifests.Count -eq 0 -and $missingSamples.Count -eq 0
$manifestSafetyPassed = $kindAndNamespaceReady -and $labelsReady -and $runtimeReady -and -not $unsafeManifestHit
$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# Kubernetes Workload Deployment Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S022-kubernetes-workload-deployment-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Validation mode: **$validationMode**") | Out-Null
$summaryLines.Add("- Required file check result: **$(if ($requiredFilesPassed) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Manifest safety check result: **$(if ($manifestSafetyPassed) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Deployment evidence parsing result: **$(if ($deploymentPassed) { 'PASS' } else { 'FAIL' })** ($($activeDeployments.Count) row(s))") | Out-Null
$summaryLines.Add("- Pod evidence parsing result: **$(if ($podPassed) { 'PASS' } else { 'FAIL' })** ($($activePods.Count) row(s), $restartCount restart(s))") | Out-Null
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
$summaryLines.Add("Static mode does not invoke kubectl. LiveKubectl mode runs only read-only workload listings and stores aggregate status rather than raw cluster details.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) { exit 1 }
exit 0
