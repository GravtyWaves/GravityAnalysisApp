# GravityAnalysisApp - Coding Standards & Guidelines

## Table of Contents
1. [Python Coding Standards](#python-coding-standards)
2. [JavaScript/Frontend Standards](#javascriptfrontend-standards)
3. [Database Standards](#database-standards)
4. [API Design Standards](#api-design-standards)
5. [Testing Standards](#testing-standards)
6. [Documentation Standards](#documentation-standards)
7. [Security Standards](#security-standards)
8. [Git & Version Control](#git--version-control)
9. [Code Review Checklist](#code-review-checklist)
10. [Performance Standards](#performance-standards)

---

## Python Coding Standards

### 1. General Rules
- **PEP 8 Compliance**: All Python code MUST follow PEP 8
- **Python Version**: Python 3.9+ required
- **Language**: English ONLY for all code, comments, variables, functions
- **Line Length**: Maximum 100 characters (not 79)
- **Encoding**: UTF-8 with BOM for all files

### 2. Naming Conventions

```python
# ✅ GOOD
class MarketDataService:  # PascalCase for classes
    """Service for market data operations"""
    
    def __init__(self, base_url: str):  # snake_case for functions/methods
        self.base_url = base_url  # snake_case for attributes
        self._cache = {}  # _prefix for internal/private
        self.MAX_RETRIES = 3  # UPPER_CASE for constants
    
    def get_symbol_price(self, symbol_code: str) -> Optional[Dict]:
        """snake_case for methods, type hints required"""
        pass

# ❌ BAD
class marketDataService:  # Wrong case
    def GetSymbolPrice(self, symbolCode):  # Wrong case, no type hints
        BASE_URL = 'http://localhost'  # Constant in method
```

### 3. Type Hints (MANDATORY)

```python
from typing import List, Dict, Optional, Union, Tuple

# ✅ GOOD - Complete type hints
def calculate_rsi(
    prices: List[float], 
    period: int = 14
) -> float:
    """Calculate RSI with type hints"""
    pass

def get_financial_data(
    symbol_code: str,
    years: int = 3
) -> Optional[Dict[str, Union[int, float, str]]]:
    """Return None if not found"""
    pass

# ❌ BAD - No type hints
def calculate_rsi(prices, period=14):
    pass
```

### 4. Docstrings (MANDATORY)

```python
# ✅ GOOD - Google style docstrings
def fetch_market_data(symbol_code: str, days: int = 30) -> Dict:
    """
    Fetch market data from GravityTSE microservice.
    
    This function calls the external GravityTSE service to retrieve
    historical price data for the specified symbol.
    
    Args:
        symbol_code: TSE symbol code (e.g., 'فملی', 'فولاد')
        days: Number of days of historical data (1-365)
    
    Returns:
        Dictionary containing market data with keys:
            - symbol_code: str
            - prices: List[Dict]
            - current_price: float
            - volume: int
    
    Raises:
        ValueError: If days is not in range 1-365
        ConnectionError: If microservice is unavailable
        HTTPError: If API returns error status
    
    Example:
        >>> data = fetch_market_data('فملی', days=7)
        >>> print(data['current_price'])
        5420
    
    Note:
        Requires GravityTSE microservice running on port 5001
    """
    if not 1 <= days <= 365:
        raise ValueError(f"days must be 1-365, got {days}")
    
    # Implementation...
```

### 5. Imports Organization

```python
# ✅ GOOD - Organized imports
# 1. Standard library
import os
import sys
from datetime import datetime, timedelta
from typing import List, Dict, Optional

# 2. Third-party
import requests
from flask import Flask, jsonify, request
from sqlalchemy import Column, Integer, String

# 3. Local application
from database.db_manager import DatabaseManager
from services.market_data_service import MarketDataService
from utils.validators import validate_symbol_code

# ❌ BAD
from flask import *  # Never use star imports
import requests, os, sys  # Don't combine imports
from services.market_data_service import MarketDataService
import os  # Duplicate
```

### 6. Error Handling

```python
# ✅ GOOD - Specific exceptions, proper logging
import logging

logger = logging.getLogger(__name__)

def get_symbol_data(symbol_code: str) -> Optional[Dict]:
    """Fetch symbol data with comprehensive error handling"""
    
    # Validate input
    if not symbol_code or len(symbol_code) > 10:
        raise ValueError(f"Invalid symbol code: {symbol_code}")
    
    try:
        response = requests.get(
            f'{BASE_URL}/api/symbols/{symbol_code}',
            timeout=10
        )
        response.raise_for_status()
        return response.json()
        
    except requests.Timeout:
        logger.error(f"Timeout fetching data for {symbol_code}")
        return None
        
    except requests.ConnectionError as e:
        logger.error(f"Connection error for {symbol_code}: {e}")
        return None
        
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            logger.warning(f"Symbol not found: {symbol_code}")
        else:
            logger.error(f"HTTP error {e.response.status_code}: {e}")
        return None
        
    except Exception as e:
        logger.exception(f"Unexpected error fetching {symbol_code}")
        raise  # Re-raise unexpected exceptions

# ❌ BAD - Bare except, no logging
def get_symbol_data_bad(symbol_code):
    try:
        return requests.get(f'{BASE_URL}/api/symbols/{symbol_code}').json()
    except:  # Too broad!
        return None  # Silent failure!
```

### 7. Class Structure

```python
# ✅ GOOD - Well-structured class
from abc import ABC, abstractmethod
from typing import List, Dict, Optional

class BaseService(ABC):
    """Abstract base class for all services"""
    
    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url
        self.timeout = timeout
        self._session = requests.Session()
    
    @abstractmethod
    def health_check(self) -> bool:
        """Check if service is healthy"""
        pass

class MarketDataService(BaseService):
    """Concrete service for market data"""
    
    # Class-level constants
    DEFAULT_PORT = 5001
    MAX_DAYS = 365
    
    def __init__(self, base_url: str = None):
        if base_url is None:
            base_url = f'http://localhost:{self.DEFAULT_PORT}'
        super().__init__(base_url)
    
    def health_check(self) -> bool:
        """Check GravityTSE service health"""
        try:
            response = self._session.get(
                f'{self.base_url}/health',
                timeout=5
            )
            return response.status_code == 200
        except:
            return False
    
    def get_symbols(self) -> List[Dict]:
        """Fetch all symbols"""
        # Implementation
        pass
```

---

## JavaScript/Frontend Standards

### 1. General Rules
- **ES6+**: Use modern JavaScript features
- **Strict Mode**: Always use `'use strict';`
- **No jQuery**: Use vanilla JS or modern frameworks
- **English Only**: All code, comments, variable names

### 2. Naming Conventions

```javascript
// ✅ GOOD
class SymbolChart {  // PascalCase for classes
    constructor(canvasId, options = {}) {
        this.canvasId = canvasId;  // camelCase for properties
        this.chart = null;
        this.DEFAULT_OPTIONS = {  // UPPER_CASE for constants
            responsive: true,
            maintainAspectRatio: false
        };
    }
    
    async loadPriceData(symbolCode) {  // camelCase for methods
        // Implementation
    }
    
    _renderChart(data) {  // _prefix for private methods
        // Implementation
    }
}

// Constants in separate file
const API_BASE_URL = 'http://localhost:5000';
const REQUEST_TIMEOUT = 30000;

// ❌ BAD
class symbol_chart {  // Wrong case
    constructor(canvasId, options) {
        this.CanvasId = canvasId;  // Inconsistent case
    }
}
```

### 3. Modern JavaScript Patterns

```javascript
// ✅ GOOD - Modern, clean, async/await
class ApiClient {
    constructor(baseUrl) {
        this.baseUrl = baseUrl;
    }
    
    async fetchSymbols() {
        try {
            const response = await axios.get(`${this.baseUrl}/api/symbols`);
            
            if (response.data.success) {
                return response.data.data;
            } else {
                throw new Error(response.data.error);
            }
        } catch (error) {
            console.error('Failed to fetch symbols:', error);
            this._showError('خطا در دریافت نمادها');
            return [];
        }
    }
    
    _showError(message) {
        // Use template literals
        const errorHtml = `
            <div class="alert alert-danger alert-dismissible fade show" role="alert">
                <strong>خطا!</strong> ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            </div>
        `;
        document.getElementById('errorContainer').innerHTML = errorHtml;
    }
}

// ❌ BAD - Old style, callbacks, concatenation
function fetchSymbols(callback) {
    $.ajax({
        url: 'http://localhost:5000/api/symbols',
        success: function(data) {
            callback(data);
        },
        error: function() {
            alert('Error!');  // Bad UX
        }
    });
}
```

### 4. DOM Manipulation

```javascript
// ✅ GOOD - Clean, efficient
class SymbolTable {
    constructor(tableId) {
        this.table = document.getElementById(tableId);
        this.tbody = this.table.querySelector('tbody');
    }
    
    render(symbols) {
        // Clear existing rows
        this.tbody.innerHTML = '';
        
        // Use DocumentFragment for better performance
        const fragment = document.createDocumentFragment();
        
        symbols.forEach(symbol => {
            const row = this._createRow(symbol);
            fragment.appendChild(row);
        });
        
        this.tbody.appendChild(fragment);
    }
    
    _createRow(symbol) {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${symbol.code}</td>
            <td>${symbol.name}</td>
            <td class="${symbol.change >= 0 ? 'text-success' : 'text-danger'}">
                ${symbol.change.toFixed(2)}%
            </td>
            <td>
                <button class="btn btn-sm btn-primary" data-symbol="${symbol.code}">
                    مشاهده
                </button>
            </td>
        `;
        return row;
    }
}

// ❌ BAD - Inefficient, repetitive
function renderSymbols(symbols) {
    $('#symbolTable tbody').empty();  // jQuery dependency
    symbols.forEach(symbol => {
        $('#symbolTable tbody').append(  // Multiple DOM operations
            '<tr><td>' + symbol.code + '</td></tr>'  // String concatenation
        );
    });
}
```

### 5. Event Handling

```javascript
// ✅ GOOD - Event delegation, clean handlers
class SymbolManager {
    constructor() {
        this.init();
    }
    
    init() {
        // Event delegation for dynamic elements
        document.getElementById('symbolTable').addEventListener('click', (e) => {
            if (e.target.matches('button[data-symbol]')) {
                const symbolCode = e.target.dataset.symbol;
                this.handleSymbolClick(symbolCode);
            }
        });
        
        // Form submission
        document.getElementById('searchForm').addEventListener('submit', (e) => {
            e.preventDefault();
            this.handleSearch();
        });
    }
    
    async handleSymbolClick(symbolCode) {
        console.log(`Symbol clicked: ${symbolCode}`);
        await this.loadSymbolDetails(symbolCode);
    }
}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new SymbolManager();
});

// ❌ BAD - Inline handlers, no delegation
// In HTML: <button onclick="handleClick('فملی')">  // Bad!
function handleClick(code) {
    // Global function pollution
}
```

---

## Database Standards

### 1. Schema Design

```python
from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

# ✅ GOOD - Proper schema with constraints
class Symbol(Base):
    """
    Symbol master table.
    Stores basic information about TSE symbols.
    """
    __tablename__ = 'symbols'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(10), nullable=False, unique=True, index=True)
    name = Column(String(100), nullable=False)
    industry = Column(String(50), nullable=True, index=True)
    
    # Metadata
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, 
                       onupdate=datetime.utcnow)
    
    __table_args__ = (
        Index('ix_code_industry', 'code', 'industry'),
    )
    
    def __repr__(self):
        return f"<Symbol(code='{self.code}', name='{self.name}')>"

class MarketData(Base):
    """Daily market data for symbols"""
    __tablename__ = 'market_data'
    
    id = Column(Integer, primary_key=True)
    symbol_id = Column(Integer, ForeignKey('symbols.id'), nullable=False, index=True)
    date = Column(Date, nullable=False, index=True)
    
    # OHLCV data with proper precision
    open_price = Column(Numeric(15, 2), nullable=False)
    high_price = Column(Numeric(15, 2), nullable=False)
    low_price = Column(Numeric(15, 2), nullable=False)
    close_price = Column(Numeric(15, 2), nullable=False)
    volume = Column(BigInteger, nullable=False)
    value = Column(BigInteger, nullable=False)
    
    __table_args__ = (
        UniqueConstraint('symbol_id', 'date', name='uix_symbol_date'),
        Index('ix_symbol_date_desc', 'symbol_id', desc('date')),
    )
```

### 2. Query Optimization

```python
# ✅ GOOD - Optimized queries
from sqlalchemy import func, and_

class MarketDataRepository:
    """Repository pattern for market data"""
    
    def __init__(self, session):
        self.session = session
    
    def get_recent_prices(self, symbol_code: str, days: int = 30) -> List[MarketData]:
        """
        Fetch recent prices with optimized query.
        Uses index on (symbol_id, date DESC).
        """
        # Join with symbols table
        # Use limit to reduce data transfer
        # Order by date descending
        return (
            self.session.query(MarketData)
            .join(Symbol)
            .filter(Symbol.code == symbol_code)
            .order_by(MarketData.date.desc())
            .limit(days)
            .all()
        )
    
    def get_price_statistics(self, symbol_code: str) -> Dict:
        """Aggregate query for statistics"""
        result = (
            self.session.query(
                func.max(MarketData.high_price).label('max_price'),
                func.min(MarketData.low_price).label('min_price'),
                func.avg(MarketData.close_price).label('avg_price'),
                func.sum(MarketData.volume).label('total_volume')
            )
            .join(Symbol)
            .filter(Symbol.code == symbol_code)
            .first()
        )
        
        return {
            'max_price': float(result.max_price),
            'min_price': float(result.min_price),
            'avg_price': float(result.avg_price),
            'total_volume': int(result.total_volume)
        }

# ❌ BAD - N+1 query problem
def get_symbols_with_latest_price():
    symbols = session.query(Symbol).all()
    result = []
    for symbol in symbols:
        # N+1 queries! Bad!
        latest = session.query(MarketData).filter(
            MarketData.symbol_id == symbol.id
        ).order_by(MarketData.date.desc()).first()
        result.append({'symbol': symbol, 'price': latest})
    return result

# ✅ GOOD - Single query with join
def get_symbols_with_latest_price():
    subquery = (
        session.query(
            MarketData.symbol_id,
            func.max(MarketData.date).label('max_date')
        )
        .group_by(MarketData.symbol_id)
        .subquery()
    )
    
    return (
        session.query(Symbol, MarketData)
        .join(subquery, Symbol.id == subquery.c.symbol_id)
        .join(MarketData, and_(
            MarketData.symbol_id == subquery.c.symbol_id,
            MarketData.date == subquery.c.max_date
        ))
        .all()
    )
```

---

## API Design Standards

### 1. RESTful Conventions

```python
# ✅ GOOD - RESTful API design
from flask import Blueprint, jsonify, request
from http import HTTPStatus

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/symbols', methods=['GET'])
def get_symbols():
    """
    GET /api/symbols
    List all symbols with optional filtering
    """
    # Query parameters for filtering
    industry = request.args.get('industry')
    search = request.args.get('search')
    
    symbols = symbol_service.get_symbols(industry=industry, search=search)
    
    return jsonify({
        'success': True,
        'data': symbols,
        'count': len(symbols)
    }), HTTPStatus.OK

@api.route('/symbols/<symbol_code>', methods=['GET'])
def get_symbol(symbol_code: str):
    """
    GET /api/symbols/{symbol_code}
    Get specific symbol details
    """
    symbol = symbol_service.get_symbol(symbol_code)
    
    if not symbol:
        return jsonify({
            'success': False,
            'error': f'Symbol {symbol_code} not found'
        }), HTTPStatus.NOT_FOUND
    
    return jsonify({
        'success': True,
        'data': symbol
    }), HTTPStatus.OK

@api.route('/symbols/<symbol_code>/price', methods=['GET'])
def get_symbol_price(symbol_code: str):
    """
    GET /api/symbols/{symbol_code}/price?days=30
    Get price data for symbol
    """
    days = request.args.get('days', default=30, type=int)
    
    if not 1 <= days <= 365:
        return jsonify({
            'success': False,
            'error': 'days must be between 1 and 365'
        }), HTTPStatus.BAD_REQUEST
    
    price_data = market_service.get_price_data(symbol_code, days)
    
    return jsonify({
        'success': True,
        'data': price_data
    }), HTTPStatus.OK

# ❌ BAD - Not RESTful
@app.route('/getSymbols')  # Should be GET /api/symbols
def get_symbols_bad():
    return symbol_service.get_symbols()  # No status code, no structure

@app.route('/symbolPrice')  # Missing resource hierarchy
def get_price_bad():
    code = request.args.get('code')  # Inconsistent parameter naming
    return prices  # No error handling
```

### 2. Response Format

```python
# ✅ GOOD - Consistent response structure
{
    "success": true,
    "data": {
        "symbol_code": "فملی",
        "name": "ملی صنایع مس ایران",
        "current_price": 5420,
        "price_change": 120,
        "price_change_percent": 2.26
    },
    "meta": {
        "timestamp": "2024-11-16T10:30:00Z",
        "version": "1.0.0"
    }
}

# Error response
{
    "success": false,
    "error": "Symbol not found",
    "error_code": "SYMBOL_NOT_FOUND",
    "meta": {
        "timestamp": "2024-11-16T10:30:00Z"
    }
}

# ❌ BAD - Inconsistent structure
# Success:
{"data": [...]}

# Error:
{"message": "Error occurred"}  # Different structure!
```

---

## Testing Standards

### 1. Test Structure

```python
# tests/test_market_data_service.py
import pytest
from unittest.mock import Mock, patch, MagicMock
from services.market_data_service import MarketDataService

class TestMarketDataService:
    """Test suite for MarketDataService"""
    
    @pytest.fixture
    def service(self):
        """Create service instance for testing"""
        return MarketDataService(base_url='http://test:5001')
    
    @pytest.fixture
    def mock_symbols_response(self):
        """Mock successful symbols API response"""
        mock = Mock()
        mock.status_code = 200
        mock.json.return_value = {
            'success': True,
            'data': [
                {'code': 'TEST1', 'name': 'Test Symbol 1'},
                {'code': 'TEST2', 'name': 'Test Symbol 2'}
            ]
        }
        return mock
    
    def test_get_symbols_success(self, service, mock_symbols_response):
        """Test successful symbol retrieval"""
        with patch('requests.get', return_value=mock_symbols_response):
            result = service.get_symbols()
            
            assert len(result) == 2
            assert result[0]['code'] == 'TEST1'
            assert result[1]['code'] == 'TEST2'
    
    def test_get_symbols_connection_error(self, service):
        """Test handling of connection errors"""
        with patch('requests.get', side_effect=ConnectionError('Connection failed')):
            result = service.get_symbols()
            
            # Should return empty list, not raise exception
            assert result == []
    
    def test_get_symbols_timeout(self, service):
        """Test handling of timeout"""
        with patch('requests.get', side_effect=Timeout('Request timeout')):
            result = service.get_symbols()
            
            assert result == []
    
    @pytest.mark.parametrize('status_code,expected', [
        (400, []),
        (404, []),
        (500, []),
        (503, [])
    ])
    def test_get_symbols_http_errors(self, service, status_code, expected):
        """Test handling of various HTTP error codes"""
        mock_response = Mock()
        mock_response.status_code = status_code
        mock_response.raise_for_status.side_effect = HTTPError()
        
        with patch('requests.get', return_value=mock_response):
            result = service.get_symbols()
            
            assert result == expected
```

### 2. Coverage Requirements

- **Minimum**: 80% overall coverage
- **Critical paths**: 100% coverage
- **Run coverage**:
  ```bash
  pytest --cov=. --cov-report=html --cov-report=term
  ```

---

## Documentation Standards

### 1. README.md Structure

```markdown
# Project Name

Brief one-line description

## Features
- Feature 1
- Feature 2

## Quick Start
(Get user running in < 5 minutes)

## Installation
(Detailed setup)

## Usage
(Examples)

## API Documentation
(Link to API docs)

## Contributing
(How to contribute)

## License
```

### 2. Code Comments

```python
# ✅ GOOD - Explain WHY, not WHAT
def calculate_eps(net_income: float, shares_outstanding: int) -> float:
    """Calculate Earnings Per Share"""
    
    # Avoid division by zero in case of stock buybacks completion
    if shares_outstanding == 0:
        return 0.0
    
    # EPS can be negative if company has net loss
    return net_income / shares_outstanding

# ❌ BAD - States the obvious
def calculate_eps(net_income, shares_outstanding):
    # Divide net income by shares outstanding
    return net_income / shares_outstanding
```

---

## Security Standards

1. **Input Validation**: Validate ALL user inputs
2. **SQL Injection**: Use parameterized queries ALWAYS
3. **XSS Prevention**: Sanitize outputs, use CSP headers
4. **Authentication**: Use JWT with proper expiration
5. **HTTPS**: Enforce HTTPS in production
6. **Secrets**: Never commit API keys, passwords
7. **Dependencies**: Keep all packages updated
8. **Error Messages**: Don't leak sensitive info

---

## Git & Version Control

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**: feat, fix, docs, style, refactor, test, chore

**Example**:
```
feat(market-data): integrate GravityTSE microservice

- Replace mock data with real API calls
- Add retry logic with exponential backoff
- Implement circuit breaker pattern
- Add comprehensive error handling

Closes #123
```

---

## Code Review Checklist

Before submitting PR:
- [ ] Code follows all standards above
- [ ] Unit tests written and passing
- [ ] Integration tests passing (if applicable)
- [ ] Code coverage ≥ 80%
- [ ] Documentation updated
- [ ] No hardcoded values
- [ ] Error handling complete
- [ ] Security review passed
- [ ] Performance acceptable
- [ ] Self-reviewed code

---

## Performance Standards

- API Response Time: < 2 seconds (p95)
- Database Queries: < 100ms (simple), < 500ms (complex)
- Frontend Load: < 3 seconds (First Contentful Paint)
- Memory Usage: < 512MB (per service)
- Test Execution: < 60 seconds (full suite)

---

**Version**: 1.0.0  
**Last Updated**: 2024-11-16  
**Maintained by**: Technical Writing Team
