# راهنمای نصب گام به گام

## پیش‌نیازها

قبل از شروع، مطمئن شوید که موارد زیر نصب شده‌اند:

- ✅ **Python 3.8 یا بالاتر**
  - دانلود از: https://www.python.org/downloads/
  - در هنگام نصب، گزینه "Add Python to PATH" را فعال کنید

- ✅ **Git** (اختیاری، برای clone کردن پروژه)
  - دانلود از: https://git-scm.com/downloads

- ✅ **یک ویرایشگر کد** (اختیاری اما توصیه می‌شود)
  - VS Code، PyCharm، یا هر ویرایشگر دیگر

---

## روش 1: نصب خودکار (توصیه می‌شود) ⚡

### مرحله 1: دانلود پروژه

با Git:
```powershell
git clone https://github.com/GravtyWaves/GravityAnalysisApp.git
cd GravityAnalysisApp
```

یا دانلود مستقیم:
- فایل ZIP پروژه را دانلود کنید
- آن را Extract کنید
- وارد پوشه پروژه شوید

### مرحله 2: اجرای اسکریپت نصب

```powershell
.\setup.ps1
```

اسکریپت به صورت خودکار:
- محیط مجازی ایجاد می‌کند
- وابستگی‌ها را نصب می‌کند
- دیتابیس را راه‌اندازی می‌کند

### مرحله 3: بارگذاری داده‌های نمونه (اختیاری)

```powershell
python load_sample_data.py
```

### مرحله 4: اجرای برنامه

```powershell
.\run.ps1
```

یا:
```powershell
python app.py
```

### مرحله 5: مشاهده برنامه

مرورگر خود را باز کنید و به آدرس زیر بروید:
```
http://localhost:5000
```

✅ **تمام! برنامه شما آماده است.**

---

## روش 2: نصب دستی 🔧

### مرحله 1: دانلود پروژه
همانند روش 1

### مرحله 2: ایجاد محیط مجازی

```powershell
# ایجاد محیط مجازی
python -m venv venv
```

### مرحله 3: فعال‌سازی محیط مجازی

```powershell
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# یا Windows CMD
venv\Scripts\activate.bat
```

**نکته**: اگر با خطای Execution Policy مواجه شدید:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### مرحله 4: نصب وابستگی‌ها

```powershell
pip install -r requirements.txt
```

این فرآیند ممکن است چند دقیقه طول بکشد.

### مرحله 5: راه‌اندازی دیتابیس

```powershell
python -c "from database.db_manager import DatabaseManager; DatabaseManager().init_db()"
```

یا:
```powershell
python
>>> from database.db_manager import DatabaseManager
>>> db = DatabaseManager()
>>> db.init_db()
>>> exit()
```

### مرحله 6: بارگذاری داده‌های نمونه (اختیاری)

```powershell
python load_sample_data.py
```

### مرحله 7: اجرای برنامه

```powershell
python app.py
```

پیام زیر را باید ببینید:
```
 * Running on http://0.0.0.0:5000
 * Restarting with stat
```

### مرحله 8: مشاهده برنامه

مرورگر خود را باز کنید:
```
http://localhost:5000
```

---

## تست نصب

برای اطمینان از نصب صحیح، تست‌ها را اجرا کنید:

```powershell
python test_app.py
```

باید پیام "All tests passed! 🎉" را ببینید.

---

## رفع مشکلات رایج

### مشکل 1: Python یافت نشد
**علت**: Python در PATH نیست

**راه حل**:
1. Python را دوباره نصب کنید
2. در هنگام نصب، "Add Python to PATH" را فعال کنید
3. یا به صورت دستی Python را به PATH اضافه کنید

### مشکل 2: خطای Execution Policy
**علت**: PowerShell اجازه اجرای اسکریپت را نمی‌دهد

**راه حل**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### مشکل 3: خطای نصب کتابخانه
**علت**: مشکل در اتصال اینترنت یا pip

**راه حل**:
```powershell
# به‌روزرسانی pip
python -m pip install --upgrade pip

# نصب مجدد با verbose
pip install -r requirements.txt --verbose
```

### مشکل 4: پورت 5000 در حال استفاده است
**علت**: برنامه دیگری از پورت 5000 استفاده می‌کند

**راه حل**:
در فایل `app.py` پورت را تغییر دهید:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # پورت 5001
```

### مشکل 5: خطای Import
**علت**: محیط مجازی فعال نیست

**راه حل**:
```powershell
.\venv\Scripts\Activate.ps1
```

---

## دستورات مفید

### فعال‌سازی محیط مجازی
```powershell
.\venv\Scripts\Activate.ps1
```

### غیرفعال کردن محیط مجازی
```powershell
deactivate
```

### پاک کردن دیتابیس
```powershell
Remove-Item gravity_analysis.db
python -c "from database.db_manager import DatabaseManager; DatabaseManager().init_db()"
```

### مشاهده لاگ‌ها
برنامه را با verbose mode اجرا کنید:
```powershell
python app.py --debug
```

---

## نصب در سیستم‌های دیگر

### Linux/Mac

```bash
# ایجاد محیط مجازی
python3 -m venv venv

# فعال‌سازی
source venv/bin/activate

# نصب وابستگی‌ها
pip install -r requirements.txt

# راه‌اندازی دیتابیس
python -c "from database.db_manager import DatabaseManager; DatabaseManager().init_db()"

# اجرا
python app.py
```

---

## مراحل بعدی

پس از نصب موفق:

1. ✅ **داشبورد را بررسی کنید**: http://localhost:5000
2. ✅ **نمادها را مشاهده کنید**: /symbols
3. ✅ **تحلیل تکنیکال را امتحان کنید**: انتخاب یک نماد
4. ✅ **گزارش مالی آپلود کنید**: /upload
5. ✅ **تحلیل بنیادی را مشاهده کنید**

---

## کمک و پشتیبانی

اگر با مشکلی مواجه شدید:

1. مستندات را بخوانید: `README_FA.md`
2. API documentation: `API_DOCUMENTATION.md`
3. ساختار پروژه: `PROJECT_STRUCTURE.md`
4. Issue در GitHub ایجاد کنید

---

## به‌روزرسانی برنامه

```powershell
# دریافت آخرین تغییرات
git pull

# به‌روزرسانی وابستگی‌ها
pip install -r requirements.txt --upgrade

# به‌روزرسانی دیتابیس (در صورت نیاز)
python -c "from database.db_manager import DatabaseManager; DatabaseManager().init_db()"
```

---

**نکته مهم**: این برنامه برای محیط توسعه (Development) طراحی شده است. برای استفاده در محیط تولید (Production)، تنظیمات امنیتی و عملکردی بیشتری نیاز است.

**موفق باشید! 🚀**
