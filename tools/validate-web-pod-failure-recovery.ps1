param(
    [switch]$LiveKubectl,
    [string]$Namespace,
    [string]$DeploymentName
)

$ErrorActionPreference="Stop";Set-StrictMode -Version Latest
$repositoryRoot=Split-Path -Parent $PSScriptRoot
$runbookPath=Join-Path $repositoryRoot "runbooks\web-pod-failure-recovery-validation.md"
$commandPath=Join-Path $repositoryRoot "runbooks\web-pod-failure-recovery-commands.example.md"
$criteriaPath=Join-Path $repositoryRoot "runbooks\web-pod-failure-recovery-criteria.example.md"
$evidenceRoot=Join-Path $repositoryRoot "evidence\L4-failure-recovery\S031-web-pod-failure-recovery-validation"
$prePath=Join-Path $evidenceRoot "logs\pre-failure-pods.sample.txt"
$faultPath=Join-Path $evidenceRoot "logs\failure-injection-event.sample.txt"
$postPath=Join-Path $evidenceRoot "logs\post-recovery-pods.sample.txt"
$rolloutPath=Join-Path $evidenceRoot "logs\rollout-status.sample.txt"
$endpointPath=Join-Path $evidenceRoot "logs\service-endpoints-after-recovery.sample.txt"
$logDirectory=Join-Path $evidenceRoot "logs";$configDirectory=Join-Path $evidenceRoot "configs"
$logPath=Join-Path $logDirectory "web-pod-failure-recovery-validation.log"
$summaryPath=Join-Path $configDirectory "web-pod-failure-recovery-summary.md"
$validationMode=if($LiveKubectl){"LiveKubectl"}else{"Static"}

New-Item -ItemType Directory -Force -Path $logDirectory,$configDirectory|Out-Null
$results=[System.Collections.Generic.List[object]]::new();$outputLines=[System.Collections.Generic.List[string]]::new();$criticalFailures=0;$warningCount=0
function Add-ValidationResult{param([string]$Id,[string]$Description,[ValidateSet("PASS","WARN","FAIL")][string]$Result,[string]$Detail);if($Result-eq"FAIL"){$script:criticalFailures++};if($Result-eq"WARN"){$script:warningCount++};$line="[$Result] $Id ${Description}: $Detail";Write-Host $line;$script:outputLines.Add($line)|Out-Null;$script:results.Add([pscustomobject]@{Id=$Id;Description=$Description;Result=$Result;Detail=$Detail})|Out-Null}
function Read-Artifact{param([string]$Path);if(Test-Path -LiteralPath $Path -PathType Leaf){return Get-Content -LiteralPath $Path -Raw};return ""}
function Get-DataRows{param([string]$Content,[string]$HeaderPattern);return @($Content-split'\r?\n'|ForEach-Object{$_.Trim()}|Where-Object{$_-and$_-notmatch'^(?:SAMPLE /|Original_Pod_State:)'-and$_-notmatch$HeaderPattern})}

$baselinePaths=@($runbookPath,$commandPath,$criteriaPath);$missingBaseline=@($baselinePaths|Where-Object{-not(Test-Path -LiteralPath $_ -PathType Leaf)})
Add-ValidationResult "V001" "Required recovery baseline files" $(if($missingBaseline.Count-eq 0){"PASS"}else{"FAIL"}) $(if($missingBaseline.Count-eq 0){"Runbook, command reference, and criteria matrix exist."}else{"One or more recovery baseline files are missing."})
$runbookContent=Read-Artifact $runbookPath;$commandContent=Read-Artifact $commandPath;$criteriaContent=Read-Artifact $criteriaPath;$preContent=Read-Artifact $prePath;$faultContent=Read-Artifact $faultPath;$postContent=Read-Artifact $postPath;$rolloutContent=Read-Artifact $rolloutPath;$endpointContent=Read-Artifact $endpointPath
$combinedContent=@($runbookContent,$commandContent,$criteriaContent,$preContent,$faultContent,$postContent,$rolloutContent,$endpointContent)-join"`n"

