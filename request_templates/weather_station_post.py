import requests
import os
import json

API_URL = 'http://127.0.0.1:8000/api/devices/wxstatreadings/'
API_KEY = os.environ['TESTAUTH']

headers = {'Authorization': f'Token {API_KEY}'}

s = """
{
	"LocationID": 2311,
	"LocationDescription": "Weather Station",
	"SystemType": "Metric",
	"Devices": {
    	"WeatherStations": {
        	"deviceID": 887,
        	"deviceDataArray": [
            	{
                	"datetime": "2020-06-01T21:10:24.000Z",
                	"AirTemp": 13.75,
                	"Humidity": 44.2,
                	"WindAvgSpdKph": 9.81,
                	"WindAvgDirect": 250.38,
                	"WindStdDev": -1,
                	"Rainmm": 0,
              		"SoilTemp": null,
                	"SolarRad": 4.43,
                	"Barometric": 1015.4,
                	"Evaporation": null,
                	"AirTemp10M": null,
                	"AirTempInversion": null,
                	"WindDirection1": "WSW",
                	"WindDirection2": "N ",
                	"WindDirection1Percent": 100,
                	"WindDirection2Percent": 0,
                	"WindSpeedMax": 13.86,
                	"WindSpeedMin": 8.01,
                	"WindSpeedAvg": 9.61
            	},
            	{
                    "datetime": "2020-06-01T21:29:36.000Z",
                	"AirTemp": 13.44,
                	"Humidity": 45.4,
                	"WindAvgSpdKph": 9.36,
                	"WindAvgDirect": 252.58,
                	"WindStdDev": -1,
                	"Rainmm": 0,
                	"SoilTemp": null,
                	"SolarRad": 4.03,
                	"Barometric": 1015.9,
                	"Evaporation": null,
                	"AirTemp10M": null,
  	                "AirTempInversion": null,
                	"WindDirection1": "WSW",
                	"WindDirection2": "N  ",
                	"WindDirection1Percent": 100,
                	"WindDirection2Percent": 0,
                	"WindSpeedMax": 13.5,
                	"WindSpeedMin": 8.64,
                	"WindSpeedAvg": 10.99
            	},
            	{
                	"datetime": "2020-06-01T22:10:08.000Z",
                	"AirTemp": 13,
                	"Humidity": 48.2,
                	"WindAvgSpdKph": 12.51,
           	     	"WindAvgDirect": 249.68,
                	"WindStdDev": -1,
                	"Rainmm": 0,
                	"SoilTemp": null,
                	"SolarRad": 3.22,
                	"Barometric": 1016.2,
                	"Evaporation": null,
                	"AirTemp10M": null,
                	"AirTempInversion": null,
                	"WindDirection1": "WSW",
                	"WindDirection2": "N  ",
                	"WindDirection1Percent": 100,
                	"WindDirection2Percent": 0,
                	"WindSpeedMax": 14.13,
                	"WindSpeedMin": 9.81,
                	"WindSpeedAvg": 11.28
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
