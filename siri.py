import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[2].id)
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Anup")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! Anup")

    elif hour>=18 and hour<10:
        speak("Good Night! Anup")   

    else:
        speak("Good Evening! Anup")  

    speak("I am Siri. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com")

        elif 'open hackerrank' in query:
            webbrowser.open("https://www.hackerrank.com")  

        elif 'open gmail' in query:
            webbrowser.open("https://www.gmail.com")

        elif 'panu dekhbo' in query:
            webbrowser.open("https://www.xvideos.com")


        elif 'play music' in query:
            music_dir = 'C:\\Users\\ANUP\\Music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[3]))

        elif "time please" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Time is{strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ANUP\\PycharmProjects\\FirstProgram\\binary_search.py"
            os.startfile(codePath)

        elif 'email to anup' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "anupjana59008@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Anup. I am not able to send this email")