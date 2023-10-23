import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter.ttk import *
from window import win
import sys
from ..base import fonts

welcomeScreen = Frame(win)
welcomeScreen.grid(row=0, column=0)


class Welcome(tk.Frame):
    # Constructors
    def __init__(self, container, controller):
        tk.Frame.__init__(self, container)
        print("Constructing Welcome frame...")

        pageLabel = tk.Label(self, text='Welcome Page',
                             relief="raised")
        pageLabel.place(x=10, y=10)

        backgroundImageFile = PhotoImage(
            file=r"./image_components/welcome-background.png")
        original_width = backgroundImageFile.width()
        original_height = backgroundImageFile.height()
        aspect_ratio = original_width / original_height
        new_width = int(800 * aspect_ratio)
        new_height = 800

        resizedImage = backgroundImageFile.subsample(
            original_width // new_width, original_height // new_height)
        backgroundImage = tk.Label(
            self, image=resizedImage, bg="#000000")
        backgroundImage.place(relheight=1, relwidth=1)
        letsGoButtonImage = PhotoImage(
            file=r"./image_components/lets-go-button.png")
        letsGoButton = tk.Button(self, image=letsGoButtonImage,
                                 command=lambda: print("Clicked Lets Go"))
        letsGoButton.place(x=78, y=591, height=68, width=320)

        knowMoreButtonImage = PhotoImage(
            file=r"./image_components/know-more-button.png")
        knowMoreButton = tk.Button(self, image=knowMoreButtonImage,
                                   command=lambda: print("Clicked Lets Go"), default="normal", border=0)
        knowMoreButton.place(x=78, y=678, height=68, width=320)