$samplePaths=@($prePath,$faultPath,$postPath,$rolloutPath,$endpointPath);$missingSamples=@($samplePaths|Where-Object{-not(Test-Path -LiteralPath $_ -PathType Leaf)})
Add-ValidationResult "V002" "Required recovery samples" $(if($missingSamples.Count-eq 0){"PASS"}else{"FAIL"}) $(if($missingSamples.Count-eq 0){"Pre-failure, fault, post-recovery, rollout, and endpoint samples exist."}else{"One or more recovery samples are missing."})

$runbookTerms=@('<namespace>','<deployment-name>','<pod-name>','<replacement-pod-name>','<replica-count>','<recovery-time-threshold-seconds>','<service-name>','<endpoint-url-placeholder>','<evidence-path>','Pre-failure','Failure injection','Replacement','Ready','Rollout','Service','Static mode','LiveKubectl');$missingRunbook=@($runbookTerms|Where-Object{$runbookContent-notmatch[regex]::Escape($_)})
Add-ValidationResult "V003" "Recovery workflow documentation" $(if($missingRunbook.Count-eq 0){"PASS"}else{"FAIL"}) $(if($missingRunbook.Count-eq 0){"Controlled failure, replacement, readiness, rollout, endpoint, timing, and mode boundaries are documented."}else{"Recovery runbook is incomplete."})

$phases=@('Pre-failure deployment state','Pre-failure pod readiness','Fault injection event','Failed pod termination','Replacement pod creation','Replacement pod Ready state','Deployment replica consistency','Rollout status','Service endpoint continuity','Recovery time threshold');$missingPhases=@($phases|Where-Object{$criteriaContent-notmatch[regex]::Escape($_)});$criteriaReady=$missingPhases.Count-eq 0-and$criteriaContent-match'Recovery Phase'-and$criteriaContent-match'Operational Judgment'-and$criteriaContent-match'Evidence Reference'
Add-ValidationResult "V004" "Recovery criteria matrix" $(if($criteriaReady){"PASS"}else{"FAIL"}) $(if($criteriaReady){"All ten recovery phases and required columns exist."}else{"Recovery criteria matrix is incomplete."})

$requiredReadOnly=@('kubectl get deployment <deployment-name> -n <namespace>','kubectl get pods -n <namespace> -l app=<app-label-placeholder>','kubectl describe pod <pod-name> -n <namespace>','kubectl rollout status deployment/<deployment-name> -n <namespace>','kubectl get endpoints <service-name> -n <namespace>');$missingCommands=@($requiredReadOnly|Where-Object{$commandContent-notmatch[regex]::Escape($_)});$manualDeleteReady=$commandContent-match'MANUAL FAULT INJECTION ONLY'-and$commandContent-match[regex]::Escape('kubectl delete pod <pod-name> -n <namespace>')-and$commandContent-match'delete command is never executed by the validator'-and$commandContent-match'disposable lab namespace'
Add-ValidationResult "V005" "Command and manual fault boundary" $(if($missingCommands.Count-eq 0-and$manualDeleteReady){"PASS"}else{"FAIL"}) $(if($missingCommands.Count-eq 0-and$manualDeleteReady){"Read-only references exist and Pod deletion is manual disposable-lab-only."}else{"Command references or manual fault boundary are incomplete."})

$preRows=Get-DataRows $preContent '^NAME\s+READY';$preHealthy=@($preRows|Where-Object{$_-match'\s1/1\s' -and $_-match'\sRunning\s'}).Count-ge 1
Add-ValidationResult "V006" "Pre-failure Pod evidence" $(if($preHealthy){"PASS"}else{"FAIL"}) $(if($preHealthy){"At least one pre-failure Pod is Running and Ready 1/1."}else{"Pre-failure healthy Pod evidence is missing."})

$manualFaultReady=$faultContent-match'SAMPLE / NON-PRODUCTION'-and$faultContent-match'MANUAL FAULT INJECTION SAMPLE'-and$faultContent-match[regex]::Escape('kubectl delete pod sample-web-placeholder-abcde -n snsd-example')-and$faultContent-match'pod deleted placeholder'
Add-ValidationResult "V007" "Manual fault injection evidence" $(if($manualFaultReady){"PASS"}else{"FAIL"}) $(if($manualFaultReady){"The sample is explicitly manual, non-production, and placeholder-only."}else{"Manual fault sample is missing or ambiguously marked."})

