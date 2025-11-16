"""
Sample data loader for testing
This script adds sample symbols and data to the database
"""

from database.db_manager import DatabaseManager
from datetime import datetime, timedelta
import random

def add_sample_symbols():
    """Add sample symbols to database"""
    db = DatabaseManager()
    
    symbols = [
        {
            'code': 'فولاد',
            'name': 'فولاد مبارکه اصفهان',
            'name_en': 'Mobarakeh Steel Company',
            'company_name': 'شرکت فولاد مبارکه اصفهان',
            'industry': 'فلزات اساسی',
            'sector': 'صنعت',
            'market': 'بورس'
        },
        {
            'code': 'شپنا',
            'name': 'پالایش نفت اصفهان',
            'name_en': 'Isfahan Oil Refining',
            'company_name': 'شرکت پالایش نفت اصفهان',
            'industry': 'فرآورده‌های نفتی',
            'sector': 'صنعت',
            'market': 'بورس'
        },
        {
            'code': 'خودرو',
            'name': 'ایران خودرو',
            'name_en': 'Iran Khodro',
            'company_name': 'شرکت ایران خودرو',
            'industry': 'خودرو و ساخت قطعات',
            'sector': 'صنعت',
            'market': 'بورس'
        },
        {
            'code': 'وبملت',
            'name': 'بانک ملت',
            'name_en': 'Bank Mellat',
            'company_name': 'بانک ملت',
            'industry': 'بانک‌ها و موسسات اعتباری',
            'sector': 'مالی',
            'market': 'بورس'
        },
        {
            'code': 'کگل',
            'name': 'گل گهر',
            'name_en': 'Gol Gohar',
            'company_name': 'شرکت معدنی و صنعتی گل گهر',
            'industry': 'استخراج کانه‌های فلزی',
            'sector': 'معدن',
            'market': 'بورس'
        },
        {
            'code': 'شستا',
            'name': 'سرمایه گذاری تامین اجتماعی',
            'name_en': 'Shasta',
            'company_name': 'شرکت سرمایه گذاری تامین اجتماعی',
            'industry': 'سرمایه گذاری',
            'sector': 'مالی',
            'market': 'بورس'
        },
        {
            'code': 'شبندر',
            'name': 'بیمه ایران',
            'name_en': 'Iran Insurance',
            'company_name': 'شرکت بیمه ایران',
            'industry': 'بیمه',
            'sector': 'مالی',
            'market': 'بورس'
        },
        {
            'code': 'وتجارت',
            'name': 'بانک تجارت',
            'name_en': 'Bank Tejarat',
            'company_name': 'بانک تجارت',
            'industry': 'بانک‌ها و موسسات اعتباری',
            'sector': 'مالی',
            'market': 'بورس'
        }
    ]
    
    print("Adding sample symbols...")
    for symbol in symbols:
        db.add_symbol(**symbol)
        print(f"  ✓ Added: {symbol['code']} - {symbol['name']}")
    
    print(f"\n✓ {len(symbols)} symbols added successfully!")
    return symbols

def add_sample_market_data():
    """Add sample market data"""
    db = DatabaseManager()
    
    symbols = ['فولاد', 'شپنا', 'خودرو']
    
    print("\nAdding sample market data...")
    
    for symbol in symbols:
        data = []
        base_price = random.randint(8000, 15000)
        
        for i in range(60):  # 60 days of data
            date = datetime.now() - timedelta(days=60-i)
            
            # Generate realistic price movement
            change = random.randint(-200, 200)
            base_price = max(base_price + change, base_price * 0.95)  # Max 5% drop
            
            volume = random.randint(500000, 3000000)
            
            data.append({
                'date': date.strftime('%Y-%m-%d'),
                'open': base_price - random.randint(0, 100),
                'high': base_price + random.randint(0, 200),
                'low': base_price - random.randint(0, 150),
                'close': base_price,
                'volume': volume,
                'value': base_price * volume,
                'trades': random.randint(300, 1000),
                'yesterday_price': base_price - change
            })
        
        db.save_market_data(symbol, data)
        print(f"  ✓ Added market data for: {symbol} ({len(data)} days)")
    
    print("\n✓ Market data added successfully!")

def add_sample_financial_data():
    """Add sample financial data"""
    db = DatabaseManager()
    
    financial_data = {
        'symbol_code': 'فولاد',
        'report_type': 'ترازنامه',
        'period': 'سال مالی',
        'year': 1402,
        'mhtml_file': 'sample_report.mhtml',
        'balance_sheet': {
            'total_assets': 1500000000000,
            'current_assets': 600000000000,
            'non_current_assets': 900000000000,
            'total_liabilities': 800000000000,
            'current_liabilities': 300000000000,
            'non_current_liabilities': 500000000000,
            'equity': 700000000000
        },
        'income_statement': {
            'revenue': 2000000000000,
            'cost_of_goods_sold': 1200000000000,
            'gross_profit': 800000000000,
            'operating_expenses': 300000000000,
            'operating_income': 500000000000,
            'net_income': 400000000000,
            'eps': 1250
        },
        'cash_flow': {
            'operating_cash_flow': 350000000000,
            'investing_cash_flow': -150000000000,
            'financing_cash_flow': -100000000000,
            'net_cash_flow': 100000000000
        },
        'raw_data': {
            'parsed': True,
            'sample': True
        }
    }
    
    print("\nAdding sample financial data...")
    db.save_financial_data(financial_data)
    print(f"  ✓ Added financial data for: {financial_data['symbol_code']}")
    print("\n✓ Financial data added successfully!")

def main():
    """Load all sample data"""
    print("="*60)
    print("Loading Sample Data - Gravity Analysis App")
    print("="*60)
    print()
    
    try:
        # Initialize database
        db = DatabaseManager()
        db.init_db()
        print("✓ Database initialized\n")
        
        # Add sample data
        add_sample_symbols()
        add_sample_market_data()
        add_sample_financial_data()
        
        print()
        print("="*60)
        print("✅ Sample data loaded successfully!")
        print("="*60)
        print()
        print("You can now:")
        print("  1. Run 'python app.py' to start the server")
        print("  2. Visit http://localhost:5000")
        print("  3. Explore the sample data")
        print()
        
    except Exception as e:
        print(f"\n❌ Error loading sample data: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
