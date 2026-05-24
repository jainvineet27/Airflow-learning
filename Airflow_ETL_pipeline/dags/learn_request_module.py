print("Hello World")

import requests
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY")

url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"

response = requests.get(url)
data = response.json()
for key, value in data.items():
    print(f"{key}: {value}")