$postRows=Get-DataRows $postContent '^NAME\s+READY';$replacementReady=@($postRows|Where-Object{$_-match'^sample-web-placeholder-klmno\s' -and $_-match'\s1/1\s' -and $_-match'\sRunning\s'}).Count-eq 1;$originalInactive=$postContent-match'Original_Pod_State:\s*sample-web-placeholder-abcde\s+no-longer-active'
Add-ValidationResult "V008" "Replacement Pod recovery evidence" $(if($replacementReady-and$originalInactive){"PASS"}else{"FAIL"}) $(if($replacementReady-and$originalInactive){"Original is inactive and the replacement is Running/Ready."}else{"Replacement Pod or original termination evidence is missing."})

$rolloutReady=$rolloutContent-match'SAMPLE / NON-PRODUCTION'-and$rolloutContent-match'deployment "sample-web-placeholder" successfully rolled out'
Add-ValidationResult "V009" "Rollout status evidence" $(if($rolloutReady){"PASS"}else{"FAIL"}) $(if($rolloutReady){"The deployment successfully rolled out."}else{"Successful rollout evidence is missing."})

$endpointRows=Get-DataRows $endpointContent '^NAME\s+ENDPOINTS';$endpointReady=@($endpointRows|Where-Object{$_-match'^sample-service-placeholder\s' -and $_-match'<pod-ip-placeholder>:80' -and $_-notmatch'(?i)<none>'}).Count-eq 1
Add-ValidationResult "V010" "Service endpoint continuity evidence" $(if($endpointReady){"PASS"}else{"FAIL"}) $(if($endpointReady){"The service has a symbolic non-empty endpoint after recovery."}else{"Endpoint evidence is empty, missing, or unsanitized."})

$elapsedMatch=[regex]::Match($faultContent,'(?im)^Recovery_Elapsed_Seconds:[ \t]*(\d+(?:\.\d+)?)\s*$');$timingResult=if($elapsedMatch.Success){"PASS"}else{"WARN"};$timingDetail=if($elapsedMatch.Success){"A numeric sanitized elapsed time is available for threshold review."}else{"Elapsed time is not measured in this sample; recovery-time compliance remains unproven."}
Add-ValidationResult "V011" "Recovery time evidence" $timingResult $timingDetail

$unhealthyPattern='(?i)CrashLoopBackOff|ImagePullBackOff|ErrImagePull|\bFailed\b|\bPending\b|\bUnknown\b|\b0/1\b';$postSafe=$postContent-notmatch$unhealthyPattern-and$endpointContent-notmatch'(?i)<none>'
Add-ValidationResult "V012" "Post-recovery failure indicators" $(if($postSafe){"PASS"}else{"FAIL"}) $(if($postSafe){"No failed/Pending/Unknown/image/restart-readiness or empty-endpoint indicator exists."}else{"Unhealthy post-recovery state was detected."})

$forbiddenFiles=@(Get-ChildItem -LiteralPath $repositoryRoot -Recurse -File -Force -ErrorAction SilentlyContinue|Where-Object{$_.FullName-notmatch'[\\/]\.git[\\/]'-and$_.Name-match'(?i)(^|\.)kubeconfig($|\.)|service[-_]?account.*token|\.crt$|\.cer$|\.pem$|\.key$|\.p12$|\.pfx$'})
Add-ValidationResult "V013" "Kubernetes credential file safety" $(if($forbiddenFiles.Count-eq 0){"PASS"}else{"FAIL"}) $(if($forbiddenFiles.Count-eq 0){"No kubeconfig, token, certificate, or private-key file exists."}else{"A forbidden Kubernetes/TLS file was detected."})

$ipMatches=@([regex]::Matches($combinedContent,'(?<![A-Za-z0-9<])(?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?(?![A-Za-z0-9>])'));$domains=@([regex]::Matches($combinedContent,'(?i)(?<![A-Za-z0-9<.-])(?:[a-z0-9-]+\.)+[a-z]{2,}(?![A-Za-z0-9>.-])')|ForEach-Object{$_.Value.ToLowerInvariant()});$unexpectedDomains=@($domains|Where-Object{$_-notmatch'\.(?:md|txt|ps1)$'}|Sort-Object -Unique);$urls=@([regex]::Matches($combinedContent,'(?i)https?://(?!<)[^\s"`]+'));$secretHit=$combinedContent-match'(?im)^\s*(?:token|password|secret|authorization|client-key-data|client-certificate-data)\s*[:=]\s*(?!["'']?<)\S+'-or$combinedContent-match'-----BEGIN (?:CERTIFICATE|(?:[A-Z ]+ )?PRIVATE KEY)-----';$contentSafe=$ipMatches.Count-eq 0-and$unexpectedDomains.Count-eq 0-and$urls.Count-eq 0-and-not$secretHit
Add-ValidationResult "V014" "Cluster endpoint and secret safety" $(if($contentSafe){"PASS"}else{"FAIL"}) $(if($contentSafe){"No real endpoint, domain, address, Pod/Node IP, token, certificate, key, or secret exists."}else{"Concrete cluster or sensitive content was detected."})

