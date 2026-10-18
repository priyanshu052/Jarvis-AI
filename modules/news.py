import datetime
import requests
import json
import os
from utils.voice import speak

# ----------- Tell Current Time -----------
def tell_time():
    now = datetime.datetime.now()
    time_str = now.strftime("The time is %I:%M %p")
    speak(time_str)
    return time_str

# ----------- Get Current Weather (Dynamic City) -----------
def get_weather(config, custom_city=None):
    try:
        city = custom_city or config.get("default_city", "Delhi")
        api_key = config["weather_api_key"]
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

        response = requests.get(url)
        data = response.json()

        if "error" in data:
            message = f"Sorry, I couldn't fetch the weather for {city}. Please try a different city."
            speak(message)
            return message

        condition = data["current"]["condition"]["text"]
        temp_c = data["current"]["temp_c"]
        feels_like = data["current"]["feelslike_c"]
        humidity = data["current"]["humidity"]
        wind = data["current"]["wind_kph"]

        weather_report = (
            f"Weather in {city}: {condition}. "
            f"Temperature is {temp_c}°C, feels like {feels_like}°C. "
            f"Humidity is {humidity}%, wind speed is {wind} km/h."
        )

        speak(weather_report)
        print(f"🌦️ {weather_report}")
        return weather_report

    except Exception as e:
        error_msg = "Unable to get weather information right now."
        speak(error_msg)
        print("[Weather ERROR]", e)
        return error_msg

# ----------- (Other functions remain unchanged) -----------

HISTORY_FILE = "data/news_history.json"

def save_to_history(date, news_data):
    if not os.path.exists("data"):
        os.makedirs("data")

    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)
    else:
        history = {}

    history[date] = news_data

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

def get_latest_news(config):
    try:
        api_key = config["newsdata_api_key"]
        url = f"https://newsdata.io/api/1/news?apikey={api_key}&country=in&language=en&category=top"

        response = requests.get(url)
        data = response.json()

        articles = data.get("results", [])[:5]

        if not articles:
            speak("Couldn't find any news at the moment.")
            return

        speak("Here are the top headlines for today.")
        news_list = []
        for article in articles:
            title = article.get("title", "No title")
            link = article.get("link", "")
            news_list.append(f"{title}. Link: {link}")
            speak(title)
            print(f"🔖 {title}\n🔗 {link}\n")

        today = str(datetime.date.today())
        save_to_history(today, news_list)

    except Exception as e:
        print("[NEWS ERROR]", e)
        speak("Failed to fetch the latest news.")

def get_past_news_by_date(config, date_str, keyword=None):
    try:
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r") as f:
                history = json.load(f)
        else:
            history = {}

        if date_str in history:
            news_list = history[date_str]
        else:
            api_key = config["newsdata_api_key"]
            url = f"https://newsdata.io/api/1/news?apikey={api_key}&country=in&language=en&from_date={date_str}&to_date={date_str}"
            if keyword:
                url += f"&q={keyword}"
            response = requests.get(url)
            data = response.json()
            news_list = []
            for article in data.get("results", [])[:5]:
                title = article.get("title", "No title")
                link = article.get("link", "")
                news_list.append(f"{title}. Link: {link}")

            if news_list:
                save_to_history(date_str, news_list)

        if not news_list:
            speak(f"No news found for {date_str}.")
            return

        if keyword:
            news_list = [n for n in news_list if keyword.lower() in n.lower()]
            if not news_list:
                speak(f"No news found for keyword '{keyword}' on {date_str}.")
                return

        speak(f"Here are the news highlights from {date_str}.")
        for news in news_list:
            speak(news.split(". Link:")[0])
            print(news)

    except Exception as e:
        print("[PAST NEWS ERROR]", e)
        speak("Failed to fetch past news.")
