import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title("Second-Timer")
win.geometry("500x550")
win.config(bg="red")

messagebox.showinfo("Second-Timer", "This is a Second Timer.")

label = tk.Label(win, text="0", font=("Arial", 25))
label.pack(pady=20)

def plus():
    current = int(label.cget("text"))
    label.config(text=str(current + 1))
    win.after(1000, plus)

button = tk.Button(win, text="START", command=plus)
button.pack(pady=10)

win.mainloop()

