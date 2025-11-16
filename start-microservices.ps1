# Start All Microservices
# Run this script to start all 4 required microservices

Write-Host "🚀 Starting all GravityAnalysis microservices..." -ForegroundColor Cyan
Write-Host ""

$projectRoot = "e:\Shakour\GravityProjects"

$services = @(
    @{
        Name = "GravityTSE"
        Path = "$projectRoot\GravityTSE"
        Port = 5001
        Color = "Green"
    },
    @{
        Name = "Gravity_TechAnalysis"
        Path = "$projectRoot\Gravity_TechAnalysis"
        Port = 5002
        Color = "Yellow"
    },
    @{
        Name = "Gravity_TSE_Codal"
        Path = "$projectRoot\Gravity_TSE_Codal"
        Port = 5003
        Color = "Magenta"
    },
    @{
        Name = "Gravity_FundamentalAnalysis"
        Path = "$projectRoot\Gravity_FundamentalAnalysis"
        Port = 5004
        Color = "Blue"
    }
)

# Check if all services exist
$allExist = $true
foreach ($service in $services) {
    if (-not (Test-Path $service.Path)) {
        Write-Host "❌ $($service.Name) not found at $($service.Path)" -ForegroundColor Red
        Write-Host "   Please clone from GitHub first!" -ForegroundColor Yellow
        $allExist = $false
    }
}

if (-not $allExist) {
    Write-Host ""
    Write-Host "Please install all microservices first. See MICROSERVICES_SETUP.md" -ForegroundColor Red
    exit 1
}

# Start each service in a new window
foreach ($service in $services) {
    Write-Host "Starting $($service.Name) on port $($service.Port)..." -ForegroundColor $service.Color
    
    # Create startup command
    $command = @"
cd '$($service.Path)'
`$host.UI.RawUI.WindowTitle = '$($service.Name) - Port $($service.Port)'
if (Test-Path '.\venv\Scripts\Activate.ps1') {
    .\venv\Scripts\Activate.ps1
} else {
    Write-Host 'Virtual environment not found. Creating...' -ForegroundColor Yellow
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    pip install -r requirements.txt
}
Write-Host '🚀 Starting $($service.Name)...' -ForegroundColor $($service.Color)
python app.py
"@
    
    # Start in new PowerShell window
    Start-Process powershell -ArgumentList "-NoExit", "-Command", $command
    
    Start-Sleep -Seconds 3
}

Write-Host ""
Write-Host "⏳ Waiting 15 seconds for all services to initialize..." -ForegroundColor Yellow
Start-Sleep -Seconds 15

# Verify all services
Write-Host ""
Write-Host "🔍 Verifying all services..." -ForegroundColor Cyan
Write-Host ""

$allRunning = $true

foreach ($service in $services) {
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:$($service.Port)/health" -TimeoutSec 10 -ErrorAction Stop
        Write-Host "✅ $($service.Name) is running on port $($service.Port)" -ForegroundColor Green
    } catch {
        Write-Host "❌ $($service.Name) is NOT responding on port $($service.Port)" -ForegroundColor Red
        $allRunning = $false
    }
}

Write-Host ""

if ($allRunning) {
    Write-Host "🎉 All microservices are running successfully!" -ForegroundColor Green
    Write-Host ""
    Write-Host "You can now start GravityAnalysisApp:" -ForegroundColor Cyan
    Write-Host "  cd e:\Shakour\GravityProjects\GravityAnalysisApp" -ForegroundColor White
    Write-Host "  .\venv\Scripts\Activate.ps1" -ForegroundColor White
    Write-Host "  python app.py" -ForegroundColor White
} else {
    Write-Host "⚠️  Some microservices failed to start." -ForegroundColor Yellow
    Write-Host "Please check the individual service windows for errors." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Service URLs:" -ForegroundColor Cyan
Write-Host "  GravityTSE:                http://localhost:5001" -ForegroundColor White
Write-Host "  Gravity_TechAnalysis:      http://localhost:5002" -ForegroundColor White
Write-Host "  Gravity_TSE_Codal:         http://localhost:5003" -ForegroundColor White
Write-Host "  Gravity_FundamentalAnalysis: http://localhost:5004" -ForegroundColor White
Write-Host "  GravityAnalysisApp:        http://localhost:5000 (start manually)" -ForegroundColor White
Write-Host ""
