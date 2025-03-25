import os
import tkinter as tk
from tkinter import filedialog
import pygame
from mutagen.mp3 import MP3

class AudioPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("🎵  Music Player")
        self.root.geometry("400x350")
        self.root.configure(bg="#1E1E1E")

        pygame.mixer.init()  # Initialize pygame mixer

        # Label for Song Info
        self.song_label = tk.Label(root, text="No Song Selected", font=("Arial", 14, "bold"), bg="#1E1E1E", fg="white")
        self.song_label.pack(pady=10)

        # Progress Bar
        self.progress = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, length=300, bg="cyan", sliderlength=10)
        self.progress.pack(pady=5)

        # Button Frame
        button_frame = tk.Frame(root, bg="#1E1E1E")
        button_frame.pack(pady=10)

        # Buttons
        self.prev_button = tk.Button(button_frame, text="⏮ Prev", font=("Arial", 12, "bold"), bg="gray", fg="white",
                                     width=8, command=self.prev_song)
        self.prev_button.pack(side=tk.LEFT, padx=5)

        self.play_button = tk.Button(button_frame, text="▶ Play", font=("Arial", 12, "bold"), bg="green", fg="white",
                                     width=8, command=self.play_pause)
        self.play_button.pack(side=tk.LEFT, padx=5)

        self.next_button = tk.Button(button_frame, text="⏭ Next", font=("Arial", 12, "bold"), bg="gray", fg="white",
                                     width=8, command=self.next_song)
        self.next_button.pack(side=tk.LEFT, padx=5)

        # Load Music Button
        self.load_button = tk.Button(root, text="📂 Load Music Folder", font=("Arial", 12, "bold"), bg="blue", fg="white",
                                     width=20, command=self.load_music)
        self.load_button.pack(pady=10)

        # Variables
        self.song_list = []
        self.current_index = 0
        self.playing = False

    def load_music(self):
        """Opens a folder and loads all MP3 files"""
        folder = filedialog.askdirectory()
        if folder:
            self.song_list = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".mp3")]
            if self.song_list:
                self.current_index = 0
                self.show_song_info()
            else:
                self.song_label.config(text="No MP3 files found")

    def show_song_info(self):
        """Displays song title from metadata"""
        if self.song_list:
            song_path = self.song_list[self.current_index]
            song = MP3(song_path)  # Get metadata
            song_name = os.path.basename(song_path).replace(".mp3", "")
            self.song_label.config(text=f"🎵 {song_name}")

    def play_pause(self):
        """Plays or pauses the current song"""
        if not self.song_list:
            return
        if not self.playing:
            pygame.mixer.music.load(self.song_list[self.current_index])
            pygame.mixer.music.play()
            self.playing = True
            self.play_button.config(text="⏸ Pause", bg="red")
        else:
            pygame.mixer.music.pause()
            self.playing = False
            self.play_button.config(text="▶ Play", bg="green")

    def next_song(self):
        """Plays the next song in the list"""
        if self.song_list:
            self.current_index = (self.current_index + 1) % len(self.song_list)
            self.show_song_info()
            self.play_pause()

    def prev_song(self):
        """Plays the previous song in the list"""
        if self.song_list:
            self.current_index = (self.current_index - 1) % len(self.song_list)
            self.show_song_info()
            self.play_pause()

# Run the GUI
root = tk.Tk()
app = AudioPlayer(root)
root.mainloop()
