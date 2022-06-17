from kivy.lang import Builder                               # GUI
from kivymd.app import MDApp
import pyttsx3                                              # to convert text to speech
import speech_recognition as sr                             # to recognize our speech
import webbrowser                                           # to interact with web browser
import datetime                                             # to show date and time
import os                                                   # OS related functions
import random
import wikipedia                                            # to fetch info from wikipedia
import pyautogui                                            # to take screenshot
import requests                                             # to execute functions using OS
import json                                                 # api handling purposes
import pyjokes                                              # to tell random python jokes
import wolframalpha                                         # interact with wolframalpha
from countryinfo import CountryInfo                         # to get country's capital and all
from PyDictionary import PyDictionary                       # to show meaning of words
import randfacts                                            # to show random facts
import smtplib                                              # email related functions
import winsound                                             # to make the beep sound
from win10toast import ToastNotifier                        # to show Windows 10 notifications


# this method is for taking the commands speech_Recognition module
# we will use the Recognizer
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
        try:
            print("Recognizing...")
            Query = r.recognize_google(audio, language='en-in')
            print("you said :", Query)

        except Exception as e:
            print(e)
            print("Press mic button and Say that again sir")
            return "None"

        return Query


def speak(audio):
    engine = pyttsx3.init()
    # getter method(gets the current value
    # of engine property)
    voices = engine.getProperty('voices')

    # [0]=female voice in set Property.
    engine.setProperty('voice', voices[0].id)

    # Method for the speaking of the assistant
    engine.say(audio)

    # Blocks while processing all the queued commands
    engine.runAndWait()

# this function is to set alarm / reminder
def timer(sub, sec):
    noti = ToastNotifier()
    noti.show_toast("Reminder By sheJarvis", f"""Alarm will go off in {sec} seconds""", duration=20)
    noti.show_toast(f"Reminder By sheJarvis", sub, duration=20)
    frequency = 2500
    duration = 1000
    winsound.Beep(frequency, duration)