$scriptContent=Get-Content -LiteralPath $PSCommandPath -Raw;$requiredArgumentPatterns=@('\$deploymentArgs\s*=\s*@\("get","deployment",\$DeploymentName,"-n",\$Namespace\)','\$podArgs\s*=\s*@\("get","pods","-n",\$Namespace\)','\$rolloutArgs\s*=\s*@\("rollout","status","deployment/\$DeploymentName","-n",\$Namespace\)','\$endpointArgs\s*=\s*@\("get","endpoints","-n",\$Namespace\)');$missingArgumentPatterns=@($requiredArgumentPatterns|Where-Object{$scriptContent-notmatch$_});$prohibitedInvocation=$scriptContent-match'(?im)^\s*(?:&\s*)?kubectl\s+(?:delete|apply|patch|edit|scale|restart|cordon|drain|taint)\b';$executionSafe=$missingArgumentPatterns.Count-eq 0-and-not$prohibitedInvocation
Add-ValidationResult "V015" "Execution safety boundary" $(if($executionSafe){"PASS"}else{"FAIL"}) $(if($executionSafe){"Live mode contains four read-only argument sets and no destructive kubectl invocation."}else{"Read-only command guards are incomplete or destructive automation exists."})

$liveResult="PASS";$liveDetail="Static mode completed without kubectl, cluster access, Pod deletion, or resource mutation.";$sanitizedLive=@("NOT_RUN")
if($LiveKubectl){
 if([string]::IsNullOrWhiteSpace($Namespace)-or[string]::IsNullOrWhiteSpace($DeploymentName)){$liveResult="FAIL";$liveDetail="LiveKubectl requires Namespace and DeploymentName; no command was run.";$sanitizedLive=@("MISSING_PARAMETERS")}
 else{$kubectl=Get-Command kubectl -CommandType Application -ErrorAction SilentlyContinue;if($null-eq$kubectl){$liveResult="FAIL";$liveDetail="kubectl is unavailable; no cluster query was run.";$sanitizedLive=@("KUBECTL_MISSING")}
  else{$deploymentArgs=@("get","deployment",$DeploymentName,"-n",$Namespace);$podArgs=@("get","pods","-n",$Namespace);$rolloutArgs=@("rollout","status","deployment/$DeploymentName","-n",$Namespace);$endpointArgs=@("get","endpoints","-n",$Namespace)
   $deploymentOutput=@(&$kubectl.Source @deploymentArgs 2>&1);$dExit=$LASTEXITCODE;$podOutput=@(&$kubectl.Source @podArgs 2>&1);$pExit=$LASTEXITCODE;$rolloutOutput=@(&$kubectl.Source @rolloutArgs 2>&1);$rExit=$LASTEXITCODE;$endpointOutput=@(&$kubectl.Source @endpointArgs 2>&1);$eExit=$LASTEXITCODE
   if(@(@($dExit,$pExit,$rExit,$eExit)|Where-Object{$_-ne 0}).Count-gt 0){$liveResult="FAIL";$liveDetail="A read-only kubectl query failed; raw output was not stored.";$sanitizedLive=@("QUERY_FAILED")}
   else{$deploymentText=$deploymentOutput-join"`n";$podText=$podOutput-join"`n";$rolloutText=$rolloutOutput-join"`n";$endpointText=$endpointOutput-join"`n";$readyPods=@($podOutput|ForEach-Object{"$_"}|Where-Object{$_-match'\s\d+/\d+\s+Running\s'-and$_-notmatch'\s0/\d+\s'}).Count;$rolloutOk=$rolloutText-match'successfully rolled out';$endpointRowsLive=@($endpointOutput|ForEach-Object{"$_"}|Where-Object{$_-and$_-notmatch'^NAME\s'-and$_-notmatch'(?i)<none>'}).Count;$deploymentFound=$deploymentText-match[regex]::Escape($DeploymentName);$sanitizedLive=@("deployment-found=$deploymentFound","ready-running-pods=$readyPods","rollout-success=$rolloutOk","nonempty-endpoint-rows=$endpointRowsLive");if($deploymentFound-and$readyPods-gt 0-and$rolloutOk-and$endpointRowsLive-gt 0){$liveDetail="Read-only deployment, Pod, rollout, and endpoint judgments are healthy; raw details were not stored."}else{$liveResult="FAIL";$liveDetail="Live read-only recovery state is unhealthy; raw details were not stored."}}
  }
 }
}
Add-ValidationResult "V016" "Validation mode and live recovery state" $liveResult $liveDetail

