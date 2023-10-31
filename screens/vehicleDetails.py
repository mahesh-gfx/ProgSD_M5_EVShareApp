import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont


class VehicleDetails(ttk.Frame):

    def __init__(self, container, controller):
        super().__init__(container)
        print("Constructing Vehicle Details frame...")

        self.localController = controller
        self.styled = ttk.Style()
        self.styled.configure("TButton", font=("Helvetica", 16))
        self.styled.configure('TMenu', anchor='w', justify='left')
        self.styled.configure("Custom.TFrame", background="white")
        self.style = "Custom.TFrame"

        self.backButtonArrow = tk.PhotoImage(
            file="./image_components/arrow_alt_left.png")
        self.backButton = ttk.Button(self,
                                     image=self.backButtonArrow, command=lambda: controller.change_frame('vehiclesView'))
        self.backButton.place(x=10, y=10)

        self.backgroundImage = tk.PhotoImage(
            file=f"./image_components/{controller.get_selected_vehicle()['image']}_full.png")
        self.backgroundImageLabel = tk.Label(self, image=self.backgroundImage)
        self.backgroundImageLabel.place(x=35, y=55)

        self.mapIconDark = tk.PhotoImage(
            file="./image_components/map_duotone_dark.png")

        self.mapIconLight = tk.PhotoImage(
            file="./image_components/map_duotone_light.png")

        self.label_make = tk.Label(
            self, text=controller.get_selected_vehicle()["make"] + " " + controller.get_selected_vehicle()["model"], bg=controller.get_selected_vehicle()["bg"], fg=controller.get_selected_vehicle()["fg"], font=(
                'Helvetica', 18, "bold"), anchor='w', justify='left')
        self.label_make.grid(row=0, column=0, sticky='nw', padx=75, pady=230)

        self.label_distance_icon = tk.Label()

        if (controller.get_selected_vehicle()['fg'] == '#000000'):
            self.label_distance_icon = tk.Label(
                self, image=self.mapIconDark, bg=controller.get_selected_vehicle()["bg"])
        else:
            self.label_distance_icon = tk.Label(
                self, image=self.mapIconLight, bg=controller.get_selected_vehicle()["bg"])

        self.label_distance_icon.grid(
            row=0, column=0, sticky='nw', padx=75, pady=270)

        # text=controller.get_selected_vehicle()["distance"]
        self.label_distance = tk.Label(
            self, text="10"+" miles away", bg=controller.get_selected_vehicle()["bg"], fg=controller.get_selected_vehicle()["fg"], font=(
                'Helvetica', 12), anchor='w', justify='left')
        self.label_distance.grid(
            row=0, column=0, sticky='nw', padx=106, pady=271)

        self.label_rate = tk.Label(
            self, text="£"+str(controller.get_selected_vehicle()["ratePerWeek"]) + "/week", bg=controller.get_selected_vehicle()["bg"], fg=controller.get_selected_vehicle()["fg"], font=(
                'Helvetica', 14, 'bold'), anchor='w', justify='left')
        self.label_rate.grid(row=0, column=0, sticky='nw', padx=75, pady=310)

        self.label_specs = tk.Label(self, text='Specs', font=(
            'Helvetica', 8), bg=controller.get_selected_vehicle()["bg"], fg=controller.get_selected_vehicle()["fg"])
        self.label_specs.place(x=75, y=370)

        self.label_seats = tk.Label(
            self, text="Seats "+str(controller.get_selected_vehicle()["seatingCapacity"]), bg=controller.get_selected_vehicle()["bg"], fg=controller.get_selected_vehicle()["fg"], font=(
                'Helvetica', 12), anchor='w', justify='left')
        self.label_seats.grid(row=0, column=0, sticky='nw', padx=75, pady=400)

        self.label_doors = tk.Label(
            self, text=str(controller.get_selected_vehicle()["doors"])+" doors", bg=controller.get_selected_vehicle()["bg"], fg=controller.get_selected_vehicle()["fg"], font=(
                'Helvetica', 12), anchor='w', justify='left')
        self.label_doors.grid(row=0, column=0, sticky='nw', padx=175, pady=400)

        self.label_hp = tk.Label(
            self, text=str(controller.get_selected_vehicle()["horsePower"]) + " BHP", bg=controller.get_selected_vehicle()["bg"], fg=controller.get_selected_vehicle()["fg"], font=(
                'Helvetica', 12), anchor='w', justify='left')
        self.label_hp.grid(row=0, column=0, sticky='nw', padx=275, pady=400)

        self.label_battery_capacity = tk.Label(
            self, text=controller.get_selected_vehicle()["batteryCapacity"], bg=controller.get_selected_vehicle()["bg"], fg=controller.get_selected_vehicle()["fg"], font=(
                'Helvetica', 12), anchor='w', justify='left')
        self.label_battery_capacity.grid(
            row=0, column=0, sticky='nw', padx=75, pady=480)

        self.label_range = tk.Label(
            self, text=str(controller.get_selected_vehicle()["range"])+" miles", bg=controller.get_selected_vehicle()["bg"], fg=controller.get_selected_vehicle()["fg"], font=(
                'Helvetica', 12), anchor='w', justify='left')
        self.label_range.grid(row=0, column=0, sticky='nw', padx=175, pady=480)

        self.label_max_speed = tk.Label(
            self, text=str(controller.get_selected_vehicle()["maxSpeed"]) + " miles/hour", bg=controller.get_selected_vehicle()["bg"], fg=controller.get_selected_vehicle()["fg"], font=(
                'Helvetica', 12), anchor='w', justify='left')
        self.label_max_speed.grid(
            row=0, column=0, sticky='nw', padx=275, pady=480)

        self.lets_go_button = ttk.Button(
            self, text='Book now', compound="left", command=lambda: controller.change_frame('paymentBill'))
        self.lets_go_button.place(x=310, y=250, height=52, width=150)

        # self.bind("<Enter>", lambda event, frame=self: frame.refresh_data)

    def refresh_data(self):
        print("Refreshing data on the vehicle details page..")
        self.backgroundImage = tk.PhotoImage(
            file=f"./image_components/{self.localController.get_selected_vehicle()['image']}_full.png")
        self.backgroundImageLabel.configure(image=self.backgroundImage)
        # self.backgroundImageLabel.place(x=35, y=55)

        self.label_make.configure(text=self.localController.get_selected_vehicle()[
                                  "make"] + " " + self.localController.get_selected_vehicle()["model"], bg=self.localController.get_selected_vehicle()["bg"], fg=self.localController.get_selected_vehicle()["fg"])

        if (self.localController.get_selected_vehicle()['fg'] == '#000000'):
            self.label_distance_icon.configure(
                image=self.mapIconDark, bg=self.localController.get_selected_vehicle()["bg"])
        else:
            self.label_distance_icon.configure(
                image=self.mapIconLight, bg=self.localController.get_selected_vehicle()["bg"])

        # text=self.localController.get_selected_vehicle()["distance"]
        self.label_distance.config(text='10'+" miles away", bg=self.localController.get_selected_vehicle()[
                                   "bg"], fg=self.localController.get_selected_vehicle()["fg"])

        self.label_rate.configure(text="£"+str(self.localController.get_selected_vehicle()[
                                  "ratePerWeek"]) + "/week", bg=self.localController.get_selected_vehicle()["bg"], fg=self.localController.get_selected_vehicle()["fg"],)

        self.label_specs.configure(bg=self.localController.get_selected_vehicle()[
                                   "bg"], fg=self.localController.get_selected_vehicle()["fg"])

        self.label_seats.configure(text="Seats "+str(self.localController.get_selected_vehicle()[
                                   "seatingCapacity"]), bg=self.localController.get_selected_vehicle()["bg"], fg=self.localController.get_selected_vehicle()["fg"])

        self.label_doors.configure(text=str(self.localController.get_selected_vehicle()[
                                   "doors"])+" doors", bg=self.localController.get_selected_vehicle()["bg"], fg=self.localController.get_selected_vehicle()["fg"],)

        self.label_hp.configure(text=str(self.localController.get_selected_vehicle()[
                                "horsePower"]) + " BHP", bg=self.localController.get_selected_vehicle()["bg"], fg=self.localController.get_selected_vehicle()["fg"])

        self.label_battery_capacity.configure(text=self.localController.get_selected_vehicle(
        )["batteryCapacity"], bg=self.localController.get_selected_vehicle()["bg"], fg=self.localController.get_selected_vehicle()["fg"])

        self.label_range.configure(text=str(self.localController.get_selected_vehicle()[
                                   "range"])+" miles", bg=self.localController.get_selected_vehicle()["bg"], fg=self.localController.get_selected_vehicle()["fg"])

        self.label_max_speed.configure(text=str(self.localController.get_selected_vehicle(
        )["maxSpeed"]) + " miles/hour", bg=self.localController.get_selected_vehicle()["bg"], fg=self.localController.get_selected_vehicle()["fg"])

        return True

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
#         vehicleDetailsFrame = VehicleDetails(container, controller=self)
#         vehicleDetailsFrame.grid(row=0, column=0, sticky="nsew")

#         vehicleDetailsFrame.tkraise()


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()
