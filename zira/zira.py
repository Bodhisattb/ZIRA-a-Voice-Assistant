import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  

def speak(audio):
    """Function to make the assistant speak"""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Greets the user based on the time of the day"""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Sarah. How may I help you?")

def takecommand():
    """Takes voice input from user and returns the recognized text"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')  
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again, please....")
        return "None"  
    return query.lower()

if __name__ == "__main__":
    wishMe()
    while True:
        query = takecommand()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = "D:\\music"  # Make sure this directory exists
            songs = os.listdir(music_dir)  # Get list of songs
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))  # Play the first song
            else:
                speak("No music files found in the directory.")

        elif 'exit' in query or 'quit' in query:
            speak("Goodbye! Have a great day.")
            break
