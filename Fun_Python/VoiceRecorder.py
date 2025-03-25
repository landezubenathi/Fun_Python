import pyaudio
import wave
import threading
import tkinter as tk
from tkinter import messagebox
import os
import time
import random

class AudioRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎙 Audio Recorder")
        self.root.geometry("400x400")
        self.root.configure(bg="#1E1E1E")

        # Title Label
        self.title_label = tk.Label(root, text="🎙 Audio Recorder", font=("Arial", 18, "bold"), bg="#1E1E1E", fg="white")
        self.title_label.pack(pady=10)

        # Waves Animation Canvas
        self.canvas = tk.Canvas(root, width=300, height=50, bg="#1E1E1E", highlightthickness=0)
        self.canvas.pack()

        # Recording Status Label
        self.status_label = tk.Label(root, text="", font=("Arial", 12, "italic"), bg="#1E1E1E", fg="red")
        self.status_label.pack()

        # Timer Label (Initially Hidden)
        self.timer_label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#1E1E1E", fg="cyan")
        self.timer_label.pack()

        # Button Frame (For Record & Stop)
        button_frame = tk.Frame(root, bg="#1E1E1E")
        button_frame.pack(pady=5)

        # Record Button
        self.record_button = tk.Button(button_frame, text="🎤 Record", font=("Arial", 14, "bold"), bg="red", fg="white",
                                       width=12, height=1, command=self.start_recording)
        self.record_button.pack(side=tk.LEFT, padx=5)

        # Stop Button
        self.stop_button = tk.Button(button_frame, text="⏹ Stop", font=("Arial", 14, "bold"), bg="black", fg="white",
                                     width=12, height=1, command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        # Play Button (Below Record & Stop)
        self.play_button = tk.Button(root, text="▶ Play", font=("Arial", 14, "bold"), bg="green", fg="white",
                                     width=12, height=1, command=self.play_audio, state=tk.DISABLED)
        self.play_button.pack(pady=5)

        # Recording Variables
        self.recording = False
        self.file_name = "recorded_audio.wav"
        self.start_time = 0  # To store start time
        self.waves = []  # Store wave objects for animation

    def start_recording(self):
        self.recording = True
        self.record_button.config(state=tk.DISABLED, bg="#555")
        self.stop_button.config(state=tk.NORMAL, bg="black")
        self.play_button.config(state=tk.DISABLED, bg="#555")
        self.status_label.config(text="Recording...", fg="red")

        # Show timer label and start timer
        self.timer_label.config(text="⏳ Time: 0s")
        self.timer_label.pack()
        self.start_time = time.time()  # Record start time
        threading.Thread(target=self.record_audio).start()
        self.update_timer()  # Start the timer
        self.animate_waves()  # Start waves animation

    def update_timer(self):
        """Updates the timer label while recording"""
        if self.recording:
            elapsed_time = int(time.time() - self.start_time)
            self.timer_label.config(text=f"⏳ Time: {elapsed_time}s")
            self.root.after(1000, self.update_timer)  # Update every second
        else:
            self.timer_label.config(text="")  # Hide timer when stopped

    def animate_waves(self):
        """Creates a simple waves effect while recording"""
        if self.recording:
            self.canvas.delete("all")  # Clear previous waves
            for i in range(10):  # Generate 10 waves
                x = i * 30
                height = random.randint(10, 30)  # Random wave height
                self.canvas.create_line(x, 25 - height, x, 25 + height, width=4, fill="cyan", capstyle=tk.ROUND)
            self.root.after(300, self.animate_waves)  # Update every 300ms

    def record_audio(self):
        chunk = 1024  # Buffer size
        format = pyaudio.paInt16  # Audio format
        channels = 1  # Mono audio
        rate = 44100  # Sample rate

        p = pyaudio.PyAudio()
        stream = p.open(format=format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk)

        frames = []
        while self.recording:
            data = stream.read(chunk)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

        # Save to WAV file
        wf = wave.open(self.file_name, "wb")
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(rate)
        wf.writeframes(b"".join(frames))
        wf.close()

        self.status_label.config(text="✅ Recording saved!", fg="green")
        self.play_button.config(state=tk.NORMAL, bg="green")
        messagebox.showinfo("Recording Saved", "Audio saved as recorded_audio.wav")

    def stop_recording(self):
        self.recording = False
        self.record_button.config(state=tk.NORMAL, bg="red")
        self.stop_button.config(state=tk.DISABLED, bg="#555")
        self.status_label.config(text="Processing...", fg="blue")
        self.canvas.delete("all")  # Stop waves animation
        self.timer_label.config(text="")  # Hide timer when stopped

    def play_audio(self):
        os.system(f"start {self.file_name}" if os.name == "nt" else f"afplay {self.file_name}")

# Run the GUI
root = tk.Tk()
app = AudioRecorderApp(root)
root.mainloop()
