import requests
import os

API_URL = 'http://127.0.0.1:8000/api/devices/devicetype/'
API_KEY = os.environ['TESTAUTH']
headers = {'Authorization': f'Token {API_KEY}'}

r = requests.get(API_URL, headers=headers)
data = r.json()
for ln in data:
    print(ln)