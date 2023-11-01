import tkinter as tk
from tkinter import ttk

class VehiclesView(ttk.Frame):

    cars = []

    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller
        print("Constructing Vehicles View self.navigation...")
        self.cars = controller.get_all_vehicles()

        self.styled = ttk.Style()
        self.styled.configure("TButton", font=("Helvetica", 16))
        self.styled.configure('TMenu', anchor='w', justify='left')
        self.styled.configure("Custom.TFrame", background="white")
        self.style = "Custom.TFrame"

        self.selected_vehicle = tk.StringVar()  # Create the StringVar here
        self.options = ['Car', 'Bike', 'Car']
        self.selected_vehicle.set(self.options[0])

        # locations drop down
        self.locations = ["Bath St.", "Havannah St.", "Hannover St."]
        self.val = tk.StringVar()
        self.val.set(self.locations[0])
        self.locations_drop_down = ttk.Combobox(self, textvariable=self.val, values=self.locations, state="readonly",
                                                      font=('Mako', 14), style="CustomStyles.TCombobox")
        self.locations_drop_down.place(x=200, y=45, height=42, width=260)


        self.label = tk.Label(self, text="I want to rent a",
                              font=("Helvetica", 20))
        self.label.place(x=25, y=132)

        self.canvasLine = tk.Canvas(self, width=400, height=400)
        self.canvasLine.create_line(0, 100, 150, 100, fill="black", width=2)
        self.canvasLine.place(x=32, y=105)

        self.dropdown = ttk.OptionMenu(
            self, self.selected_vehicle, *self.options)
        self.dropdown.place(x=35, y=164, height=40, width=150)

        self.styled = ttk.Style()
        self.styled.configure('TMenubutton', font=(
            'Helvetica', 18, "bold"), anchor='w', justify='left')

        self.label.lift()
        self.dropdown.lift()
        self.render_view(container)

    def render_view(self, controller):
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
        self.homeIcon = tk.PhotoImage(
            file="./image_components/home_light.png")
        self.historyIcon = tk.PhotoImage(
            file="./image_components/time_progress_light.png")
        self.signOutIcon = tk.PhotoImage(
            file="./image_components/sign_out_circle_light.png")

        self.navigation = tk.Frame(self)
        button1 = ttk.Button(
            self.navigation, image=self.homeIcon)
        button2 = ttk.Button(
            self.navigation, image=self.historyIcon)
        button3 = ttk.Button(
            self.navigation, image=self.signOutIcon)

        self.navigation.grid_columnconfigure(0, weight=1)
        self.navigation.grid_columnconfigure(1, weight=1)
        self.navigation.grid_columnconfigure(2, weight=1)

        button1.grid(row=0, column=0, padx=5)
        button2.grid(row=0, column=1, padx=5)
        button3.grid(row=0, column=2, padx=5)

        self.navigation.place(x=0, y=700, height=100, width=480)

        self.index = 1
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

            # car["distance"]
            label_distance = tk.Label(
                scrollable_frame, text=car["location"], bg=car["bg"], fg=car["fg"], font=(
                    'Helvetica', 12), anchor='w', justify='left')
            label_distance.grid(row=0, column=0, sticky='nw', padx=62, pady=62)

            label_seats = tk.Label(
                scrollable_frame, text="Seats "+str(car["seatingCapacity"]), bg=car["bg"], fg=car["fg"], font=(
                    'Helvetica', 12), anchor='w', justify='left')
            label_seats.grid(row=0, column=0, sticky='nw', padx=30, pady=88)

            label_rate = tk.Label(
                scrollable_frame, text="£"+str(car["ratePerWeek"]) + "/week", bg=car["bg"], fg=car["fg"], font=(
                    'Helvetica', 14, 'bold'), anchor='w', justify='left')
            label_rate.grid(row=0, column=0, sticky='sw', padx=30, pady=50)

            label_image.bind(
                "<Button-1>", lambda event, car=car, index=self.index: self.handle_click_on_vehicle(self.controller, car, index))
            scrollable_frame.pack()
            self.index += 1

        self.carsContainer.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    def getLocation(self):
        self.locationButton.config(
            text='Getting Location...')
        self.after(4000, lambda: self.locationButton.config(
            text='G4 0AS, Glasgow'))

    def handle_click_on_vehicle(self, controller, car, index):
        # print("Clicked on label..." + str(index), car)
        controller.set_selected_vehicle(car)
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
