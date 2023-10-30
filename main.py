import tkinter as tk
from database import db
from screens.welcome import Welcome
from screens.vehiclesView import VehiclesView
from screens.vehicleDetails import VehicleDetails
from screens.payment_bill import pay_bill_Screen
from screens.payment_access import pay_access_Screen
from screens.defect import defect_page
from screens.addcard import add_card_Screen
from screens.login import login_page
from screens.register import register_page


class App(tk.Tk):
    # Attributes
    vehicles = []
    db_name = 'zevo-dev.db'
    _selectedVehicle = ""
    database = db()
    usertype = ''
    username = ''
    loggedInUserType = ''
    userEmail = ''
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
        self._selectedVehicle = {
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
        self.activeFrames = {}
        self.allFrames = {'welcome': Welcome,
                          'vehiclesView': VehiclesView,
                          'paymentAccess': pay_access_Screen,
                          'paymentBill': pay_bill_Screen,
                          'reportDefect': defect_page,
                          'vehicleDetails': VehicleDetails,
                          'addCard': add_card_Screen,
                          'login': login_page,
                          'register': register_page
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
    def get_selected_vehicle(self):
        return self._selectedVehicle

    # Setters
    def set_selected_vehicle(self, vehicle):
        print("Changing selected vehicle details...", vehicle)
        self._selectedVehicle = vehicle

    def signUpAndLogin(self,username,secret,email):
        # get username and secret from login pageas paramaters for this method
        print("Signing up...")
        print(username)
        print(secret)
        print(email)
        response = self.database.run_query(
            '''INSERT INTO users (username, email, secret, usertype)
            VALUES
            (?, ?, ?, 'user');
            ''', parameters=(username, email, secret))
        self.database.conn.commit()

        # self.login()

    def login(self,username,secret):
        # get username and secret from login pageas paramaters for this method
        print("Logging in...")
        print(username)
        print(secret)
        self.database.run_query(
            '''SELECT * FROM users
                WHERE username = ? AND secret = ?
                LIMIT 1;
            ''', parameters=(username, secret))
        result = self.database.c.fetchone()
        print(result)

        if (str(result) != 'none'):
            if (str(result[5]) == 'user'):
                self.username = str(result[2])
                self.loggedInUserType = str(result[5])
                self.userEmail = str(result[3])
                self.change_frame('vehiclesView')
                print("A User logged in..")
            if (str(result[5]) == 'manager'):
                self.username = str(result[2])
                self.loggedInUserType = str(result[5])
                self.userEmail = str(result[3])
                # self.change_frame('manager')
                # self.geometry("1080x1960")
                print("A Manager logged in..")
            if (str(result[5]) == 'operator'):
                self.username = str(result[2])
                self.loggedInUserType = str(result[5])
                self.userEmail = str(result[3])
                # self.geometry("1080x1960")
                # self.change_frame('operator')
                print("An Operator logged in..")


if __name__ == "__main__":
    app = App()
    app.mainloop()
