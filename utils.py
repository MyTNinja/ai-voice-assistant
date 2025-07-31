import re
import os
import tempfile
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

def remove_think_tags(text):
    return re.sub(r"<think>.*?</think>", "", str(text), flags=re.DOTALL).strip()

def speak(text, lang='en'):
    try:
        tts = gTTS(text=text, lang=lang)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            filename = fp.name
            tts.save(filename)
        playsound(filename)
        os.remove(filename)
    except Exception as e:
        print("TTS Error:", e)

def get_voice_input():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()
    print("Speak now...")
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return None
    except sr.RequestError:
        print("Speech Recognition service unavailable.")
        return None
