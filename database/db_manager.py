"""
Database models for Gravity Analysis App
"""
import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Any, Optional


class DatabaseManager:
    """Manage SQLite database operations"""
    
    def __init__(self, db_path: str = 'gravity_analysis.db'):
        self.db_path = db_path
        
    def get_connection(self):
        """Get database connection"""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_db(self):
        """Initialize database tables"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Symbols table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS symbols (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT UNIQUE NOT NULL,
                name TEXT NOT NULL,
                name_en TEXT,
                company_name TEXT,
                industry TEXT,
                sector TEXT,
                market TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Market data table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS market_data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol_code TEXT NOT NULL,
                date DATE NOT NULL,
                open REAL,
                high REAL,
                low REAL,
                close REAL,
                volume INTEGER,
                value REAL,
                trades INTEGER,
                yesterday_price REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (symbol_code) REFERENCES symbols (code),
                UNIQUE(symbol_code, date)
            )
        ''')
        
        # Financial reports table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS financial_reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol_code TEXT NOT NULL,
                report_type TEXT NOT NULL,
                period TEXT NOT NULL,
                year INTEGER NOT NULL,
                mhtml_file TEXT,
                data TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (symbol_code) REFERENCES symbols (code)
            )
        ''')
        
        # Balance sheet table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS balance_sheet (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol_code TEXT NOT NULL,
                report_id INTEGER,
                period TEXT NOT NULL,
                year INTEGER NOT NULL,
                total_assets REAL,
                current_assets REAL,
                non_current_assets REAL,
                total_liabilities REAL,
                current_liabilities REAL,
                non_current_liabilities REAL,
                equity REAL,
                data TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (symbol_code) REFERENCES symbols (code),
                FOREIGN KEY (report_id) REFERENCES financial_reports (id)
            )
        ''')
        
        # Income statement table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS income_statement (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol_code TEXT NOT NULL,
                report_id INTEGER,
                period TEXT NOT NULL,
                year INTEGER NOT NULL,
                revenue REAL,
                cost_of_goods_sold REAL,
                gross_profit REAL,
                operating_expenses REAL,
                operating_income REAL,
                net_income REAL,
                eps REAL,
                data TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (symbol_code) REFERENCES symbols (code),
                FOREIGN KEY (report_id) REFERENCES financial_reports (id)
            )
        ''')
        
        # Cash flow table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cash_flow (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol_code TEXT NOT NULL,
                report_id INTEGER,
                period TEXT NOT NULL,
                year INTEGER NOT NULL,
                operating_cash_flow REAL,
                investing_cash_flow REAL,
                financing_cash_flow REAL,
                net_cash_flow REAL,
                data TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (symbol_code) REFERENCES symbols (code),
                FOREIGN KEY (report_id) REFERENCES financial_reports (id)
            )
        ''')
        
        # Technical analysis results table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS technical_analysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol_code TEXT NOT NULL,
                analysis_date DATE NOT NULL,
                indicators TEXT,
                signals TEXT,
                summary TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (symbol_code) REFERENCES symbols (code)
            )
        ''')
        
        # Fundamental analysis results table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS fundamental_analysis (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol_code TEXT NOT NULL,
                analysis_date DATE NOT NULL,
                ratios TEXT,
                valuation TEXT,
                summary TEXT,
                score REAL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (symbol_code) REFERENCES symbols (code)
            )
        ''')
        
        # Create indexes
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_market_data_symbol ON market_data(symbol_code)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_market_data_date ON market_data(date)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_financial_reports_symbol ON financial_reports(symbol_code)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_technical_analysis_symbol ON technical_analysis(symbol_code)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_fundamental_analysis_symbol ON fundamental_analysis(symbol_code)')
        
        conn.commit()
        conn.close()
        
        print("Database initialized successfully!")
    
    def add_symbol(self, code: str, name: str, **kwargs) -> bool:
        """Add a new symbol"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT OR REPLACE INTO symbols 
                (code, name, name_en, company_name, industry, sector, market, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            ''', (
                code, name,
                kwargs.get('name_en'),
                kwargs.get('company_name'),
                kwargs.get('industry'),
                kwargs.get('sector'),
                kwargs.get('market')
            ))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error adding symbol: {e}")
            return False
    
    def get_all_symbols(self) -> List[Dict]:
        """Get all symbols"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM symbols ORDER BY code')
        rows = cursor.fetchall()
        
        conn.close()
        
        return [dict(row) for row in rows]
    
    def get_symbol_data(self, symbol_code: str) -> Optional[Dict]:
        """Get symbol data"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM symbols WHERE code = ?', (symbol_code,))
        row = cursor.fetchone()
        
        conn.close()
        
        return dict(row) if row else None
    
    def save_market_data(self, symbol_code: str, data: List[Dict]) -> bool:
        """Save market data"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            for item in data:
                cursor.execute('''
                    INSERT OR REPLACE INTO market_data
                    (symbol_code, date, open, high, low, close, volume, value, trades, yesterday_price)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    symbol_code,
                    item.get('date'),
                    item.get('open'),
                    item.get('high'),
                    item.get('low'),
                    item.get('close'),
                    item.get('volume'),
                    item.get('value'),
                    item.get('trades'),
                    item.get('yesterday_price')
                ))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error saving market data: {e}")
            return False
    
    def get_price_history(self, symbol_code: str, days: int = 365) -> List[Dict]:
        """Get price history"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM market_data 
            WHERE symbol_code = ?
            ORDER BY date DESC
            LIMIT ?
        ''', (symbol_code, days))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def save_financial_data(self, data: Dict) -> bool:
        """Save financial report data"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            # Save financial report
            cursor.execute('''
                INSERT INTO financial_reports
                (symbol_code, report_type, period, year, mhtml_file, data)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                data.get('symbol_code'),
                data.get('report_type'),
                data.get('period'),
                data.get('year'),
                data.get('mhtml_file'),
                json.dumps(data.get('raw_data', {}), ensure_ascii=False)
            ))
            
            report_id = cursor.lastrowid
            
            # Save balance sheet
            if 'balance_sheet' in data:
                bs = data['balance_sheet']
                cursor.execute('''
                    INSERT INTO balance_sheet
                    (symbol_code, report_id, period, year, total_assets, current_assets,
                     non_current_assets, total_liabilities, current_liabilities,
                     non_current_liabilities, equity, data)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    data.get('symbol_code'),
                    report_id,
                    data.get('period'),
                    data.get('year'),
                    bs.get('total_assets'),
                    bs.get('current_assets'),
                    bs.get('non_current_assets'),
                    bs.get('total_liabilities'),
                    bs.get('current_liabilities'),
                    bs.get('non_current_liabilities'),
                    bs.get('equity'),
                    json.dumps(bs, ensure_ascii=False)
                ))
            
            # Save income statement
            if 'income_statement' in data:
                inc = data['income_statement']
                cursor.execute('''
                    INSERT INTO income_statement
                    (symbol_code, report_id, period, year, revenue, cost_of_goods_sold,
                     gross_profit, operating_expenses, operating_income, net_income, eps, data)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    data.get('symbol_code'),
                    report_id,
                    data.get('period'),
                    data.get('year'),
                    inc.get('revenue'),
                    inc.get('cost_of_goods_sold'),
                    inc.get('gross_profit'),
                    inc.get('operating_expenses'),
                    inc.get('operating_income'),
                    inc.get('net_income'),
                    inc.get('eps'),
                    json.dumps(inc, ensure_ascii=False)
                ))
            
            # Save cash flow
            if 'cash_flow' in data:
                cf = data['cash_flow']
                cursor.execute('''
                    INSERT INTO cash_flow
                    (symbol_code, report_id, period, year, operating_cash_flow,
                     investing_cash_flow, financing_cash_flow, net_cash_flow, data)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    data.get('symbol_code'),
                    report_id,
                    data.get('period'),
                    data.get('year'),
                    cf.get('operating_cash_flow'),
                    cf.get('investing_cash_flow'),
                    cf.get('financing_cash_flow'),
                    cf.get('net_cash_flow'),
                    json.dumps(cf, ensure_ascii=False)
                ))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error saving financial data: {e}")
            return False
    
    def get_financial_data(self, symbol_code: str) -> Optional[Dict]:
        """Get financial data for a symbol"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Get latest financial report
        cursor.execute('''
            SELECT * FROM financial_reports
            WHERE symbol_code = ?
            ORDER BY year DESC, period DESC
            LIMIT 1
        ''', (symbol_code,))
        
        report = cursor.fetchone()
        
        if not report:
            conn.close()
            return None
        
        report_id = report['id']
        
        # Get balance sheet
        cursor.execute('''
            SELECT * FROM balance_sheet
            WHERE report_id = ?
        ''', (report_id,))
        balance_sheet = cursor.fetchone()
        
        # Get income statement
        cursor.execute('''
            SELECT * FROM income_statement
            WHERE report_id = ?
        ''', (report_id,))
        income_statement = cursor.fetchone()
        
        # Get cash flow
        cursor.execute('''
            SELECT * FROM cash_flow
            WHERE report_id = ?
        ''', (report_id,))
        cash_flow = cursor.fetchone()
        
        conn.close()
        
        return {
            'report': dict(report),
            'balance_sheet': dict(balance_sheet) if balance_sheet else None,
            'income_statement': dict(income_statement) if income_statement else None,
            'cash_flow': dict(cash_flow) if cash_flow else None
        }
    
    def save_technical_analysis(self, symbol_code: str, analysis: Dict) -> bool:
        """Save technical analysis results"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO technical_analysis
                (symbol_code, analysis_date, indicators, signals, summary)
                VALUES (?, DATE('now'), ?, ?, ?)
            ''', (
                symbol_code,
                json.dumps(analysis.get('indicators', {}), ensure_ascii=False),
                json.dumps(analysis.get('signals', {}), ensure_ascii=False),
                json.dumps(analysis.get('summary', {}), ensure_ascii=False)
            ))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error saving technical analysis: {e}")
            return False
    
    def save_fundamental_analysis(self, symbol_code: str, analysis: Dict) -> bool:
        """Save fundamental analysis results"""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO fundamental_analysis
                (symbol_code, analysis_date, ratios, valuation, summary, score)
                VALUES (?, DATE('now'), ?, ?, ?, ?)
            ''', (
                symbol_code,
                json.dumps(analysis.get('ratios', {}), ensure_ascii=False),
                json.dumps(analysis.get('valuation', {}), ensure_ascii=False),
                json.dumps(analysis.get('summary', {}), ensure_ascii=False),
                analysis.get('score')
            ))
            
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Error saving fundamental analysis: {e}")
            return False
    
    def search_symbols(self, query: str) -> List[Dict]:
        """Search symbols by code or name"""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        search_pattern = f'%{query}%'
        cursor.execute('''
            SELECT * FROM symbols
            WHERE code LIKE ? OR name LIKE ? OR company_name LIKE ?
            ORDER BY code
            LIMIT 20
        ''', (search_pattern, search_pattern, search_pattern))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
