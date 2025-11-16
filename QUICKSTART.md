# راه‌اندازی سریع - Gravity Analysis App

## نصب و اجرا

### 1. نصب وابستگی‌ها

```powershell
# ایجاد محیط مجازی
python -m venv venv

# فعال‌سازی محیط مجازی
.\venv\Scripts\Activate.ps1

# نصب کتابخانه‌ها
pip install -r requirements.txt
```

### 2. راه‌اندازی دیتابیس

```powershell
python -c "from database.db_manager import DatabaseManager; DatabaseManager().init_db()"
```

### 3. اجرای برنامه

```powershell
python app.py
```

برنامه در آدرس http://localhost:5000 اجرا خواهد شد.

## ویژگی‌های اصلی

✅ تحلیل تکنیکال (RSI, MACD, MA, BB, Stochastic)  
✅ تحلیل بنیادی (نسبت‌های مالی)  
✅ آپلود گزارش‌های مالی MHTML  
✅ رابط کاربری فارسی و زیبا  
✅ دیتابیس SQLite محلی  

## نکات مهم

⚠️ برنامه در حالت Mock داده‌ها اجرا می‌شود  
⚠️ برای استفاده واقعی، میکروسرویس‌ها را راه‌اندازی کنید  
⚠️ URL های میکروسرویس‌ها را در config.py تنظیم کنید  

برای اطلاعات بیشتر: [README_FA.md](README_FA.md)
