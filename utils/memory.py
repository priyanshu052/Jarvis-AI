import json

def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_memory(data):
    with open("memory.json", "w") as f:
        json.dump(data, f, indent=4)

def greet_user():
    memory = load_memory()
    name = memory.get("name")
    if not name:
        from utils.voice import speak, listen
        speak("What's your name?")
        name = listen()
        memory["name"] = name
        save_memory(memory)
    return f"Good morning, {name}."