$timestamp=(Get-Date).ToString("yyyy-MM-ddTHH:mm:ssK");$overallResult=if($criticalFailures-eq 0){"PASS"}else{"FAIL"};$overallLine="[$overallResult] Web Pod failure recovery ($validationMode): $criticalFailures critical failure(s), $warningCount warning(s).";Write-Host $overallLine
@("SNSD Multi-Cloud Ops - S031 Web Pod Failure Recovery Validation","Generated: $timestamp","Validation mode: $validationMode","Sanitized live findings: $($sanitizedLive-join', ')","")+@($outputLines)+@("",$overallLine,"No kubeconfig, token, certificate, key, cluster endpoint, IP, UID, raw live row, or secret was stored; no Pod was deleted by the validator.")|Set-Content -LiteralPath $logPath -Encoding UTF8
$requiredFileCheck=$missingBaseline.Count-eq 0-and$missingSamples.Count-eq 0;$secretSafety=$forbiddenFiles.Count-eq 0-and$contentSafe
$summaryLines=[System.Collections.Generic.List[string]]::new();$summaryLines.Add("# Web Pod Failure Recovery Summary")|Out-Null;$summaryLines.Add("")|Out-Null;$summaryLines.Add("- Scenario: S031-web-pod-failure-recovery-validation")|Out-Null;$summaryLines.Add("- Generated: $timestamp")|Out-Null;$summaryLines.Add("- Validation mode: **$validationMode**")|Out-Null;$summaryLines.Add("- Required file check result: **$(if($requiredFileCheck){'PASS'}else{'FAIL'})**")|Out-Null;$summaryLines.Add("- Pre-failure Pod evidence result: **$(if($preHealthy){'PASS'}else{'FAIL'})**")|Out-Null;$summaryLines.Add("- Manual fault injection evidence result: **$(if($manualFaultReady){'PASS'}else{'FAIL'})**")|Out-Null;$summaryLines.Add("- Post-recovery Pod evidence result: **$(if($replacementReady-and$originalInactive){'PASS'}else{'FAIL'})**")|Out-Null;$summaryLines.Add("- Rollout status result: **$(if($rolloutReady){'PASS'}else{'FAIL'})**")|Out-Null;$summaryLines.Add("- Endpoint continuity evidence result: **$(if($endpointReady){'PASS'}else{'FAIL'})**")|Out-Null;$summaryLines.Add("- Recovery time threshold documentation result: **$(if($runbookContent-match'<recovery-time-threshold-seconds>'){'PASS'}else{'FAIL'})**")|Out-Null;$summaryLines.Add("- Secret-safety check result: **$(if($secretSafety){'PASS'}else{'FAIL'})**")|Out-Null;$summaryLines.Add("- Final judgment: **$overallResult**")|Out-Null;$summaryLines.Add("")|Out-Null;$summaryLines.Add("| Check ID | Check | Result | Detail |")|Out-Null;$summaryLines.Add("|---|---|---|---|")|Out-Null;foreach($result in $results){$detail=$result.Detail.Replace("|","\|");$summaryLines.Add("| $($result.Id) | $($result.Description) | $($result.Result) | $detail |")|Out-Null};$summaryLines|Set-Content -LiteralPath $summaryPath -Encoding UTF8
if($criticalFailures-gt 0){exit 1};exit 0
