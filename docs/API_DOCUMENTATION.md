# API Documentation - Gravity Analysis App

## Base URL
```
http://localhost:5000
```

## Authentication
Currently, the API does not require authentication (for development purposes).

---

## Market Data Endpoints

### Get All Symbols
```http
GET /api/market/symbols
```

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "code": "فولاد",
      "name": "فولاد مبارکه اصفهان",
      "name_en": "Mobarakeh Steel Company",
      "industry": "فلزات اساسی",
      "sector": "صنعت",
      "market": "بورس"
    }
  ]
}
```

### Get Price Data
```http
GET /api/market/price/{symbol_code}?days=30
```

**Parameters:**
- `symbol_code` (path): نماد سهم
- `days` (query, optional): تعداد روزها (پیش‌فرض: 30)

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "date": "2024-01-15",
      "open": 10450,
      "high": 10650,
      "low": 10350,
      "close": 10500,
      "volume": 1500000,
      "value": 15750000000,
      "trades": 650
    }
  ]
}
```

### Update Market Data
```http
POST /api/market/update/{symbol_code}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "symbol_code": "فولاد",
    "last_price": 10500,
    "last_change": 150,
    "last_change_percent": 1.45,
    "timestamp": "2024-01-15T14:30:00"
  }
}
```

---

## Technical Analysis Endpoints

### Analyze Symbol
```http
GET /api/technical/analyze/{symbol_code}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "indicators": {
      "RSI": {
        "value": 52.34,
        "signal": "خنثی",
        "overbought": 70,
        "oversold": 30
      },
      "MACD": {
        "macd": 45.23,
        "signal": 42.15,
        "histogram": 3.08,
        "trend": "خرید"
      },
      "MA": {
        "MA5": 10450,
        "MA10": 10380,
        "MA20": 10320,
        "MA50": 10150,
        "current_price": 10500
      },
      "BB": {
        "upper": 10800,
        "middle": 10500,
        "lower": 10200,
        "signal": "خنثی"
      }
    },
    "signals": {
      "buy": 2,
      "sell": 1,
      "neutral": 2
    },
    "summary": {
      "overall_signal": "خرید",
      "strength": 65.5,
      "buy_signals": 2,
      "sell_signals": 1
    }
  }
}
```

### Get Specific Indicators
```http
GET /api/technical/indicators/{symbol_code}?indicators=RSI,MACD
```

**Parameters:**
- `indicators` (query): لیست اندیکاتورها (RSI, MACD, MA, BB, STOCH)

**Response:**
```json
{
  "success": true,
  "data": {
    "RSI": { ... },
    "MACD": { ... }
  }
}
```

---

## File Upload Endpoints

### Upload MHTML File
```http
POST /api/upload/mhtml
Content-Type: multipart/form-data
```

**Form Data:**
- `file`: فایل MHTML

**Response:**
```json
{
  "success": true,
  "message": "فایل با موفقیت آپلود و پردازش شد",
  "data": {
    "symbol_code": "فولاد",
    "report_type": "ترازنامه",
    "period": "سال مالی",
    "year": 1402
  }
}
```

---

## Fundamental Analysis Endpoints

### Analyze Symbol
```http
GET /api/fundamental/analyze/{symbol_code}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "ratios": {
      "liquidity": {
        "current_ratio": 2.0,
        "quick_ratio": 1.5
      },
      "profitability": {
        "gross_margin": 40.0,
        "operating_margin": 25.0,
        "net_margin": 20.0,
        "roa": 15.5,
        "roe": 22.3
      },
      "leverage": {
        "debt_to_equity": 1.14,
        "debt_to_assets": 0.53
      },
      "efficiency": {
        "asset_turnover": 1.33
      },
      "per_share": {
        "eps": 1250
      }
    },
    "valuation": {
      "eps": 1250,
      "book_value_per_share": 700
    },
    "score": 75.5,
    "summary": {
      "rating": "خوب",
      "score": 75.5,
      "recommendation": "سهام مناسب برای سرمایه‌گذاری",
      "strengths": [
        "بازده بالای حقوق صاحبان سهام",
        "نقدینگی بسیار خوب"
      ],
      "weaknesses": []
    }
  }
}
```

### Get Financial Ratios
```http
GET /api/fundamental/ratios/{symbol_code}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "liquidity": { ... },
    "profitability": { ... },
    "leverage": { ... },
    "efficiency": { ... }
  }
}
```

---

## Search Endpoint

### Search Symbols
```http
GET /api/search?q={query}
```

**Parameters:**
- `q` (query): عبارت جستجو (حداقل 2 کاراکتر)

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "code": "فولاد",
      "name": "فولاد مبارکه اصفهان",
      "industry": "فلزات اساسی"
    }
  ]
}
```

---

## Error Responses

### 404 Not Found
```json
{
  "success": false,
  "error": "اطلاعات مالی برای این نماد یافت نشد"
}
```

### 400 Bad Request
```json
{
  "success": false,
  "error": "فایلی انتخاب نشده است"
}
```

### 500 Internal Server Error
```json
{
  "success": false,
  "error": "خطا در پردازش درخواست"
}
```

---

## Rate Limiting
Currently, there are no rate limits (for development purposes).

## Notes
- تمام پاسخ‌ها به صورت JSON هستند
- تمام تاریخ‌ها به فرمت ISO 8601 هستند
- قیمت‌ها به ریال هستند
- درصدها به صورت عدد اعشاری هستند (مثلاً 1.45 برای 1.45%)
