$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$baselinePath = Join-Path $repositoryRoot "security-baseline\kubernetes-rbac-baseline.md"
$matrixPath = Join-Path $repositoryRoot "security-baseline\kubernetes-rbac-rule-matrix.example.md"
$manifestRoot = Join-Path $repositoryRoot "kubernetes\security\rbac-baseline"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L2-security-baseline\S018-kubernetes-rbac-validation"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "kubernetes-rbac-validation.log"
$summaryPath = Join-Path $configDirectory "kubernetes-rbac-summary.md"

$requiredFiles = @(
    "README.md",
    "namespace.example.yaml",
    "serviceaccount.application.example.yaml",
    "serviceaccount.monitoring.example.yaml",
    "role.application-readwrite-limited.example.yaml",
    "role.monitoring-readonly.example.yaml",
    "rolebinding.application.example.yaml",
    "rolebinding.monitoring.example.yaml"
)
$requiredSubjects = @(
    '<application-service-account>', '<monitoring-service-account>',
    '<deployment-automation-service-account>', '<read-only-operator-service-account>'
)
$requiredStatements = @(
    'Least Privilege RBAC Principle',
    'Namespace-scoped `Role` and `RoleBinding` are preferred',
    'ServiceAccount separation by workload',
    'The `default` ServiceAccount must not be used',
    'No `cluster-admin` binding',
    'No wildcard apiGroups, resources, or verbs',
    'read-only `get`, `list`, and `watch`',
    'Write privileges are limited',
    'Secrets access is denied by default',
    '<namespace>', '<service-account>', '<application-workload>',
    '<monitoring-service-account>', '<role-name>', '<rolebinding-name>', '<evidence-path>'
)

New-Item -ItemType Directory -Force -Path $logDirectory, $configDirectory | Out-Null
$results = [System.Collections.Generic.List[object]]::new()
$outputLines = [System.Collections.Generic.List[string]]::new()
$criticalFailures = 0

function Add-ValidationResult {
    param(
        [string] $Id,
        [string] $Description,
        [ValidateSet("PASS", "WARN", "FAIL")] [string] $Result,
        [string] $Detail
    )
    if ($Result -eq "FAIL") { $script:criticalFailures++ }
    $line = "[$Result] $Id ${Description}: $Detail"
    Write-Host $line
    $script:outputLines.Add($line) | Out-Null
    $script:results.Add([pscustomobject]@{ Id = $Id; Description = $Description; Result = $Result; Detail = $Detail }) | Out-Null
}

$baselineExists = Test-Path -LiteralPath $baselinePath -PathType Leaf
Add-ValidationResult "V001" "RBAC baseline" $(if ($baselineExists) { "PASS" } else { "FAIL" }) $(if ($baselineExists) { "Baseline document exists." } else { "Baseline document is missing." })

$matrixExists = Test-Path -LiteralPath $matrixPath -PathType Leaf
Add-ValidationResult "V002" "RBAC rule matrix" $(if ($matrixExists) { "PASS" } else { "FAIL" }) $(if ($matrixExists) { "Rule matrix exists." } else { "Rule matrix is missing." })

$manifestRootExists = Test-Path -LiteralPath $manifestRoot -PathType Container
Add-ValidationResult "V003" "RBAC manifest directory" $(if ($manifestRootExists) { "PASS" } else { "FAIL" }) $(if ($manifestRootExists) { "Manifest example directory exists." } else { "Manifest example directory is missing." })

$missingFiles = @($requiredFiles | Where-Object { -not (Test-Path -LiteralPath (Join-Path $manifestRoot $_) -PathType Leaf) })
Add-ValidationResult "V004" "Required manifest examples" $(if ($missingFiles.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingFiles.Count -eq 0) { "All required example files exist." } else { "Missing files: " + ($missingFiles -join ", ") })

$baselineContent = if ($baselineExists) { Get-Content -LiteralPath $baselinePath -Raw } else { "" }
$matrixContent = if ($matrixExists) { Get-Content -LiteralPath $matrixPath -Raw } else { "" }
$missingSubjects = @($requiredSubjects | Where-Object { $matrixContent -notmatch [regex]::Escape($_) })
$missingStatements = @($requiredStatements | Where-Object { $baselineContent -notmatch [regex]::Escape($_) })
$policyReady = $missingSubjects.Count -eq 0 -and $missingStatements.Count -eq 0
Add-ValidationResult "V005" "Policy statements and subjects" $(if ($policyReady) { "PASS" } else { "FAIL" }) $(if ($policyReady) { "Required least-privilege statements and four subject placeholders exist." } else { "Policy or subject placeholders are incomplete." })

