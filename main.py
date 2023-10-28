import tkinter as tk
from database import db
from screens.welcome import Welcome
from screens.vehiclesView import VehiclesView
from screens.vehicleDetails import VehicleDetails
from screens.payment_bill import pay_bill_Screen
from screens.payment_access import pay_access_Screen
from screens.addcard import add_card_Screen


class App(tk.Tk):
    # Attributes
    vehicles = []
    db_name = 'zevo-dev.db'
    selectedVehicle = {
        "type": "Car",
        "vehicleClass": "SUV",
        "make": "Tesla",
        "model": "Model S",
        "licensePlateNumber": "XYZ 123",
        "ratePerWeek": "20",
        "ratePerDay": "4",
        "ratePerHour": "0.2",
        "batteryCapacity": "64kWh",
        "range": "550",
        "doors": "5",
        "seatingCapacity": "7",
        "horsepower": "200",
        "maxSpeed": "310",
        "inUse": False,
        "atSite": True,
        "history": [],
        "defects": [],
        "image": "blue-tesla",
        "bg": "#04317D",
        "fg": "#FFFFFF",
        "distance": "0.2",
    }
    # Constructors

    def __init__(self):
        super().__init__()
        self.geometry("480x800")
        self.title("Zevo | EV Rental")
        self.resizable(False, True)
        self.database = db()

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        print("Constructing App...")

        self.activeFrames = {}
        self.allFrames = {'welcome': Welcome,
                          'vehiclesView': VehiclesView,
                          'paymentAccess': pay_access_Screen,
                          'paymentBill': pay_bill_Screen,
                          'vehicleDetails': VehicleDetails,
                          'addCard': add_card_Screen
                          }

        for key in self.allFrames:
            print('Key: ', key)
            frame = self.allFrames[key](self.container, controller=self)
            self.activeFrames[key] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.change_frame('welcome')

    def change_frame(self, pageName):
        frame = self.activeFrames[pageName]
        frame.tkraise()
        print('Changed Frame to ', pageName)

    # Getters
    def get_selected_car_details():
        return ""

    # Setters
    def set_selected_vehicle_details(self, vehicle):
        print("Changing selected vehicle details...", vehicle)
        self.selectedVehicle = vehicle


if __name__ == "__main__":
    app = App()
    app.mainloop()
