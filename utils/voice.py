import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 160)
engine.setProperty('volume', 0.9)

voices = engine.getProperty('voices')
try:
    engine.setProperty('voice', voices[1].id)
except:
    pass

def speak(text):
    print(f"JARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = r.listen(source, timeout=6, phrase_time_limit=8)
            command = r.recognize_google(audio, language="en-IN")
            print(f"USER: {command}")
            return command
        except sr.WaitTimeoutError:
            print("⏰ Timeout: No voice detected.")
            speak("I didn’t hear anything. Please try again.")
            return ""
        except sr.UnknownValueError:
            print("🙁 Could not understand audio.")
            speak("Sorry, I didn’t understand that.")
            return ""
        except sr.RequestError as e:
            print(f"❌ Google Speech API error: {e}")
            speak("Speech service is unavailable right now. Please check your internet connection.")
            return ""
