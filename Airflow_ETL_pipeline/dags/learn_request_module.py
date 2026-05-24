print("Hello World")

import requests
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

API_KEY = os.getenv("API_KEY")

url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

response = requests.get(url)
data = response.json()
for key, value in data.items():
    print(f"{key}")

