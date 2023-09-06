from decouple import config

API_URL = config(BANK_API_URL) or config('API_URL')
