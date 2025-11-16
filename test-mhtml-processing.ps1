# Test MHTML Processing with Gravity_TSE_Codal
# This script tests the Codal microservice with sample MHTML files

Write-Host "🧪 Testing MHTML Processing with Gravity_TSE_Codal" -ForegroundColor Cyan
Write-Host ""

# Check if Codal service is running
try {
    $response = Invoke-WebRequest -Uri "http://localhost:5003/health" -TimeoutSec 5
    Write-Host "✅ Gravity_TSE_Codal is running" -ForegroundColor Green
} catch {
    Write-Host "❌ Gravity_TSE_Codal is NOT running!" -ForegroundColor Red
    Write-Host "   Please start it first: .\start-microservices.ps1" -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# Sample MHTML files
$mhtmlPath = "database\Source_Codal_Data"
$mhtmlFiles = @(
    "کاوه - ترازنامه - گزارش_های مالی _ انیگما.mhtml",
    "کاوه - سود و زیان - گزارش_های مالی _ انیگما.mhtml",
    "کاوه - نسبت های مالی - گزارش_های مالی _ انیگما.mhtml"
)

Write-Host "Testing with $($mhtmlFiles.Count) sample MHTML files..." -ForegroundColor Cyan
Write-Host ""

foreach ($file in $mhtmlFiles) {
    $fullPath = Join-Path $mhtmlPath $file
    
    if (-not (Test-Path $fullPath)) {
        Write-Host "⚠️  File not found: $file" -ForegroundColor Yellow
        continue
    }
    
    Write-Host "Processing: $file" -ForegroundColor White
    
    try {
        # Prepare multipart form data
        $boundary = [System.Guid]::NewGuid().ToString()
        $fileContent = [System.IO.File]::ReadAllBytes($fullPath)
        $fileName = [System.IO.Path]::GetFileName($fullPath)
        
        # Create multipart body
        $bodyLines = @(
            "--$boundary",
            "Content-Disposition: form-data; name=`"file`"; filename=`"$fileName`"",
            "Content-Type: application/mhtml",
            "",
            [System.Text.Encoding]::UTF8.GetString($fileContent),
            "--$boundary--"
        )
        $body = $bodyLines -join "`r`n"
        
        # Send request
        $response = Invoke-RestMethod -Uri "http://localhost:5003/api/process/mhtml" `
            -Method Post `
            -ContentType "multipart/form-data; boundary=$boundary" `
            -Body $body `
            -TimeoutSec 30
        
        if ($response.success) {
            Write-Host "  ✅ Successfully processed" -ForegroundColor Green
            Write-Host "     Symbol: $($response.data.symbol_code)" -ForegroundColor Gray
            Write-Host "     Report Type: $($response.data.report_type)" -ForegroundColor Gray
        } else {
            Write-Host "  ❌ Processing failed: $($response.error)" -ForegroundColor Red
        }
        
    } catch {
        Write-Host "  ❌ Error: $($_.Exception.Message)" -ForegroundColor Red
    }
    
    Write-Host ""
}

Write-Host "Test complete!" -ForegroundColor Green
