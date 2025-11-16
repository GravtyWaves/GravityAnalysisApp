"""
Test script for Gravity Analysis App
Run this to test the basic functionality
"""

from database.db_manager import DatabaseManager
from services.market_data_service import MarketDataService
from services.technical_analysis_service import TechnicalAnalysisService
from services.fundamental_analysis_service import FundamentalAnalysisService

def test_database():
    """Test database initialization"""
    print("Testing Database...")
    db = DatabaseManager()
    db.init_db()
    
    # Add test symbol
    db.add_symbol('فولاد', 'فولاد مبارکه اصفهان', 
                  name_en='Mobarakeh Steel',
                  industry='فلزات اساسی',
                  sector='صنعت',
                  market='بورس')
    
    symbols = db.get_all_symbols()
    print(f"✓ Database OK - {len(symbols)} symbols found")
    return True

def test_market_service():
    """Test market data service"""
    print("\nTesting Market Data Service...")
    service = MarketDataService()
    
    symbols = service.get_symbols()
    print(f"✓ Market Service OK - {len(symbols)} symbols")
    
    price_data = service.get_price_data('فولاد', 10)
    print(f"✓ Price Data OK - {len(price_data)} days")
    return True

def test_technical_service():
    """Test technical analysis service"""
    print("\nTesting Technical Analysis Service...")
    service = TechnicalAnalysisService()
    market_service = MarketDataService()
    
    price_data = market_service.get_price_data('فولاد', 60)
    analysis = service.analyze(price_data)
    
    if 'indicators' in analysis and 'summary' in analysis:
        print(f"✓ Technical Analysis OK")
        print(f"  - Overall Signal: {analysis['summary'].get('overall_signal', 'N/A')}")
        print(f"  - RSI: {analysis['indicators'].get('RSI', {}).get('value', 'N/A')}")
        return True
    return False

def test_fundamental_service():
    """Test fundamental analysis service"""
    print("\nTesting Fundamental Analysis Service...")
    service = FundamentalAnalysisService()
    
    # Mock financial data
    financial_data = {
        'balance_sheet': {
            'total_assets': 1500000000000,
            'current_assets': 600000000000,
            'equity': 700000000000,
            'total_liabilities': 800000000000,
            'current_liabilities': 300000000000
        },
        'income_statement': {
            'revenue': 2000000000000,
            'gross_profit': 800000000000,
            'operating_income': 500000000000,
            'net_income': 400000000000,
            'eps': 1250
        },
        'cash_flow': {
            'operating_cash_flow': 350000000000
        }
    }
    
    ratios = service.calculate_ratios(financial_data)
    
    if 'liquidity' in ratios and 'profitability' in ratios:
        print(f"✓ Fundamental Analysis OK")
        print(f"  - Current Ratio: {ratios['liquidity'].get('current_ratio', 'N/A')}")
        print(f"  - ROE: {ratios['profitability'].get('roe', 'N/A')}%")
        return True
    return False

def main():
    """Run all tests"""
    print("="*50)
    print("Gravity Analysis App - Test Suite")
    print("="*50)
    
    tests = [
        ("Database", test_database),
        ("Market Service", test_market_service),
        ("Technical Analysis", test_technical_service),
        ("Fundamental Analysis", test_fundamental_service)
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"✗ {name} Failed: {e}")
            results.append((name, False))
    
    print("\n" + "="*50)
    print("Test Results:")
    print("="*50)
    
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status} - {name}")
    
    passed = sum(1 for _, r in results if r)
    total = len(results)
    
    print("\n" + "="*50)
    print(f"Total: {passed}/{total} tests passed")
    print("="*50)
    
    if passed == total:
        print("\n🎉 All tests passed! The application is ready to use.")
        print("Run 'python app.py' to start the server.")
    else:
        print("\n⚠ Some tests failed. Please check the errors above.")

if __name__ == '__main__':
    main()
