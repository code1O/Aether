import pyttsx3
import speech_recognition as sr
from Scripts import (battery)
from configparser import ConfigParser

config = ConfigParser()
config.read('configuration.ini')

class speaker:
    def __init__(self, voice) -> None:
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[voice].id)
        
    def speak(self, query):
        self.engine.say(query)
        self.engine.runAndWait()

def voice_recognize():
    r = sr.Recognizer()
    with sr.microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_amazon(source, language=config.get('SYSTEM', 'Language'))
        print(f"{query}")
    except Exception as e:
        print(e)
        speaker().speak("Sorry i did not recognize that, try again")
        return "None"
    return query.lower()

def process_voiceCommands(query):
    if "battery" in query:
        speaker().speak(battery.percent_as_string())