import requests
from config import Config

def extract_data(api_key, patient_id):
    url = f"https://hospital.api.com/data/{patient_id}"
    headers = {
        'Authorization': f'Bearer {api_key}',
    }
    response = requests.get(url, headers=headers)
    return response.json()