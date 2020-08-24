import requests
import os
import json

API_URL = 'http://127.0.0.1:8000/api/devices/soilprobereadings/'
API_KEY = os.environ['TESTAUTH']

headers = {'Authorization': f'Token {API_KEY}'}

s = """
{
	"LocationID": 11385,
	"LocationDescription": "Soil Probe",
	"SystemType": "Metric",
	"Devices": {
    	"Probes": {
        	"deviceID": 9702,
        	"deviceDataArray": [
            	{
                    "datetime": "2020-06-02T19:34:32.000Z",
                	"depth1": 35.3,
                	"depth2": 35.5,
                	"depth3": 36.4,
                	"depth4": 40,
                	"depth5": 41.6,
                	"depth6": 41.2,
                	"depth7": 40.3,
                	"depth8": 39.8,
                	"depth9": null,
                	"depth10": null,
                	"depth11": null,
                	"depth12": null,
                	"depth13": null,
                	"depth14": null,
                	"depth15": null,
                	"depth16": null,
                	"soiltotal": 268.05,
                	"rainfall": null,
                	"IrrigationDueActual": null,
                	"IrrigationDueDefault": null,
                	"DailyUse": null,
                    "temp": null,
                	"Humidity": null,
                	"depth1Temp": 9,
                	"depth2Temp": 9.5,
                	"depth3Temp": 10,
                	"depth4Temp": 11,
                	"depth5Temp": 11.5,
                	"depth6Temp": 12.5,
                	"depth7Temp": 13,
                	"depth8Temp": 13.5,
                	"depth9Temp": null,
                	"depth10Temp": null,
                	"depth11Temp": null,
                	"depth12Temp": null,
                	"depth13Temp": null,
                	"depth14Temp": null,
                	"depth15Temp": null,
                	"depth16Temp": null
       	        }
        	]
    	}
	}
}
"""
s = json.loads(s)
print(s.keys())

r = requests.post(API_URL, headers=headers, json=s)
print(r.status_code)
