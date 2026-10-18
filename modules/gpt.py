import os

from openai import OpenAI, OpenAIError
from utils.voice import speak


def handle_ai_conversation(command):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("[OpenAI ERROR] OPENAI_API_KEY is not set.")
        speak("OpenAI API key is missing. Set the OPENAI_API_KEY environment variable.")
        return

    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": command}],
        )
        answer = response.choices[0].message.content
        if answer:
            print(f"🧠 ChatGPT says: {answer}")
            speak(answer)
        else:
            speak("I didn't quite get that. Could you rephrase?")
    except OpenAIError as error:
        print(f"[OpenAI ERROR] {error}")
        speak("Sorry, I'm having trouble connecting to the AI service.")
