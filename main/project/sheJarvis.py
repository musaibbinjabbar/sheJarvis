from kivy.lang import Builder
from kivymd.app import MDApp

import sheJarvis
from kivymd.uix.button import MDIconButton
import pyttsx3
import requests
import webbrowser
import datetime
import wikipedia

PATH = "http://api.openweathermap.org/data/2.5/weather?"
def takeCommand():
    Query = input("what ")
    return Query


def speak(audio):
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)

    engine.say(audio)

    engine.runAndWait()


def tellDay():
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)
        Value = day_of_the_week
        return Value



def tellTime():
    time = str(datetime.datetime.now())

    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is sir" + hour + "Hours and" + min + "Minutes")
    Value = time
    return Value


def Hello():
    # This function is for when the assistant
    # is called it will say hello and then
    # take query
    speak("hello sir I am your desktop Tell me how may I help you")
    Value = "hello sir I am your desktop Tell me how may I help you"


def tellnews():
    key = {"api-key": "yjGaBu8APLGlfbcXg5amsNOoeO3HMDya"}
    path = "https://api.nytimes.com/svc/topstories/v2/world.json?"
    file = requests.get(path, key)
    decode = file.json()
    arr= [0,0,0,0,0]
    for i in range(0, 5):

        arr[i] = decode['results'][i]['multimedia'][0]['caption']
        # print(decode['results'][i]['multimedia'][0]['caption'])
        speak(decode['results'][i]['multimedia'][0]['caption'])
    print(arr)
    return arr



def tellweather(city):
    PARAMS = {
        "q": city,
        "appid": '2f90e3a992aebf5c57c2e7c116933ce6',
    }

    respon = requests.get(PATH, PARAMS)
    makeit = respon.json()
    tempindegree = int(makeit['main']['temp'] - 273.15)
    windspeed = makeit['wind']['speed']
    discription = makeit['weather'][0]['description']
    speak(f"The city {city} have {tempindegree} Temparature of wind speed {windspeed}, "
          f"having quit {discription}")
    arr = "temparrature is "+str(tempindegree) +"wind speed is " +str(windspeed)+"discription " +str(discription)
    Value=arr
    return Value


class SheJarvis(MDApp):
    def __init__(self, **kwargs):
        super(SheJarvis, self).__init__(**kwargs)
        self.theme_cls.theme_style = "Dark"
        self.kv = Builder.load_string('''
#:kivy 2.0.0
MDRelativeLayout:
    id: box
    MDLabel:
        id: aa
        text: "User wrote here."
        adaptive_height: True
        pos:350,560
        canvas.before:
            Color:
                rgba: 0,255,255,.2
            Rectangle:
                pos: 335,560
                size: 500,20
    MDLabel:
        id: n
        text: "AI wrote here."
        adaptive_height: True
        pos:5,360
        canvas.before:
            Color:
                rgba: 0,255,0,0.2
            Rectangle:
                pos: self.pos
                size: self.size
    MDIconButton:
        id: button
        icon:"mic.png"
        pos:350,20
  
''')


    def build(self):
        self.kv.ids.n.text="mk"
        self.kv.ids.aa.text = "hello sir I am your desktop Tell me how may I help you"
        self.kv.ids.button.bind(on_press = self.call)
        return self.kv
    def call(self,event):
        speak("hello sir I am your desktop Tell me how may I help you")
        Value = "hello sir I am your desktop Tell me how may I help you"
        self.kv.ids.aa.text = "hello sir I am your desktop Tell me how may I help you"


        print("sss")
        query = takeCommand().lower()
        if "open youtube" in query:
            speak("Opening YouTube ")
            self.kv.ids.aa.text="opening youtube"
            webbrowser.open("www.youtube.com")


        elif "open google" in query:
                speak("Opening Google ")
                self.kv.ids.aa.text="opening google"
                webbrowser.open("www.google.com")


        elif "which day it is" in query:
                self.kv.ids.aa.text = "Which day it is"
                self.kv.ids.n.text = tellDay()

        elif "tell me the time" in query:

            # self.kv.ids.aa.text= "Tell me the time"
            time = str(datetime.datetime.now())
            print(time)
            hour = time[11:13]

            min = time[14:16]
            speak("The time is sir" + hour + "Hours and" + min + "Minutes")


        elif "weather" in query:
                speak("which city sir ")
                self.kv.ids.aa.text="tell me weather"
                print("which city sir ")
                city = input()

                self.kv.ids.n.text = tellweather(city)

        elif "bye" in query:
                self.kv.ids.aa.text="bye"
                speak("Bye for now")
                self.kv.ids.n.text = "Bye you son of a"
        elif "news" in query:
            self.kv.ids.aa.text="tell me news"
            key = {"api-key": "yjGaBu8APLGlfbcXg5amsNOoeO3HMDya"}
            path = "https://api.nytimes.com/svc/topstories/v2/world.json?"
            file = requests.get(path, key)
            decode = file.json()
            arr = [0,0,0,0,0]
            for i in range(0, 5):
                 arr[i] = " "+ decode['results'][i]['multimedia'][0]['caption']
                # print(decode['results'][i]['multimedia'][0]['caption'])
                 speak(decode['results'][i]['multimedia'][0]['caption'])
            str = " "
            res = str.join(arr)
            self.kv.ids.n.text = res

        elif "from wikipedia" in query:
                self.kv.ids.aa.text = "From wikipedia"
                speak("Checking the wikipedia ")
                query = query.replace("wikipedia", "")

                result = wikipedia.summary(query, sentences=5)
                speak("According to wikipedia")
                speak(result)
                self.kv.ids.n.text = result

        elif "your name" in query:
                self.kv.ids.aa.text="Your name"
                speak("your dad son of bitch")
                self.kv.ids.n.text = "your dad son of bitch"


if __name__ == '__main__':
    SheJarvis().run()
    # Take_query()
