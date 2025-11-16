"""
Codal Service
Integrates with Gravity_TSE_Codal microservice
Repository: https://github.com/GravtyWaves/Gravity_TSE_Codal

IMPORTANT: This service requires Gravity_TSE_Codal microservice to be running on port 5003
"""
import requests
from typing import Dict, Optional
import os


class CodalService:
    """Service for processing Codal MHTML files via Gravity_TSE_Codal microservice"""
    
    def __init__(self, base_url: str = 'http://localhost:5003'):
        self.base_url = base_url
        self.timeout = 120
    
    def process_mhtml(self, file_path: str) -> Optional[Dict]:
        """POST /api/process/mhtml"""
        try:
            if not os.path.exists(file_path):
                print(f"❌ File not found: {file_path}")
                return None
            
            print(f"🔄 Gravity_TSE_Codal: POST {self.base_url}/api/process/mhtml")
            print(f"   File: {os.path.basename(file_path)}")
            
            with open(file_path, 'rb') as f:
                files = {'file': (os.path.basename(file_path), f, 'application/mhtml')}
                
                response = requests.post(
                    f'{self.base_url}/api/process/mhtml',
                    files=files,
                    timeout=self.timeout
                )
            
            if response.status_code == 200:
                data = response.json().get('data', {})
                print(f"✅ MHTML processed successfully")
                print(f"   Symbol: {data.get('symbol_code', 'N/A')}")
                return data
            else:
                print(f"⚠️  Status {response.status_code}")
                if response.status_code == 400:
                    print(f"   Error: {response.json().get('error', '')}")
                return None
        except requests.exceptions.ConnectionError:
            print(f"❌ Cannot connect to Gravity_TSE_Codal at {self.base_url}")
            print("   Make sure the microservice is running!")
            return None
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
    
    def validate_mhtml(self, file_path: str) -> bool:
        """Validate MHTML file"""
        if not os.path.exists(file_path):
            return False
        
        if not file_path.lower().endswith(('.mhtml', '.mht')):
            print(f"⚠️  Invalid extension. Must be .mhtml or .mht")
            return False
        
        file_size = os.path.getsize(file_path)
        if file_size > 16 * 1024 * 1024:
            print(f"⚠️  File too large: {file_size/(1024*1024):.1f}MB (max 16MB)")
            return False
        
        return True
    
    def extract_symbol_from_mhtml(self, file_path: str) -> Optional[str]:
        """POST /api/extract/symbol"""
        try:
            if not os.path.exists(file_path):
                return None
            
            with open(file_path, 'rb') as f:
                files = {'file': (os.path.basename(file_path), f, 'application/mhtml')}
                
                response = requests.post(
                    f'{self.base_url}/api/extract/symbol',
                    files=files,
                    timeout=30
                )
            
            if response.status_code == 200:
                return response.json().get('symbol_code')
            return None
        except:
            return None
