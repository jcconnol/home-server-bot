import requests
import json
import os
#get request from openweather api

speakString = "espeak \"Good morning. "

#add alarmWeatherAPIKey to end
weather = requests.get('http://api.openweathermap.org/data/2.5/weather?q=indianapolis,us&appid=b476a356e09e0290b71c5b3c4c4a2896')

#pprint(str(weather.json()).replace("\'","\""))

weatherJson = json.loads(str(weather.json()).replace("\'", "\""))


if(weather.status_code == 200):
    cloudCover = weatherJson['weather'][0]['description']
    location = weatherJson["name"]
    temp = weatherJson["main"]["temp"]
    windMPH = weatherJson["wind"]["speed"]
    windDegrees = 10
    #windDegrees = weatherJson["wind"]["deg"]
    windGusts = weatherJson["wind"]["gust"]

    temp = int((((temp - 272.15) * 1.8) + 32))
    windMPH = int((windMPH * 0.62))
    windGusts = int((windGusts * 0.62))

    windDir = ""

    if(windDegrees < 165 and windDegrees > 15):
        windDir = "North "
    elif(windDegrees < 345 and windDegrees > 195):
        windDir = "South "

    if(windDegrees < 75 or windDegrees > 285):
        windDir = windDir + "East"
    elif(windDegrees > 105 and windDegrees < 255):
        windDir = windDir + "West"

    speakString = speakString + "The weather in " + location + " is " + str(temp) + " degrees with "+ cloudCover + ". The wind conditions are " + str(windMPH) + " miles per hour from the " + windDir + " with gusts reaching a max of " + str(windGusts) + " miles per hour." + "\""
    print(speakString)
else:
    speakString = speakString + " I could not retrieve the weather information. You might want to check my programming."

#os.system(speakString)
