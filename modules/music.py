# modules/music.py
import os
import random
import pygame
from utils.voice import speak

# Initialize pygame mixer
pygame.mixer.init()

def play_music():
    music_dir = "C:\\Music"  # Change to your music directory
    try:
        if not os.path.exists(music_dir):
            os.makedirs(music_dir)

        songs = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav'))]

        if not songs:
            speak("No music files found in your directory.")
            return

        song = random.choice(songs)
        file_path = os.path.join(music_dir, song)

        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        speak(f"Playing {os.path.splitext(song)[0]}")

    except Exception as e:
        speak("Failed to play music.")
        print(f"[Music ERROR] {e}")