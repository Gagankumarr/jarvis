import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os




engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait() 




def wishMe():   
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good morning!")
    
    
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    
    
    else:
        speak("Good evening")

    speak("I am Jarvis sir, speed 1 terahertz, memory 1 zettabyte.., tell me how may i help you?")


def take_command():
    r=sr.Recognizer() 
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        r.energy_threshold=2000
        audio=r.listen(source)


    try:
        print("Recognizing....")
        query=r.recognize_google(audio, language='en-in')    
        print(f"User said....{query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...." )
        return "None"   
    return query


if __name__ == "__main__":
   
    wishMe()
    while True:
        query=take_command().lower()
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query=query.replace("wikipedia", "")
            result=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(result)
            speak(result)


        elif 'open youtube' in query:
            speak("opening sir.. please wait....")
            webbrowser.open("youtube.com")


        elif 'open google' in query:
            speak("opening sir.. please wait....")
            webbrowser.open("google.com")    
            
           



        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  

        elif 'play music' in query:
            speak("okay boss....")
            music_dir='C:\\Users\\Bagga\\Downloads\\my songs'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            speak("please wait sir .....")
            strTime=datetime.datetime.now().strftime("%H:%M:%S") 
            print(f"Sir, the time is {strTime}")   
            speak(f"Sir, the time is {strTime}")


        elif 'open code' in query:
            speak("opening sir.. please wait....")
            codePath="C:\\Users\\Bagga\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"    
            os.startfile(codePath)

        elif 'open pycharm' in query:
            speak("opening sir.. please wait....")
            pycharmPath="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.1\\bin\\pycharm64.exe"    
            os.startfile(pycharmPath)
    

        elif 'open chrome' in query:
            speak("opening sir.. please wait....")
            chromePath= "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)    

         
        elif 'open anydesk' in query:
            speak("opening sir.. please wait....")
            ADPath="C:\\Program Files (x86)\\AnyDesk\\AnyDesk.exe"    
            os.startfile(ADPath)   

        elif 'who are you' in query:
            speak("I am jarvis and i want love")
            
    


        elif 'quit' in query:
            speak("Quiting sir.... pleasure to serve you...")
            exit()


    

