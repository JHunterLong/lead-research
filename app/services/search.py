import requests
import os

def search_company(company_name):
    api_key = os.getenv("GOOGLE_API_KEY")
    cx = os.getenv("SEARCH_ENGINE_ID")
    url = f"https://www.googleapis.com/customsearch/v1?q={company_name}&key={api_key}&cx={cx}"
    response = requests.get(url)
    return response.json().get('items', [])
