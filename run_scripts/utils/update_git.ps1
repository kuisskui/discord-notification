# Path to your local git repository
$RepoPath = "C:\Users\kuisskui\Desktop\discord-notification"
# Discord Webhook URL
$WebhookUrl = "https://discord.com/api/webhooks/1349760374517403698/fULeZmojgOeItgB3RDTHFs-0iuC_vITK_278Z_t4ThYUbTwVnj5KINDmgywCoUtipsdx"

# Navigate to the repository
Set-Location $RepoPath

# Pull from main branch and capture the output
$GitOutput = git pull

# Check if there were updates
if ($GitOutput -notmatch "Already up to date.") {
    Write-Host "Repository updated. Sending Discord notification..."

    # Create the payload
    $Message = @{
        content = "Git repository has been updated."
    }

    # Send the message (convert JSON at send time)
    Invoke-RestMethod -Uri $WebhookUrl -Method Post -Body ($Message | ConvertTo-Json -Depth 2 -Compress) -ContentType 'application/json'
} else {
    Write-Host "No updates found. No Discord message sent."
}
