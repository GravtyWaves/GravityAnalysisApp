"""
Market Data Service
Integrates with GravityTSE microservice
Repository: https://github.com/GravityWavesMl/GravityTSE

IMPORTANT: This service requires GravityTSE microservice to be running on port 5001
"""
import requests
from typing import List, Dict, Optional


class MarketDataService:
    """Service for fetching market data from TSE via GravityTSE microservice"""
    
    def __init__(self, base_url: str = 'http://localhost:5001'):
        self.base_url = base_url
        self.timeout = 30
    
    def get_symbols(self) -> List[Dict]:
        """GET /api/symbols"""
        try:
            print(f"🔄 GravityTSE: GET {self.base_url}/api/symbols")
            response = requests.get(f'{self.base_url}/api/symbols', timeout=self.timeout)
            
            if response.status_code == 200:
                data = response.json().get('data', [])
                print(f"✅ Received {len(data)} symbols")
                return data
            else:
                print(f"⚠️  Status {response.status_code}")
                return []
        except requests.exceptions.ConnectionError:
            print(f"❌ Cannot connect to GravityTSE at {self.base_url}")
            print("   Make sure the microservice is running!")
            return []
        except Exception as e:
            print(f"❌ Error: {e}")
            return []
    
    def get_price_data(self, symbol_code: str, days: int = 30) -> List[Dict]:
        """GET /api/price/{symbol_code}?days={days}"""
        try:
            print(f"🔄 GravityTSE: GET {self.base_url}/api/price/{symbol_code}?days={days}")
            response = requests.get(
                f'{self.base_url}/api/price/{symbol_code}',
                params={'days': days},
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                data = response.json().get('data', [])
                print(f"✅ Received {len(data)} days of data")
                return data
            else:
                print(f"⚠️  Status {response.status_code}")
                return []
        except requests.exceptions.ConnectionError:
            print(f"❌ Cannot connect to GravityTSE")
            return []
        except Exception as e:
            print(f"❌ Error: {e}")
            return []
    
    def update_symbol_data(self, symbol_code: str) -> Optional[Dict]:
        """POST /api/update/{symbol_code}"""
        try:
            print(f"🔄 GravityTSE: POST {self.base_url}/api/update/{symbol_code}")
            response = requests.post(
                f'{self.base_url}/api/update/{symbol_code}',
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                data = response.json().get('data', {})
                print(f"✅ Updated successfully")
                return data
            else:
                print(f"⚠️  Status {response.status_code}")
                return None
        except requests.exceptions.ConnectionError:
            print(f"❌ Cannot connect to GravityTSE")
            return None
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
    
    def get_market_overview(self) -> Dict:
        """GET /api/market/overview"""
        try:
            print(f"🔄 GravityTSE: GET {self.base_url}/api/market/overview")
            response = requests.get(
                f'{self.base_url}/api/market/overview',
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                data = response.json().get('data', {})
                print(f"✅ Market overview received")
                return data
            else:
                return {}
        except requests.exceptions.ConnectionError:
            print(f"❌ Cannot connect to GravityTSE")
            return {}
        except Exception as e:
            return {}