$yamlFiles = if ($manifestRootExists) { @(Get-ChildItem -LiteralPath $manifestRoot -File -Filter "*.yaml") } else { @() }
$yamlContent = @($yamlFiles | ForEach-Object { Get-Content -LiteralPath $_.FullName -Raw }) -join "`n"
$allMarked = $yamlFiles.Count -ge 7 -and @($yamlFiles | Where-Object { (Get-Content -LiteralPath $_.FullName -Raw) -notmatch 'NON-PRODUCTION EXAMPLE' }).Count -eq 0
$expectedKindByFile = @{
    "namespace.example.yaml"                            = "Namespace"
    "serviceaccount.application.example.yaml"           = "ServiceAccount"
    "serviceaccount.monitoring.example.yaml"            = "ServiceAccount"
    "role.application-readwrite-limited.example.yaml"   = "Role"
    "role.monitoring-readonly.example.yaml"             = "Role"
    "rolebinding.application.example.yaml"              = "RoleBinding"
    "rolebinding.monitoring.example.yaml"               = "RoleBinding"
}
$kindMismatches = @(
    foreach ($entry in $expectedKindByFile.GetEnumerator()) {
        $path = Join-Path $manifestRoot $entry.Key
        if (-not (Test-Path -LiteralPath $path -PathType Leaf) -or (Get-Content -LiteralPath $path -Raw) -notmatch "(?im)^kind:\s*$([regex]::Escape($entry.Value))\s*$") {
            $entry.Key
        }
    }
)
$structureReady = $allMarked -and
    $kindMismatches.Count -eq 0 -and
    $yamlContent -notmatch '(?im)^\s*namespace:\s*(?!snsd-example\s*$)\S+'
Add-ValidationResult "V006" "Namespace-scoped RBAC structure" $(if ($structureReady) { "PASS" } else { "FAIL" }) $(if ($structureReady) { "Dedicated accounts, namespaced Roles/RoleBindings, example markers, and namespace scope are correct." } else { "RBAC structure or namespace scope is incomplete." })

$clusterWideHit = $yamlContent -match '(?im)^kind:\s*ClusterRoleBinding\s*$' -or $yamlContent -match '(?i)cluster-admin'
Add-ValidationResult "V007" "Cluster-wide privilege denial" $(if (-not $clusterWideHit) { "PASS" } else { "FAIL" }) $(if (-not $clusterWideHit) { "No ClusterRoleBinding or cluster-admin binding exists." } else { "A forbidden cluster-wide binding was detected." })

$permissionLines = @($yamlContent -split "`r?`n" | Where-Object { $_ -match '(?i)^\s*(?:apiGroups|resources|verbs):' })
$wildcardHit = @($permissionLines | Where-Object { $_ -match '["'']\*["'']' }).Count -gt 0
Add-ValidationResult "V008" "Wildcard permission denial" $(if (-not $wildcardHit) { "PASS" } else { "FAIL" }) $(if (-not $wildcardHit) { "No wildcard apiGroup, resource, or verb exists." } else { "A wildcard permission was detected." })

$applicationRolePath = Join-Path $manifestRoot "role.application-readwrite-limited.example.yaml"
$applicationRoleContent = if (Test-Path -LiteralPath $applicationRolePath) { Get-Content -LiteralPath $applicationRolePath -Raw } else { "" }
$applicationBindingPath = Join-Path $manifestRoot "rolebinding.application.example.yaml"
$applicationBindingContent = if (Test-Path -LiteralPath $applicationBindingPath) { Get-Content -LiteralPath $applicationBindingPath -Raw } else { "" }
$applicationSafe = $applicationRoleContent -notmatch '(?im)^\s*resources:\s*\[[^\]]*["'']secrets["'']' -and
    $applicationBindingContent -match '(?im)^\s*name:\s*snsd-example-application\s*$' -and
    $applicationBindingContent -notmatch '(?im)^\s*name:\s*default\s*$'
Add-ValidationResult "V009" "Application account restrictions" $(if ($applicationSafe) { "PASS" } else { "FAIL" }) $(if ($applicationSafe) { "Application binding uses its dedicated account and receives no secrets access." } else { "Application secrets access or default account use was detected." })

$defaultApprovalHit = $yamlContent -match '(?im)^\s*name:\s*default\s*$' -or $matrixContent -match '(?i)default ServiceAccount\s*(?:is|=)\s*(?:approved|allowed)'
Add-ValidationResult "V010" "Default ServiceAccount denial" $(if (-not $defaultApprovalHit) { "PASS" } else { "FAIL" }) $(if (-not $defaultApprovalHit) { "Default ServiceAccount is not used or approved for application workloads." } else { "Default ServiceAccount use or approval was detected." })

