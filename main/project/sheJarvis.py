
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


def tellTime():
	
	
	time = str(datetime.datetime.now())
	
	
	print(time)
	hour = time[11:13]
	min = time[14:16]
	speak("The time is sir" + hour + "Hours and" + min + "Minutes")	

def Hello():
	
	# This function is for when the assistant
	# is called it will say hello and then
	# take query
	speak("hello sir I am your desktop Tell me how may I help you")

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


def Take_query():

	
	Hello()
	


	while(True):
		
		
		query = takeCommand().lower()
		if "open youtube" in query:
			speak("Opening YouTube ")
			
			
			webbrowser.open("www.youtube.com")
			continue
		
		elif "open google" in query:
			speak("Opening Google ")
			webbrowser.open("www.google.com")
			continue
			
		elif "which day it is" in query:
			tellDay()
			continue
		

                
			continue
		elif "tell me the time" in query:
			tellTime()
			continue
		elif "weather" in query:
			speak("which city sir ")
			print("which city sir ")
			city = input()
			tellweather(city)
		
		elif "bye" in query:
			speak("Bye for now")
			exit()
		
		elif "from wikipedia" in query:
			
			
			speak("Checking the wikipedia ")
			query = query.replace("wikipedia", "")
			
			
			result = wikipedia.summary(query, sentences=5)
			speak("According to wikipedia")
			speak(result)
		
		elif "tell me your name" in query:
			speak("I am SheeJarvis. Your deskstop Assistant")

if __name__ == '__main__':
	
	
	Take_query()
