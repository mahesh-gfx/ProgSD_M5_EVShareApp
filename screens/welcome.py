import tkinter as tk
from tkinter import *
from tkinter.ttk import *


class Welcome(tk.Frame):
    # Constructors
    def __init__(self, container, controller):
        tk.Frame.__init__(self, container)
        print("Constructing Welcome frame...")

        self.pageLabel = tk.Label(self, text='Welcome Page',
                                  relief="raised")
        self.pageLabel.place(x=10, y=10)

        self.backgroundImageFile = PhotoImage(
            file=r"./image_components/welcome-background.png")
        self.original_width = self.backgroundImageFile.width()
        self.original_height = self.backgroundImageFile.height()
        self.aspect_ratio = self.original_width / self.original_height
        self.new_width = int(800 * self.aspect_ratio)
        self.new_height = 800

        self.resizedImage = self.backgroundImageFile.subsample(
            self.original_width // self.new_width, self.original_height // self.new_height)
        self.backgroundImage = tk.Label(
            self, image=self.resizedImage, bg="#000000")
        self.backgroundImage.place(relheight=1, relwidth=1)
        self.letsGoButtonImage = PhotoImage(
            file=r"./image_components/lets-go-button.png")
        self.letsGoButton = tk.Button(self, image=self.letsGoButtonImage, compound=TOP, borderwidth=0, background='#FFF',
                                      command=lambda: controller.change_frame('login'))
        self.letsGoButton.place(x=78, y=591, height=68, width=320)

        self.knowMoreButtonImage = PhotoImage(
            file=r"./image_components/know-more-button.png")
        self.knowMoreButton = tk.Button(self, image=self.knowMoreButtonImage,
                                        command=lambda: self.operator(controller), default="normal", compound=TOP, borderwidth=0, border=0, background='#FFF')
        self.knowMoreButton.place(x=78, y=678, height=68, width=320)

    def operator(self, controller):
        controller.geometry("1536x864")
        controller.change_frame('operator')


# # single screen development
# class App(tk.Tk):
#     # Attributes
#     vehicles = []
#     db_name = 'zevo-dev.db'
#     # Constructors

#     def __init__(self):
#         super().__init__()
#         self.geometry("480x800")
#         self.title("Zevo | EV Rental")
#         self.resizable(False, True)
#         print("Constructing App...")

#         self.container = tk.Frame(self)
#         self.container.pack(side="top", fill="both", expand=True)
#         self.container.grid_rowconfigure(0, weight=1)
#         self.container.grid_columnconfigure(0, weight=1)
#         self.welcome = Welcome(self.container, controller=self)
#         self.welcome.grid(row=0, column=0, sticky="nsew")
#         self.welcome.tkraise()


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()
