import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
#PyAudio Required!


print("Serpento Assistant Online.")
r= sr.Recognizer()

engine = pyttsx3.init(driverName='sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
boss = "YourName"
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def whatHour():
    hour=int(datetime.datetime.now().hour)
    minute=int(datetime.datetime.now().minute)
    time = str(hour)+str(minute)
    if hour>=0 and hour <= 4:
        speak("The time is:" + time + "... I think you should consider going to sleep "+boss)
    elif hour > 4 and hour <= 8:
        speak("The time is:"+ time + "... You got up really early "+boss)
    elif hour >8:
        speak("The time is:"+ time + " ... Have a great day "+boss)

def commandTaker():
    
    with sr.Microphone() as source:
        speak("I'm awaiting your commands.")
        print("Speak Now")
        audio = r.listen(source)
    try : 
        query = r.recognize_google(audio)
        if 'wikipedia' in query.lower():
            speak('searching wikipedia...')
            query=query.replace("according to","")
            query=query.replace("search in","")
            query=query.replace("what is","")
            query=query.replace("who is","")
            query=query.replace("Wikipedia","")
            query=query.replace("what are","")
            query=query.replace("who are","")
            results = wikipedia.summary(query, sentences=4)
            speak(results)
        elif 'open messenger' in query.lower():
           speak("Do you want me to open a conversation with your girlfriend, your dad, your mum, artur, with your colleagues from class or with your friends?")
           print("speak now") 
           r2 = sr.Recognizer()
           query2=None
           with sr.Microphone() as source:
               audio = r2.listen(source)
               while query2==None:
                   try:
                       query2=r2.recognize_google(audio)
                   except sr.UnknownValueError:
                       speak("Please, speak again")
                       query2=None
                   except sr.RequestError:
                       query2=None
                       print("failed")
           if "girlfriend" in query2:    
               webbrowser.open("MESSENGER LINK")
           elif "Arthur" in query2:
               webbrowser.open("MESSENGER LINK")    
           elif "dad" in query2:
               webbrowser.open("MESSENGER LINK")
           elif "mom" in query2:
               webbrowser.open('MESSENGER LINK')
           elif "friends" in query2:
               webbrowser.open('MESSENGER LINK')
           elif "colleagues" in query:
               webbrowser.open("MESSENGER LINK")
        elif 'music' in query.lower():
            speak("Which kind of music do you want to listen to boss?")
            speak("American Rap, polish rap,rock,pop or the polish toplist?")
            print("speak now")  
            r2 = sr.Recognizer()
            query2=None
            with sr.Microphone() as source:
                audio = r2.listen(source)
                while query2==None:
                    try:
                        query2=r2.recognize_google(audio)
                    except sr.UnknownValueError:
                        speak("Please, speak again")
                        query2==None
                    except sr.RequestError:
                        query2=None
                        print("failed")
            if "polish rap" in query2.lower():
                speak("Okay, lets play some badass polish hip hop")
                webbrowser.open("https://www.youtube.com/watch?v=gODYNfahP1o&list=PLlYKDqBVDxX2m_ZPY2hJbN3EXiDUxuQpk", autoraise=False)
            elif "american rap" in query2.lower():
                speak("Damn son, american rap it is than")
                webbrowser.open("https://www.youtube.com/watch?v=ZBOoVj6IW3s&list=PL-FVH5VWgRPHNz24zZ5_FLHQWoidN6O1d", autoraise=False)
            elif "rock" in query2.lower():
                speak("Let's rock an rollll")
                webbrowser.open("https://www.youtube.com/watch?v=8SbUC-UaAxE&list=PL3485902CC4FB6C67",autoraise=False)
            elif "pop" in query2.lower():
                speak("okay, pop is cool as well")
                webbrowser.open("https://www.youtube.com/watch?v=fnPn6At3v28&list=PLyORnIW1xT6xu8M0BYUiP2vub8n8KI_-G",autoraise=False)
            elif "romantic" in query2.lower(): 
                speak("I think Shawn Mendes wouldn't be bad boss")
                webbrowser.open("https://www.youtube.com/watch?v=lY2yjAdbvdQ&list=PLCNNHFKf2brOy3PkZKz1Eb9U-oAIfYIbt",autoraise=False)     
            elif "top list" in query2.lower():
                speak("let's see what rocks the partys at the moment")
                webbrowser.open("https://www.youtube.com/watch?v=wkUcu4IzHcY",autoraise=False)
   
 
        
    except sr.UnkonownValueError:
        speak("I fell into an issue, try again")
        query = None
    except sr.RequestError:
        speak("failed".format())
        query = None   
        
  

pr=sr.Recognizer()
whatHour()
speak("Serpento Assistant is Online. How can i help you Boss?")
while True:
    with sr.Microphone() as source: 
        print("speak")
        audio = pr.listen(source,timeout=10)
            
        try:
            call = pr.recognize_google(audio)
            if "wake up" in call.lower():
                print("pop")
                commandTaker()
            elif "sleep" in call.lower():
                speak("Im going off Boss")
                break
        except sr.UnknownValueError:
            print("-")
        except sr.WaitTimeError:
            print("-")
