import requests
import os
import json
import io

API_URL = 'http://127.0.0.1:8000/api/devices/raingaugereadings/'
API_KEY = os.environ['TESTAUTH']

headers = {'Authorization': f'Token {API_KEY}'}

s="""
{   
    "LocationID": 11444,
	"LocationDescription": "Rain Gauge",
	"SystemType": "Metric",
	"Devices": {
    	"RainGauges": {
        	"deviceID": 10074,
            "deviceDataArray": [
            	{
                    "rain": 0.2,
                	"datetime": "2020-06-02T19:21:18.000Z",
                	"AccumulatedRain": null
            	},
            	{
                    "rain": 0,
                	"datetime": "2020-06-02T19:59:48.000Z",
                	"AccumulatedRain": null
            	}
        		]
    		}
	}
}
"""
s=json.loads(s)
print(s.keys())

r = requests.post(API_URL, headers=headers, json=s)
print(r.status_code)
