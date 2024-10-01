import speech_recognition as sr
import webbrowser
import pyttsx3
import songLibary


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text) :
    engine.say(text)
    engine.runAndWait()
    

def processCommand(command) :
    if "open google" in command.lower() :
        speak("opening google")
        webbrowser.open("https://google.com")
    elif "open facebook" in command.lower() :
        speak("opening facebook")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in command.lower() :
        speak("opening youtube")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in command.lower() :
        speak("opening linkedin")
        webbrowser.open("https://linkedin.com")
    elif "play song" in command.lower():
        play = command.lower().split("play song")[0].strip()  # Extract text after "play song"
        try:
            songLibary.song[play]  # Play the song
        except KeyError:
            speak("Sorry, I couldn't find that song.")

    elif "describe" in command.lower():
        speak("I am Jarvis, a voice-activated personal assistant.Developed by Minhaajuddin. I can perform various tasks like opening websites, playing songs, and providing basic information. I am still under development, but I am constantly learning and improving.")
        
    else:
        # Let openAI handle the request (if implemented)
        pass


if __name__ == "__main__" :
    speak("Initializing jarvis...")
    # listen for the wake word "Jarvis"
    # obtain audio from the microphone
    while True :
        r = sr.Recognizer()
        # recognize speech using google
        print("recognizing...")
        try :
            with sr.Microphone() as source :
                print("Listening...!")
                audio = r.listen(source, timeout = 5, phrase_time_limit = 3)
                      
            word = r.recognize_google(audio)
            
            if(word.lower() == "jarvis") :
                speak("Yes sir, I am here")
                # listen for command
                
                with sr.Microphone() as source :
                    print("Jarvis Active...")
                    audio = r.listen(source, timeout = 5, phrase_time_limit = 3)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
                    
                    
        except Exception as e :
            print("Error; {0}".format(e))