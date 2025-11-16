# Gravity Analysis App

<div dir="rtl">

## تحلیل‌گر بازار سرمایه گراویتی

یک برنامه وب جامع برای تحلیل بنیادی و تکنیکال نمادهای بازار سرمایه ایران

### ویژگی‌های اصلی

- 📊 **تحلیل تکنیکال**: محاسبه اندیکاتورهای تکنیکال (RSI, MACD, MA, Bollinger Bands, Stochastic)
- 📈 **تحلیل بنیادی**: محاسبه نسبت‌های مالی و ارزیابی بنیادی شرکت‌ها
- 📁 **آپلود گزارش مالی**: آپلود و پردازش فایل‌های MHTML از کدال
- 💾 **دیتابیس SQLite**: ذخیره‌سازی داده‌ها به صورت محلی
- 🎨 **رابط کاربری زیبا**: طراحی مدرن و کاربرپسند با Bootstrap RTL
- 🔌 **معماری میکروسرویس**: یکپارچه‌سازی با میکروسرویس‌های مختلف

### میکروسرویس‌های مورد استفاده

1. **GravityTSE**: دریافت داده‌های قیمت و بازار
   - Repository: https://github.com/GravityWavesMl/GravityTSE

2. **Gravity_TechAnalysis**: تحلیل تکنیکال
   - Repository: https://github.com/Shakour-Data/Gravity_TechAnalysis

3. **Gravity_TSE_Codal**: پردازش گزارش‌های مالی MHTML
   - Repository: https://github.com/GravtyWaves/Gravity_TSE_Codal

4. **Gravity_FundamentalAnalysis**: تحلیل بنیادی
   - Repository: https://github.com/GravtyWaves/Gravity_FundamentalAnalysis

### نصب و راه‌اندازی

#### پیش‌نیازها

- Python 3.8 یا بالاتر
- pip (Python package manager)

#### مراحل نصب

1. کلون کردن پروژه:
```bash
git clone https://github.com/GravtyWaves/GravityAnalysisApp.git
cd GravityAnalysisApp
```

2. ایجاد محیط مجازی:
```bash
python -m venv venv
```

3. فعال‌سازی محیط مجازی:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. نصب کتابخانه‌ها:
```bash
pip install -r requirements.txt
```

5. راه‌اندازی دیتابیس:
```bash
python -c "from database.db_manager import DatabaseManager; DatabaseManager().init_db()"
```

6. اجرای برنامه:
```bash
python app.py
```

7. مشاهده برنامه:
برنامه در آدرس http://localhost:5000 در دسترس خواهد بود

### ساختار پروژه

```
GravityAnalysisApp/
│
├── app.py                          # فایل اصلی برنامه Flask
├── config.py                       # تنظیمات برنامه
├── requirements.txt                # وابستگی‌های Python
│
├── database/                       # دیتابیس و مدل‌ها
│   ├── __init__.py
│   └── db_manager.py              # مدیریت دیتابیس SQLite
│
├── services/                       # سرویس‌های میکروسرویس
│   ├── __init__.py
│   ├── market_data_service.py     # سرویس دریافت داده‌های بازار
│   ├── technical_analysis_service.py  # سرویس تحلیل تکنیکال
│   ├── codal_service.py           # سرویس پردازش MHTML
│   └── fundamental_analysis_service.py  # سرویس تحلیل بنیادی
│
├── templates/                      # قالب‌های HTML
│   ├── base.html                  # قالب پایه
│   ├── index.html                 # صفحه اصلی
│   ├── symbols.html               # لیست نمادها
│   ├── symbol_detail.html         # جزئیات نماد
│   ├── technical_analysis.html    # صفحه تحلیل تکنیکال
│   ├── fundamental_analysis.html  # صفحه تحلیل بنیادی
│   ├── upload.html                # صفحه آپلود
│   ├── 404.html                   # صفحه خطا 404
│   └── 500.html                   # صفحه خطا 500
│
├── uploads/                        # پوشه آپلود فایل‌ها
│   └── mhtml/                     # فایل‌های MHTML
│
└── README.md                       # این فایل
```

