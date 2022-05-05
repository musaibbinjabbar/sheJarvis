import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import os
import random
import wikipedia
import pyautogui
import requests
import json
import pyjokes
import wolframalpha
import pandas as pd
from countryinfo import CountryInfo
from PyDictionary import PyDictionary
import randfacts
import time
import smtplib

# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
def takeCommand():

        r = sr.Recognizer()

        # from the speech_Recognition module
        # we will use the Microphone module
        # for listening the command
        with sr.Microphone() as source:
                print('Listening...')
                
                # seconds of non-speaking audio before
                # a phrase is considered complete
                r.pause_threshold = 0.7
                audio = r.listen(source)
                
                # Now we will be using the try and catch
                # method so that if sound is recognized
                # it is good else we will have exception
                # handling
                try:
                        print("Recognizing...")
                        
                        # for Listening the command in indian
                        # english we can also use 'hi-In'
                        # for hindi recognizing
                        Query = r.recognize_google(audio, language='en-in')
                        print("you said :", Query)
                        
                except Exception as e:
                        print(e)
                        print("Say that again sir")
                        return "None"
                
                return Query

def speak(audio):
        
        engine = pyttsx3.init()
        # getter method(gets the current value
        # of engine property)
        voices = engine.getProperty('voices')
        
        # setter method .[0]=male voice and
        # [1]=female voice in set Property.
        engine.setProperty('voice', voices[0].id)
        
        # Method for the speaking of the the assistant
        engine.say(audio)
        
        # Blocks while processing all the currently
        # queued commands
        engine.runAndWait()

def tellToday():
        
        # This function is for telling the
        # day of the week
        day = datetime.datetime.today().weekday() + 1
        
        #this line tells us about the number
        # that will help us in telling the day
        Day_dict = {1: 'Monday', 2: 'Tuesday',
                                3: 'Wednesday', 4: 'Thursday',
                                5: 'Friday', 6: 'Saturday',
                                7: 'Sunday'}
        
        if day in Day_dict.keys():
                day_of_the_week = Day_dict[day]
                print(day_of_the_week)
                speak("Today is " + day_of_the_week)

def listToString(s): 
    
    # initialize an empty string
        str1 = "" 
    
    # traverse in the string  
        for ele in s: 
                str1 += ele  
    
    # return string  
        return str1

def tellTomorrow():
        
        # This function is for telling the
        # day of the week
        day = datetime.datetime.today().weekday() + 2
        
        #this line tells us about the number
        # that will help us in telling the day
        Day_dict = {1: 'Monday', 2: 'Tuesday',
                                3: 'Wednesday', 4: 'Thursday',
                                5: 'Friday', 6: 'Saturday',
                                7: 'Sunday'}
        
        if day in Day_dict.keys():
                day_of_the_week = Day_dict[day]
                print(day_of_the_week)
                speak("Tomorrow is " + day_of_the_week)

def sendEmail(to,content):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('mailforproject3@gmail.com','projectmailpswd.txt')
        server.sendmail('mailforproject3@gmail.com',to,content)
        server.close()

        
def screenshot():
    img = pyautogui.screenshot()
    img.save(r'C:\\Users\\DELL\\Pictures\\Screenshots\\screenshot_by_jarvis.png')

def tellTime():
        
        # This method will give the time
        time = str(datetime.datetime.now())
        
        # the time will be displayed like
        # this "2020-06-05 17:50:14.582630"
        #nd then after slicing we can get time
        print(time)
        hour = time[11:13]
        min = time[14:16]
        speak( "The time is " + hour + "Hours and" + min + "Minutes")
       
         
def Hello():
        
        # This function is for when the assistant
        # is called it will say hello and then
        # take query
        speak("Hello I am shee jarvis")


