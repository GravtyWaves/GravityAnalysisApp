# راه‌اندازی خودکار - Gravity Analysis App
# این اسکریپت تمام مراحل نصب و راه‌اندازی را انجام می‌دهد

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Gravity Analysis App - راه‌اندازی  " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# بررسی نصب Python
Write-Host "[1/6] بررسی نصب Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version
    Write-Host "✓ Python نصب شده است: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python یافت نشد. لطفا ابتدا Python را نصب کنید." -ForegroundColor Red
    Write-Host "دانلود از: https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

Write-Host ""

# ایجاد محیط مجازی
Write-Host "[2/6] ایجاد محیط مجازی..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "محیط مجازی از قبل وجود دارد." -ForegroundColor Yellow
} else {
    python -m venv venv
    if ($LASTEXITCODE -eq 0) {
        Write-Host "✓ محیط مجازی ایجاد شد" -ForegroundColor Green
    } else {
        Write-Host "✗ خطا در ایجاد محیط مجازی" -ForegroundColor Red
        exit 1
    }
}

Write-Host ""

# فعال‌سازی محیط مجازی
Write-Host "[3/6] فعال‌سازی محیط مجازی..." -ForegroundColor Yellow
try {
    & ".\venv\Scripts\Activate.ps1"
    Write-Host "✓ محیط مجازی فعال شد" -ForegroundColor Green
} catch {
    Write-Host "⚠ خطا در فعال‌سازی محیط مجازی" -ForegroundColor Yellow
    Write-Host "در صورت مشکل Execution Policy، دستور زیر را اجرا کنید:" -ForegroundColor Yellow
    Write-Host "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser" -ForegroundColor Cyan
}

Write-Host ""

# نصب وابستگی‌ها
Write-Host "[4/6] نصب کتابخانه‌های مورد نیاز..." -ForegroundColor Yellow
Write-Host "این مرحله ممکن است چند دقیقه طول بکشد..." -ForegroundColor Gray

pip install -r requirements.txt --quiet

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ کتابخانه‌ها با موفقیت نصب شدند" -ForegroundColor Green
} else {
    Write-Host "✗ خطا در نصب کتابخانه‌ها" -ForegroundColor Red
    exit 1
}

Write-Host ""

# ایجاد پوشه‌های مورد نیاز
Write-Host "[5/6] ایجاد پوشه‌های مورد نیاز..." -ForegroundColor Yellow

$folders = @("uploads", "uploads/mhtml")
foreach ($folder in $folders) {
    if (-not (Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder | Out-Null
        Write-Host "✓ پوشه $folder ایجاد شد" -ForegroundColor Green
    }
}

Write-Host ""

# راه‌اندازی دیتابیس
Write-Host "[6/6] راه‌اندازی دیتابیس..." -ForegroundColor Yellow

python -c "from database.db_manager import DatabaseManager; db = DatabaseManager(); db.init_db(); print('Database initialized successfully!')"

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ دیتابیس با موفقیت ایجاد شد" -ForegroundColor Green
} else {
    Write-Host "✗ خطا در ایجاد دیتابیس" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "  نصب با موفقیت انجام شد! 🎉          " -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "برای اجرای برنامه دستور زیر را وارد کنید:" -ForegroundColor Cyan
Write-Host "  python app.py" -ForegroundColor Yellow
Write-Host ""
Write-Host "برنامه در آدرس زیر اجرا خواهد شد:" -ForegroundColor Cyan
Write-Host "  http://localhost:5000" -ForegroundColor Yellow
Write-Host ""

# پرسش برای اجرای فوری برنامه
$response = Read-Host "آیا می‌خواهید برنامه را الان اجرا کنید؟ (Y/N)"
if ($response -eq 'Y' -or $response -eq 'y') {
    Write-Host ""
    Write-Host "در حال اجرای برنامه..." -ForegroundColor Green
    Write-Host "برای توقف برنامه Ctrl+C را بزنید" -ForegroundColor Gray
    Write-Host ""
    python app.py
}
