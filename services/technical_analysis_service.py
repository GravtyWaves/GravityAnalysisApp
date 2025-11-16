"""
Technical Analysis Service
Integrates with Gravity_TechAnalysis microservice
Repository: https://github.com/Shakour-Data/Gravity_TechAnalysis

IMPORTANT: This service requires Gravity_TechAnalysis microservice to be running on port 5002
"""
import requests
from typing import List, Dict


class TechnicalAnalysisService:
    """Service for technical analysis via Gravity_TechAnalysis microservice"""
    
    def __init__(self, base_url: str = 'http://localhost:5002'):
        self.base_url = base_url
        self.timeout = 60
    
    def analyze(self, price_data: List[Dict]) -> Dict:
        """POST /api/analyze"""
        try:
            print(f"🔄 Gravity_TechAnalysis: POST {self.base_url}/api/analyze")
            print(f"   Sending {len(price_data)} days of price data")
            
            response = requests.post(
                f'{self.base_url}/api/analyze',
                json={'price_data': price_data},
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                data = response.json().get('data', {})
                print(f"✅ Technical analysis completed")
                return data
            else:
                print(f"⚠️  Status {response.status_code}")
                return {}
        except requests.exceptions.ConnectionError:
            print(f"❌ Cannot connect to Gravity_TechAnalysis at {self.base_url}")
            print("   Make sure the microservice is running!")
            return {}
        except Exception as e:
            print(f"❌ Error: {e}")
            return {}
    
    def calculate_indicators(self, price_data: List[Dict], indicator_list: List[str]) -> Dict:
        """POST /api/indicators"""
        try:
            print(f"🔄 Gravity_TechAnalysis: POST {self.base_url}/api/indicators")
            print(f"   Indicators: {', '.join(indicator_list)}")
            
            response = requests.post(
                f'{self.base_url}/api/indicators',
                json={
                    'price_data': price_data,
                    'indicators': indicator_list
                },
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                data = response.json().get('data', {})
                print(f"✅ Indicators calculated")
                return data
            else:
                print(f"⚠️  Status {response.status_code}")
                return {}
        except requests.exceptions.ConnectionError:
            print(f"❌ Cannot connect to Gravity_TechAnalysis")
            return {}
        except Exception as e:
            print(f"❌ Error: {e}")
            return {}
