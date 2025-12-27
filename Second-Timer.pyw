import tkinter as tk
from tkinter import messagebox


win = tk.Tk()
win.title("KodPixel-X-Second-Timer")
win.geometry("520x570")
win.config(bg="red")

messagebox.showinfo("KodPixel-X-Second-Timer", "This is a Second Timer.")
                                        

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
    win.config(bg="blue")

def red():
    win.config(bg="red")

def green():
    win.config(bg="green")

def yellow():
    win.config(bg="yellow")

    

button = tk.Button(win, text="Start", command=plus)
button.pack(pady=10)

buttonb = tk.Button(win, text="Make the background color blue.", command=blue)
buttonb.pack()

buttonr = tk.Button(win, text="Make the background color red.", command=red)
buttonr.pack()

buttong = tk.Button(win, text="Make the background color blue.", command=green)
buttong.pack()

buttony = tk.Button(win, text="Make the background color yellow.", command=yellow)
buttony.pack()

buttonPause = tk.Button(win, text="Pause", command=Pause)
buttonPause.pack()

buttonStop = tk.Button(win, text="Stop", command=Stop)
buttonStop.pack()

win.mainloop()

