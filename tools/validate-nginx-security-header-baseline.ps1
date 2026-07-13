$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

$repositoryRoot = Split-Path -Parent $PSScriptRoot
$baselinePath = Join-Path $repositoryRoot "security-baseline\nginx-security-header-baseline.md"
$matrixPath = Join-Path $repositoryRoot "security-baseline\nginx-security-header-rule-matrix.example.md"
$configPath = Join-Path $repositoryRoot "traffic-management\nginx-security-headers.example.conf"
$evidenceRoot = Join-Path $repositoryRoot "evidence\L2-security-baseline\S019-nginx-security-header-validation"
$logDirectory = Join-Path $evidenceRoot "logs"
$configDirectory = Join-Path $evidenceRoot "configs"
$logPath = Join-Path $logDirectory "nginx-security-header-validation.log"
$summaryPath = Join-Path $configDirectory "nginx-security-header-summary.md"

$requiredHeaders = @(
    "X-Frame-Options", "X-Content-Type-Options", "Referrer-Policy",
    "Content-Security-Policy", "Strict-Transport-Security", "Permissions-Policy"
)
$requiredMatrixEntries = @("server_tokens") + $requiredHeaders
$requiredBaselineTerms = @(
    'X-XSS-Protection', 'legacy compatibility', 'Server token exposure',
    'Header Validation Evidence Model', 'Limitations of Static Config Validation',
    '<public-service-domain>', '<reverse-proxy-host>', '<backend-service>',
    '<tls-termination-point>', '<evidence-path>'
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
Add-ValidationResult "V001" "Security header baseline" $(if ($baselineExists) { "PASS" } else { "FAIL" }) $(if ($baselineExists) { "Baseline document exists." } else { "Baseline document is missing." })

$matrixExists = Test-Path -LiteralPath $matrixPath -PathType Leaf
Add-ValidationResult "V002" "Security header rule matrix" $(if ($matrixExists) { "PASS" } else { "FAIL" }) $(if ($matrixExists) { "Rule matrix exists." } else { "Rule matrix is missing." })

$configExists = Test-Path -LiteralPath $configPath -PathType Leaf
Add-ValidationResult "V003" "Nginx example config" $(if ($configExists) { "PASS" } else { "FAIL" }) $(if ($configExists) { "Non-production config example exists." } else { "Config example is missing." })

$baselineContent = if ($baselineExists) { Get-Content -LiteralPath $baselinePath -Raw } else { "" }
$matrixContent = if ($matrixExists) { Get-Content -LiteralPath $matrixPath -Raw } else { "" }
$configContent = if ($configExists) { Get-Content -LiteralPath $configPath -Raw } else { "" }
$combinedContent = @($baselineContent, $matrixContent, $configContent) -join "`n"

$serverTokensReady = $configContent -match '(?im)^\s*server_tokens\s+off\s*;\s*$'
Add-ValidationResult "V004" "Server token reduction" $(if ($serverTokensReady) { "PASS" } else { "FAIL" }) $(if ($serverTokensReady) { "server_tokens off is present." } else { "server_tokens off is missing." })

$missingHeaders = @($requiredHeaders | Where-Object { $configContent -notmatch "(?im)^\s*add_header\s+$([regex]::Escape($_))\s+" })
Add-ValidationResult "V005" "Required security headers" $(if ($missingHeaders.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingHeaders.Count -eq 0) { "All six required add_header directives exist." } else { "Missing headers: " + ($missingHeaders -join ", ") })

$valueChecks = @(
    '(?im)^\s*add_header\s+X-Frame-Options\s+"SAMEORIGIN"\s+always\s*;\s*$',
    '(?im)^\s*add_header\s+X-Content-Type-Options\s+"nosniff"\s+always\s*;\s*$',
    '(?im)^\s*add_header\s+Referrer-Policy\s+"strict-origin-when-cross-origin"\s+always\s*;\s*$',
    '(?im)^\s*add_header\s+Content-Security-Policy\s+"<content-security-policy-placeholder>"\s+always\s*;\s*$',
    '(?im)^\s*add_header\s+Strict-Transport-Security\s+"max-age=31536000; includeSubDomains"\s+always\s*;\s*$',
    '(?im)^\s*add_header\s+Permissions-Policy\s+"<permissions-policy-placeholder>"\s+always\s*;\s*$'
)
$missingValues = @($valueChecks | Where-Object { $configContent -notmatch $_ })
Add-ValidationResult "V006" "Required header values" $(if ($missingValues.Count -eq 0) { "PASS" } else { "FAIL" }) $(if ($missingValues.Count -eq 0) { "All required values and placeholders are exact." } else { "One or more required header values is missing or changed." })

$headerLines = @($configContent -split "`r?`n" | Where-Object { $_ -match '(?i)^\s*add_header\s+' })
$missingAlways = @($headerLines | Where-Object { $_ -notmatch '(?i)\s+always\s*;\s*$' })
$alwaysReady = $headerLines.Count -eq 6 -and $missingAlways.Count -eq 0
Add-ValidationResult "V007" "Always directive" $(if ($alwaysReady) { "PASS" } else { "FAIL" }) $(if ($alwaysReady) { "All six security headers use always." } else { "A security add_header directive is missing always or an unexpected directive exists." })

$missingMatrixEntries = @($requiredMatrixEntries | Where-Object { $matrixContent -notmatch [regex]::Escape($_) })
$missingBaselineTerms = @($requiredBaselineTerms | Where-Object { $baselineContent -notmatch [regex]::Escape($_) })
$documentationReady = $missingMatrixEntries.Count -eq 0 -and $missingBaselineTerms.Count -eq 0
Add-ValidationResult "V008" "Baseline and matrix completeness" $(if ($documentationReady) { "PASS" } else { "FAIL" }) $(if ($documentationReady) { "All matrix entries, placeholders, legacy note, evidence model, and static limitations exist." } else { "Required baseline or matrix content is incomplete." })

$tlsPathHit = $configContent -match '(?im)^\s*(?:ssl_certificate|ssl_certificate_key)\s+' -or $configContent -match '(?i)(?:/etc/letsencrypt|\.pem\b|\.key\b|\.crt\b|\.cer\b)'
$privateMaterialHit = $combinedContent -match '-----BEGIN (?:[A-Z ]+ )?PRIVATE KEY-----'
$tlsSafe = -not $tlsPathHit -and -not $privateMaterialHit
Add-ValidationResult "V009" "TLS material safety" $(if ($tlsSafe) { "PASS" } else { "FAIL" }) $(if ($tlsSafe) { "No certificate path, private-key path, or private material exists." } else { "TLS path or private material was detected." })

$ipMatches = @([regex]::Matches($combinedContent, '(?<![A-Za-z0-9<])((?:\d{1,3}\.){3}\d{1,3})(?:/\d{1,2})?(?![A-Za-z0-9>])'))
$domainMatches = @([regex]::Matches($combinedContent, '(?i)(?<![A-Za-z0-9<.-])(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+(?:com|net|org|io|co|kr|cloud|dev)(?![A-Za-z0-9>.-])'))
$addressSafe = $ipMatches.Count -eq 0 -and $domainMatches.Count -eq 0
Add-ValidationResult "V010" "Address and domain safety" $(if ($addressSafe) { "PASS" } else { "FAIL" }) $(if ($addressSafe) { "No numeric address or real-looking domain is hardcoded." } else { "A numeric address or real-looking domain was detected." })

$credentialHit = $combinedContent -match '(?im)^\s*(?:password|passwd|secret|token|credential|api[_-]?key)\s*[:=]\s*(?!["'']?<)\S+' -or
    $combinedContent -match '(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b'
Add-ValidationResult "V011" "Credential and account safety" $(if (-not $credentialHit) { "PASS" } else { "FAIL" }) $(if (-not $credentialHit) { "No credential, secret assignment, or account-specific identifier exists." } else { "Credential-like or account-specific content was detected." })

$scriptContent = Get-Content -LiteralPath $PSCommandPath -Raw
$activeCommandPatterns = @(
    '(?im)^\s*(?:&\s*)?nginx\b',
    '(?im)^\s*(?:&\s*)?curl\b',
    '(?im)^\s*(?:Invoke-WebRequest|Invoke-RestMethod|Test-NetConnection)\b',
    '(?im)^\s*(?:ssh|scp)\b'
)
$activeCommandHit = $false
foreach ($pattern in $activeCommandPatterns) { if ($scriptContent -match $pattern) { $activeCommandHit = $true; break } }
Add-ValidationResult "V012" "Execution safety boundary" $(if (-not $activeCommandHit) { "PASS" } else { "FAIL" }) $(if (-not $activeCommandHit) { "The validator contains no Nginx, curl, host, or network execution command." } else { "A prohibited live execution command was detected." })

$timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK")
$overallResult = if ($criticalFailures -eq 0) { "PASS" } else { "FAIL" }
$overallLine = "[$overallResult] Repository-side Nginx security header baseline: $criticalFailures critical failure(s)."
Write-Host $overallLine

$logLines = @(
    "SNSD Multi-Cloud Ops - S019 Nginx Security Header Validation"
    "Generated: $timestamp"
    "Scope: repository baseline, rule matrix, config example, and safety checks only"
    ""
) + @($outputLines) + @(
    ""
    $overallLine
    "No Nginx execution, reload, config modification, curl, host connection, live response validation, TLS access, or network operation was performed."
)
$logLines | Set-Content -LiteralPath $logPath -Encoding UTF8

$summaryLines = [System.Collections.Generic.List[string]]::new()
$summaryLines.Add("# Nginx Security Header Summary") | Out-Null
$summaryLines.Add("") | Out-Null
$summaryLines.Add("- Scenario: S019-nginx-security-header-validation") | Out-Null
$summaryLines.Add("- Generated: $timestamp") | Out-Null
$summaryLines.Add("- Overall result: **$overallResult**") | Out-Null
$summaryLines.Add("- Scope: local policy, matrix, example config, and safety checks") | Out-Null
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
$summaryLines.Add("This validation read repository files only. It did not run or reload Nginx, modify configuration, curl an endpoint, connect to a host, or validate live HTTP/TLS behavior.") | Out-Null
$summaryLines | Set-Content -LiteralPath $summaryPath -Encoding UTF8

if ($criticalFailures -gt 0) { exit 1 }
exit 0
