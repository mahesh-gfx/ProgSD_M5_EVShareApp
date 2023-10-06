import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter.ttk import *
from window import win
import sys
from ..base import fonts

welcomeScreen = Frame(win)
welcomeScreen.grid(row=0, column=0)

# Labels
label1 = Label(welcomeScreen, text="Seamless",
               font=fonts.title, justify="left")
label1.pack(padx=20)
label2 = Label(welcomeScreen, text="EV rental", font=fonts.title)
label2.pack(padx=20)
label3 = Label(welcomeScreen, text="a cleaner tomorrow...", font=fonts.title)
label3.pack(padx=20)
label3.place()
