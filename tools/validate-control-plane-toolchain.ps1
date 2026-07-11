$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$evidenceRoot = Join-Path $repositoryRoot "evidence\L1-foundation\S001-control-plane-toolchain-validation"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "control-plane-toolchain-validation.log"
$summaryPath = Join-Path $configDirectory "control-plane-toolchain-summary.md"

New-Item -ItemType Directory -Force -Path $logDirectory, $configDirectory | Out-Null

$toolChecks = @(
    [pscustomobject]@{ Id = "V001"; Name = "Git"; Command = "git"; Arguments = @("--version"); Tier = "CORE" },
    [pscustomobject]@{ Id = "V002"; Name = "PowerShell"; Command = "powershell"; Arguments = @("-NoProfile", "-Command", '$PSVersionTable.PSVersion.ToString()'); Tier = "CORE" },
    [pscustomobject]@{ Id = "V003"; Name = "SSH"; Command = "ssh"; Arguments = @("-V"); Tier = "CORE" },
    [pscustomobject]@{ Id = "V004"; Name = "Python"; Command = "python"; Arguments = @("--version"); Tier = "CORE" },
    [pscustomobject]@{ Id = "V005"; Name = "Terraform"; Command = "terraform"; Arguments = @("version"); Tier = "LATER_STAGE" },
    [pscustomobject]@{ Id = "V006"; Name = "Ansible"; Command = "ansible"; Arguments = @("--version"); Tier = "LATER_STAGE" },
    [pscustomobject]@{ Id = "V007"; Name = "kubectl"; Command = "kubectl"; Arguments = @("version", "--client"); Tier = "LATER_STAGE" },
    [pscustomobject]@{ Id = "V008"; Name = "Docker"; Command = "docker"; Arguments = @("--version"); Tier = "LATER_STAGE" }
)

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$results = [System.Collections.Generic.List[object]]::new()
$consoleLines = [System.Collections.Generic.List[string]]::new()
$coreFailures = 0

foreach ($tool in $toolChecks) {
    $commandInfo = Get-Command -Name $tool.Command -ErrorAction SilentlyContinue | Select-Object -First 1
    $classification = "PASS"
    $detail = ""

    if ($null -eq $commandInfo) {
        if ($tool.Tier -eq "CORE") {
            $classification = "FAIL"
            $coreFailures++
        }
        else {
            $classification = "WARN"
        }
        $detail = "Command not found."
    }
    else {
        $commandName = $tool.Command
        $arguments = @($tool.Arguments)
        $previousErrorActionPreference = $ErrorActionPreference
        try {
            # Some version commands, notably ssh -V, return normal output on stderr.
            $ErrorActionPreference = "Continue"
            $output = @(& $commandName @arguments 2>&1)
            $exitCode = $LASTEXITCODE
        }
        finally {
            $ErrorActionPreference = $previousErrorActionPreference
        }

        if ($exitCode -ne 0) {
            if ($tool.Tier -eq "CORE") {
                $classification = "FAIL"
                $coreFailures++
            }
            else {
                $classification = "WARN"
            }
            $detail = "Version command exited with code $exitCode."
        }
        else {
            $firstLine = @(
                $output |
                    ForEach-Object { $_.ToString().Trim() } |
                    Where-Object { -not [string]::IsNullOrWhiteSpace($_) }
            ) | Select-Object -First 1

            if ([string]::IsNullOrWhiteSpace($firstLine)) {
                if ($tool.Tier -eq "CORE") {
                    $classification = "FAIL"
                    $coreFailures++
                }
                else {
                    $classification = "WARN"
                }
                $detail = "Version command returned no output."
            }
            else {
                $detail = $firstLine
            }
        }
    }

    $line = "[$classification] $($tool.Name) [$($tool.Tier)]: $detail"
    Write-Host $line
    $consoleLines.Add($line) | Out-Null
    $results.Add([pscustomobject]@{
        Id = $tool.Id
        Tool = $tool.Name
        Tier = $tool.Tier
        Result = $classification
        Detail = $detail
    }) | Out-Null
}

$overallResult = if ($coreFailures -eq 0) { "PASS" } else { "FAIL" }
$coreCount = @($toolChecks | Where-Object { $_.Tier -eq "CORE" }).Count
$overallLine = "[$overallResult] Core control plane readiness: $coreCount core checks evaluated; $coreFailures core failure(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S001 Control Plane Toolchain Validation"
    "Generated: $timestamp"
    "Scope: local command availability and version output only"
    ""
) + @($consoleLines) + @(
    ""
    $overallLine
    "No cloud authentication, cluster connection, credential read, kubeconfig read, tfstate access, or infrastructure action was performed."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# Control Plane Toolchain Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S001-control-plane-toolchain-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Overall result: **$overallResult**") | Out-Null
$summaryLines.Add("- Exit rule: non-zero only when a core tool is unavailable or cannot return version output") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("| Check ID | Tool | Classification | Result | Version or Detail |") | Out-Null
$summaryLines.Add("|---|---|---|---|---|") | Out-Null
foreach ($result in $results) {
    $safeDetail = $result.Detail.Replace("|", "\|")
    $summaryLines.Add("| $($result.Id) | $($result.Tool) | $($result.Tier) | $($result.Result) | $safeDetail |") | Out-Null
}
$summaryLines.Add("") | Out-Null
$summaryLines.Add("## Safety Boundary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("The validation used command discovery and local version-only invocations. It did not authenticate to cloud providers or registries, connect to Kubernetes clusters, read kubeconfig or credentials, access tfstate, or change infrastructure.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($coreFailures -gt 0) {
    exit 1
}

exit 0
