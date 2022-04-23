import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import requests
import json
import pyjokes


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

def tellDay():
        
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
                speak("The day is " + day_of_the_week)

def tellWeather(city):
        API = "weather.txt"            #vikd03c60fef0f5305a7f0238a134c4ccd2bha
        PATH = "http://api.openweathermap.org/data/2.5/weather?"
        PARAMS = {
                "q": city,
                "appid": API,
        }
        respond = reuests.get(PATH, PARAMS)
        makeit = respond.json()
        tempindegree = int(makeit['main']['temp']-273.15)
        windspeed = makeit['wind']['speed']
        description = makeit['weather'][0]['description']
        print(f"the city {city} have {tempindegree} temperature and wind speed is {windspeed}, "
                                                        f"having quite {description}") 
        speak("the city " + city + "have" + tempindegree + "temperature and wind speed is " + windspeed + "having quite" + description)



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
        speak("hello I am shee jarvis Tell me how may I help you")


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
                elif "open instagram" in query.lower():
                        speak("Opening Instagram")
                        webbrowser.open("www.instagram.com")
                        continue

                
                elif "open google" in query:
                        speak("Opening Google ")
                        webbrowser.open("www.google.com")
                        continue
                        
                elif "which day it is" in query or "what day is today" in query or "what day it is" in query:
                        tellDay()
                        continue
                
                elif "tell me the time" in query or "what is the time" in query or "what time is it" in query:
                        tellTime()
                        continue

                
                elif "weather" in query or "temperature" in query:
                        key = "d03c60fef0f5305a7f0238a134c4ccd2"
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
                                weather_response = "the temperature is " + str(temperature) + " celsius " + " the humidity is " + str(humidity) + " and weather is " + str(desc)
                                print(weather_response)
                                speak(weather_response)
                        else:
                                speak("city not found")
                
                # this will exit and terminate the program
                elif "bye" in query or "exit" in query:
                        speak("Bye have a nice day ")
                        exit()
                
                elif "from wikipedia" in query:
                        
                        # if any one wants to have a information
                        # from wikipedia
                        speak("Checking the wikipedia ")
                        query = query.replace("wikipedia", "")
                        
                        # it will give the summary of 3 lines from
                        # wikipedia we can increase and decrease
                        # it also.
                        result = wikipedia.summary(query, sentences=3)
                        speak("According to wikipedia")
                        speak(result)

                elif "joke" in query or "jokes" in query:
                        #print(pyjokes.get_joke())
                        speak(pyjokes.get_joke())

                elif "where is" in query:
                        ind = query.lower().split().index("is")
                        location = query.split()[ind + 1:]
                        url = "https://www.google.com/maps/place/" + "".join(location)
                        speak("this is where" + str(location) + "is")
                        webbrowser.open(url)
                
                elif "tell me your name" in query or "what is your name" in query:
                        speak("I am shee Jarvis. Your deskstop Assistant")

if __name__ == '__main__':
        
        # main method for executing
        # the functions
        Take_query()
