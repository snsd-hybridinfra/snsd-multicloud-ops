param(
    [switch] $LiveKubectl
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$parserModulePath = Join-Path $PSScriptRoot "modules\NodeReadinessParser.psm1"
Import-Module -Name $parserModulePath -Force
$baselinePath = Join-Path $repositoryRoot "kubernetes\node-readiness-validation.md"
$commandReferencePath = Join-Path $repositoryRoot "kubernetes\node-readiness-commands.example.md"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L3-service-operations\S021-kubernetes-node-readiness-validation"
$samplePath = Join-Path $evidenceRoot "logs\kubectl-get-nodes.sample.txt"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "kubernetes-node-readiness-validation.log"
$summaryPath = Join-Path $configDirectory "kubernetes-node-readiness-summary.md"
$validationMode = if ($LiveKubectl) { "LiveKubectl" } else { "Static" }

$requiredCommands = @(
    'kubectl get nodes',
    'kubectl get nodes -o wide',
    'kubectl describe node <node-name>',
    "kubectl get node <node-name> -o jsonpath='{.status.conditions}'",
    "kubectl get --raw='/readyz?verbose'"
)
$requiredBaselineTerms = @(
    'Ready=True', 'NotReady', 'SchedulingDisabled', 'kubelet readiness',
    '<kubernetes-cluster>', '<control-plane-node>', '<worker-node>',
    '<node-name>', '<node-role>', '<node-readiness-condition>', '<evidence-path>',
    'Static evidence validation', 'LiveKubectl'
)
$requiredSampleNodes = @(
    'control-plane-placeholder', 'worker-node-placeholder-01', 'worker-node-placeholder-02'
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

$baselineExists = Test-Path -LiteralPath $baselinePath -PathType Leaf
Add-ValidationResult "V001" "Node-readiness baseline" $(if ($baselineExists) { "PASS" } else { "FAIL" }) $(if ($baselineExists) { "Baseline document exists." } else { "Baseline document is missing." })

$commandReferenceExists = Test-Path -LiteralPath $commandReferencePath -PathType Leaf
Add-ValidationResult "V002" "Command reference" $(if ($commandReferenceExists) { "PASS" } else { "FAIL" }) $(if ($commandReferenceExists) { "Command reference exists." } else { "Command reference is missing." })

$sampleExists = Test-Path -LiteralPath $samplePath -PathType Leaf
Add-ValidationResult "V003" "Sample node evidence" $(if ($sampleExists) { "PASS" } else { "FAIL" }) $(if ($sampleExists) { "Sample evidence exists." } else { "Sample evidence is missing." })

$baselineContent = if ($baselineExists) { Get-Content -LiteralPath $baselinePath -Raw } else { "" }
$commandContent = if ($commandReferenceExists) { Get-Content -LiteralPath $commandReferencePath -Raw } else { "" }
$sampleContent = if ($sampleExists) { Get-Content -LiteralPath $samplePath -Raw } else { "" }
$combinedContent = @($baselineContent, $commandContent, $sampleContent) -join "`n"

$missingCommands = @($requiredCommands | Where-Object { $commandContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V004" "Required command examples" $(if ($missingCommands.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingCommands.Count -eq 0) { "All five read-only command examples are documented." } else { "Missing command references: " + ($missingCommands -join ", ") })

$missingBaselineTerms = @($requiredBaselineTerms | Where-Object { $baselineContent -notmatch [regex]::Escape($_) })
Add-ValidationResult "V005" "Readiness model and placeholders" $(if ($missingBaselineTerms.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingBaselineTerms.Count -eq 0) { "Ready, NotReady, scheduling, kubelet, role, evidence, and mode rules exist." } else { "Required readiness terms are missing." })

$sampleParse = if ($sampleExists) {
    ConvertFrom-NodeStatusEvidence -Lines ([object[]](Get-Content -LiteralPath $samplePath))
}
else {
    ConvertFrom-NodeStatusEvidence -Lines $null
}
$sampleNodes = [System.Collections.Generic.List[object]]::new()
foreach ($node in $sampleParse.Nodes) {
    $sampleNodes.Add($node) | Out-Null
}
$sampleNodeNames = @($sampleNodes | ForEach-Object Name)
$missingSampleNodes = @($requiredSampleNodes | Where-Object { $_ -notin $sampleNodeNames })
Add-ValidationResult "V006" "Required sample nodes" $(if ($sampleParse.IsValid -and $missingSampleNodes.Count -eq 0) { "PASS" } else { "FAIL" }) $(if (-not $sampleParse.IsValid) { "Sample evidence contains $($sampleParse.MalformedCount) malformed record(s)." } elseif ($missingSampleNodes.Count -eq 0) { "All three placeholder nodes are present." } else { "Missing sample nodes: " + ($missingSampleNodes -join ", ") })

$activeNodes = [System.Collections.Generic.List[object]]::new()
foreach ($node in $sampleNodes) {
    $activeNodes.Add($node) | Out-Null
}
$activeParseValid = $sampleParse.IsValid
$liveCommandPassed = $true
$liveCommandDetail = "Live kubectl was not requested; static evidence is authoritative for this run."
if ($LiveKubectl) {
    $kubectlCommand = Get-Command "kubectl" -CommandType Application -ErrorAction SilentlyContinue
    if ($null -eq $kubectlCommand) {
        $liveCommandPassed = $false
        $activeNodes.Clear()
        $activeParseValid = $true
        $liveCommandDetail = "LiveKubectl was requested but kubectl is unavailable."
    }
    else {
        $kubectlArguments = @("get", "nodes", "--no-headers")
        $liveOutput = @(& $kubectlCommand.Source @kubectlArguments 2>&1)
        $liveExitCode = $LASTEXITCODE
        if ($liveExitCode -ne 0) {
            $liveCommandPassed = $false
            $activeNodes.Clear()
            $activeParseValid = $true
            $liveCommandDetail = "The read-only kubectl command failed; raw error output was not stored."
        }
        else {
            $liveParse = ConvertFrom-NodeStatusEvidence -Lines ([object[]]@($liveOutput | ForEach-Object { [string]$_ }))
            $activeNodes.Clear()
            foreach ($node in $liveParse.Nodes) {
                $activeNodes.Add($node) | Out-Null
            }
            $activeParseValid = $liveParse.IsValid
            $liveCommandPassed = $activeParseValid -and $activeNodes.Count -gt 0
            $liveCommandDetail = if (-not $activeParseValid) { "The read-only kubectl output contained $($liveParse.MalformedCount) malformed row(s); raw rows were not stored." } elseif ($liveCommandPassed) { "Read-only kubectl returned $($activeNodes.Count) node status row(s); raw rows were not stored." } else { "kubectl returned no parseable node status rows." }
        }
    }
}

$notReadyNodes = @($activeNodes | Where-Object { $_.Status -match '(?i)NotReady' })
$nonReadyNodes = @($activeNodes | Where-Object { $_.Status -notmatch '(?i)(^|,)Ready($|,)' })
$readinessPassed = $activeParseValid -and $activeNodes.Count -gt 0 -and $notReadyNodes.Count -eq 0 -and $nonReadyNodes.Count -eq 0
Add-ValidationResult "V007" "Node readiness evidence" $(if ($readinessPassed) { "PASS" } else { "FAIL" }) $(if ($readinessPassed) { "All $($activeNodes.Count) evaluated node(s) include Ready and none include NotReady." } else { "Node evidence is empty, NotReady, or lacks Ready status." })

$schedulingDisabledNodes = @($activeNodes | Where-Object { $_.Status -match '(?i)SchedulingDisabled' })
Add-ValidationResult "V008" "SchedulingDisabled awareness" $(if ($schedulingDisabledNodes.Count -eq 0) { "PASS" } else { "WARN" }) $(if ($schedulingDisabledNodes.Count -eq 0) { "No evaluated node is SchedulingDisabled." } else { "$($schedulingDisabledNodes.Count) node(s) are SchedulingDisabled; confirm expected maintenance." })

$forbiddenFiles = @(Get-ChildItem -LiteralPath $repositoryRoot -File -Recurse -Force -ErrorAction SilentlyContinue | Where-Object {
    $_.FullName -notmatch '[\\/]\.git[\\/]' -and
    ($_.Name -match '(?i)(^|\.)kubeconfig($|\.)|service[-_]?account.*token|\.crt$|\.cer$|\.pem$|\.key$|\.p12$|\.pfx$')
})
Add-ValidationResult "V009" "Kubernetes credential files" $(if ($forbiddenFiles.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($forbiddenFiles.Count -eq 0) { "No kubeconfig, service-account token, certificate, or private-key file exists." } else { "A forbidden Kubernetes credential file was detected." })

$endpointHit = $combinedContent -match '(?i)https?://[^\s<]+'
$secretHit = $combinedContent -match '-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----' -or
    $combinedContent -match '(?im)^\s*(?:token|password|secret|client-certificate-data|client-key-data)\s*[:=]\s*(?!["'']?<)\S+'
$ipMatches = @([regex]::Matches($combinedContent, '(?<![A-Za-z0-9<])((?:\d{1,3}\.){3}\d{1,3})(?:/\d{1,2})?(?![A-Za-z0-9>])'))
$contentSafe = -not $endpointHit -and -not $secretHit -and $ipMatches.Count -eq 0
Add-ValidationResult "V010" "Evidence sensitive-content safety" $(if ($contentSafe) { "PASS" } else { "FAIL" }) $(if ($contentSafe) { "No endpoint URL, numeric address, token, certificate data, key, password, or secret exists." } else { "Sensitive or account-specific evidence content was detected." })

$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$readOnlyInvocationPresent = $scriptContent -match '\$kubectlArguments\s*=\s*@\("get",\s*"nodes",\s*"--no-headers"\)'
$prohibitedInvocation = $scriptContent -match '(?im)^\s*(?:&\s*)?kubectl\s+(?:apply|delete|patch|cordon|drain|taint|edit)\b'
$executionSafe = $readOnlyInvocationPresent -and -not $prohibitedInvocation
Add-ValidationResult "V011" "Execution safety boundary" $(if ($executionSafe) { "PASS" } else { "FAIL" }) $(if ($executionSafe) { "The only live argument set is get nodes --no-headers and it is guarded by LiveKubectl." } else { "The optional live command is missing its read-only boundary or a mutation command exists." })

Add-ValidationResult "V012" "Validation mode" $(if ($liveCommandPassed) { "PASS" } else { "FAIL" }) $(if ($LiveKubectl) { $liveCommandDetail } else { "Static mode completed without invoking kubectl." })

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Kubernetes node readiness ($validationMode): $criticalFailures critical failure(s), $warningCount warning(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S021 Kubernetes Node Readiness Validation"
    "Generated: $timestamp"
    "Validation mode: $validationMode"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No kubeconfig path, token, certificate, endpoint, node address, or raw live node row was stored."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# Kubernetes Node Readiness Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S021-kubernetes-node-readiness-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Validation mode: **$validationMode**") | Out-Null
$summaryLines.Add("- Required files check result: **$(if ($baselineExists -and $commandReferenceExists -and $sampleExists) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- Evidence parsing result: **$(if ($activeNodes.Count -gt 0) { 'PASS' } else { 'FAIL' })** ($($activeNodes.Count) node row(s))") | Out-Null
$summaryLines.Add("- Node readiness result: **$(if ($readinessPassed) { 'PASS' } else { 'FAIL' })**") | Out-Null
$summaryLines.Add("- NotReady findings: $($notReadyNodes.Count)") | Out-Null
$summaryLines.Add("- SchedulingDisabled findings: $($schedulingDisabledNodes.Count)") | Out-Null
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
$summaryLines.Add("Static mode does not invoke kubectl. LiveKubectl mode runs only read-only node listing and stores status counts rather than raw cluster details.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) { exit 1 }
exit 0