def Take_query():

        # calling the Hello function for
        # making it more interactive
        Hello()
        
        # This loop is infinite as it will take
        # our queries continuously until and unless
        # we do not say bye to exit or terminate
        # the program
        while(True):
                
                # taking the query and making it into
                # lower case so that most of the times
                # query matches and we get the perfect
                # output
                query = takeCommand().lower()
                if "open youtube" in query:
                        speak("Opening YouTube ")
                        
                        # in the open method we just to give the link
                        # of the website and it automatically open
                        # it in your default browser
                        webbrowser.open("www.youtube.com")
                        continue
                elif "open facebook" in query:
                        speak("Opening Facebook")
                        webbrowser.open("www.facebook.com")
                        continue
                elif "open instagram" in query:
                        speak("Opening Instagram")
                        webbrowser.open("www.instagram.com")
                        continue
                elif "open twitter" in query:
                        speak("Opening Twitter")
                        webbrowser.open("www.twitter.com")
                        continue
                elif "open github" in query:
                        speak("Opening GitHub")
                        webbrowser.open("www.github.com")
                        continue
                elif "open stackoverflow" in query or "open stack overflow" in query or "open stack over flow" in query:
                        speak("Opening stackoverflow")
                        webbrowser.open("www.stackoverflow.com")
                        continue
                elif "screenshot" in query or "screen shot" in query:
                    speak("taking screenshot")
                    screenshot()
                    continue
                elif "open google" in query:
                        speak("Opening Google ")
                        webbrowser.open("www.google.com")
                        continue
                        
                elif "which day it is" in query or "what day is today" in query or "what day it is" in query or "what is the day" in query:
                        tellToday()
                        continue
                    
                elif "which day is tomorrow" in query or "what day is tomorrow" in query or "what is the day tomorrow" in query:
                        tellTomorrow()
                        continue
                
                elif "tell me the time" in query or "what is the time" in query or "what time is it" in query:
                        tellTime()
                        continue
                
                elif "play music" in query or "play songs" in query or "play song" in query:
                        
                        fav_dir = "C:\\Users\\DELL\\Music\\fav_dir"
                        rand = random.choice(os.listdir(fav_dir))
                        #songs = os.listdir(fav_dir)
                        speak("opening music")
                        os.startfile(os.path.join(fav_dir,rand))

                
                elif "weather" in query or "temperature" in query:
                        key = "api key here"
                        weather_url = "http://api.openweathermap.org/data/2.5/weather?"
                        ind = query.split().index("in")
                        location = query.split()[ind + 1:]
                        location = "".join(location)
                        url = weather_url + "appid=" + key + "&q=" + location
                        js = requests.get(url).json()
                        if js["cod"] != "404":
                                weather = js["main"]
                                temperature = weather["temp"]
                                temperature = temperature - 273.15
                                humidity = weather["humidity"]
                                desc = js["weather"][0]["description"]
                                weather_response = "the temperature is " + str(temperature) + " degree celsius " + " the humidity is " + str(humidity) + " and weather is " + str(desc)
                                print(weather_response)
                                speak(weather_response)
                        else:
                                speak("city not found")
                
                # this will exit and terminate the program
                elif "bye" in query or "exit" in query or "quit" in query:
                        speak("Bye, have a nice day ")
                        exit()

                
                
                elif "from wikipedia" in query:
                        
                        # if any one wants to have a information
                        # from wikipedia
                        speak("Checking the wikipedia ")
                        query = query.replace("wikipedia", "")
                        
                        # it will give the summary of 3 lines from
                        
                        result = wikipedia.summary(query, sentences=3)
                        speak("According to wikipedia")
                        speak(result)

                elif "news" in query:
                        url = ('http://newsapi.org/v2/top-headlines?'
                               'country=in&'
                               'category=general&'
                               'pageSize=5&'
                               'apiKey=apikey here')
                        try:
                                response = requests.get(url)
                        except:
                                speak("please check your connection")
                        news = json.loads(response.text)
                        #print(news)
                        for new in news['articles']:
                                print(str(new['title']), "\n")
                                speak(str(new['title']))

                elif "capital of" in query:
                        try:
                                ind = query.lower().split().index("of")
                                text = listToString(query.split()[ind + 1:])
                                #response = text
                                #df = pd.DataFrame(text)
                                capital = CountryInfo(text).capital()
                                speak("the capital of " + text + " is " + capital)
                                print("the capital of " + text + " is " + capital)
                        except KeyError:
                                print("no results found")
                                speak("no results found")
                                
                elif "meaning of" in query:
                        try:
                                ind = query.lower().split().index("of")
                                text = listToString(query.split()[ind + 1:])
                                dic = PyDictionary()
                                word = dic.meaning(text)
                                #print(len(word))
         
                                for state in word:
                                    print(word[state])
                                    speak("the meaning is " + str(word[state]))
                        except TypeError:
                                print("no results found")
                                speak("no results found")
                                
                elif "email to nitin" in query or "mail to nitin" in query:
                        try:
                                speak("what message should I send?")
                                content = takeCommand()
                                to = "nitin22092001@gmail.com"
                                sendEmail(to,content)
                                speak("email sent successfully")
                        except Exception as e:
                                print(e)
                                speak("sorry ,something went wrong")

                elif "email to bhavik" in query or "mail to bhavik" in query:
                        try:
                                speak("what message should I send?")
                                content = takeCommand()
                                to = "bhavikjain2888@gmail.com"
                                sendEmail(to,content)
                                speak("email sent successfully")
                        except Exception as e:
                                print(e)
                                speak("sorry ,something went wrong")

                elif "fact" in query or "facts" in query:
                        x = randfacts.get_fact()
                        print(x)
                        speak(x)
                                                
                elif "calculate" in query:
                        app_id = "app_id here"
                        client = wolframalpha.Client(app_id)
                        ind = query.lower().split().index("calculate")
                        text = query.split()[ind + 1:]
                        res = client.query("".join(text))
                        answer = next(res.results).text
                        print("ths answer is " + answer)
                        speak("the answer is " + answer)
                        

                elif "what is" in query or "who is" in query:
                    try:
                        
                        app_id = "app_id here"
                        client = wolframalpha.Client(app_id)
                        ind = query.split().index("is")
                        text = query.split()[ind + 1:]
                        res = client.query("".join(text))
                        #print(res.results)
                        answer = next(res.results).text
                        print(answer)
                        speak("the answer is " + answer)
                    except StopIteration:
                        print("no results found")
                        speak("no results found")

                elif "where do you live" in query:
                    speak("I live in India")
                    
                elif "notepad" in query.lower():
                        speak("opening notepad")
                        os.startfile(
                                r"C:\\WINDOWS\\system32\\notepad.exe"
                                )
                
                elif "excel" in query.lower():
                        speak("opening microsoft excel")
                        os.startfile(
                                r"C:\\Program Files (x86)\\Microsoft Office\\Office14\\EXCEL.EXE"
                                )
                elif "word" in query.lower():
                        speak("opening microsoft word")
                        os.startfile(
                                r"C:\\Program Files (x86)\\Microsoft Office\\Office14\\WINWORD.EXE"
                                )
                elif "powerpoint" in query.lower():
                        speak("opening microsoft powerpoint")
                        os.startfile(
                                r"C:\\Program Files (x86)\\Microsoft Office\\Office14\\POWERPNT.EXE"
                                )

                elif "joke" in query or "jokes" in query:
                        speak(pyjokes.get_joke())

                elif "how are you" in query or "how do you do" in query:
                        speak("i am fine , how do you do")

                elif "where is" in query:
                        ind = query.lower().split().index("is")
                        location = query.split()[ind + 1:]
                        url = "https://www.google.com/maps/place/" + "".join(location)
                        speak("this is where" + str(location) + "is")
                        webbrowser.open(url)
                
                elif "tell me your name" in query or "who are you" in query:
                        speak("I am shee Jarvis. Your deskstop Assistant")

if __name__ == '__main__':
        
        # main method for executing
        # the functions
        Take_query()
