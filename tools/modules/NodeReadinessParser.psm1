Set-StrictMode -Version Latest

function ConvertFrom-NodeStatusEvidence {
    [CmdletBinding()]
    param(
        [AllowNull()]
        [AllowEmptyCollection()]
        [object[]] $Lines
    )

    $nodes = [System.Collections.Generic.List[object]]::new()
    $malformedRecords = [System.Collections.Generic.List[object]]::new()
    $inputLines = if ($null -eq $Lines) { [object[]]@() } else { [object[]]$Lines }
    $lineNumber = 0

    foreach ($lineValue in $inputLines) {
        $lineNumber++
        if ($null -eq $lineValue) {
            $malformedRecords.Add([pscustomobject]@{
                LineNumber = $lineNumber
                Reason = 'NULL_RECORD'
            }) | Out-Null
            continue
        }

        $trimmed = ([string]$lineValue).Trim()
        if (-not $trimmed -or $trimmed -match '^(?:SAMPLE|NON-PRODUCTION|#)' -or $trimmed -match '^NAME\s+STATUS') {
            continue
        }

        $columns = [string[]]@($trimmed -split '\s+')
        if ($columns.Count -lt 2) {
            $malformedRecords.Add([pscustomobject]@{
                LineNumber = $lineNumber
                Reason = 'MISSING_STATUS_COLUMN'
            }) | Out-Null
            continue
        }

        $status = $columns[1]
        if ($status -notmatch '^(?i:(?:Ready|NotReady|Unknown)(?:,SchedulingDisabled)?)$') {
            $malformedRecords.Add([pscustomobject]@{
                LineNumber = $lineNumber
                Reason = 'INVALID_STATUS_VALUE'
            }) | Out-Null
            continue
        }

        $nodes.Add([pscustomobject]@{
            Name = $columns[0]
            Status = $status
        }) | Out-Null
    }

    return [pscustomobject]@{
        Nodes = [object[]]$nodes.ToArray()
        MalformedRecords = [object[]]$malformedRecords.ToArray()
        NodeCount = $nodes.Count
        MalformedCount = $malformedRecords.Count
        IsValid = $malformedRecords.Count -eq 0
        InputWasNull = $null -eq $Lines
    }
}

Export-ModuleMember -Function ConvertFrom-NodeStatusEvidence
