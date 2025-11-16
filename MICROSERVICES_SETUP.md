# MICROSERVICES INSTALLATION & SETUP GUIDE

## ⚠️ CRITICAL: Install ALL Microservices First!

This application **REQUIRES** 4 external microservices to function. You MUST install and run them before starting GravityAnalysisApp.

---

## 📦 Required Microservices

### 1. GravityTSE (Port 5001)
**Purpose**: Market data and price information from Tehran Stock Exchange

**Repository**: https://github.com/GravityWavesMl/GravityTSE

**Installation**:
```powershell
# Navigate to parent directory
cd e:\Shakour\GravityProjects

# Clone repository
git clone https://github.com/GravityWavesMl/GravityTSE.git
cd GravityTSE

# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run service
python app.py
# Should run on http://localhost:5001
```

**Test**:
```powershell
curl http://localhost:5001/health
curl http://localhost:5001/api/symbols
```

---

### 2. Gravity_TechAnalysis (Port 5002)
**Purpose**: Technical analysis calculations (RSI, MACD, MA, etc.)

**Repository**: https://github.com/Shakour-Data/Gravity_TechAnalysis

**Installation**:
```powershell
cd e:\Shakour\GravityProjects

git clone https://github.com/Shakour-Data/Gravity_TechAnalysis.git
cd Gravity_TechAnalysis

python -m venv venv
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

python app.py
# Should run on http://localhost:5002
```

**Test**:
```powershell
curl http://localhost:5002/health
```

---

### 3. Gravity_TSE_Codal (Port 5003)
**Purpose**: Process MHTML files from CODAL (financial reports)

**Repository**: https://github.com/GravtyWaves/Gravity_TSE_Codal

**Installation**:
```powershell
cd e:\Shakour\GravityProjects

git clone https://github.com/GravtyWaves/Gravity_TSE_Codal.git
cd Gravity_TSE_Codal

python -m venv venv
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

python app.py
# Should run on http://localhost:5003
```

**Test with sample MHTML**:
```powershell
# Test with one of your MHTML files
$file = "E:\Shakour\GravityProjects\GravityAnalysisApp\database\Source_Codal_Data\کاوه - ترازنامه - گزارش_های مالی _ انیگما.mhtml"
curl -X POST http://localhost:5003/api/process/mhtml -F "file=@$file"
```

---

### 4. Gravity_FundamentalAnalysis (Port 5004)
**Purpose**: Fundamental analysis, financial ratios, valuation

**Repository**: https://github.com/GravtyWaves/Gravity_FundamentalAnalysis

**Installation**:
```powershell
cd e:\Shakour\GravityProjects

git clone https://github.com/GravtyWaves/Gravity_FundamentalAnalysis.git
cd Gravity_FundamentalAnalysis

python -m venv venv
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

python app.py
# Should run on http://localhost:5004
```

**Test**:
```powershell
curl http://localhost:5004/health
```

---

## 🚀 Quick Start All Services

### Option 1: Manual (4 terminals)
Open 4 separate PowerShell terminals and run each service:

**Terminal 1 - GravityTSE**:
```powershell
cd e:\Shakour\GravityProjects\GravityTSE
.\venv\Scripts\Activate.ps1
python app.py
```

**Terminal 2 - Gravity_TechAnalysis**:
```powershell
cd e:\Shakour\GravityProjects\Gravity_TechAnalysis
.\venv\Scripts\Activate.ps1
python app.py
```

**Terminal 3 - Gravity_TSE_Codal**:
```powershell
cd e:\Shakour\GravityProjects\Gravity_TSE_Codal
.\venv\Scripts\Activate.ps1
python app.py
```

**Terminal 4 - Gravity_FundamentalAnalysis**:
```powershell
cd e:\Shakour\GravityProjects\Gravity_FundamentalAnalysis
.\venv\Scripts\Activate.ps1
python app.py
```

**Terminal 5 - GravityAnalysisApp**:
```powershell
cd e:\Shakour\GravityProjects\GravityAnalysisApp
.\venv\Scripts\Activate.ps1
python app.py
```

---

### Option 2: PowerShell Script (Automated)

