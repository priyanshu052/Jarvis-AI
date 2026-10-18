# utils/security.py

from utils.voice import speak

def voice_unlock():
    # Voice authentication removed — direct access granted
    print("Voice authentication bypassed.")
    speak("Welcome back, Priyanshu.")
    return True
