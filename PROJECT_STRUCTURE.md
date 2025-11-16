# ساختار کامل پروژه - Gravity Analysis App

## 📁 ساختار پوشه‌ها و فایل‌ها

```
GravityAnalysisApp/
│
├── 📄 app.py                          # فایل اصلی برنامه Flask
├── 📄 config.py                       # تنظیمات و پیکربندی
├── 📄 requirements.txt                # وابستگی‌های Python
├── 📄 .gitignore                      # فایل‌های نادیده گرفته شده Git
│
├── 📖 README.md                       # مستندات اصلی (English)
├── 📖 README_FA.md                    # مستندات کامل فارسی
├── 📖 QUICKSTART.md                   # راهنمای سریع
├── 📖 API_DOCUMENTATION.md            # مستندات API
│
├── 🔧 setup.ps1                       # اسکریپت نصب خودکار
├── 🚀 run.ps1                         # اسکریپت اجرای سریع
├── 🧪 test_app.py                     # فایل تست برنامه
│
├── 📂 database/                       # دیتابیس و مدل‌ها
│   ├── __init__.py
│   └── db_manager.py                  # مدیریت SQLite
│
├── 📂 services/                       # سرویس‌های میکروسرویس
│   ├── __init__.py
│   ├── market_data_service.py         # دریافت داده‌های بازار
│   ├── technical_analysis_service.py  # تحلیل تکنیکال
│   ├── codal_service.py              # پردازش MHTML
│   └── fundamental_analysis_service.py # تحلیل بنیادی
│
├── 📂 templates/                      # قالب‌های HTML
│   ├── base.html                      # قالب پایه (Bootstrap RTL)
│   ├── index.html                     # داشبورد اصلی
│   ├── symbols.html                   # لیست نمادها
│   ├── symbol_detail.html             # جزئیات نماد
│   ├── technical_analysis.html        # صفحه تحلیل تکنیکال
│   ├── fundamental_analysis.html      # صفحه تحلیل بنیادی
│   ├── upload.html                    # صفحه آپلود فایل
│   ├── 404.html                       # صفحه خطا 404
│   └── 500.html                       # صفحه خطا 500
│
└── 📂 uploads/                        # پوشه آپلود (ایجاد خودکار)
    └── mhtml/                         # فایل‌های MHTML

```

## 🎯 فایل‌های کلیدی

### Backend (Python/Flask)

1. **app.py** (350+ خط)
   - تعریف روت‌های Flask
   - API endpoints
   - مدیریت آپلود فایل
   - پردازش درخواست‌ها

2. **database/db_manager.py** (400+ خط)
   - مدیریت SQLite
   - 8 جدول دیتابیس
   - CRUD operations
   - جستجو و فیلتر

3. **services/technical_analysis_service.py** (300+ خط)
   - محاسبه RSI, MACD, MA, BB, Stochastic
   - تولید سیگنال‌های خرید/فروش
   - خلاصه تحلیل

4. **services/fundamental_analysis_service.py** (250+ خط)
   - محاسبه نسبت‌های مالی
   - ارزیابی بنیادی
   - امتیازدهی شرکت

5. **services/market_data_service.py** (150+ خط)
   - دریافت قیمت‌ها
   - لیست نمادها
   - به‌روزرسانی داده‌ها

6. **services/codal_service.py** (100+ خط)
   - پردازش فایل‌های MHTML
   - استخراج گزارش‌های مالی

### Frontend (HTML/CSS/JavaScript)

7. **templates/base.html** (300+ خط)
   - قالب پایه RTL
   - Navigation
   - Styling with Bootstrap
   - JavaScript utilities

8. **templates/index.html** (150+ خط)
   - داشبورد اصلی
   - نمایش آمار بازار
   - لینک‌های سریع

9. **templates/technical_analysis.html** (200+ خط)
   - نمایش اندیکاتورها
   - چارت‌ها
   - سیگنال‌ها

