[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$SourceDirectory,

    [Parameter(Mandatory = $true)]
    [string]$BuildDirectory,

    [Parameter(Mandatory = $true)]
    [string]$OutputDirectory,

    [Parameter(Mandatory = $true)]
    [string]$ReleaseAssetUrl
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repositoryRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$lockPath = Join-Path $repositoryRoot "applications/internal-iaas-portal/supply-chain/runner-bundle-source-lock.json"
$bundleAssets = Join-Path $repositoryRoot "applications/internal-iaas-portal/supply-chain/runner-bundle"
$tar = (Get-Command tar.exe -ErrorAction Stop).Source
$utf8NoBom = [Text.UTF8Encoding]::new($false)

foreach ($path in @($lockPath, $bundleAssets, $SourceDirectory)) {
    if (-not (Test-Path -LiteralPath $path)) { throw "Required bundle input is missing: $path" }
}
$resolvedSource = (Resolve-Path -LiteralPath $SourceDirectory).Path
$resolvedBuild = [IO.Path]::GetFullPath($BuildDirectory)
$resolvedOutput = [IO.Path]::GetFullPath($OutputDirectory)
foreach ($target in @($resolvedBuild, $resolvedOutput)) {
    if (Test-Path -LiteralPath $target) { throw "Refusing to overwrite bundle target: $target" }
}

$releaseUri = [Uri]$ReleaseAssetUrl
if ($releaseUri.Scheme -ne "https" -or -not $releaseUri.DnsSafeHost) {
    throw "ReleaseAssetUrl must be an exact HTTPS URL."
}
$lock = Get-Content -LiteralPath $lockPath -Raw | ConvertFrom-Json
if ($lock.schema_version -ne "1.0.0" -or $lock.platform -ne "linux-x86_64") {
    throw "Runner bundle source lock is invalid."
}
$sources = @($lock.sources)
$expectedIds = @("actions-runner", "cosign", "docker", "docker-buildx", "gh", "git", "syft", "trivy")
$actualIds = @($sources.id | Sort-Object)
if (@(Compare-Object -ReferenceObject $expectedIds -DifferenceObject $actualIds -SyncWindow 0).Count -ne 0) {
    throw "Runner source set is not exact."
}

function Invoke-CheckedTar([string[]]$Arguments) {
    & $tar @Arguments
    if ($LASTEXITCODE -ne 0) { throw "tar failed: $($Arguments -join ' ')" }
}

function Get-Source([string]$Id) {
    $record = $sources | Where-Object id -eq $Id
    if (@($record).Count -ne 1) { throw "Source ID is not unique: $Id" }
    $path = Join-Path $resolvedSource $record.file
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { throw "Locked source is missing: $($record.file)" }
    $actual = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
    if ($actual -ne $record.sha256) { throw "Locked source digest mismatch: $Id" }
    return [pscustomobject]@{ Record = $record; Path = $path }
}

$createdBuild = $false
$createdOutput = $false
try {
    New-Item -ItemType Directory -Path $resolvedBuild | Out-Null
    $createdBuild = $true
    New-Item -ItemType Directory -Path $resolvedOutput | Out-Null
    $createdOutput = $true
    $stage = Join-Path $resolvedBuild "bundle"
    $payload = Join-Path $stage "payload"
    New-Item -ItemType Directory -Path $payload -Force | Out-Null

    $runner = Get-Source "actions-runner"
    Copy-Item -LiteralPath $runner.Path -Destination (Join-Path $payload "actions-runner.tar.gz")
    $runnerProbe = Join-Path $resolvedBuild "runner-probe"
    New-Item -ItemType Directory -Path $runnerProbe | Out-Null
    Invoke-CheckedTar @("-xzf", $runner.Path, "-C", $runnerProbe, "./bin/Runner.Listener")

    $docker = Get-Source "docker"
    $dockerTemp = Join-Path $resolvedBuild "docker"
    New-Item -ItemType Directory -Path $dockerTemp | Out-Null
    Invoke-CheckedTar @("-xzf", $docker.Path, "-C", $dockerTemp)
    Copy-Item -LiteralPath (Join-Path $dockerTemp "docker") -Destination (Join-Path $payload "docker") -Recurse

    foreach ($archiveId in @("trivy", "syft")) {
        $source = Get-Source $archiveId
        $extract = Join-Path $resolvedBuild $archiveId
        New-Item -ItemType Directory -Path $extract | Out-Null
        Invoke-CheckedTar @("-xzf", $source.Path, "-C", $extract)
        Copy-Item -LiteralPath (Join-Path $extract $archiveId) -Destination (Join-Path $payload $archiveId)
    }

    $gh = Get-Source "gh"
    $ghTemp = Join-Path $resolvedBuild "gh"
    New-Item -ItemType Directory -Path $ghTemp | Out-Null
    Invoke-CheckedTar @("-xzf", $gh.Path, "-C", $ghTemp)
    $ghBinary = Get-ChildItem -LiteralPath $ghTemp -Filter gh -File -Recurse
    if (@($ghBinary).Count -ne 1) { throw "GitHub CLI archive binary is not exact." }
    Copy-Item -LiteralPath $ghBinary.FullName -Destination (Join-Path $payload "gh")

    foreach ($rawId in @("docker-buildx", "cosign")) {
        $source = Get-Source $rawId
        Copy-Item -LiteralPath $source.Path -Destination (Join-Path $payload $rawId)
    }

    $git = Get-Source "git"
    $gitAr = Join-Path $resolvedBuild "git-ar"
    $gitData = Join-Path $resolvedBuild "git-data"
    New-Item -ItemType Directory -Path $gitAr | Out-Null
    New-Item -ItemType Directory -Path $gitData | Out-Null
    Invoke-CheckedTar @("-xf", $git.Path, "-C", $gitAr)
    $dataArchive = Get-ChildItem -LiteralPath $gitAr -Filter "data.tar.*" -File
    if (@($dataArchive).Count -ne 1) { throw "Ubuntu Git data archive is not exact." }
    Invoke-CheckedTar @("-xf", $dataArchive.FullName, "-C", $gitData, "./usr/bin/git")
    $gitBinary = Join-Path $gitData "usr/bin/git"
    if (-not (Test-Path -LiteralPath $gitBinary -PathType Leaf)) { throw "Ubuntu Git binary is missing." }
    Copy-Item -LiteralPath $gitBinary -Destination (Join-Path $payload "git")

    foreach ($name in @("install.sh", "idp-egress-policy-apply", "idp-egress-policy-check")) {
        Copy-Item -LiteralPath (Join-Path $bundleAssets $name) -Destination (Join-Path $stage $name)
    }

    $toolPaths = [ordered]@{
        "actions-runner" = Join-Path $runnerProbe "bin/Runner.Listener"
        "cosign" = Join-Path $payload "cosign"
        "docker" = Join-Path (Join-Path $payload "docker") "docker"
        "docker-buildx" = Join-Path $payload "docker-buildx"
        "gh" = Join-Path $payload "gh"
        "git" = Join-Path $payload "git"
        "syft" = Join-Path $payload "syft"
        "trivy" = Join-Path $payload "trivy"
    }
    $installedPaths = @{
        "actions-runner" = "/opt/actions-runner/bin/Runner.Listener"
        "cosign" = "/usr/local/bin/cosign"
        "docker" = "/usr/local/bin/docker"
        "docker-buildx" = "/usr/local/lib/docker/cli-plugins/docker-buildx"
        "gh" = "/usr/local/bin/gh"
        "git" = "/usr/local/bin/git"
        "syft" = "/usr/local/bin/syft"
        "trivy" = "/usr/local/bin/trivy"
    }
    $tools = [ordered]@{}
    foreach ($id in $expectedIds) {
        $sourceRecord = ($sources | Where-Object id -eq $id)
        $tools[$id] = [ordered]@{
            version = [string]$sourceRecord.version
            path = $installedPaths[$id]
            sha256 = (Get-FileHash -LiteralPath $toolPaths[$id] -Algorithm SHA256).Hash.ToLowerInvariant()
        }
    }

    $bundlePath = Join-Path $resolvedOutput $lock.release_asset
    Push-Location $stage
    try { Invoke-CheckedTar @("-czf", $bundlePath, ".") } finally { Pop-Location }
    $bundleSha = (Get-FileHash -LiteralPath $bundlePath -Algorithm SHA256).Hash.ToLowerInvariant()
    $manifest = [ordered]@{
        schema_version = "1.0.0"
        os = "ubuntu-24.04"
        architecture = "x86_64"
        bundle = [ordered]@{
            version = [string]$lock.bundle_version
            url = $releaseUri.AbsoluteUri
            approved_host = $releaseUri.DnsSafeHost
            sha256 = $bundleSha
        }
        tools = $tools
    }
    $manifestPath = Join-Path $resolvedOutput "runner-bundle-manifest.json"
    [IO.File]::WriteAllText($manifestPath, (($manifest | ConvertTo-Json -Depth 8) + "`n"), $utf8NoBom)

    [pscustomobject]@{
        bundle = $bundlePath
        bundle_sha256 = $bundleSha
        manifest = $manifestPath
        source_count = $sources.Count
        tool_count = $tools.Count
        release_tag = $lock.release_tag
        runtime_validated = $false
    } | ConvertTo-Json -Depth 4
}
catch {
    if ($createdOutput -and (Test-Path -LiteralPath $resolvedOutput)) {
        Remove-Item -LiteralPath $resolvedOutput -Recurse -Force
    }
    throw
}
finally {
    if ($createdBuild -and (Test-Path -LiteralPath $resolvedBuild)) {
        Remove-Item -LiteralPath $resolvedBuild -Recurse -Force
    }
}
