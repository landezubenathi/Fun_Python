import datetime
import time
from tkinter import *

def get_current_date():
    today = datetime.date.today()
    return today.strftime("%d /%B /%Y")

def get_current_time():
    current_time = datetime.datetime.now()
    return current_time

def update_date():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.pack(pady=20)

'''root = Tk()
root.title("Digital Clock")

clock_label = Label(root, font=("Helvetica", 48),fg="black", bg="Light Blue")
clock_label = Button(bg="Blue")
clock_label.pack(pady=20, padx=20)

update_date()
root.mainloop()

#print(get_current_date())'''