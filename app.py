#!/usr/bin/env python3
"""
Simple Python application for testing cache in GitHub Actions
"""

import requests
import pandas as pd
import numpy as np
from datetime import datetime

def main():
    print("🐍 Starting Python application...")
    print(f"⏰ Current time: {datetime.now()}")
    
    # Test some libraries
    data = np.array([1, 2, 3, 4, 5])
    df = pd.DataFrame({'numbers': data, 'squares': data**2})
    
    print("📊 DataFrame created:")
    print(df)
    
    # Simple API call
    try:
        response = requests.get('https://httpbin.org/json')
        print(f"🌐 API Response status: {response.status_code}")
        print(f"📝 Response data: {response.json()}")
    except Exception as e:
        print(f"❌ API call failed: {e}")
    
    print("✅ Application completed successfully!")

if __name__ == "__main__":
    main()