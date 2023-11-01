import tkinter as tk
from tkinter import ttk
import tkintermapview
from tkinter import messagebox


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
        self.container = container
        self.controller = controller
        print("Constructing Operator View...")

        self.styled = ttk.Style()
        self.styled.configure("TButton", font=("Helvetica", 14))
        self.styled.configure('TMenu', anchor='w', justify='left')
        self.styled.configure("Custom.TFrame", background="white")
        self.style = "Custom.TFrame"

        self.frame_label = tk.Label(
            self, text="Operator Dashboard", font=("Helvetica", 20, 'bold'))
        self.frame_label.place(x=35, y=45)

        self.cars = controller.get_all_vehicles()
        # print(self.cars)

        self.styled = ttk.Style()
        self.styled.configure('TMenubutton', font=(
            'Helvetica', 14, "bold"), anchor='w', justify='left')

        self.button1 = ttk.Button(self, text="All Vehicles")

        self.map_widget = tkintermapview.TkinterMapView(
            self, width=400, height=600, corner_radius=0)
        self.map_widget.place(x=1050, y=150)
        self.map_widget.set_position(55.859015320462596, -
                                     4.234950142328189)

        self.canvas = tk.Canvas(self)
        self.canvas.place(x=25, y=150, height=600, width=1000)

        self.carsContainer = tk.Frame(self.canvas)
        self.canvas.create_window(
            (0, 0), window=self.carsContainer, anchor="w")

        scrollbar = tk.Scrollbar(
            self, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")
        self.canvas.config(yscrollcommand=scrollbar.set)
        header_make = tk.Label(self, text="Make and Model",
                               anchor='w', justify='left')
        header_license = tk.Label(
            self, text="License Plate", anchor='w', justify='left')
        header_location = tk.Label(
            self, text="Location", anchor='w', justify='left')
        header_use = tk.Label(self, text="In use")
        header_make.place(x=50, y=100)
        header_license.place(x=273, y=100)
        header_location.place(x=415, y=100)
        header_use.place(x=560, y=100)

        self.refresh_data()
        self.carsContainer.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def handle_track(self, location):
        print(location)
        print(self.get_coordinates(location))
        lat, long = self.get_coordinates(location)
        self.map_widget.set_position(float(lat), float(long), marker=True)

    def get_coordinates(self, location):
        for item in self.coordinates:
            if item["Location"] == location:
                return item["latitude"], item["longitude"]
        return None, None  # Return None for latitude and longitude if location is not found

    def move_vehicle(self, vehicle):
        if vehicle['inUse']:
            messagebox.showerror(
                "Cannot Move", "Vehicle in use, cannot move!")
        else:
            print("Can move")
            # self.controller.move_vehicle()
            popup = tk.Toplevel(self.controller)
            popup.title("Move Vehicle")

            # Calculate the position for the popup window
            x = self.controller.winfo_x() + 250  # Adjust as needed
            y = self.controller.winfo_y() + 250  # Adjust as needed

            popup.geometry(f"400x300+{x}+{y}")

            # Create a frame for the popup content
            popup_frame = tk.Frame(popup)
            popup_frame.place(x=0, y=0, height=300, width=400)

            # Add widgets to the popup frame
            label = tk.Label(popup_frame, text="Move Vehicle", font=(
                'Helvetica', 16, "bold"))
            label.place(x=30, y=30)

            current = tk.Label(
                popup_frame, text="Current Location: " + vehicle['location'], font=('Mako', 16))
            current.place(x=30, y=75)
            selected_location = tk.StringVar()
            available_locations = ['Havannah St.', 'Bath St.', 'Hannover St.',
                                   'Argyle St.', 'Helen St.', 'Govan Road', '5 Morefield Rd']
            selected_location.set(available_locations[0])

            dropdown = ttk.Combobox(popup_frame, textvariable=selected_location, values=available_locations, state="readonly",
                                    font=('Mako', 14), style="CustomStyles.TCombobox")
            dropdown.place(x=30, y=110)
            # self.selected_vehicle.trace("w", self.on_combobox_select)

            self.styled.configure(
                "Custom.TButton", foreground="blue")

            def confirm_move():
                print("Confirming Move...")
                result = self.controller.move_vehicle(
                    vehicle['vehicle_id'], selected_location.get())
                if result:
                    self.refresh_data()
                    messagebox.showinfo(
                        "Moved vehicle", "Successfully moved the vehicle!")

                else:
                    messagebox.showerror(
                        "Error: Move Vehicle", "Couldn't move the vehicle!")

            confirm_button = ttk.Button(
                popup_frame, text="Confirm Move", command=confirm_move, style="Custom.TButton")
            close_button = ttk.Button(
                popup_frame, text="Cancel", command=popup.destroy)

            close_button.place(x=30, y=170)
            confirm_button.place(x=30, y=210)

    def refresh_data(self):
        self.cars = self.controller.get_all_vehicles()
        index = 0
        self.bg = "lightblue"
        for car in self.cars:
            if (index % 2 == 0):
                self.bg = "white"
            else:
                self.bg = "lightblue"

            scrollable_frame = tk.Frame(
                self.carsContainer, height=80, width=600, bg=self.bg)

            row_frame = tk.Frame(
                scrollable_frame, relief=tk.SOLID, borderwidth=2, bg=self.bg)
            row_frame.grid(row=0, column=0, padx=20, sticky="w")

            label_make = tk.Label(
                scrollable_frame, text=car["make"] + " " + car["model"], fg='black', font=(
                    'Helvetica', 16), anchor='w', justify='left', bg=self.bg, width=15)
            label_make.grid(row=0, column=0, padx=20, sticky="w")

            label_license = tk.Label(
                scrollable_frame, text=car["licensePlateNumber"], font=(
                    'Helvetica', 16), anchor='w', justify='left', bg=self.bg, width=10)
            label_license.grid(row=0, column=1, padx=20,
                               sticky="w")

            label_location = tk.Label(
                scrollable_frame, text=car["location"], fg='black', font=(
                    'Helvetica', 16), anchor='w', justify='left', bg=self.bg,  width=10)
            label_location.grid(row=0, column=2, sticky="w")

            inUse = "No"
            if car['inUse']:
                inUse = "Yes"
            else:
                inUse = "No"

            label_in_use = tk.Label(
                scrollable_frame, text=inUse, fg="black", font=(
                    'Helvetica', 14, 'bold'), anchor='w', justify='left', width=5)
            label_in_use.grid(row=0, column=3, padx=30)

            # command=lambda event, car=car: self.handle_track(location = car["location"])
            track = ttk.Button(scrollable_frame, text="Track", width=7,
                               command=lambda location=car["location"]: self.handle_track(location))
            charge = ttk.Button(scrollable_frame, text="Charge", width=7)
            move = ttk.Button(scrollable_frame, text="Move", width=7,
                              command=lambda vehicle=car: self.move_vehicle(vehicle))
            repair = ttk.Button(scrollable_frame, text="Repair", width=7)
            track.grid(row=0, column=4)
            charge.grid(row=0, column=5)
            move.grid(row=0, column=6)
            repair.grid(row=0, column=7)
            index += 1
            scrollable_frame.pack(side="top", fill="x")

        self.carsContainer.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.update_idletasks()

    def delete_child_frames(self, container_frame):
        for widget in container_frame.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()
