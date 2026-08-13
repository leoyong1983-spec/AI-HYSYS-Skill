param(
    [string]$RepoRoot = (Split-Path -Parent $PSScriptRoot),
    [string]$Destination = (Join-Path $env:USERPROFILE ".codex\skills\ai-hysys-basic-package"),
    [string]$StateRoot = (Join-Path (Split-Path -Parent $PSScriptRoot) "downloads\local-skill-sync"),
    [switch]$AllowBootstrapOverwrite
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Get-Sha256([string]$Path) {
    return (Get-FileHash -LiteralPath $Path -Algorithm SHA256).Hash.ToLowerInvariant()
}

function Get-RelativePath([string]$Root, [string]$Path) {
    $rootFull = (Resolve-Path -LiteralPath $Root).Path.TrimEnd("\")
    $pathFull = (Resolve-Path -LiteralPath $Path).Path
    $prefix = $rootFull + "\"
    if (-not $pathFull.StartsWith($prefix, [System.StringComparison]::OrdinalIgnoreCase)) {
        throw "Path is outside the payload root: $pathFull"
    }
    return $pathFull.Substring($prefix.Length).Replace("\", "/")
}

git -C $RepoRoot fetch origin main | Out-Null
if ($LASTEXITCODE -ne 0) {
    throw "Failed to fetch origin/main."
}

$sourceCommit = (git -C $RepoRoot rev-parse origin/main).Trim()
if (-not $sourceCommit) {
    throw "Could not resolve origin/main."
}

$stamp = Get-Date -Format "yyyyMMdd-HHmmss"
$stagingRoot = Join-Path $StateRoot "staging\$stamp"
$payloadRoot = Join-Path $stagingRoot "payload"
$backupRoot = Join-Path $StateRoot "backups\$stamp"
$manifestPath = Join-Path $StateRoot "manifest.json"
$archivePath = Join-Path $stagingRoot "payload.zip"

New-Item -ItemType Directory -Force -Path $payloadRoot, $backupRoot | Out-Null

git -C $RepoRoot archive --format=zip --output=$archivePath origin/main SKILL.md agents references scripts
if ($LASTEXITCODE -ne 0) {
    throw "Failed to archive the runtime payload from origin/main."
}
Expand-Archive -LiteralPath $archivePath -DestinationPath $payloadRoot -Force

$sourceRecords = @(
    Get-ChildItem -LiteralPath $payloadRoot -Recurse -File |
        Where-Object {
            $_.FullName -notmatch "[\\/]__pycache__[\\/]" -and
            $_.Extension -ne ".pyc"
        } |
        ForEach-Object {
            [pscustomobject]@{
                path = Get-RelativePath $payloadRoot $_.FullName
                sha256 = Get-Sha256 $_.FullName
                source_path = $_.FullName
            }
        }
)

$previous = $null
if (Test-Path -LiteralPath $manifestPath) {
    $previous = Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
}

$previousByPath = @{}
if ($previous) {
    foreach ($record in $previous.managed_files) {
        $previousByPath[$record.path] = $record
    }
}

$conflicts = @()
foreach ($record in $sourceRecords) {
    $installedPath = Join-Path $Destination ($record.path.Replace("/", "\"))
    if (-not (Test-Path -LiteralPath $installedPath)) {
        continue
    }

    $currentHash = Get-Sha256 $installedPath
    if ($previousByPath.ContainsKey($record.path)) {
        if ($currentHash -ne $previousByPath[$record.path].sha256) {
            $conflicts += $record.path
        }
    } elseif ($currentHash -ne $record.sha256 -and -not $AllowBootstrapOverwrite) {
        $conflicts += $record.path
    }
}

if ($previous) {
    foreach ($record in $previous.managed_files) {
        $installedPath = Join-Path $Destination ($record.path.Replace("/", "\"))
        if (Test-Path -LiteralPath $installedPath) {
            $currentHash = Get-Sha256 $installedPath
            if ($currentHash -ne $record.sha256 -and $record.path -notin $conflicts) {
                $conflicts += $record.path
            }
        }
    }
}

if ($conflicts.Count -gt 0) {
    throw "Managed installed files have local edits or bootstrap collisions: $($conflicts -join ', ')"
}

$copied = @()
$removed = @()
try {
    foreach ($record in $sourceRecords) {
        $relativeWindows = $record.path.Replace("/", "\")
        $installedPath = Join-Path $Destination $relativeWindows
        $backupPath = Join-Path $backupRoot $relativeWindows
        New-Item -ItemType Directory -Force -Path (Split-Path -Parent $installedPath) | Out-Null

        if (Test-Path -LiteralPath $installedPath) {
            New-Item -ItemType Directory -Force -Path (Split-Path -Parent $backupPath) | Out-Null
            Copy-Item -LiteralPath $installedPath -Destination $backupPath -Force
        }

        Copy-Item -LiteralPath $record.source_path -Destination $installedPath -Force
        $copied += $record.path
    }

    if ($previous) {
        $currentPaths = @($sourceRecords.path)
        foreach ($record in $previous.managed_files) {
            if ($record.path -notin $currentPaths) {
                $relativeWindows = $record.path.Replace("/", "\")
                $installedPath = Join-Path $Destination $relativeWindows
                if (Test-Path -LiteralPath $installedPath) {
                    $backupPath = Join-Path $backupRoot $relativeWindows
                    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $backupPath) | Out-Null
                    Copy-Item -LiteralPath $installedPath -Destination $backupPath -Force
                    Remove-Item -LiteralPath $installedPath -Force
                    $removed += $record.path
                }
            }
        }
    }

    foreach ($record in $sourceRecords) {
        $installedPath = Join-Path $Destination ($record.path.Replace("/", "\"))
        if ((Get-Sha256 $installedPath) -ne $record.sha256) {
            throw "Hash verification failed for $($record.path)."
        }
    }

    $skillText = Get-Content -LiteralPath (Join-Path $Destination "SKILL.md") -Raw -Encoding UTF8
    if ($skillText -notmatch "(?s)\A---\r?\n.*?\r?\n---\r?\n") {
        throw "Installed SKILL.md has invalid front matter."
    }
    if ($skillText -notmatch "(?m)^name:\s*ai-hysys-basic-package\s*$") {
        throw "Installed SKILL.md has an unexpected skill name."
    }
    if (-not (Test-Path -LiteralPath (Join-Path $Destination "agents\openai.yaml"))) {
        throw "Installed skill is missing agents/openai.yaml."
    }

    $pythonFiles = @(
        $sourceRecords |
            Where-Object { $_.path.EndsWith(".py", [System.StringComparison]::OrdinalIgnoreCase) } |
            ForEach-Object { Join-Path $Destination ($_.path.Replace("/", "\")) }
    )
    if ($pythonFiles.Count -gt 0) {
        & py -3.12 -m py_compile @pythonFiles
        if ($LASTEXITCODE -ne 0) {
            throw "Installed Python syntax validation failed."
        }
    }
} catch {
    foreach ($relative in $copied) {
        $relativeWindows = $relative.Replace("/", "\")
        $installedPath = Join-Path $Destination $relativeWindows
        $backupPath = Join-Path $backupRoot $relativeWindows
        if (Test-Path -LiteralPath $backupPath) {
            Copy-Item -LiteralPath $backupPath -Destination $installedPath -Force
        } elseif (Test-Path -LiteralPath $installedPath) {
            Remove-Item -LiteralPath $installedPath -Force
        }
    }
    foreach ($relative in $removed) {
        $relativeWindows = $relative.Replace("/", "\")
        $installedPath = Join-Path $Destination $relativeWindows
        $backupPath = Join-Path $backupRoot $relativeWindows
        if (Test-Path -LiteralPath $backupPath) {
            New-Item -ItemType Directory -Force -Path (Split-Path -Parent $installedPath) | Out-Null
            Copy-Item -LiteralPath $backupPath -Destination $installedPath -Force
        }
    }
    throw
}

$manifest = [ordered]@{
    schema_version = 1
    synced_at_utc = (Get-Date).ToUniversalTime().ToString("o")
    source_repository = "https://github.com/leoyong1983-spec/AI-HYSYS-Skill"
    source_ref = "origin/main"
    source_commit = $sourceCommit
    destination = $Destination
    bootstrap = ($null -eq $previous)
    managed_file_count = $sourceRecords.Count
    managed_files = @($sourceRecords | Sort-Object path | Select-Object path, sha256)
}

$manifest | ConvertTo-Json -Depth 6 | Set-Content -LiteralPath $manifestPath -Encoding UTF8

[pscustomobject]@{
    source_commit = $sourceCommit
    destination = $Destination
    managed_file_count = $sourceRecords.Count
    copied_file_count = $copied.Count
    removed_file_count = $removed.Count
    hash_verification = "passed"
    installed_validation = "passed"
    manifest = $manifestPath
    backup = $backupRoot
} | ConvertTo-Json -Depth 4
