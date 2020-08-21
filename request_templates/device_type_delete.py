import requests
import os

API_URL = 'http://127.0.0.1:8000/api/devices/devicetype/1/'
API_KEY = os.environ['TESTAUTH']
headers = {'Authorization': f'Token {API_KEY}'}

r = requests.delete(API_URL, headers=headers)
print(r.status_code)

