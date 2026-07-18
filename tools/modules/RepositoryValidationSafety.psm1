Set-StrictMode -Version Latest

function Get-Sha256Text {
    param([AllowEmptyString()][string] $Text)

    $sha256 = [System.Security.Cryptography.SHA256]::Create()
    try {
        $bytes = [System.Text.Encoding]::UTF8.GetBytes($Text)
        return ([System.BitConverter]::ToString($sha256.ComputeHash($bytes))).Replace('-', '').ToLowerInvariant()
    }
    finally {
        $sha256.Dispose()
    }
}

function Get-RepositoryStateSnapshot {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string] $RepositoryRoot
    )

    $resolvedRoot = (Resolve-Path -LiteralPath $RepositoryRoot).Path
    $statusLines = @(& git -c core.quotePath=false -C $resolvedRoot status --porcelain=v1 --untracked-files=all)
    if ($LASTEXITCODE -ne 0) {
        throw "Unable to capture Git status for repository: $resolvedRoot"
    }

    $entries = [System.Collections.Generic.List[object]]::new()
    foreach ($line in $statusLines) {
        if ([string]::IsNullOrWhiteSpace($line) -or $line.Length -lt 4) {
            continue
        }

        $gitState = $line.Substring(0, 2)
        $relativePath = $line.Substring(3).Trim('"')
        if ($relativePath -match ' -> ') {
            $relativePath = ($relativePath -split ' -> ')[-1].Trim('"')
        }

        $fullPath = Join-Path $resolvedRoot $relativePath
        if (Test-Path -LiteralPath $fullPath -PathType Leaf) {
            $item = Get-Item -LiteralPath $fullPath
            $hash = (Get-FileHash -LiteralPath $fullPath -Algorithm SHA256).Hash.ToLowerInvariant()
            $length = $item.Length
            $lastWriteTimeUtc = $item.LastWriteTimeUtc.ToString('o')
        }
        else {
            $hash = 'MISSING'
            $length = -1
            $lastWriteTimeUtc = 'MISSING'
        }

        $entries.Add([pscustomobject]@{
            Path = $relativePath.Replace('\', '/')
            GitState = $gitState
            Length = $length
            LastWriteTimeUtc = $lastWriteTimeUtc
            Sha256 = $hash
        }) | Out-Null
    }

    $canonicalLines = @($entries | Sort-Object Path, GitState | ForEach-Object {
        '{0}|{1}|{2}|{3}|{4}' -f $_.GitState, $_.Path, $_.Length, $_.LastWriteTimeUtc, $_.Sha256
    })
    $trackedModifiedCount = @($entries | Where-Object { $_.GitState -ne '??' }).Count
    $untrackedCount = @($entries | Where-Object { $_.GitState -eq '??' }).Count
    $stagedCount = @($entries | Where-Object {
        $_.GitState[0] -ne ' ' -and $_.GitState[0] -ne '?' -and $_.GitState[0] -ne '!'
    }).Count

    return [pscustomobject]@{
        RepositoryRoot = $resolvedRoot
        Entries = [object[]]$entries.ToArray()
        TrackedModifiedCount = $trackedModifiedCount
        UntrackedCount = $untrackedCount
        StagedCount = $stagedCount
        Fingerprint = Get-Sha256Text -Text ($canonicalLines -join "`n")
    }
}

function Compare-RepositoryStateSnapshot {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [psobject] $Before,

        [Parameter(Mandatory)]
        [psobject] $After
    )

    $beforeByPath = @{}
    foreach ($entry in $Before.Entries) {
        $beforeByPath[$entry.Path] = $entry
    }
    $afterByPath = @{}
    foreach ($entry in $After.Entries) {
        $afterByPath[$entry.Path] = $entry
    }

    $allPaths = @($beforeByPath.Keys + $afterByPath.Keys | Sort-Object -Unique)
    $differences = [System.Collections.Generic.List[object]]::new()
    foreach ($path in $allPaths) {
        $hasBefore = $beforeByPath.ContainsKey($path)
        $hasAfter = $afterByPath.ContainsKey($path)
        if (-not $hasBefore) {
            $differences.Add([pscustomobject]@{ Path = $path; Change = 'ADDED' }) | Out-Null
            continue
        }
        if (-not $hasAfter) {
            $differences.Add([pscustomobject]@{ Path = $path; Change = 'REMOVED' }) | Out-Null
            continue
        }

        $beforeEntry = $beforeByPath[$path]
        $afterEntry = $afterByPath[$path]
        if (
            $beforeEntry.GitState -ne $afterEntry.GitState -or
            $beforeEntry.Length -ne $afterEntry.Length -or
            $beforeEntry.LastWriteTimeUtc -ne $afterEntry.LastWriteTimeUtc -or
            $beforeEntry.Sha256 -ne $afterEntry.Sha256
        ) {
            $differences.Add([pscustomobject]@{ Path = $path; Change = 'CHANGED' }) | Out-Null
        }
    }

    return [pscustomobject]@{
        Unchanged = $Before.Fingerprint -eq $After.Fingerprint -and $differences.Count -eq 0
        Differences = [object[]]$differences.ToArray()
        BeforeFingerprint = $Before.Fingerprint
        AfterFingerprint = $After.Fingerprint
    }
}

function Assert-RepositoryStateUnchanged {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [psobject] $Before,

        [Parameter(Mandatory)]
        [psobject] $After
    )

    $comparison = Compare-RepositoryStateSnapshot -Before $Before -After $After
    if (-not $comparison.Unchanged) {
        $paths = @($comparison.Differences | ForEach-Object { "$($_.Change):$($_.Path)" })
        throw "Repository state changed during read-only validation: $($paths -join ', ')"
    }
    return $comparison
}

Export-ModuleMember -Function Get-RepositoryStateSnapshot, Compare-RepositoryStateSnapshot, Assert-RepositoryStateUnchanged
