# services/data_fetcher.py
import requests
import pandas as pd
from config import SPRING_BOOT_API_URL

def fetch_user_activity():
    """Fetch user activity data from Spring Boot API."""
    try:
        response = requests.get(SPRING_BOOT_API_URL)
        response.raise_for_status()
        data = response.json()

        print(f"📡 Raw API Response: {data}") 
        df = pd.DataFrame(data)
        print(f"📊 DataFrame Preview:\n{df.head()}") 
        
        return df
    except Exception as e:
        print(f"❌ Error fetching user activity: {e}")
        return pd.DataFrame() 
