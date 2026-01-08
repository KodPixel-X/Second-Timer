import configparser
import os
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

win = tk.Tk()
win.title("KodPixel-X-Second-Timer")
win.geometry("790x630")


def about():
   messagebox.showinfo("KodPixel-X-Second-Timer", "This is a Second Timer, an open-source project. This project is licensed under GPL V3.")



def DarkTheme():
   win.config(bg="black")
   button.config(bg="white")
   buttonb.config(bg="white")
   buttonr.config(bg="white")
   buttong.config(bg="white")
   buttony.config(bg="white")
   buttonbb.config(bg="white")
   buttonw.config(bg="white")
   buttono.config(bg="white")
   txtopenb.config(bg="white")
   buttonPause.config(bg="white")
   buttonStop.config(bg="white")
   buttonabout.config(bg="white")
   button.config(fg="black")
   buttonb.config(fg="black")
   buttonr.config(fg="black")
   txtsavebutton(bg="white")
   txtsavebutton(fg="black")
   txtopenb.config(bg="black")
   buttong.config(fg="black")
   buttony.config(fg="black")
   buttonbb.config(fg="black")
   buttonw.config(fg="black")
   buttono.config(fg="black")
   buttonPause.config(fg="black")
   buttonStop.config(fg="black")
   buttonabout.config(fg="black")

   config['settings'] = {
       'color': 'darktheme'
   }
   with open ('Settings.ini', 'w') as f:
     config.write(f)

def LightTheme():
    win.config(bg="white")
    button.config(bg="white")
    buttonb.config(bg="white")
    buttonr.config(bg="white")
    buttong.config(bg="white")
    buttony.config(bg="white")
    txtopenb.config(bg="white")
    buttonbb.config(bg="white")
    buttonw.config(bg="white")
    buttono.config(bg="white")
    buttonPause.config(bg="white")
    buttonStop.config(bg="white")
    buttonabout.config(bg="white")
    txtsavebutton.config(bg="white")
    txtsavebutton.config(fg="black")
    button.config(fg="black")
    buttonb.config(fg="black")
    txtopenb.config(fg="black")
    buttonr.config(fg="black")
    buttong.config(fg="black")
    buttony.config(fg="black")
    buttonbb.config(fg="black")
    buttonw.config(fg="black")
    buttono.config(fg="black")
    buttonPause.config(fg="black")
    buttonStop.config(fg="black")
    buttonabout.config(fg="black")
    config['settings'] = {
       'color': 'lighttheme'
   }
    with open ('Settings.ini', 'w') as f:
     config.write(f)


def DefaultTheme():
   win.config(bg="red")
   button.config(bg="green")
   buttonb.config(bg="yellow")
   buttonr.config(bg="yellow")
   buttong.config(bg="yellow")
   buttony.config(bg="yellow")
   buttonbb.config(bg="yellow")
   txtopenb.config(bg="yellow")
   buttonw.config(bg="yellow")
   buttono.config(bg="yellow")
   buttonPause.config(bg="orange")
   buttonStop.config(bg="red")
   buttonabout.config(bg="blue")
   txtsavebutton.config(bg="green")
   txtsavebutton.config(fg="black")
   button.config(fg="black")
   buttonb.config(fg="black")
   buttonr.config(fg="black")
   buttong.config(fg="black")
   txtopenb.config(fg="black")
   buttony.config(fg="black")
   buttonbb.config(fg="black")
   buttonw.config(fg="black")
   buttono.config(fg="black")
   buttonPause.config(fg="black")
   buttonStop.config(fg="black")
   buttonabout.config(fg="black")
   config['settings'] = {
       'color': 'defaulttheme'
   }
   with open ('Settings.ini', 'w') as f:
     config.write(f)


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

def txtsave4():
    txt51 = txtsave.get()
    path = filedialog.asksaveasfile(
      defaultextension=".txt",
      mode="w"
   )

    if path:
      path.write(txt51)

def txtsave999():
   pathopen = filedialog.askopenfile(mode="r")
   pathread = pathopen.read()
   txtopenl.config(text=pathread)

label = tk.Label(win, text="0", font=("Arial", 25))
label.pack(pady=20)


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

DarkTheme2 = tk.Button(win, text="DarkTheme", command=DarkTheme)
DarkTheme2.pack()

LightTheme2  = tk.Button(win, text="LightTheme", command=LightTheme)
LightTheme2.pack()

DefaultTheme2 = tk.Button(win, text="DefaultTheme", command=DefaultTheme)
DefaultTheme2.pack()

global txtsave

txtsave = tk.Entry(win)
txtsave.pack()


txtsave.bind("<Return>", txtsave4)

txtsavebutton = tk.Button(win, text="Save", command=txtsave4)
txtsavebutton.pack()

txtopenl = tk.Label(win, text="", font=("Arial", 9))
txtopenl.pack()

txtopenb = tk.Button(win, text="open", command=txtsave999)
txtopenb.pack()

config = configparser.ConfigParser()

def FileControl():
   if os.path.exists("Settings.ini"):
    print("File Creating")
    config.read("Settings.ini")
   else:
    print("Creating File")
    config['settings'] = {
       'color': 'defaulttheme',

   }

    with open ('Settings.ini', 'w') as f:
     config.write(f)
    

      

FileControl()

config.read('Settings.ini')

color = config.get('settings', 'color')

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

elif color == "darktheme":
   DarkTheme()


elif color == "lighttheme":
   LightTheme()

elif color == "defaulttheme":
   DefaultTheme()



win.mainloop()
