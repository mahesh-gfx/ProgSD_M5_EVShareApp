import tkinter as tk
from screens import welcome
from database import db
from screens.welcome import Welcome
from screens.vehiclesView import VehiclesView


class App(tk.Tk):
    # Attributes
    vehicles = []
    db_name = 'zevo-dev.db'
    # Constructors

    def __init__(self):
        super().__init__()
        self.geometry("480x800")
        self.title("Zevo | EV Rental")
        self.resizable(False, True)
        self.database = db()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        print("Constructing App...")

        self.activeFrames = {}
        self.allFrames = {'welcome': Welcome,
                          'vehiclesView': VehiclesView}

        for key in self.allFrames:
            print('Key: ', key)
            frame = self.allFrames[key](container, controller=self)
            self.activeFrames[key] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.change_frame('vehiclesView')

    def change_frame(self, pageName):
        frame = self.activeFrames[pageName]
        frame.tkraise()
        print('Changed Frame to ', pageName)


if __name__ == "__main__":
    app = App()
    app.mainloop()
