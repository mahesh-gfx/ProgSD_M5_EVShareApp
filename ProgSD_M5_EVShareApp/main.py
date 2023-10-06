import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter.ttk import *

win = tk.Tk()
win.geometry("480x800")
win.title("Zevo | EV Rental")
win.resizable(False, True)


# font styles // components
button = font.Font(size=16)
body = font.Font(size=14)
title = font.Font(size=22)
subtitle = font.Font(size=18)

# styled // components
styledButton = Style()
styledButton.configure('W.TButton', font=(
    'calibri', 10, 'bold'), foreground='white')


# Pages
welcomeScreen = Frame(win)  # welcome.py
loginScreen = Frame(win)
signUpScreen = Frame(win)
customerScreen = Frame(win)
carDetailsScreen = Frame(win)

welcomeScreen.grid(row=0, column=0)  # welcome.py
loginScreen.grid(row=0, column=0)
signUpScreen.grid(row=0, column=0)
customerScreen.grid(row=0, column=0)
carDetailsScreen.grid(row=0, column=0)

# Labels || welcome.py
label1 = Label(welcomeScreen, text="Seamless", font=title, justify="left")
label1.pack(padx=20)
label2 = Label(welcomeScreen, text="EV rental", font=title)
label2.pack(padx=20)
label3 = Label(welcomeScreen, text="a cleaner tomorrow...", font=title)
label3.pack(padx=20)

label4 = Label(loginScreen, text="Page 2", font=title)
label4.pack()

# Buttons
letsGoButton = Button(welcomeScreen, text="Let's Go",
                      command=lambda: loginScreen.tkraise())
letsGoButton.place(x=72, y=90, width=320, height=68)
letsGoButton.pack()

welcomeScreen.tkraise()
win.mainloop()
