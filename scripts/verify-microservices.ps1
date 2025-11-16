# Verify All Microservices
# Quick script to check if all microservices are running

Write-Host "🔍 Checking microservices status..." -ForegroundColor Cyan
Write-Host ""

$services = @{
    "GravityTSE (Market Data)" = @{
        URL = "http://localhost:5001/health"
        Port = 5001
    }
    "Gravity_TechAnalysis (Technical)" = @{
        URL = "http://localhost:5002/health"
        Port = 5002
    }
    "Gravity_TSE_Codal (MHTML Processing)" = @{
        URL = "http://localhost:5003/health"
        Port = 5003
    }
    "Gravity_FundamentalAnalysis (Fundamental)" = @{
        URL = "http://localhost:5004/health"
        Port = 5004
    }
}

$allRunning = $true
$runningCount = 0

foreach ($service in $services.GetEnumerator()) {
    Write-Host "Checking $($service.Key)..." -NoNewline
    
    try {
        $response = Invoke-WebRequest -Uri $service.Value.URL -TimeoutSec 5 -ErrorAction Stop
        
        if ($response.StatusCode -eq 200) {
            Write-Host " ✅ Running" -ForegroundColor Green
            $runningCount++
        } else {
            Write-Host " ⚠️  Responded but status $($response.StatusCode)" -ForegroundColor Yellow
        }
    } catch {
        Write-Host " ❌ Not running" -ForegroundColor Red
        Write-Host "   Error: $($_.Exception.Message)" -ForegroundColor Gray
        $allRunning = $false
    }
}

Write-Host ""
Write-Host "Status: $runningCount / 4 services running" -ForegroundColor $(if ($runningCount -eq 4) { "Green" } else { "Yellow" })

if ($allRunning) {
    Write-Host ""
    Write-Host "🎉 All microservices are operational!" -ForegroundColor Green
    Write-Host ""
    Write-Host "You can start GravityAnalysisApp now:" -ForegroundColor Cyan
    Write-Host "  cd e:\Shakour\GravityProjects\GravityAnalysisApp" -ForegroundColor White
    Write-Host "  .\venv\Scripts\Activate.ps1" -ForegroundColor White
    Write-Host "  python app.py" -ForegroundColor White
} else {
    Write-Host ""
    Write-Host "⚠️  Some microservices are not running!" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "To start all services, run:" -ForegroundColor Cyan
    Write-Host "  .\start-microservices.ps1" -ForegroundColor White
    Write-Host ""
    Write-Host "Or see MICROSERVICES_SETUP.md for manual installation" -ForegroundColor Gray
}

Write-Host ""
