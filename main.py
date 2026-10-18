from utils.voice import speak, listen
from modules.music import play_music
from modules.search import search_google
from modules.messaging import send_whatsapp_message
from modules.news import tell_time, get_weather, get_latest_news, get_past_news_by_date
from modules.apps import open_application
from modules.gpt import handle_ai_conversation
import json
import sys
import os

def load_config():
    config_path = "config.json"
    if not os.path.exists(config_path):
        speak("Configuration file is missing.")
        print("❌ config.json file not found.")
        sys.exit()
    with open(config_path, "r") as f:
        return json.load(f)

def main():
    config = load_config()
    print("✅ Jarvis started successfully.")
    speak("Initializing Jarvis. How can I assist you?")

    fail_count = 0
    max_fails = 3

    while True:
        command = listen()

        if not command:
            fail_count += 1
            if fail_count >= max_fails:
                speak("Speech recognition is not working. Please check your internet connection and restart me.")
                print("🛑 Too many speech recognition failures. Exiting.")
                break
            continue
        fail_count = 0

        command = command.lower()
        print(f"🎧 You said: {command}")

        if 'play music' in command:
            play_music()
        elif 'search' in command:
            search_google(command)
        elif 'send message' in command or 'whatsapp' in command:
            send_whatsapp_message(config)
        elif 'time' in command:
            tell_time()
        elif 'weather' in command:
            speak("Which city's weather would you like to know?")
            city = listen()
            if city:
                get_weather(config, city)
            else:
                get_weather(config)
        elif 'open' in command:
            open_application(command)
        elif "news" in command or "latest news" in command or "aaj ki news" in command or "highlights" in command:
            get_latest_news(config)
        elif "past news" in command or "news from" in command or "pichle saal" in command or "highlight" in command:
            speak("Please tell me the date in YYYY dash MM dash DD format.")
            date = listen()
            if not date:
                speak("Date was not understood. Try again.")
                continue
            speak("Do you want to search by keyword? Say cricket or ai or say no.")
            keyword = listen()
            if keyword and keyword.lower() == "no":
                keyword = None
            get_past_news_by_date(config, date, keyword)
        elif 'stop' in command or 'exit' in command or 'shutdown' in command:
            speak("Goodbye Priyanshu. Shutting down.")
            print("🛑 Jarvis has been stopped.")
            break
        else:
            # 💬 Fallback to OpenAI for AI conversation
            print("🤖 Thinking...")
            handle_ai_conversation(command)

if __name__ == "__main__":
    print("🔓 Running Jarvis without voice authentication...")
    main()
