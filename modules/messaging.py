# modules/messaging.py
import pywhatkit as kit
import time
from utils.voice import speak, listen

def send_whatsapp_message(config):
    try:
        default_phone = config.get("whatsapp_phone")

        speak("Who should I send the message to? Please say the name or number.")
        recipient = listen()

        if 'default' in recipient or 'same' in recipient:
            phone = default_phone
        else:
            # In real implementation, you'd have a contacts database
            phone = input("Enter phone number with country code: ")

        speak("What should the message say?")
        message = listen()

        if not message:
            speak("Message not received.")
            return

        kit.sendwhatmsg_instantly(phone, message, 15, True, 3)
        time.sleep(10)
        speak("Message sent successfully.")
    except Exception as e:
        speak("Failed to send the WhatsApp message.")
        print(f"[WhatsApp ERROR] {e}")