Create `start-all-services.ps1`:
```powershell
# Start all microservices in background

$services = @(
    @{Name="GravityTSE"; Path="e:\Shakour\GravityProjects\GravityTSE"; Port=5001},
    @{Name="Gravity_TechAnalysis"; Path="e:\Shakour\GravityProjects\Gravity_TechAnalysis"; Port=5002},
    @{Name="Gravity_TSE_Codal"; Path="e:\Shakour\GravityProjects\Gravity_TSE_Codal"; Port=5003},
    @{Name="Gravity_FundamentalAnalysis"; Path="e:\Shakour\GravityProjects\Gravity_FundamentalAnalysis"; Port=5004}
)

foreach ($service in $services) {
    Write-Host "Starting $($service.Name) on port $($service.Port)..." -ForegroundColor Green
    
    Start-Process powershell -ArgumentList @(
        "-NoExit",
        "-Command",
        "cd '$($service.Path)'; .\venv\Scripts\Activate.ps1; python app.py"
    )
    
    Start-Sleep -Seconds 2
}

Write-Host "`nAll microservices started!" -ForegroundColor Green
Write-Host "Waiting 10 seconds for services to initialize..." -ForegroundColor Yellow
Start-Sleep -Seconds 10

# Verify all services
Write-Host "`nVerifying services..." -ForegroundColor Cyan
foreach ($service in $services) {
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:$($service.Port)/health" -TimeoutSec 5
        Write-Host "✅ $($service.Name) is running" -ForegroundColor Green
    } catch {
        Write-Host "❌ $($service.Name) failed to start" -ForegroundColor Red
    }
}

Write-Host "`nYou can now start GravityAnalysisApp!" -ForegroundColor Green
```

**Usage**:
```powershell
.\start-all-services.ps1
```

---

### Option 3: Docker Compose (Recommended for Production)

Create `docker-compose.yml` in `e:\Shakour\GravityProjects`:
```yaml
version: '3.8'

services:
  gravitytse:
    build: ./GravityTSE
    ports:
      - "5001:5001"
    environment:
      - FLASK_ENV=production
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5001/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  gravity-techanalysis:
    build: ./Gravity_TechAnalysis
    ports:
      - "5002:5002"
    environment:
      - FLASK_ENV=production
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5002/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  gravity-codal:
    build: ./Gravity_TSE_Codal
    ports:
      - "5003:5003"
    environment:
      - FLASK_ENV=production
    volumes:
      - ./mhtml_uploads:/app/uploads
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5003/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  gravity-fundamental:
    build: ./Gravity_FundamentalAnalysis
    ports:
      - "5004:5004"
    environment:
      - FLASK_ENV=production
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:5004/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  gravityanalysisapp:
    build: ./GravityAnalysisApp
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - GRAVITYTSE_URL=http://gravitytse:5001
      - GRAVITY_TECH_URL=http://gravity-techanalysis:5002
      - GRAVITY_CODAL_URL=http://gravity-codal:5003
      - GRAVITY_FUNDAMENTAL_URL=http://gravity-fundamental:5004
    depends_on:
      - gravitytse
      - gravity-techanalysis
      - gravity-codal
      - gravity-fundamental
    restart: unless-stopped
    volumes:
      - ./GravityAnalysisApp/database:/app/database
```

**Usage**:
```powershell
cd e:\Shakour\GravityProjects
docker-compose up -d
```

---

## 📝 MHTML File Naming Convention

Based on your sample files, the standard naming is:

```
{SymbolCode} - {ReportType} - گزارش_های مالی _ انیگما.mhtml
```

**Example Files**:
- `کاوه - ترازنامه - گزارش_های مالی _ انیگما.mhtml` → Balance Sheet
- `کاوه - سود و زیان - گزارش_های مالی _ انیگما.mhtml` → Income Statement
- `کاوه - نسبت های مالی - گزارش_های مالی _ انیگما.mhtml` → Financial Ratios
- `کاوه - عملکرد ماهانه - گزارش_های مالی _ انیگما.mhtml` → Monthly Performance
- `کاوه - بهای تمام شده - گزارش_های مالی _ انیگما.mhtml` → Cost of Goods
- `کاوه - سربار - گزارش_های مالی _ انیگما.mhtml` → Overhead
- `کاوه - درآمدهای عملیاتی - گزارش_های مالی _ انیگما.mhtml` → Operating Income
- `کاوه - گردش موجودی - گزارش_های مالی _ انیگما.mhtml` → Inventory Turnover
- `کاوه - مواد اولیه - گزارش_های مالی _ انیگما.mhtml` → Raw Materials
- `کاوه - هزینه های عمومی - گزارش_های مالی _ انیگما.mhtml` → General Expenses

**Parsing Logic**:
```python
import re

