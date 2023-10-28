import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont


class VehicleDetails(ttk.Frame):

    def __init__(self, container, controller):
        super().__init__(container)
        print("Constructing Vehicle Details frame...")

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
            file=f"./image_components/{controller.selectedVehicle['image']}_full.png")
        self.backgroundImageLabel = tk.Label(self, image=self.backgroundImage)
        self.backgroundImageLabel.place(x=35, y=55)

        self.mapIconDark = tk.PhotoImage(
            file="./image_components/map_duotone_dark.png")

        self.mapIconLight = tk.PhotoImage(
            file="./image_components/map_duotone_light.png")

        label_make = tk.Label(
            self, text=controller.selectedVehicle["make"] + " " + controller.selectedVehicle["model"], bg=controller.selectedVehicle["bg"], fg=controller.selectedVehicle["fg"], font=(
                'Helvetica', 18, "bold"), anchor='w', justify='left')
        label_make.grid(row=0, column=0, sticky='nw', padx=75, pady=230)

        self.label_distance_icon = tk.Label()

        if (controller.selectedVehicle['fg'] == '#000000'):
            self.label_distance_icon = tk.Label(
                self, image=self.mapIconDark, bg=controller.selectedVehicle["bg"])
        else:
            self.label_distance_icon = tk.Label(
                self, image=self.mapIconLight, bg=controller.selectedVehicle["bg"])

        self.label_distance_icon.grid(
            row=0, column=0, sticky='nw', padx=75, pady=270)

        label_distance = tk.Label(
            self, text=controller.selectedVehicle["distance"]+" miles away", bg=controller.selectedVehicle["bg"], fg=controller.selectedVehicle["fg"], font=(
                'Helvetica', 12), anchor='w', justify='left')
        label_distance.grid(row=0, column=0, sticky='nw', padx=106, pady=271)

        label_rate = tk.Label(
            self, text="£"+controller.selectedVehicle["ratePerWeek"] + "/week", bg=controller.selectedVehicle["bg"], fg=controller.selectedVehicle["fg"], font=(
                'Helvetica', 14, 'bold'), anchor='w', justify='left')
        label_rate.grid(row=0, column=0, sticky='nw', padx=75, pady=310)

        label_specs = tk.Label(self, text='Specs', font=(
            'Helvetica', 8), bg=controller.selectedVehicle["bg"], fg=controller.selectedVehicle["fg"])
        label_specs.place(x=75, y=370)

        label_seats = tk.Label(
            self, text="Seats "+controller.selectedVehicle["seatingCapacity"], bg=controller.selectedVehicle["bg"], fg=controller.selectedVehicle["fg"], font=(
                'Helvetica', 12), anchor='w', justify='left')
        label_seats.grid(row=0, column=0, sticky='nw', padx=75, pady=400)

        label_seats = tk.Label(
            self, text=controller.selectedVehicle["doors"]+" doors", bg=controller.selectedVehicle["bg"], fg=controller.selectedVehicle["fg"], font=(
                'Helvetica', 12), anchor='w', justify='left')
        label_seats.grid(row=0, column=0, sticky='nw', padx=175, pady=400)

        label_seats = tk.Label(
            self, text=controller.selectedVehicle["horsepower"] + " BHP", bg=controller.selectedVehicle["bg"], fg=controller.selectedVehicle["fg"], font=(
                'Helvetica', 12), anchor='w', justify='left')
        label_seats.grid(row=0, column=0, sticky='nw', padx=275, pady=400)

        label_seats = tk.Label(
            self, text=controller.selectedVehicle["batteryCapacity"], bg=controller.selectedVehicle["bg"], fg=controller.selectedVehicle["fg"], font=(
                'Helvetica', 12), anchor='w', justify='left')
        label_seats.grid(row=0, column=0, sticky='nw', padx=75, pady=480)

        label_seats = tk.Label(
            self, text=controller.selectedVehicle["range"]+" miles", bg=controller.selectedVehicle["bg"], fg=controller.selectedVehicle["fg"], font=(
                'Helvetica', 12), anchor='w', justify='left')
        label_seats.grid(row=0, column=0, sticky='nw', padx=175, pady=480)

        label_seats = tk.Label(
            self, text=controller.selectedVehicle["maxSpeed"] + " miles/hour", bg=controller.selectedVehicle["bg"], fg=controller.selectedVehicle["fg"], font=(
                'Helvetica', 12), anchor='w', justify='left')
        label_seats.grid(row=0, column=0, sticky='nw', padx=275, pady=480)

        self.letsGoButton = ttk.Button(
            self, text='Book now', compound="left", command=lambda: controller.change_frame('paymentBill'))
        self.letsGoButton.place(x=310, y=250, height=52, width=150)


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
