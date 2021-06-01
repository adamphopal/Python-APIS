#! python3

# Chapter 14 Project Fetching Current Weather Data
# Prints the weather data for a location from the command line.
#python quick_weather.py Moorpark
import json
import requests
import sys

if len(sys.argv) < 2:
    print('Usage: script.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])



url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=5f9bd7eefef982fbf2b863518b868af1' % (location)
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
#print(weatherData)
w = weatherData['weather']
print('Current weather is %s:' % (location))
print('The Description for todays weather is:')
print(w[0]['description'])


