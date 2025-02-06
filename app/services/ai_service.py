import requests

class AIService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.external-ai-service.com"

    def standardize_medical_text(self, text):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "text": text
        }
        response = requests.post(f"{self.base_url}/standardize", headers=headers, json=payload)
        return response.json()