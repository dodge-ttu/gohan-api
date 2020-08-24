import requests
import os
import json

API_URL = 'http://127.0.0.1:8000/api/devices/tankmonitorreading/'
API_KEY = os.environ['TESTAUTH']

headers = {'Authorization': f'Token {API_KEY}'}

s="""
{	
    "LocationID": 11137,
	"LocationDescription": "Tank Sensor",
	"SystemType": "Metric",
	"Devices": {
    	"TankMonitors": {
        	"deviceID": 9325,
        	"deviceDataArray": [
            	{
                	"DateTime": "2020-05-31T18:32:34.000Z",
                	"WaterHeightMillimetres": 114.843,
                	"RainFallMillimeters": null
            	},
            	{
                	"DateTime": "2020-05-31T19:32:35.000Z",
                	"WaterHeightMillimetres": 114.843,
                	"RainFallMillimeters": null
            	},
            	{
          	     
                	"DateTime": "2020-05-31T20:32:36.000Z",
                	"WaterHeightMillimetres": 113.203,
                	"RainFallMillimeters": null
            	},
            	{
                	"DateTime": "2020-05-31T21:32:38.000Z",
                	"WaterHeightMillimetres": 113.203,
                	"RainFallMillimeters": null
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