### API Endpoints

#### دریافت داده‌های بازار

- `GET /api/market/symbols` - دریافت لیست نمادها
- `GET /api/market/price/{symbol_code}?days=30` - دریافت قیمت‌ها
- `POST /api/market/update/{symbol_code}` - به‌روزرسانی داده‌ها

#### تحلیل تکنیکال

- `GET /api/technical/analyze/{symbol_code}` - انجام تحلیل تکنیکال
- `GET /api/technical/indicators/{symbol_code}?indicators=RSI,MACD` - محاسبه اندیکاتورها

#### آپلود و پردازش

- `POST /api/upload/mhtml` - آپلود فایل MHTML

#### تحلیل بنیادی

- `GET /api/fundamental/analyze/{symbol_code}` - انجام تحلیل بنیادی
- `GET /api/fundamental/ratios/{symbol_code}` - دریافت نسبت‌های مالی

#### جستجو

- `GET /api/search?q={query}` - جستجوی نماد

### نحوه استفاده

#### 1. مشاهده داشبورد
- به صفحه اصلی بروید و وضعیت کلی بازار را مشاهده کنید

#### 2. مشاهده لیست نمادها
- از منو گزینه "نمادها" را انتخاب کنید
- می‌توانید نمادها را جستجو کنید

#### 3. تحلیل تکنیکال
- نماد مورد نظر را انتخاب کنید
- روی "تحلیل تکنیکال" کلیک کنید
- اندیکاتورها و سیگنال‌ها نمایش داده می‌شوند

#### 4. آپلود گزارش مالی
- از منو گزینه "آپلود گزارش" را انتخاب کنید
- فایل MHTML گزارش مالی از کدال را آپلود کنید
- سیستم به صورت خودکار داده‌ها را پردازش می‌کند

#### 5. تحلیل بنیادی
- برای نمادهایی که گزارش مالی آپلود شده
- روی "تحلیل بنیادی" کلیک کنید
- نسبت‌های مالی و ارزیابی بنیادی نمایش داده می‌شود

### توجهات مهم

⚠️ **نکته**: این برنامه به صورت پیش‌فرض از داده‌های Mock استفاده می‌کند. برای استفاده در محیط واقعی:

1. میکروسرویس‌های مورد نیاز را راه‌اندازی کنید
2. URL های میکروسرویس‌ها را در `config.py` تنظیم کنید
3. کدهای Mock در فایل‌های service را با فراخوانی‌های واقعی API جایگزین کنید

### تنظیمات پیشرفته

#### تغییر پورت برنامه
در فایل `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

#### تنظیم URL های میکروسرویس
در فایل `config.py`:
```python
GRAVITY_TSE_URL = 'http://localhost:5001'
TECH_ANALYSIS_URL = 'http://localhost:5002'
CODAL_SERVICE_URL = 'http://localhost:5003'
FUNDAMENTAL_ANALYSIS_URL = 'http://localhost:5004'
```

### توسعه‌دهندگان

برای مشارکت در توسعه:

1. Fork کنید
2. یک branch جدید ایجاد کنید
3. تغییرات خود را commit کنید
4. Push کنید
5. Pull Request ایجاد کنید

### مجوز

این پروژه تحت مجوز MIT منتشر شده است.

### پشتیبانی

برای گزارش مشکلات یا پیشنهادات:
- Issue در GitHub ایجاد کنید
- یا با ایمیل تماس بگیرید

### تشکر

از تمامی توسعه‌دهندگانی که در ایجاد میکروسرویس‌های مورد استفاده مشارکت داشتند، تشکر می‌کنیم.

---

**نکته مهم**: این برنامه صرفاً برای اهداف آموزشی و تحلیلی است و نباید به عنوان توصیه سرمایه‌گذاری تلقی شود.

</div>
