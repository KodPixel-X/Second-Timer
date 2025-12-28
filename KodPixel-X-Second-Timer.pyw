import configparser
import os
import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title("KodPixel-X-Second-Timer")
win.geometry("520x570")

config = configparser.ConfigParser()

def FileControl():
   if os.path.exists("Settings.ini"):
    print("File Creating")
    config.read("Settings.ini")
   else:
    print("Creating File")
    config['settings'] = {
       'color': 'red'
   }

    with open ('Settings.ini', 'w') as f:
     config.write(f)
    

      

FileControl()


def about():
   messagebox.showinfo("KodPixel-X-Second-Timer", "This is a Second Timer, an open-source project. This project is licensed under GPL V3.")


color = config.get('settings', 'color')
config.read('Settings.ini')

if color == "red":
    win.config(bg="red")

elif color == "green":
    win.config(bg="green")

elif color == "yellow":
    win.config(bg="yellow")

elif color == "blue":
    win.config(bg="blue")

elif color == "black":
   win.config(bg="black")

elif color == "white":
   win.config(bg="white")

elif color == "orange":
   win.config(bg="orange")

label = tk.Label(win, text="0", font=("Arial", 25))
label.pack(pady=20)

def plus():
    ButtonBool = True
    if ButtonBool == True:
        current = int(label.cget("text"))
        label.config(text=str(current + 1))
        global winafter
        winafter = win.after(1000, plus)
        winafter()

def Pause():
    global ButtonBool
    ButtonBool = False    
    winafter2 = win.after_cancel(winafter)
    winafter2()
    label.config(text="0")

def Stop():
    global ButtonBool
    ButtonBool = False   
    label.config(text="0") 
    winafter2 = win.after_cancel(winafter)
    winafter2()


def blue():
    global blue
    blue = win.config(bg="blue")

    config['settings'] = {
       'color': 'blue'
    }

    with open ('Settings.ini', 'w') as f:
     config.write(f)


def red():
    global red
    red = win.config(bg="red")
    config['settings'] = {
       'color': 'red'
   }

    with open ('Settings.ini', 'w') as f:
     config.write(f)

def green():
    global green
    green = win.config(bg="green")
    config['settings'] = {
       'color': 'green'
   }

    with open ('Settings.ini', 'w') as f:
     config.write(f)
    

def yellow():
    global yellow
    yellow = win.config(bg="yellow")
    config['settings'] = {
       'color': 'yellow'
   }

    with open ('Settings.ini', 'w') as f:
     config.write(f)


def Black():
   win.config(bg="black")
   config['settings'] = {
       'color': 'black'
   }
   
   with open ('Settings.ini', 'w') as f:
     config.write(f)


def white():
   win.config(bg="white")
   config['settings'] = {
       'color': 'white'
   }
   
   with open ('Settings.ini', 'w') as f:
     config.write(f)

def orange():
   win.config(bg="orange")
   config['settings'] = {
       'color': 'orange'
   }
   
   with open ('Settings.ini', 'w') as f:
     config.write(f)
    

button = tk.Button(win, text="Start", command=plus)
button.pack(pady=10,)

buttonb = tk.Button(win, text="Make the background color blue.", command=blue)
buttonb.pack()

buttonb.config(bg="blue")

buttonr = tk.Button(win, text="Make the background color red.", command=red)
buttonr.pack()

buttonr.config(bg="red")

buttong = tk.Button(win, text="Make the background color green.", command=green)
buttong.pack()

buttong.config(bg="green")

buttony = tk.Button(win, text="Make the background color yellow.", command=yellow)
buttony.pack()

buttony.config(bg="yellow")

buttonbb = tk.Button(win, text="Make the background color black.", command=Black)
buttonbb.pack()

buttonw = tk.Button(win, text="Make the background color white.", command=white)
buttonw.pack()

buttono = tk.Button(win, text="Make the background color orange.", command=orange)
buttono.pack()

buttono.config(bg="orange")


buttonPause = tk.Button(win, text="Pause", command=Pause)
buttonPause.pack()

buttonPause.config(bg="orange")

buttonStop = tk.Button(win, text="Stop", command=Stop)
buttonStop.pack()

buttonStop.config(bg="red")

buttonabout = tk.Button(win, text="About", command=about)
buttonabout.pack()



win.mainloop()
