# gui/interface.py
import tkinter as tk
from tkinter import scrolledtext, ttk
import threading
from utils.voice import speak, listen
from modules.music import play_music
from modules.news import tell_time

class JarvisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("J.A.R.V.I.S. Assistant")
        self.root.geometry("800x600")
        self.root.configure(bg="#0c0c0c")

        # Header
        header = tk.Frame(root, bg="#1e1e1e", height=60)
        header.pack(fill=tk.X)

        self.title = tk.Label(header, text="J.A.R.V.I.S.", font=("Arial", 24, "bold"),
                            fg="#00ffcc", bg="#1e1e1e")
        self.title.pack(side=tk.LEFT, padx=20)

        # Status bar
        self.status = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W,
                             font=("Arial", 10), fg="#00ffcc", bg="#1e1e1e")
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

        # Main content area
        main_frame = tk.Frame(root, bg="#0c0c0c")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Chat display
        chat_frame = tk.LabelFrame(main_frame, text="Conversation", font=("Arial", 12),
                                 fg="#00ffcc", bg="#1e1e1e", bd=2)
        chat_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))

        self.chat_display = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD,
                                                    bg="#1e1e1e", fg="#ffffff",
                                                    font=("Consolas", 12), bd=0)
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.chat_display.config(state=tk.DISABLED)

        # Controls
        control_frame = tk.Frame(main_frame, bg="#0c0c0c")
        control_frame.pack(fill=tk.X, pady=(5, 0))

        buttons = [
            ("Play Music", self.play_music),
            ("Current Time", self.current_time),
            ("Listen", self.start_listening),
            ("Clear", self.clear_chat),
            ("Exit", root.quit)
        ]

        for text, command in buttons:
            btn = ttk.Button(control_frame, text=text, command=command)
            btn.pack(side=tk.LEFT, padx=5, pady=5)

        # Welcome message
        self.add_to_chat("JARVIS", "Initializing systems...")
        self.add_to_chat("JARVIS", "Security protocols engaged...")
        self.add_to_chat("JARVIS", "All systems operational. How can I assist you?")

    def add_to_chat(self, sender, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)

    def play_music(self):
        self.add_to_chat("You", "Play music")
        threading.Thread(target=play_music).start()

    def current_time(self):
        self.add_to_chat("You", "What time is it?")
        threading.Thread(target=tell_time).start()

    def start_listening(self):
        self.add_to_chat("System", "Listening...")
        self.status.config(text="Listening...")
        threading.Thread(target=self.listen_command).start()

    def listen_command(self):
        command = listen()
        if command:
            self.add_to_chat("You", command)
            # In a real implementation, you would process the command here
        self.status.config(text="Ready")

    def clear_chat(self):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.delete(1.0, tk.END)
        self.chat_display.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    gui = JarvisGUI(root)
    root.mainloop()
