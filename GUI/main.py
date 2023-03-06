
import os
import wave
import time
import threading
import tkinter as tk
import pyaudio
from tkinter import messagebox


class VoiceRecorder:

    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable(True, True)
        self.Label = tk.Label(text="Please say the following phrase to recreate your voice",
		 fg = "black",
		 font = "Helvetica 16 bold italic").pack()
        self.Label = tk.Label(text="That quick beige fox jumped in the air over each thin dog. Look out, I shout, for he's foiled you again, creating chaos.",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold").pack()
        self.button = tk.Button(text="Record", font=("Arial", 60, "bold"),
                                command=self.click_trigger)
        self.button.pack()
        self.label= tk.Label(text="00:00:00")
        self.label.pack()
        self.button2 = tk.Button( 
                   text="Submit your voice",
                   command=self.click_next)
        self.button2.pack()
        self.recording = False
        self.recorded = False
        self.root.mainloop()
        

    def click_trigger(self):
        if self.recording:
            self.recording = False
            self.button.config(fg="black")
        else:
            self.recording = True
            self.button.config(fg="red")   
            threading.Thread(target=self.record).start()
            self.recorded = True

    def click_next(self):
        if self.recorded:
            print("submitted")
            self.root.destroy()
            

            root1 = tk.Tk()

            # Set the window title
            root1.title("String Input")

            # Create a label widget to display a prompt
            label = tk.Label(root1, text="Enter a phrase to recreate in your own voice:",
                             font = "Helvetica 16 bold")
            label.pack()

            # Create an entry widget for the user to enter a string
            entry = tk.Entry(root1)
            entry.pack()

            # Create a button widget to submit the input
            button = tk.Button(root1, text="Submit", command=root1.quit)
            button.pack()


            root1.mainloop()

            # Once the main loop is exited, get the user's input from the entry widget
            user_input = entry.get()

            # XXXX: Handle user input goes here
            print("User input:", user_input)

        else: 
            messagebox.showwarning(title="Error", message="You must record your voice")


    def record(self):
        audio=pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels = 1, rate=44100,
                            input=True, frames_per_buffer=1024)
        frames = [] 
        start = time.time()

        while self.recording:
            data = stream.read(1024)
            frames.append(data)

            passed = time.time() - start
            secs = passed % 60
            mins = passed //60
            hours = mins//60
            self.label.config(text=f"{int(hours):02d}:{int(mins):02d}:{int(secs):02d}")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        exists = True 
        i = 1
        while exists:
            if os.path.exists(f"recording{i}.wav"):
                i+=1
            else:
                exists = False

        sound_file = wave.open(f"recording{i}.wav", "wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b"".join(frames))
        sound_file.close()

import tkinter as tk

   
VoiceRecorder()

