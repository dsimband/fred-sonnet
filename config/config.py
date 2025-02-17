# config/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    FRED_API_KEY = os.getenv('FRED_API_KEY')
    BASE_URL = 'https://api.stlouisfed.org/fred'
    DEFAULT_PARAMS = {
        'api_key': FRED_API_KEY,
        'file_type': 'json'
    }