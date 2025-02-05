import os

class Config:
    DEBUG = os.getenv('DEBUG', False)
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///data.db')
    API_KEY = os.getenv('API_KEY', 'your_api_key_here')