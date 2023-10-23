import tkinter as tk
from tkinter import PhotoImage


class welcome():
    # Attributes
    vehicles = []

    # Constructors
    def __init__(self):
        print("Constructing App...")

        self.root = tk.Tk()
        self.root.geometry("480x800")
        self.root.title("Zevo | EV Rental")
        self.root.resizable(False, True)

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
            self.root, image=resizedImage, bg="#000000")
        backgroundImage.place(relheight=1, relwidth=1)
        letsGoButtonImage = PhotoImage(
            file=r"./image_components/lets-go-button.png")
        letsGoButton = tk.Button(self.root, image=letsGoButtonImage,
                                 command=lambda: print("Clicked Lets Go"))
        letsGoButton.place(x=78, y=591, height=68, width=320)

        knowMoreButtonImage = PhotoImage(
            file=r"./image_components/know-more-button.png")
        knowMoreButton = tk.Button(self.root, image=knowMoreButtonImage,
                                   command=lambda: print("Clicked Lets Go"), default="normal", border=0)
        knowMoreButton.place(x=78, y=678, height=68, width=320)
        self.root.mainloop()

    # Methods
