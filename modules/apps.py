# modules/apps.py
import os
import subprocess
from utils.voice import speak

def open_application(command):
    apps = {
        'chrome': ('chrome', 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe'),
        'notepad': ('notepad', 'notepad.exe'),
        'calculator': ('calculator', 'calc.exe'),
        'spotify': ('spotify', 'spotify.exe'),
        'vscode': ('code', 'code.exe'),
    }

    for app_name, (keyword, path) in apps.items():
        if keyword in command:
            try:
                subprocess.Popen(path)
                speak(f"Opening {app_name}")
                return
            except Exception as e:
                speak(f"Failed to open {app_name}")
                print(f"Error: {e}")
                return

    speak("Application not recognized.")
