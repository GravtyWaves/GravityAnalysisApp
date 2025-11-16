"""
Fundamental Analysis Service
Integrates with Gravity_FundamentalAnalysis microservice
Repository: https://github.com/GravtyWaves/Gravity_FundamentalAnalysis

IMPORTANT: This service requires Gravity_FundamentalAnalysis microservice to be running on port 5004
"""
import requests
from typing import Dict, Optional


class FundamentalAnalysisService:
    """Service for fundamental analysis via Gravity_FundamentalAnalysis microservice"""
    
    def __init__(self, base_url: str = 'http://localhost:5004'):
        self.base_url = base_url
        self.timeout = 60
    
    def analyze(self, financial_data: Dict) -> Dict:
        """POST /api/analyze"""
        try:
            print(f"🔄 Gravity_FundamentalAnalysis: POST {self.base_url}/api/analyze")
            
            response = requests.post(
                f'{self.base_url}/api/analyze',
                json=financial_data,
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                data = response.json().get('data', {})
                print(f"✅ Fundamental analysis completed")
                print(f"   Score: {data.get('score', 'N/A')}/100")
                return data
            else:
                print(f"⚠️  Status {response.status_code}")
                return {}
        except requests.exceptions.ConnectionError:
            print(f"❌ Cannot connect to Gravity_FundamentalAnalysis at {self.base_url}")
            print("   Make sure the microservice is running!")
            return {}
        except Exception as e:
            print(f"❌ Error: {e}")
            return {}
    
    def calculate_ratios(self, financial_data: Dict) -> Dict:
        """POST /api/ratios"""
        try:
            print(f"🔄 Gravity_FundamentalAnalysis: POST {self.base_url}/api/ratios")
            
            response = requests.post(
                f'{self.base_url}/api/ratios',
                json=financial_data,
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                data = response.json().get('data', {})
                print(f"✅ Ratios calculated")
                return data
            else:
                print(f"⚠️  Status {response.status_code}")
                return {}
        except requests.exceptions.ConnectionError:
            print(f"❌ Cannot connect to Gravity_FundamentalAnalysis")
            return {}
        except Exception as e:
            print(f"❌ Error: {e}")
            return {}
    
    def calculate_valuation(self, financial_data: Dict, market_price: Optional[float] = None) -> Dict:
        """POST /api/valuation"""
        try:
            print(f"🔄 Gravity_FundamentalAnalysis: POST {self.base_url}/api/valuation")
            
            payload = financial_data.copy()
            if market_price:
                payload['market_price'] = market_price
            
            response = requests.post(
                f'{self.base_url}/api/valuation',
                json=payload,
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                data = response.json().get('data', {})
                print(f"✅ Valuation calculated")
                return data
            else:
                print(f"⚠️  Status {response.status_code}")
                return {}
        except requests.exceptions.ConnectionError:
            print(f"❌ Cannot connect to Gravity_FundamentalAnalysis")
            return {}
        except Exception as e:
            print(f"❌ Error: {e}")
            return {}
