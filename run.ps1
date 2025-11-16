# اجرای سریع برنامه
# این اسکریپت برنامه را به سرعت اجرا می‌کند

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Gravity Analysis App                 " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# بررسی محیط مجازی
if (-not (Test-Path "venv")) {
    Write-Host "⚠ محیط مجازی یافت نشد!" -ForegroundColor Yellow
    Write-Host "لطفا ابتدا setup.ps1 را اجرا کنید:" -ForegroundColor Yellow
    Write-Host "  .\setup.ps1" -ForegroundColor Cyan
    exit 1
}

# فعال‌سازی محیط مجازی
Write-Host "فعال‌سازی محیط مجازی..." -ForegroundColor Yellow
try {
    & ".\venv\Scripts\Activate.ps1"
} catch {
    Write-Host "⚠ نمی‌توان محیط مجازی را فعال کرد" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "در حال اجرای برنامه..." -ForegroundColor Green
Write-Host "برنامه در آدرس http://localhost:5000 در دسترس خواهد بود" -ForegroundColor Cyan
Write-Host "برای توقف برنامه Ctrl+C را بزنید" -ForegroundColor Gray
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

# اجرای برنامه
python app.py
