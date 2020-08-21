import requests
import os

API_URL = 'http://127.0.0.1:8000/api/devices/devicetype/'
API_KEY = os.environ['TESTAUTH']

headers = {'Authorization': f'Token {API_KEY}'}

payload = {
    'device_type':'Canopy Temp Sensor',
}

r = requests.post(API_URL, headers=headers, json=payload)
print(r.status_code)
