import requests
from datetime import datetime
import keys

def makeNASARoverImageRequest():
    URL = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000"+nasaAPIKey
    response = requests.get(URL)
    json = response.json()
    if('error' not in json):
        print(json["photos"][0]['img_src'])
        return json["photos"][0]['img_src']

def getMovieInfo(inputText):
    URL = "http://www.omdbapi.com/?apikey=e49e1b9c&t=taken&type=movie"
    #i=tt3896198&
    #everything after "movie" is movie name, for example, what is the genre of the movie "Taken"
    
    
    '''
    {
       "Title":"Taken",
       "Year":"2008",
       "Rated":"PG-13",
       "Released":"30 Jan 2009",
       "Runtime":"90 min",
       "Genre":"Action, Crime, Thriller",
       "Director":"Pierre Morel",
       "Writer":"Luc Besson, Robert Mark Kamen",
       "Actors":"Liam Neeson, Maggie Grace, Famke Janssen",
       "Plot":"A retired CIA agent travels across Europe and relies on his old skills to save his estranged daughter, who has been kidnapped while on a trip to Paris.",
       "Language":"English, French, Albanian, Arabic",
       "Country":"France, United States, United Kingdom",
       "Awards":"2 wins & 2 nominations",
       "Poster":"https://m.media-amazon.com/images/M/MV5BMTM4NzQ0OTYyOF5BMl5BanBnXkFtZTcwMDkyNjQyMg@@._V1_SX300.jpg",
       "Ratings":[
          {
             "Source":"Internet Movie Database",
             "Value":"7.8/10"
          },
          {
             "Source":"Metacritic",
             "Value":"51/100"
          }
       ],
       "Metascore":"51",
       "imdbRating":"7.8",
       "imdbVotes":"576,892",
       "imdbID":"tt0936501",
       "Type":"movie",
       "DVD":"12 May 2009",
       "BoxOffice":"$145,000,989",
       "Production":"EuropaCorp, Grive Productions, M6 Films Production",
       "Website":"N/A",
       "Response":"True"
    }
    '''
    response = requests.get(URL)
    json = response.json()
    print(json)
    return json

def getTodaysWeather():
    URL = "http://api.openweathermap.org/data/2.5/weather?units=imperial&zip="+cityLocation+"&appid="+weatherAPIKey
    response = requests.get(URL)
    json = response.json()
    print(json)
    #good morning, it is {time}. the weather in {my location} is {number} degrees with {scattered} clouds
    #wind is from the {North West} at {some number} miles per hour
    #sunrise is at {some time} and sun set is at {some time}.

    now = datetime.now()
    hour = now.hour
    minute = now.minute

    if(hour > 12):
        hour = hour - 12
    elif (hour < 1):
        hour = 12

    introGreetingTime = ""
    hour=datetime.now().hour
    if hour>=0 and hour<12:
        introGreetingTime = "Good Morning"
    elif hour>=12 and hour<18:
        introGreetingTime = "Good Afternoon"
    else:
        introGreetingTime = "Good Evening"
    
    if hour > 12:
        hour = hour - 12
    
    timeString = str(hour) + " "

    if(now.minute != 0):
        if(now.minute < 10):
            timeString += "0" + str(now.minute) + " "
        else:
            timeString += str(now.minute) + " "

    timeString += datetime.today().strftime("%p")

    cloudDesc = json['weather'][0]['description']
    windSpeed = int(json['wind']['speed'])
    sunriseString = int(json['sys']['sunrise'])
    sunsetString = int(json['sys']['sunset'])
    windDegrees = int(json['wind']['deg'])
    tempFarenheit = str(int(json['main']['temp']))
    windDirection = ""
    sunriseTime = datetime.fromtimestamp(int(sunriseString))
    sunriseTimeString = str(sunriseTime.hour)  + " " + str(sunriseTime.minute) + " AM"

    sunsetTime = datetime.fromtimestamp(int(sunsetString))
    sunsetHour = sunsetTime.hour

    if(sunsetHour > 12):
        sunsetHour = sunsetTime.hour - 12
    elif (sunsetTime.hour < 1):
        sunsetHour = 12

    sunsetTimeString = str(sunsetHour)  + " " + str(sunsetTime.minute) + " PM"

    if windDegrees >= 300 or windDegrees <= 60:
        windDirection = "North"
    elif windDegrees <= 240 or windDegrees <= 120:
        windDirection = "South"

    if windDegrees <= 330 or windDegrees >= 210:
        windDirection += " West"
    elif windDegrees <= 150 or windDegrees >= 30:
        windDirection += " East"
    
    if windSpeed > 1:
        windSpeedText = "miles"
    else:
        windSpeedText = "mile"
    
    outputString = f"{introGreetingTime}, its {timeString}. The weather in {cityName} is {tempFarenheit} degrees with {cloudDesc}."
    outputString += f" The wind is from the {windDirection} at {windSpeed} {windSpeedText} per hour."
    outputString += f" Sunrise is at {sunriseTimeString} and sun set is at {sunsetTimeString}."
    print(outputString)
    return outputString
    """{
        'coord': {
            'lon': -86.16,
            'lat': 39.77
        },
            'weather': [
                {
                    'id': 804,
                    'main': 'Clouds',
                    'description': 'overcast clouds',
                    'icon': '04d'
                }
            ],
            'base': 'stations',
            'main': {
                'temp': 272.35,
                'feels_like': 268.32,
                'temp_min': 271.48,
                'temp_max': 273.15,
                'pressure': 1018,
                'humidity': 86
            },
            'visibility': 10000,
            'wind': {
                'speed': 2.38,
                'deg': 78
            },
            'clouds': {'all': 90},
            'dt': 1607267727,
            'sys': {
                'type': 1,
                'id': 4345,
                'country': 'US',
                'sunrise': 1607259125,
                'sunset': 1607293206
            },
            'timezone': -18000, 'id': 4259418, 'name': 'Indianapolis', 'cod': 200}"""
