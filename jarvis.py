import webbrowser
import pyaudio
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import pywhatkit





engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishME():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening")    
    speak("I am jarvis  Sir. Please Tell me how may I help you")   
       
def takeCommand():
     r= sr.Recognizer()
     with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1
         audio = r.listen(source)
     
     try:
         print("Recognizing...")
         query = r.recognize_google(audio, language ='en-in')
         print(f"User said:{query}\n")
      
     except Exception as e:
         print(e)
         #print("Say that again please.....")  
         return "None" 
     
     return query 
            



    

if __name__== "__main__":
    wishME()
    
    if 1:
      query = takeCommand().lower()
    #logic  for executing tasks based on query
    

    
    if  'send message' in query:
        pywhatkit.sendwhatmsg("+918989410501","Hello from Deep Singh",22, )
        print("Successfully Sent!")
        speak("Message Successfully Sent" )
      
    if 'play' in query:
        song = query.replace('play', '')
        speak('playing ' + song)
        pywhatkit.playonyt(song)
        
    if 'wikipedia' in query:
            speak("Searching wikipedia ...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query ,sentences=1)
            speak("According to wikipedia ")
            print(results)
            speak(results)
            
    
    elif 'on youtube' in query:
            query.replace("on youtube","")      
            webbrowser.open("https://www.youtube.com/results?search_query="+query)  
            
    elif 'score' in query:
        webbrowser.open("https://www.cricbuzz.com/") 
        
    elif ' spotify' in query:
        query.replace("spotify","")
        webbrowser.open("https://open.spotify.com/search/"+query)
    
    elif 'play song' in query:
        music_dir = 'F:\songs'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
    
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%M")
        speak(f"Sir,the time is {strTime}")
        
    elif 'open google' in query:
        webbrowser.open("https://www.google.co.in")  
    
    elif 'search' in query:
         pywhatkit.search("Coding Ninjas")
    
    elif 'open code' in query:
        codePath ="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
        os.startfile(codePath)
        
    elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
 
    elif "who made you" in query or "who created you" in query:
            speak("I have been created by Deep Singh.")
        
    
    elif 'reason for you' in query:
            speak("I was created as a Minor project by Deep Singh ")
    
    elif 'joke' in query:
            speak(pyjokes.get_joke())
            speak ("want to  listen more jokes sir") 
    
    