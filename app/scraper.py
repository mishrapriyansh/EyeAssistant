import requests
from app.config import TIMEOUT

def scrap_data(site):
        url = site['href']
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
            response = requests.get(url, headers=headers, timeout=TIMEOUT)
            
            if response.status_code == 200:
                return response.text
                
        except requests.exceptions.RequestException as e:
         print(f"\nERROR occurred while scraping {url}: {e}")
        return None