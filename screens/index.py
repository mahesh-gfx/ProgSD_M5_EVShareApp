import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter.ttk import *

win = tk.Tk()
win.geometry("480x800")
win.title("Zevo | EV Rental")
win.resizable(False, True)

# Pages
loginScreen = Frame(win)
signUpScreen = Frame(win)
customerScreen = Frame(win)
carDetailsScreen = Frame(win)
