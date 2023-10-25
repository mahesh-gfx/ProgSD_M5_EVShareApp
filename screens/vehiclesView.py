import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont


class VehiclesView(ttk.Frame):

    locationButtonText = 'G4 0AS, Glasgow'
    cars = [{
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
        "defects":[],
        "image":"blue-tesla",
        "bg":"#04317D",
        "fg":"#FFFFFF",
        "distance":"0.2",
    },
        {
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
        "defects":[],
        "image":"red-tesla",
        "bg":"#D22739",
        "fg":"#FFFFFF",
        "distance":"0.8",

    },
        {
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
        "defects":[],
        "image":"white-tesla",
        "bg":"#ECEDED",
        "fg":"#000000",
        "distance":"0.7",

    },
        {
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
        "defects":[],
        "image":"white-tesla",
        "bg":"#ECEDED",
        "fg":"#000000",
        "distance":"0.7",

    }, {
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
        "defects":[],
        "image":"white-tesla",
        "bg":"#ECEDED",
        "fg":"#000000",
        "distance":"0.2",
    }, {
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
        "defects":[],
        "image":"white-tesla",
        "bg":"#ECEDED",
        "fg":"#000000",
        "distance":"0.2",

    }, {
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
        "defects":[],
        "image":"white-tesla",
        "bg":"#ECEDED",
        "fg":"#000000",
        "distance":"0.2",
    }, {
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
        "defects":[],
        "image":"white-tesla",
        "bg":"#ECEDED",
        "fg":"#000000",
        "distance":"0.2",
    }, {
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
        "defects":[],
        "image":"white-tesla",
        "bg":"#ECEDED",
        "fg":"#000000",
        "distance":"0.2",
    }, {
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
        "defects":[],
        "image":"white-tesla",
        "bg":"#ECEDED",
        "fg":"#000000",
        "distance":"0.2",
    }, {
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
        "defects":[],
        "image":"white-tesla",
        "bg":"#ECEDED",
        "fg":"#000000",
        "distance":"0.2",
    }, {
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
        "defects":[],
        "image":"white-tesla",
        "bg":"#ECEDED",
        "fg":"#000000",
        "distance":"0.2",
    }, {
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
        "defects":[],
        "image":"white-tesla",
        "bg":"#ECEDED",
        "fg":"#000000",
        "distance":"0.2",
    }, {
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
        "defects":[],
        "image":"white-tesla",
        "bg":"#ECEDED",
        "fg":"#000000",
        "distance":"0.2",
    },
    ]

    def __init__(self, container, controller):
        super().__init__(container)
        print("Constructing Vehicles View self.navigation...")
        # self.configure(bg="white")
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 16))
        self.style.configure('TMenu', anchor='w', justify='left')

        self.selected_vehicle = tk.StringVar()  # Create the StringVar here
        self.options = ['Sedan', 'Bike', 'Hatchback', 'Coupe', 'SUV']
        self.selected_vehicle.set(self.options[0])

        self.locationIcon = tk.PhotoImage(
            file="./image_components/pin_duotone.png")
        self.locationButton = ttk.Button(self, text=self.locationButtonText, image=self.locationIcon, compound="left",
                                         command=lambda: self.getLocation())
        self.locationButton.place(x=200, y=45, height=42, width=260)

        self.label = tk.Label(self, text="I want to rent a",
                              font=("Helvetica", 20))
        self.label.place(x=25, y=132)

        self.canvasLine = tk.Canvas(self, width=400, height=400)
        self.canvasLine.create_line(0, 100, 150, 100, fill="black", width=2)
        self.canvasLine.place(x=32, y=105)

        self.dropdown = ttk.OptionMenu(
            self, self.selected_vehicle, *self.options)
        self.dropdown.place(x=35, y=164, height=40, width=150)

        self.style = ttk.Style()
        self.style.configure('TMenubutton', font=(
            'Helvetica', 18, "bold"), anchor='w', justify='left')

        self.label.lift()
        self.dropdown.lift()

        sortLabel = tk.Label(self, text='Sort vehicles')
        sortLabel.place(x=341, y=140)

        self.selectedSortOption = tk.StringVar()
        self.sortMenuOptions = ['Default', 'Rate: High to Low', 'Rate: Low to High',
                                'Range: High to Low', 'Range: Low to High']
        self.selectedSortOption.set(self.sortMenuOptions[0])
        self.sortMenu = tk.OptionMenu(
            self, self.selectedSortOption, *self.sortMenuOptions)

        self.sortMenu.place(x=341, y=155, height=42, width=108)

        canvas = tk.Canvas(self)
        canvas.place(x=25, y=230, height=480, width=480)

        self.carsContainer = tk.Frame(canvas)
        canvas.create_window((0, 0), window=self.carsContainer, anchor="nw")

        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.config(yscrollcommand=scrollbar.set)

        self.mapIconDark = tk.PhotoImage(
            file="./image_components/map_duotone_dark.png")

        self.mapIconLight = tk.PhotoImage(
            file="./image_components/map_duotone_light.png")

        # Navigation bar
        self.navigation = tk.Frame(self)
        button1 = tk.Button(
            self.navigation, text="Home", width=10, height=2)
        button2 = tk.Button(
            self.navigation, text="History", width=10, height=2)
        button3 = tk.Button(
            self.navigation, text="Log Out", width=10, height=2)

        self.navigation.grid_columnconfigure(0, weight=1)
        self.navigation.grid_columnconfigure(1, weight=1)
        self.navigation.grid_columnconfigure(2, weight=1)

        button1.grid(row=0, column=0, padx=5)
        button2.grid(row=0, column=1, padx=5)
        button3.grid(row=0, column=2, padx=5)

        self.navigation.place(x=0, y=700, height=100, width=480)

        for car in self.cars:
            scrollable_frame = tk.Frame(self.carsContainer, )

            car_image = tk.PhotoImage(
                file=f"./image_components/{car['image']}.png")
            label_image = tk.Label(
                scrollable_frame, image=car_image, cursor="hand2")
            label_image.image = car_image
            label_image.grid(row=0, column=0)

            label_make = tk.Label(
                scrollable_frame, text=car["make"] + " " + car["model"], bg=car["bg"], fg=car["fg"], font=(
                    'Helvetica', 18, "bold"), anchor='w', justify='left')
            label_make.grid(row=0, column=0, sticky='nw', padx=30, pady=30)

            self.label_distance_icon = tk.Label()

            if (car['fg'] == '#000000'):
                self.label_distance_icon = tk.Label(
                    scrollable_frame, image=self.mapIconDark, bg=car["bg"])
            else:
                self.label_distance_icon = tk.Label(
                    scrollable_frame, image=self.mapIconLight, bg=car["bg"])

            self.label_distance_icon.grid(
                row=0, column=0, sticky='nw', padx=30, pady=60)

            label_distance = tk.Label(
                scrollable_frame, text=car["distance"]+" miles away", bg=car["bg"], fg=car["fg"], font=(
                    'Helvetica', 12), anchor='w', justify='left')
            label_distance.grid(row=0, column=0, sticky='nw', padx=62, pady=62)

            label_seats = tk.Label(
                scrollable_frame, text="Seats "+car["seatingCapacity"], bg=car["bg"], fg=car["fg"], font=(
                    'Helvetica', 12), anchor='w', justify='left')
            label_seats.grid(row=0, column=0, sticky='nw', padx=30, pady=88)

            label_rate = tk.Label(
                scrollable_frame, text="£"+car["ratePerWeek"] + "/week", bg=car["bg"], fg=car["fg"], font=(
                    'Helvetica', 14, 'bold'), anchor='w', justify='left')
            label_rate.grid(row=0, column=0, sticky='sw', padx=30, pady=50)

            label_image.bind(
                "<Button-1>", lambda event: self.handle_click_on_vehicle(controller, car))
            scrollable_frame.pack()

        self.carsContainer.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def getLocation(self):
        self.after(4000, lambda: self.locationButton.config(
            text='Getting Location...'))

    def gotLocation(self):
        self.locationButtonText = 'G4 0AS, Glasgow'
        self.locationButton.config(
            text=self.locationButtonText)

    def handle_click_on_vehicle(self, controller, car):
        print("Clicked on label...")
        controller.set_selected_vehicle_details(car)
        controller.change_frame('vehicleDetails')


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

#         container = tk.Frame(self)
#         container.pack(side="top", fill="both", expand=True)
#         container.grid_rowconfigure(0, weight=1)
#         container.grid_columnconfigure(0, weight=1)
#         vehiclesViewFrame = VehiclesView(container, controller=self)
#         vehiclesViewFrame.grid(row=0, column=0, sticky="nsew")

#         vehiclesViewFrame.tkraise()


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()