# This function is for telling the day of the week
def tellToday():

    day = datetime.datetime.today().weekday() + 1

    # this line tells us about the number
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        return day_of_the_week


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

    # this line tells us about the number
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        return day_of_the_week


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mailforproject3@gmail.com', 'projectmailpswd.txt')
    server.sendmail('mailforproject3@gmail.com', to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save(r'C:\\Users\\DELL\\Pictures\\Screenshots\\screenshot_by_jarvis.png')


def tellTime():
    # This method will give the time
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is " + hour + "Hours and" + min + "Minutes")


def Hello():
    # This function is for when the assistant
    # is called it will say hello and then
    # take query
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 17:
        speak("good afternoon")
    else:
        speak("good evening")

    #speak("I am shee jarvis, how may I help you?")

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
        self.kv.ids.n.text = "Loading..."
        self.kv.ids.aa.text = "Press mic button and speak"
        self.kv.ids.button.bind(on_press=self.call)

        return self.kv

    Hello()
    def call(self, event):
        speak("Hello sir, how may I help you?")

        self.kv.ids.aa.text = "Hello sir, I am your desktop assistant Tell me how may I help you?"

        let =  takeCommand().lower()
        self.kv.ids.aa.text = let
        print("Hmm...")

        query = let

        if "open youtube" in query:
            speak("Opening YouTube ")

            # in the open method we just have to give the link
            # of the website and it will open in default browser
            webbrowser.open("www.youtube.com")
            self.kv.ids.n.text = "YouTube is open"

        elif "open facebook" in query:
            speak("Opening Facebook")
            webbrowser.open("www.facebook.com")
            self.kv.ids.n.text = "Facebook is open"

        elif "open instagram" in query:
            speak("Opening Instagram")
            webbrowser.open("www.instagram.com")
            self.kv.ids.n.text = "Instagram is open"

        elif "open twitter" in query:
            speak("Opening Twitter")
            webbrowser.open("www.twitter.com")
            self.kv.ids.n.text = "Twitter is open"

        elif "open github" in query:
            speak("Opening GitHub")
            webbrowser.open("www.github.com")
            self.kv.ids.n.text = "github is open"

        elif "open stackoverflow" in query or "open stack overflow" in query or "open stack over flow" in query:
            speak("Opening stackoverflow")
            webbrowser.open("www.stackoverflow.com")
            self.kv.ids.n.text = "stackoverflow is open"

        elif "screenshot" in query or "screen shot" in query:
            speak("taking screenshot")
            screenshot()
            self.kv.ids.n.text = "Screenshot saved here C://Users//DELL//Pictures//Screenshots"

        elif "open google" in query:
            speak("Opening Google ")
            webbrowser.open("www.google.com")
            self.kv.ids.n.text = "google is open"

        elif "which day it is" in query or "what day is today" in query or "what day it is" in query or \
                "what is the day" in query:
                        vari = tellToday()
                        self.kv.ids.n.text = "Today is " + vari
                        speak("today is " + vari)

        elif "which day is tomorrow" in query or "what day is tomorrow" in query or "what is the day tomorrow" in query:
            vari = tellTomorrow()
            self.kv.ids.n.text = "Tomorrow is " + vari
            speak("Tomorrow is " + vari)

        elif "tell me the time" in query or "what is the time" in query or "what time is it" in query:
            vari = tellTime()
            """
            self.kv.ids.n.text = " " + vari
            time = str(datetime.datetime.now())
            print(time)
            hour = time[11:13]
            min = time[14:16]
            speak("The time is " + hour + "Hours and" + min + "Minutes")
            self.kv.ids.n.text = "The time is " + hour + " Hours and " + min + " Minutes"
            """

        elif "play music" in query or "play songs" in query or "play song" in query or "random song" in query:

            fav_dir = "C:\\Users\\DELL\\Music\\fav_dir"
            rand = random.choice(os.listdir(fav_dir))
            # songs = os.listdir(fav_dir)
            speak("opening music")
            os.startfile(os.path.join(fav_dir, rand))


        elif "weather" in query or "temperature" in query:
            global str
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
                weather_response = "the temperature is " + str(round(temperature,2)) + " degree celsius " + \
                                   ", the humidity is " + str(humidity) + ", and weather is " \
                                   + str(desc)
                self.kv.ids.n.text = "the temperature is " + str(round(temperature,2)) + " degree celsius " + \
                                     ", the humidity is " + str(humidity) + ", and weather is " \
                                     + str(desc)
                speak(weather_response)
            else:
                speak("no results found")
                self.kv.ids.n.text = "no results found"

        # this will exit and terminate the program
        elif "bye" in query or "exit" in query or "quit" in query:
            speak("Bye, have a nice day")
            self.kv.ids.n.text = "Bye, have a nice day"
            exit()

        # reminder / alarm function
        elif "alarm" in query or "remind" in query or "reminder" in query:
            try:
                speak("What should I remind you of?")
                sub = takeCommand()
                print("alarm for subject : " + sub)
                speak("In how much seconds I should remind you?")
                sec = takeCommand()
                print("I will remind you in " + sec + " seconds")
                speak("I will remind you in " + sec + " seconds")
                timer(sub, sec)
                print("Alarm went off")
                self.kv.ids.n.text = "alarm went off"
                speak("Alarm went off")

            except Exception as e:
                print(e)
                print("sorry, something went wrong")
                speak("sorry, something went wrong")
                self.kv.ids.n.text = "sorry, something went wrong"


        # this will remember whatever you tell to remember
        elif "remember that" in query:
            rememberMsg = query.replace("remember that", "")
            rememberMsg = rememberMsg.replace("jarvis", "")
            speak("you told me to remember that " + rememberMsg)
            self.kv.ids.n.text = "you told me to remember that " + rememberMsg
            remember = open('data.txt', 'w')
            remember.write(rememberMsg)
            remember.close()

        # this will be called whenever to read what has been told to remember
        elif "what do you remember" in query or "told you to remember" in query or "tell you to remember" in query:
            try:
                remember = open('data.txt', 'r')
                speak("you told me to remember that " + remember.read())
                self.kv.ids.n.text = "you told me to remember that " + remember
            except TypeError:
                print(" ")

        elif "from wikipedia" in query:

            # if any one wants to have a information
            # from wikipedia
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")

            # it will give the summary of 3 lines from wikipedia

            result = wikipedia.summary(query, sentences=3)
            self.kv.ids.n.text = "according to wikipedia " + result
            speak("According to wikipedia")
            speak(result)

        #get news
        elif "news" in query:

            key = {"api-key": "yjGaBu8APLGlfbcXg5amsNOoeO3HMDya"}
            path = "https://api.nytimes.com/svc/topstories/v2/world.json?"
            file = requests.get(path, key)

            decode = file.json()

            arr = [0, 0, 0, 0, 0]

            for i in range(0, 5):
                arr[i] = " " + decode['results'][i]['multimedia'][0]['caption']

                # print(decode['results'][i]['multimedia'][0]['caption'])

                speak(decode['results'][i]['multimedia'][0]['caption'])

            str = " "

            res = str.join(arr)

            self.kv.ids.n.text = res

        elif "capital of" in query:
            try:
                ind = query.lower().split().index("of")
                text = listToString(query.split()[ind + 1:])
                capital = CountryInfo(text).capital()
                self.kv.ids.n.text = "the capital of " + text + " is " + capital
                speak("the capital of " + text + " is " + capital)
                print("the capital of " + text + " is " + capital)

            except KeyError:
                print("no results found")
                self.kv.ids.n.text = "no results found"
                speak("no results found")

        elif "meaning of" in query:
            try:
                ind = query.lower().split().index("of")
                text = listToString(query.split()[ind + 1:])
                dic = PyDictionary()
                word = dic.meaning(text)

                for state in word:
                    print(word[state])
                    speak("the meaning is " + listToString(word[state]))
                    self.kv.ids.n.text = "the meaning is " + listToString(word[state])
            except TypeError:
                print("no results found")
                self.kv.ids.n.text = "no results found"
                speak("no results found")

        elif "email to nitin" in query or "mail to nitin" in query:
            try:
                speak("what message should I send?")
                content = takeCommand()
                to = "nitin22092001@gmail.com"
                sendEmail(to, content)
                speak("email sent successfully")
            except Exception as e:
                print(e)
                speak("sorry ,something went wrong")

        elif "email to bhavik" in query or "mail to bhavik" in query:
            try:
                speak("what message should I send?")
                content = takeCommand()
                to = "bhavikjain2888@gmail.com"
                sendEmail(to, content)
                speak("email sent successfully")
            except Exception as e:
                print(e)
                speak("sorry ,something went wrong")

        elif "fact" in query or "facts" in query:
            x = randfacts.get_fact()
            print(x)
            self.kv.ids.n.text = x
            speak(x)

        elif "calculate" in query:
            app_id = "WERGAU-94V8K5KH28"
            client = wolframalpha.Client(app_id)
            ind = query.lower().split().index("calculate")
            text = query.split()[ind + 1:]
            res = client.query("".join(text))
            answer = next(res.results).text
            print("ths answer is " + answer)
            self.kv.ids.n.text = ("ths answer is " + answer)
            speak("the answer is " + answer)


        elif "what is" in query or "who is" in query:
            try:

                app_id = "WERGAU-94V8K5KH28"
                client = wolframalpha.Client(app_id)
                ind = query.split().index("is")
                text = query.split()[ind + 1:]
                res = client.query("".join(text))
                # print(res.results)
                answer = next(res.results).text
                print(answer)
                self.kv.ids.n.text = "the answer is " + answer
                speak("the answer is " + answer)

            except StopIteration:
                print("no results found")
                self.kv.ids.n.text = "no results found"
                speak("no results found")

        elif "where do you live" in query:
            speak("I live in India")
            self.kv.ids.n.text = "I live in India"

        elif "notepad" in query.lower():
            speak("opening notepad")
            self.kv.ids.n.text = "opening notepad "
            os.startfile(
                r"C:\\WINDOWS\\system32\\notepad.exe"
            )

        elif "excel" in query.lower():
            speak("opening microsoft excel")
            self.kv.ids.n.text = "opening microsoft excel "
            os.startfile(
                r"C:\\Program Files (x86)\\Microsoft Office\\Office14\\EXCEL.EXE"
            )
        elif "word" in query.lower():
            speak("opening microsoft word")
            self.kv.ids.n.text = "opening microsoft word "
            os.startfile(
                r"C:\\Program Files (x86)\\Microsoft Office\\Office14\\WINWORD.EXE"
            )
        elif "powerpoint" in query.lower():
            speak("opening microsoft powerpoint")
            self.kv.ids.n.text = "opening microsoft power point "
            os.startfile(
                r"C:\\Program Files (x86)\\Microsoft Office\\Office14\\POWERPNT.EXE"
            )

        elif "joke" in query or "jokes" in query:
            fu = pyjokes.get_joke()
            self.kv.ids.n.text = fu
            speak(fu)

        elif "how are you" in query or "how do you do" in query:
            speak("i am fine , how do you do?")
            self.kv.ids.n.text="i am fine , how do you do?"

        elif "where is" in query:
            ind = query.lower().split().index("is")
            location = query.split()[ind + 1:]
            url = "https://www.google.com/maps/place/" + "".join(location)
            speak("this is where" + listToString(location) + "is")
            self.kv.ids.n.text = "this is where " + listToString(location) + " is "
            webbrowser.open(url)

        elif "how to" in query:
            ind = query.lower().split().index("to")
            text = listToString(query.split()[ind + 1:])
            url = "https://www.youtube.com/results?search_query=" + "".join(text)
            speak("this is what i found on youtube")
            self.kv.ids.n.text = "opening youtube"
            webbrowser.open(url)

        elif "who made you" in query or "who created you" in query:
            self.kv.ids.n.text = "I was created by Bhavik, Nitin and Musaib"
            speak("I was created by Bhavik, Nitin and Musaib")

        elif "tell me your name" in query or "who are you" in query:
            speak("I am shee Jarvis. Your desktop Assistant")
            self.kv.ids.n.text = "I am sheJarvis. Your desktop Assistant"


if __name__ == '__main__':
    SheJarvis().run()
