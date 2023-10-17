# from screens.welcome import welcomeScreen
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter.ttk import *
from screens.index import *
from screens.welcome import welcomeScreen

# import os
# import sys

# # Get the current script's directory
# current_dir = os.path.dirname(os.path.abspath(__file__))

# # Add the project's root directory to the Python path
# project_root = os.path.abspath(os.path.join(current_dir, '..'))

# # other dependency imports
# sys.path.insert(0, project_root)


# win = tk.Tk()
# win.geometry("480x800")
# win.title("Zevo | EV Rental")
# win.resizable(False, True)


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
# loginScreen = Frame(win)
# signUpScreen = Frame(win)
# customerScreen = Frame(win)
# carDetailsScreen = Frame(win)

# welcomeScreen.grid(row=0, column=0)  # welcome.py
# loginScreen.grid(row=0, column=0)
# signUpScreen.grid(row=0, column=0)
# customerScreen.grid(row=0, column=0)
# carDetailsScreen.grid(row=0, column=0)

# Labels || welcome.py

label4 = Label(loginScreen, text="Page 2", font=title)
label4.place(x=10, y=10)

welcomeScreen.tkraise()
win.mainloop()