$monitoringRolePath = Join-Path $manifestRoot "role.monitoring-readonly.example.yaml"
$monitoringRoleContent = if (Test-Path -LiteralPath $monitoringRolePath) { Get-Content -LiteralPath $monitoringRolePath -Raw } else { "" }
$monitoringVerbLines = @($monitoringRoleContent -split "`r?`n" | Where-Object { $_ -match '(?i)^\s*verbs:' })
$monitoringReadOnly = $monitoringVerbLines.Count -ge 1 -and @($monitoringVerbLines | Where-Object { $_ -match '(?i)create|update|patch|delete|deletecollection|impersonate|bind|escalate' }).Count -eq 0 -and $monitoringRoleContent -match '"get"' -and $monitoringRoleContent -match '"list"' -and $monitoringRoleContent -match '"watch"'
Add-ValidationResult "V011" "Monitoring read-only role" $(if ($monitoringReadOnly) { "PASS" } else { "FAIL" }) $(if ($monitoringReadOnly) { "Monitoring Role uses get, list, and watch only." } else { "Monitoring Role is missing read-only verbs or contains a write verb." })

$forbiddenFiles = @(Get-ChildItem -LiteralPath $repositoryRoot -File -Recurse -Force -ErrorAction SilentlyContinue | Where-Object {
    $_.FullName -notmatch '[\\/]\.git[\\/]' -and
    ($_.Name -match '(?i)(^|\.)kubeconfig($|\.)|service[-_]?account.*token|\.crt$|\.cer$|\.pem$|\.key$|\.p12$|\.pfx$')
})
Add-ValidationResult "V012" "Kubernetes credential files" $(if ($forbiddenFiles.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($forbiddenFiles.Count -eq 0) { "No kubeconfig, service-account token, certificate, or private-key file exists." } else { "A forbidden Kubernetes credential file was detected." })

$manifestSecretHit = $yamlContent -match '(?im)^kind:\s*Secret\s*$' -or $yamlContent -match '(?im)^\s*(?:token|stringData|client-certificate-data|client-key-data):\s*\S+'
$endpointHit = $yamlContent -match '(?i)https?://[^\s<]+'
$ipMatches = @([regex]::Matches($yamlContent, '(?<![A-Za-z0-9<])((?:\d{1,3}\.){3}\d{1,3})(?:/\d{1,2})?(?![A-Za-z0-9>])'))
$secretSafe = -not $manifestSecretHit -and -not $endpointHit -and $ipMatches.Count -eq 0
Add-ValidationResult "V013" "Manifest sensitive-content safety" $(if ($secretSafe) { "PASS" } else { "FAIL" }) $(if ($secretSafe) { "No Secret resource, token, certificate data, endpoint URL, or numeric address exists." } else { "Sensitive or account-specific manifest content was detected." })

$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$activeCommandPatterns = @(
    '(?im)^\s*(?:&\s*)?kubectl\b',
    '(?im)^\s*(?:Invoke-WebRequest|Invoke-RestMethod|Test-NetConnection)\b',
    '(?im)^\s*(?:&\s*)?helm\b'
)
$activeCommandHit = $false
foreach ($pattern in $activeCommandPatterns) { if ($scriptContent -match $pattern) { $activeCommandHit = $true; break } }
Add-ValidationResult "V014" "Execution safety boundary" $(if (-not $activeCommandHit) { "PASS" } else { "FAIL" }) $(if (-not $activeCommandHit) { "The validator contains no kubectl, Helm, API, or network execution command." } else { "A prohibited live execution command was detected." })

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Repository-side Kubernetes RBAC baseline: $criticalFailures critical failure(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S018 Kubernetes RBAC Validation"
    "Generated: $timestamp"
    "Scope: repository policy, matrix, example manifests, and safety checks only"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No kubectl, kubeconfig read, cluster connection, API query, manifest apply, credential access, or resource modification was performed."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# Kubernetes RBAC Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S018-kubernetes-rbac-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Overall result: **$overallResult**") | Out-Null
$summaryLines.Add("- Scope: local policy, matrix, manifest examples, and safety checks") | Out-Null
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
$summaryLines.Add("This validation read repository files only. It did not run kubectl, read kubeconfig, connect to a cluster, query an API server, apply manifests, or access credentials.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) { exit 1 }
exit 0