10. **templates/fundamental_analysis.html** (200+ خط)
    - نسبت‌های مالی
    - ارزیابی
    - نقاط قوت/ضعف

## 📊 آمار پروژه

- **تعداد کل فایل‌ها**: 28 فایل
- **خطوط کد Python**: ~2000+ خط
- **خطوط کد HTML/CSS/JS**: ~1500+ خط
- **تعداد API endpoints**: 11 endpoint
- **تعداد صفحات وب**: 7 صفحه
- **تعداد جداول دیتابیس**: 8 جدول

## 🔧 فناوری‌های استفاده شده

### Backend
- **Flask** 3.0.0 - وب فریمورک
- **SQLite** - دیتابیس
- **Pandas** - پردازش داده
- **NumPy** - محاسبات عددی
- **TA** - اندیکاتورهای تکنیکال

### Frontend
- **Bootstrap 5 RTL** - طراحی واکنش‌گرا
- **Chart.js** - نمودارها
- **Font Awesome** - آیکون‌ها
- **Axios** - درخواست‌های AJAX

### Tools
- **PowerShell** - اسکریپت‌های اتوماسیون
- **Git** - کنترل نسخه

## 📝 جداول دیتابیس

1. **symbols** - نمادها
2. **market_data** - قیمت‌های روزانه
3. **financial_reports** - گزارش‌های مالی
4. **balance_sheet** - ترازنامه
5. **income_statement** - سود و زیان
6. **cash_flow** - جریان وجوه نقد
7. **technical_analysis** - نتایج تحلیل تکنیکال
8. **fundamental_analysis** - نتایج تحلیل بنیادی

## 🌐 صفحات وب

1. **/** - داشبورد اصلی
2. **/symbols** - لیست نمادها
3. **/symbol/{code}** - جزئیات نماد
4. **/technical-analysis/{code}** - تحلیل تکنیکال
5. **/fundamental-analysis/{code}** - تحلیل بنیادی
6. **/upload** - آپلود گزارش مالی
7. **/404**, **/500** - صفحات خطا

## 🔌 API Endpoints

### Market Data
- `GET /api/market/symbols`
- `GET /api/market/price/{symbol_code}`
- `POST /api/market/update/{symbol_code}`

### Technical Analysis
- `GET /api/technical/analyze/{symbol_code}`
- `GET /api/technical/indicators/{symbol_code}`

### Fundamental Analysis
- `GET /api/fundamental/analyze/{symbol_code}`
- `GET /api/fundamental/ratios/{symbol_code}`

### Upload & Search
- `POST /api/upload/mhtml`
- `GET /api/search`

## 📦 وابستگی‌ها

```
Flask==3.0.0
Flask-CORS==4.0.0
pandas==2.1.4
numpy==1.26.2
ta==0.11.0
pandas-ta==0.3.14b0
requests==2.31.0
beautifulsoup4==4.12.2
plotly==5.18.0
```

## 🚀 راه‌اندازی سریع

```powershell
# نصب خودکار
.\setup.ps1

# یا دستی
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

## ✅ ویژگی‌های پیاده‌سازی شده

- ✅ معماری میکروسرویس
- ✅ دیتابیس SQLite کامل
- ✅ API های RESTful
- ✅ تحلیل تکنیکال (5 اندیکاتور)
- ✅ تحلیل بنیادی (نسبت‌های مالی)
- ✅ آپلود و پردازش MHTML
- ✅ رابط کاربری زیبا و RTL
- ✅ جستجوی نماد
- ✅ داشبورد تعاملی
- ✅ مستندات کامل

## 📚 مستندات

- `README.md` - مستندات اصلی
- `README_FA.md` - مستندات کامل فارسی
- `API_DOCUMENTATION.md` - مستندات API
- `QUICKSTART.md` - راهنمای سریع
- این فایل - نمای کلی پروژه

---

**توجه**: این پروژه آماده برای توسعه و استفاده است. برای محیط production، لطفا میکروسرویس‌های واقعی را راه‌اندازی کنید.