def parse_mhtml_filename(filename: str) -> dict:
    """
    Parse MHTML filename to extract symbol and report type.
    
    Format: {Symbol} - {ReportType} - گزارش_های مالی _ انیگما.mhtml
    """
    pattern = r'^(.+?)\s*-\s*(.+?)\s*-\s*گزارش_های مالی'
    match = re.match(pattern, filename)
    
    if match:
        symbol_code = match.group(1).strip()
        report_type = match.group(2).strip()
        
        # Map Persian report types to English
        report_type_map = {
            'ترازنامه': 'balance_sheet',
            'سود و زیان': 'income_statement',
            'نسبت های مالی': 'financial_ratios',
            'عملکرد ماهانه': 'monthly_performance',
            'بهای تمام شده': 'cost_of_goods',
            'سربار': 'overhead',
            'درآمدهای عملیاتی': 'operating_income',
            'گردش موجودی': 'inventory_turnover',
            'مواد اولیه': 'raw_materials',
            'هزینه های عمومی': 'general_expenses'
        }
        
        return {
            'symbol_code': symbol_code,
            'report_type': report_type,
            'report_type_en': report_type_map.get(report_type, 'unknown')
        }
    
    return None
```

---

## ✅ Verification Checklist

Before starting GravityAnalysisApp, verify:

- [ ] GravityTSE running on http://localhost:5001
- [ ] Gravity_TechAnalysis running on http://localhost:5002
- [ ] Gravity_TSE_Codal running on http://localhost:5003
- [ ] Gravity_FundamentalAnalysis running on http://localhost:5004
- [ ] All services respond to /health endpoint
- [ ] Test MHTML upload to Codal service
- [ ] Test price data from GravityTSE
- [ ] Test technical analysis from Gravity_TechAnalysis
- [ ] Test fundamental analysis from Gravity_FundamentalAnalysis

**Verification Script**:
```powershell
Write-Host "Verifying all microservices..." -ForegroundColor Cyan

$services = @{
    "GravityTSE" = "http://localhost:5001/health"
    "Gravity_TechAnalysis" = "http://localhost:5002/health"
    "Gravity_TSE_Codal" = "http://localhost:5003/health"
    "Gravity_FundamentalAnalysis" = "http://localhost:5004/health"
}

$allRunning = $true

foreach ($service in $services.GetEnumerator()) {
    try {
        $response = Invoke-WebRequest -Uri $service.Value -TimeoutSec 5
        Write-Host "✅ $($service.Key) is running" -ForegroundColor Green
    } catch {
        Write-Host "❌ $($service.Key) is NOT running" -ForegroundColor Red
        $allRunning = $false
    }
}

if ($allRunning) {
    Write-Host "`n✅ All microservices are running! You can start GravityAnalysisApp." -ForegroundColor Green
} else {
    Write-Host "`n❌ Some microservices are not running. Please start them first." -ForegroundColor Red
}
```

---

## 🔧 Troubleshooting

### Issue: Port already in use
```powershell
# Find process using port
netstat -ano | findstr :5001

# Kill process
taskkill /PID <PID> /F
```

### Issue: Import errors
```powershell
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Issue: MHTML processing fails
- Check file encoding (UTF-8 with BOM)
- Verify file is valid MHTML
- Check file size (< 16MB)
- Test with sample file first

### Issue: Service won't start
- Check Python version (3.9+)
- Check virtual environment activated
- Check requirements installed
- Check port not in use
- Check firewall settings

---

## 📚 Next Steps

1. **Install all 4 microservices** using instructions above
2. **Verify all services running** using verification script
3. **Test each service** with sample data
4. **Start GravityAnalysisApp**
5. **Upload sample MHTML files** to test Codal processing
6. **Test full workflow** (Market Data → Tech Analysis → Fundamental Analysis)

---

**IMPORTANT**: This application will NOT work without all 4 microservices running!

**Version**: 1.0.0  
**Last Updated**: 2024-11-16
