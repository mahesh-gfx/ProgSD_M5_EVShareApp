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
        "image":"blue-tesla"
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
        "image":"red-tesla"
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
        "image":"white-tesla"
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
        "image":"white-tesla"
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
        "image":"white-tesla"
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
        "image":"white-tesla"
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
        "image":"white-tesla"
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
        "image":"white-tesla"
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
        "image":"white-tesla"
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
        "image":"white-tesla"
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
        "image":"white-tesla"
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
        "image":"white-tesla"
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
        "image":"white-tesla"
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
        "image":"white-tesla"
    },
    ]

    def __init__(self, container, controller):
        super().__init__(container)
        print("Constructing Vehicles View frame...")
        # self.configure(bg="white")
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Helvetica", 16))
        self.style.configure('TMenu', anchor='w', justify='left')

        self.selected_vehicle = tk.StringVar()  # Create the StringVar here
        self.options = ['Sedan', 'Bike', 'Hatchback', 'Coupe', 'SUV']
        self.selected_vehicle.set(self.options[0])

        locationIcon = tk.PhotoImage(
            file="./image_components/location-drop.png")
        self.locationButton = ttk.Button(self, text=self.locationButtonText, image=locationIcon, compound="left",
                                         command=lambda: self.getLocation())
        self.locationButton.place(x=35, y=45, height=42, width=260)

        label = tk.Label(self, text="I want to rent a",
                         font=("Helvetica", 20,))
        label.place(x=25, y=132)

        self.canvasLine = tk.Canvas(self, width=400, height=400)
        self.canvasLine.create_line(0, 100, 150, 100, fill="black", width=2)
        self.canvasLine.place(x=32, y=105)

        dropdown = ttk.OptionMenu(
            self, self.selected_vehicle, *self.options)
        dropdown.place(x=35, y=164, height=40, width=150)

        dropDownStyle = ttk.Style()
        dropDownStyle.configure('TMenubutton', font=(
            'Helvetica', 18, "bold"), anchor='w', justify='left')

        label.lift()
        dropdown.lift()

        sortLabel = tk.Label(text='Sort vehicles')
        sortLabel.place(x=341, y=140)

        self.selectedSortOption = tk.StringVar()
        self.sortMenuOptions = ['Default', 'Rate: High to Low', 'Rate: Low to High',
                                'Range: High to Low', 'Range: Low to High']
        self.selectedSortOption.set(self.sortMenuOptions[0])
        sortMenu = tk.OptionMenu(
            self, self.selectedSortOption, *self.sortMenuOptions)

        sortMenu.place(x=341, y=155, height=42, width=108)

        self.canvasCarsContainer = tk.Canvas(self)
        self.canvasCarsContainer.place(x=35, y=250, height=300)
        scrollbar = tk.Scrollbar(
            self, orient="vertical", command=self.canvasCarsContainer.yview)
        scrollbar.pack(side="right", fill="y")
        self.canvasCarsContainer.configure(yscrollcommand=scrollbar.set)

        carsContainer = tk.Frame(self.canvasCarsContainer)
        self.canvasCarsContainer.create_window(
            (0, 0), window=carsContainer, anchor="nw")

        # Create scrollable frames with buttons and names
        frame_list = []
        for car in self.cars:
            scrollable_frame = tk.Frame(carsContainer)
            scrollable_frame.grid(row=len(frame_list)+1,
                                  column=0, padx=10, pady=10)

            cardBackgroundImage = tk.PhotoImage(
                file="./image_components/" + car['image'] + '.png')
            cardBackground = tk.Label(image=cardBackgroundImage)
            cardBackground.place(x=0, y=0)

            label_make = tk.Label(scrollable_frame, text=car["make"])
            label_make .grid(row=0, column=0)
            label_model = tk.Label(scrollable_frame, text=car["model"])
            label_model.grid(row=1, column=0)
            label_seats = tk.Label(
                scrollable_frame, text=car["seatingCapacity"])
            label_seats.grid(row=2, column=0)

            button = tk.Button(scrollable_frame, text="Print Name",
                               command=lambda n=car: self.print_name(n))
            button.grid(row=3, column=0)

            frame_list.append(scrollable_frame)

        carsContainer.bind(
            "<Configure>", lambda event: self.on_configure(self, event))


# Bind the canvas to configure the scrollable region


    def on_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def getLocation(self):
        self.after(4000, lambda: self.locationButton.config(
            text='Getting Location...'))

    def gotLocation(self):
        self.locationButtonText = 'G4 0AS, Glasgow'
        self.locationButton.config(
            text=self.locationButtonText)

    def print_name(name):
        print("Name:", name['model'])


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
