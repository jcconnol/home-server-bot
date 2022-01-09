#import speech_recognition as sr
import pyttsx3
from datetime import datetime
import wikipedia
import webbrowser
import pyjokes
import os
import time
import subprocess
import wolframalpha
import json
import requests
import platform
import socket
from chatBotHelper import *
import keys

print('Loading your AI personal assistant')

#set properties for voice
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)

def speak(text):
    print("speak")
    #engine.say(text)
    #engine.runAndWait()

def scheduleAlarm():
    print('schedule alarm')
    #setting alarm by writing python file with alarm output function then schedule with cron tab

def wishMe():
    hour=datetime.now().hour
    if hour>=0 and hour<12:
        speak("Good Morning")
        print("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
        print("Good Afternoon")
    else:
        speak("Good Evening")
        print("Good Evening")

wishMe()

if __name__=='__main__':
    speak("Hello, how can I help you?")
    while True:
        statement = input("Enter statement: ")
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('I am shutting down, Good bye')
            print('I am shutting down, Good bye')
            break

        if 'wikipedia' in statement:
            print(statement)
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "").strip()
            print(statement)
            wikipedia.set_lang("en")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            #TODO say top 3 options then pic based off what is said
            #TODO try "New York" for example
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google Mail is open now")
            time.sleep(5)

        elif 'time' in statement:
            strTime=datetime.datetime.now().strftime("{:%a, %b %d %Y}")
            strTime = "the time is "+strTime
            speak(strTime)

        elif 'date' in statement:
            cur_dt1 = datetime.datetime.today()
            dt_str1 = '{:%A, %B %d %Y}'.format(cur_dt1)
            dt_strl = "the date is "+dt_strl
            speak(dt_str1)

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times,Happy reading')
            time.sleep(6)

        elif 'search'  in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'ask' in statement:
            #todo get wolfram alpha id
            speak('I can answer computational and geographical questions. what is your question?')
            question=input("Enter statement: ")
            client = wolframalpha.Client(wa_app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        elif "processor" in statement:
            platformString = platform.system() + ' version ' + platform.version() + ' Release ' + platform.release()
            print(platformString)
            speak(platformString)

        elif "ip address" in statement or "ipaddress" in statement:
            ipAddress = socket.gethostbyname(socket.gethostname())
            speak(ipAddress)

        elif "nasa" in statement and "rover" in statement and "pic" in statement:
            roverPicURL = makeNASARoverImageRequest()
            webbrowser.open_new_tab(roverPicURL)

        elif "today" in statement and "weather" in statement:
            outputString = getTodaysWeather()
            speak(outputString)

        elif "joke" in statement:
            joke = pyjokes.get_joke()
            speak(joke)
            
        elif "imdb" in statement or "movie" in statement:
            #http://www.omdbapi.com/?i=tt3896198
            #t param is for movie title to search for
            #type = movie, episode or series
            movie_info = getMovieInfo(statement)
            speak(movie_info)
            
            
        #TODO rest countries api https://duckduckgo.com/?q=rest+countries+api&atb=v187-1&ia=web&iai=r1-1&page=1&sexp=%7B%22prodexp%22%3A%22b%22%2C%22prdsdexp%22%3A%22c%22%2C%22biaexp%22%3A%22b%22%7D
        #TODO space https://rapidapi.com/search/space
        #TODO urban dictionary https://rapidapi.com/community/api/urban-dictionary
        #TODO IMDB https://rapidapi.com/rapidapi/api/movie-database-imdb-alternative
        #TODO city state look up https://rapidapi.com/dev132/api/city-geo-location-lookup
        #TODO currency converter https://rapidapi.com/natkapral/api/currency-converter5
        #TODO flight data https://rapidapi.com/Travelpayouts/api/flight-data
        #TODO google maps place info lookup https://developers.google.com/places/web-service/overview

        #TODO add chatbot learning responses functionality

        #TODO listen to voice and put text into place

        #TODO house automations
        #user transmitter to arduino inside light switch
        #transmitter instructions found here https://www.instructables.com/RF-433-MHZ-Raspberry-Pi/

        else:
            speak("I have no coded response for that command")
        
        speak("Is there anything else I can help you with?")

time.sleep(3)
