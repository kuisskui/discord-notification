cd C:\Users\kuisskui\Desktop\discord-notification

git fetch origin

# Retrieve the local commit hash for the main branch
$localHash = git rev-parse main 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error retrieving local main branch hash: $localHash"
    exit 1
}

# Retrieve the remote commit hash for origin/main
$remoteHash = git rev-parse origin/main 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "Error retrieving remote main branch hash: $remoteHash"
    exit 1
}

Write-Host "Local main commit hash: $localHash"
Write-Host "Remote main commit hash: $remoteHash"

$isUptodate
if ($localHash -eq $remoteHash) {
    Write-Host "The main branch is up to date."
    $isUptodate = 1
} else {
    Write-Host "The main branch is not up to date."
    $isUptodate = 0
}

if ($isUptodate -eq 0){
    Write-Host "Pull the main."
    git pull origin main
}

Write-Host "Execute the main"



