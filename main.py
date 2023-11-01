import datetime
import tkinter as tk
import pandas as pd
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
from screens.management import management
from screens.operator import Operator
from screens.purchaseHistory import PurchaseHistory
from screens.return_and_pay import ReturnAndPay


class App(tk.Tk):
    # Attributes
    vehicles = []
    db_name = 'zevo-dev.db'
    _selectedVehicle = ""
    database = db()
    usertype = ''
    username = ''
    loggedInUserType = ''
    userEmail = 'none'
    selectedOrder = {}
    amount = 0
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
            "horsePower": "200",
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
                          'register': register_page,
                          'manager': management,
                          'operator': Operator,
                          'purchaseHistory': PurchaseHistory,
                          'returnAndPay': ReturnAndPay
                          }

        for key in self.allFrames:
            print('Key: ', key)
            frame = self.allFrames[key](self.container, controller=self)
            self.activeFrames[key] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.get_all_vehicles()
        self.change_frame('welcome')

        # #ini Users
        # import random
        # import string
        # for i in range(100):
        #     name = ''.join(random.choice(string.ascii_letters) for _ in range(8))  # 生成随机名字
        #     email = f"{name}@example.com"  # 生成随机邮箱
        #     password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))  # 生成随机密码
        #     self.signUpAndLogin(username=name,secret=password,email=email)

    def change_frame(self, pageName):
        frame = self.activeFrames[pageName]
        frame.tkraise()
        # frame.update()
        list = ['returnAndPay', 'vehicleDetails',
                'purchaseHistory', 'paymentAccess']
        if pageName in list:
            frame.refresh_data()
        print('Changed Frame to ', pageName)

    # Getters
    def get_selected_vehicle(self):
        return self._selectedVehicle

    def get_selected_order(self):
        return self.selectedOrder

    def get_amount(self):
        return self.amount

    # Setters
    def set_selected_vehicle(self, vehicle):
        # print("Changing selected vehicle details...", vehicle)
        self._selectedVehicle = vehicle

    def set_selected_order(self, order):
        self.selectedOrder = order

    def set_amount(self, amount):
        self.amount = amount

    def signUpAndLogin(self, name, secret, email, phone):
        # get username and secret from login page as paramaters for this method
        print("Signing up...")
        # print(username)
        # print(secret)
        # print(email)

        # check is email is used before to create an account.
        self.database.run_query(
            '''SELECT * FROM users
                WHERE email = ?
                LIMIT 1;
            ''', parameters=[email])
        user = self.database.c.fetchone()

        print("User is ", user)
        if (user != None):
            tk.messagebox.showerror(
                "This email is already assigned to existing account")
            return
        print("Must be error here")
        response = self.database.run_query(
            '''INSERT INTO users (name, email, secret, phone, usertype)
            VALUES
            (?, ?, ?, ?, 'user');
            ''', parameters=(name, email, secret, phone))
        self.database.conn.commit()
        return response
        # self.login()

    def login(self, email, secret):
        # get username and secret from login pageas paramaters for this method
        print("Logging in...")
        # print(username)
        # print(secret)
        self.database.run_query(
            '''SELECT * FROM users
                WHERE email = ? AND secret = ?
                LIMIT 1;
            ''', parameters=(email, secret))
        result = self.database.c.fetchone()
        print(result)

        if (result != None):
            if (str(result[5]) == 'user'):
                self.username = str(result[1])
                self.loggedInUserType = str(result[4])
                self.userEmail = str(result[2])
                self.change_frame('vehiclesView')
                print("A User logged in..")
            if (str(result[5]) == 'manager'):
                self.username = str(result[1])
                self.loggedInUserType = str(result[4])
                self.userEmail = str(result[2])
                self.change_frame('manager')
                self.geometry("1600x976")

                print("A Manager logged in..")
            if (str(result[5]) == 'operator'):
                self.username = str(result[1])
                self.loggedInUserType = str(result[4])
                self.userEmail = str(result[2])
                self.geometry("1536x864")
                self.change_frame('operator')
                print("An Operator logged in..")
        else:

            from tkinter import messagebox
            messagebox.showinfo("Tips", "Please sign up your information")

            tk.messagebox.showinfo("Zevo | EV Rental", "Invalid Credentials!")
            print("Emailll")
            print(self.userEmail)

    def log_out(self):
        self.change_frame('welcome')

    def get_all_vehicles(self):
        self.database.run_query(
            '''SELECT * FROM vehicles WHERE inUse = 0''')
        response = self.database.c.fetchall()
        response = pd.DataFrame(response, columns=["vehicle_id", "vehicleClass", "make", "model", "licensePlateNumber", "ratePerWeek", "ratePerDay",
                                                   "ratePerHour", "batteryCapacity", "range", "doors", "seatingCapacity", "horsePower", "maxSpeed",
                                                   "inUse", "atSite", "history", "defects", "image", "bg", "fg", "location", "hasDefects"])

        self.vehicles = response.to_dict(orient='records')
        return self.vehicles

    def get_user_history(self):
        query = '''
            SELECT o.orderid, v.make, v.model, v.licensePlateNumber, v.bg, v.fg, v.image, o.startTime, o.endTime, o.income
            FROM orders AS o
            JOIN vehicles AS v ON o.vehicle_id = v.vehicle_id
            WHERE o.email = ?
        '''
        print("Emailkk: ")
        print(self.userEmail)
        self.database.run_query(query, parameters=[self.userEmail])
        response = self.database.c.fetchall()
        print('User History: ')
        # print(response)
        response = pd.DataFrame(response, columns=[
            "orderid", "make", "model", "licensePlateNumber", "bg", "fg", "image", "startTime", "endTime", "income"])
        response = response.sort_values(by="startTime")
        history = response.to_dict(orient='records')
        print("Historykkk")
        print(history)
        return history

    def rent(self):
        vehicle = self.get_selected_vehicle()
        print("Vehicle: ", vehicle)
        # print("vehicle: ", vehicle)
        # print("vehicle_id: ", vehicle['vehicle_id'])
        # return
        # vehicle['inUse'] = 0
        if vehicle['inUse']:
            tk.messagebox.showerror(
                "UNAVAILABLE", "The vehicle is not available at the moment.")
            return False
        # update vehicle availability
        self.database.run_query(
            'UPDATE vehicles SET inUse = ? WHERE vehicle_id = ?', (1, vehicle['vehicle_id']))
        # create order (rent)
        order_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        order_query = '''INSERT INTO 
                    orders (email, vehicle_id, startTime, endTime, income )
                    VALUES (?, ?, ?, ?, ?)'''
        order_params = (
            self.userEmail, vehicle['vehicle_id'], order_date, None, vehicle['ratePerDay'])
        self.database.run_query(order_query, order_params)
        tk.messagebox.showinfo("Booking Successful",
                               "You had booked this car successfully")
        self.change_frame('vehiclesView')

    def return_vehicle(self):
        vehicle_query = '''INSERT INTO 
                vehicles (location, inUse)
                VALUES (?, ?);'''
        vehicle_params = (self.selectedOrder['returnLocation'], 0)
        print("BEFORE RUN QUERY SELECTED ORDER: ",
              self.selectedOrder['endTime'])
        self.database.run_query(vehicle_query, vehicle_params)
        self.database.conn.commit()

        order_query = '''UPDATE orders 
                SET endTime=?, returnLocation=?
                WHERE orderid=?'''
        order_params = (
            self.selectedOrder['endTime'], self.selectedOrder['returnLocation'], self.selectedOrder['orderid'])
        print(order_params)
        self.database.run_query(order_query, order_params)
        self.database.conn.commit()
        self.database.run_query('''SELECT * from vehicles''')
        vehicle = self.database.c.fetchone()
        print("AFTER RUN QUERY: ", vehicle)

        # self.change_frame('vehiclesView')


if __name__ == "__main__":
    app = App()
    app.mainloop()
