import pywhatkit  
import speech_recognition as sr 
from gtts import gTTS
from playsound import playsound
import time


def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        text = "What do you want to search for?"
        var = gTTS(text=text, lang="en-AU")
        var.save("search.mp3")
        playsound(".\search.mp3")
        audio = r.listen(source)
        time.sleep(2)
        print("Searching..")
        time.sleep(3)
        text = "Search completed"
        var = gTTS(text=text, lang="en")
        var.save("search1.mp3")
        print("Search completed")
        playsound(".\search1.mp3") 
    play = r.recognize_google(audio, language='ar-EG')
    pywhatkit.playonyt(play)


if __name__ == "__main__":
    main()
    