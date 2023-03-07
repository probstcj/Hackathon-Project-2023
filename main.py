
import os
import wave
import time
import threading
import pyaudio
import customtkinter
from PIL import Image
from phonemizer import phonemize

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500X500")
root.title("SpeechMe")

''' YOU MUST CHANGE THIS PATH TO YOUR OWN FOR THE RECORD BUTTON IMAGE.'''
photo = customtkinter.CTkImage(light_image=Image.open("/Users/leotejkowski/Desktop/LoginWindow/recordbutton.png"),
                               dark_image=Image.open("/Users/leotejkowski/Desktop/LoginWindow/recordbutton.png"),
                               size=(30,30))

class Recording():
    def __init__(self):
         self.recorded = False
         self.recording = False

     
    def submit(self):
        self.text_to_phone()
    
    def text_to_phone(self):
        print(entry1.get())
        string = entry1.get()
        to_array = [char for char in string]
        print(to_array)

        text = [f"{string}"]
        print(text)

        phonemized = phonemize(text, language='en-us', backend='espeak')
        print(phonemized)


    def stop_recording(self):
        print("stopped recording")
        self.recording = False
    
    def click_trigger(self):
        print("click_triggered")
        self.recorded = True
        if self.recording:
            print("turned off")
            self.recording = False
            #self.button.config(fg="black")
        else:
            self.recorded = True
            print("turned on")
            self.recording = True
            #self.button.config(fg="red")   
            threading.Thread(target=self.record).start()
            self.recorded = True


    def record(self):
        print("recording")
        entry1.configure(state="normal")
        audio=pyaudio.PyAudio()
        stream = audio.open(format=pyaudio.paInt16, channels = 1, rate=44100,
                            input=True, frames_per_buffer=1024)
        frames = [] 
        start = time.time()

        while (self.recording):
            data = stream.read(1024)
            frames.append(data)

            passed = time.time() - start
            secs = passed % 60
            mins = passed //60
            hours = mins//60
            
            label2.configure(text=f"{int(hours):02d}:{int(mins):02d}:{int(secs):02d}")

        stream.stop_stream()
        stream.close()
        audio.terminate()

        exists = True 
        i = 1
        while exists:
            ''' YOU MUST CHANGE THIS PATH TO YOUR OWN FOR THE RECORDINGS'''
            if os.path.exists(f"/Users/leotejkowski/Documents/Hackathon/Hackathon-Project-2023/Recordings/recording{i}.wav"):
                i+=1
            else:
                exists = False
            ''' YOU MUST CHANGE THIS PATH TO YOUR OWN FOR THE RECORDINGS'''
        sound_file = wave.open(f"/Users/leotejkowski/Documents/Hackathon/Hackathon-Project-2023/Recordings/recording{i}.wav", "wb")
        sound_file.setnchannels(1)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate(44100)
        sound_file.writeframes(b"".join(frames))
        sound_file.close()


recordingOb = Recording()


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=40, padx=120, fill="both", expand=True)


label = customtkinter.CTkLabel(master=frame, text="Step 1: Record yourself saying this sentence", font=("Roboto", 24))
label.pack(pady=12, padx=10)
textBox = customtkinter.CTkTextbox(master=frame)

customFont = customtkinter.CTkFont(slant='italic')
label1 = customtkinter.CTkLabel(master=frame, text="\"That quick beige fox jumped in the air over each thin dog. Look out, I shout, for he's foiled you again, creating chaos.\"", font=customFont)
label1.pack(pady=12, padx=10)

print(recordingOb.recording)
button1 = customtkinter.CTkButton(master=frame, text="Record", command=recordingOb.click_trigger, fg_color="red",text_color_disabled="dark_red")
button1.pack(pady=6, padx=35)

label2 = customtkinter.CTkLabel(master=frame, text="00:00:00", font=("Roboto", 10))
label2.pack(pady=0, padx=10)

label = customtkinter.CTkLabel(master=frame, text="Step 2: Enter in a sentence you want to fake.", font=("Roboto", 24))
label.pack(pady=24, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Fake Sentence", state="disabled")
entry1.pack(pady=12, padx=35)

button2 = customtkinter.CTkButton(master=frame, text = "Submit", command=recordingOb.submit)
button2.pack(pady=12, padx=35)



root.mainloop() 












# import os
# import wave
# import time
# import threading
# import tkinter as tk
# import pyaudio
# from tkinter import messagebox


# class VoiceRecorder:

#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.resizable(True, True)
#         self.Label = tk.Label(text="Please say the following phrase to recreate your voice",
# 		 fg = "black",
# 		 font = "Helvetica 16 bold italic").pack()
#         self.Label = tk.Label(text="That quick beige fox jumped in the air over each thin dog. Look out, I shout, for he's foiled you again, creating chaos.",
# 		 fg = "light green",
# 		 bg = "dark green",
# 		 font = "Helvetica 16 bold").pack()
#         self.button = tk.Button(text="Record", font=("Arial", 60, "bold"),
#                                 command=self.click_trigger)
#         self.button.pack()
#         self.label= tk.Label(text="00:00:00")
#         self.label.pack()
#         self.button2 = tk.Button( 
#                    text="Submit your voice",
#                    command=self.click_next)
#         self.button2.pack()
#         self.recording = False
#         self.recorded = False
#         self.root.mainloop()
        

#     def click_trigger(self):
#         if self.recording:
#             self.recording = False
#             self.button.config(fg="black")
#         else:
#             self.recording = True
#             self.button.config(fg="red")   
#             threading.Thread(target=self.record).start()
#             self.recorded = True

#     def click_next(self):
#         if self.recorded:
#             print("submitted")
#             self.root.destroy()
            

#             root1 = tk.Tk()

#             # Set the window title
#             root1.title("String Input")

#             # Create a label widget to display a prompt
#             label = tk.Label(root1, text="Enter a phrase to recreate in your own voice:",
#                              font = "Helvetica 16 bold")
#             label.pack()

#             # Create an entry widget for the user to enter a string
#             entry = tk.Entry(root1)
#             entry.pack()

#             # Create a button widget to submit the input
#             button = tk.Button(root1, text="Submit", command=root1.quit)
#             button.pack()


#             root1.mainloop()

#             # Once the main loop is exited, get the user's input from the entry widget
#             user_input = entry.get()

#             # XXXX: Handle user input goes here
#             print("User input:", user_input)

#         else: 
#             messagebox.showwarning(title="Error", message="You must record your voice")


#     def record(self):
#         audio=pyaudio.PyAudio()
#         stream = audio.open(format=pyaudio.paInt16, channels = 1, rate=44100,
#                             input=True, frames_per_buffer=1024)
#         frames = [] 
#         start = time.time()

#         while self.recording:
#             data = stream.read(1024)
#             frames.append(data)

#             passed = time.time() - start
#             secs = passed % 60
#             mins = passed //60
#             hours = mins//60
#             self.label.config(text=f"{int(hours):02d}:{int(mins):02d}:{int(secs):02d}")

#         stream.stop_stream()
#         stream.close()
#         audio.terminate()

#         exists = True 
#         i = 1
#         while exists:
#             if os.path.exists(f"recording{i}.wav"):
#                 i+=1
#             else:
#                 exists = False

#         sound_file = wave.open(f"recording{i}.wav", "wb")
#         sound_file.setnchannels(1)
#         sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
#         sound_file.setframerate(44100)
#         sound_file.writeframes(b"".join(frames))
#         sound_file.close()

# import tkinter as tk

   
# VoiceRecorder()

