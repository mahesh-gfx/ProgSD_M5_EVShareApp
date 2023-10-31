import tkinter as tk
from tkinter import ttk
import tkintermapview


class Operator(ttk.Frame):

    coordinates = [{"Location": "Havannah St.", "latitude": "55.859015320462596", "longitude": "-4.234950142328189"},
                   {"Location": "Bath St.", "latitude": "55.86458152166685",
                       "longitude": "-4.261815560286359"},
                   {"Location": "Hannover St.", "latitude": "55.86435027400467",
                       "longitude": "-4.249073437803929"},
                   {"Location": "Argyle St.", "latitude": "55.86164192941104",
                       "longitude": "-4.273819787271126"},
                   {"Location": "Helen St.", "latitude": "55.85289156481755",
                       "longitude": "-4.318004605206159"},
                   {"Location": "Govan Road", "latitude": "55.85458599359976",
                       "longitude": "-4.281177167028063"},
                   {"Location": "5 Morefield Rd", "latitude": "55.857814397863415",
                       "longitude": "-4.334998534942994"},
                   ]

    def __init__(self, container, controller):
        super().__init__(container)
        print("Constructing Operator View...")
        self.styled = ttk.Style()
        self.styled.configure("TButton", font=("Helvetica", 14))
        self.styled.configure('TMenu', anchor='w', justify='left')
        self.styled.configure("Custom.TFrame", background="white")
        self.style = "Custom.TFrame"

        self.cars = controller.get_all_vehicles()

        self.styled = ttk.Style()
        self.styled.configure('TMenubutton', font=(
            'Helvetica', 14, "bold"), anchor='w', justify='left')

        self.button1 = ttk.Button(self, text="All Vehicles")

        map_widget = tkintermapview.TkinterMapView(
            self, width=400, height=400, corner_radius=0)
        map_widget.place(x=950, y=150)
        map_widget.set_position(55.859015320462596, -
                                4.234950142328189, marker=True)

        canvas = tk.Canvas(self)
        canvas.place(x=25, y=150, height=600, width=900)

        self.carsContainer = tk.Frame(canvas)
        canvas.create_window((0, 0), window=self.carsContainer, anchor="nw")

        scrollbar = tk.Scrollbar(self, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")
        canvas.config(yscrollcommand=scrollbar.set)
        header_make = tk.Label(self, text="Make and Model")
        header_license = tk.Label(self, text="License Plate")
        header_location = tk.Label(self, text="Location")
        header_use = tk.Label(self, text="In use")
        header_make.place(x=50, y=100)
        header_license.place(x=250, y=100)
        header_location.place(x=380, y=100)
        header_use.place(x=500, y=100)
        for car in self.cars:
            scrollable_frame = tk.Frame(self.carsContainer, )

            row_frame = tk.Frame(
                scrollable_frame, relief=tk.SOLID, borderwidth=2)
            row_frame.grid(row=0, column=0)

            label_make = tk.Label(
                scrollable_frame, text=car["make"] + " " + car["model"], fg='black', font=(
                    'Helvetica', 18), anchor='w', justify='left')
            label_make.grid(row=0, column=0, padx=20)

            label_license = tk.Label(
                scrollable_frame, text=car["licensePlateNumber"], font=(
                    'Helvetica', 18), anchor='w', justify='left')
            label_license.grid(row=0, column=1, padx=20)

            label_location = tk.Label(
                scrollable_frame, text="Location", fg='black', font=(
                    'Helvetica', 18), anchor='w', justify='left')
            label_location.grid(row=0, column=2,)
            inUse = "No"
            if car['inUse']:
                inUse = "Yes"
            else:
                inUse = "No"

            label_in_use = tk.Label(
                scrollable_frame, text=inUse, fg="black", font=(
                    'Helvetica', 14, 'bold'), anchor='w', justify='left')
            label_in_use.grid(row=0, column=3, padx=30)

            track = ttk.Button(scrollable_frame, text="Track", width=7)
            charge = ttk.Button(scrollable_frame, text="Charge", width=7)
            move = ttk.Button(scrollable_frame, text="Move", width=7)
            repair = ttk.Button(scrollable_frame, text="Repair", width=7)
            track.grid(row=0, column=4)
            charge.grid(row=0, column=5)
            move.grid(row=0, column=6)
            repair.grid(row=0, column=7)

            row_frame.bind(
                "<Button-1>", lambda event: self.handle_click_on_vehicle(controller, car))
            scrollable_frame.pack()

        self.carsContainer.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def handle_track(self, controller, car):
        print("Clicked on vehicle..")
        # controller.set_selected_vehicle(car)
        # controller.change_frame('vehicleDetails')


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
