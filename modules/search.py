# modules/search.py
import webbrowser
from utils.voice import speak, listen

def search_google(command):
    try:
        query = command.replace('search', '').strip()
        if not query:
            speak("What would you like me to search for?")
            query = listen()

        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {query}")
    except Exception as e:
        speak("Failed to perform the search.")
        print(f"[Search ERROR] {e}")
