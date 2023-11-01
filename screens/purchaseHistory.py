import tkinter as tk
from tkinter import ttk
from datetime import datetime


class PurchaseHistory(ttk.Frame):

    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller
        print("Constructing PurchaseHistory...")
        self.history = controller.get_user_history()

        self.frame_label = tk.Label(
            self, text="Purchase History", font=("Helvetica", 20, 'bold'))
        self.frame_label.place(x=35, y=45)

        self.backButtonArrow = tk.PhotoImage(
            file="./image_components/arrow_alt_left.png")
        self.backButton = ttk.Button(self,
                                     image=self.backButtonArrow, command=lambda: controller.change_frame('vehiclesView'))
        self.backButton.place(x=10, y=10)

        self.styled = ttk.Style()
        self.styled.configure("TButton", font=("Helvetica", 16))
        self.styled.configure('TMenu', anchor='w', justify='left')
        self.styled.configure("Custom.TFrame", background="white")
        self.style = "Custom.TFrame"

        self.selected_vehicle = tk.StringVar()  # Create the StringVar here
        self.options = ['Car', 'Bike', 'Car']
        self.selected_vehicle.set(self.options[0])

        self.canvas = tk.Canvas(self)
        self.canvas.place(x=25, y=100, height=620, width=480)

        self.carsContainer = tk.Frame(self.canvas)
        self.canvas.create_window(
            (0, 0), window=self.carsContainer, anchor="nw")

        scrollbar = tk.Scrollbar(
            self, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side="right", fill="y")
        self.canvas.config(yscrollcommand=scrollbar.set)

        self.refresh_data()
        # controller.update_idletasks()
        self.carsContainer.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def delete_child_frames(self, container_frame):
        for widget in container_frame.winfo_children():
            if isinstance(widget, tk.Frame):
                widget.destroy()

    def refresh_data(self):
        # self.canvas.delete("all")
        self.history = self.controller.get_user_history()
        self.delete_child_frames(self.carsContainer)
        self.carsContainer.update_idletasks()

        # Navigation bar
        self.homeIcon = tk.PhotoImage(
            file="./image_components/home_light.png")
        self.historyIcon = tk.PhotoImage(
            file="./image_components/time_progress_light.png")
        self.signOutIcon = tk.PhotoImage(
            file="./image_components/sign_out_circle_light.png")
        self.navigation = tk.Frame(self, background='#FFFFFF')
        button1 = ttk.Button(
            self.navigation, image=self.homeIcon, command=lambda: self.controller.change_frame('vehiclesView'))
        button2 = ttk.Button(
            self.navigation, image=self.historyIcon, command=lambda: self.controller.change_frame('purchaseHistory'))
        button3 = ttk.Button(
            self.navigation, image=self.signOutIcon, command=lambda: self.controller.change_frame('welcome'))
        self.navigation.grid_columnconfigure(0, weight=1)
        self.navigation.grid_columnconfigure(1, weight=1)
        self.navigation.grid_columnconfigure(2, weight=1)
        navLabel1 = tk.Label(self.navigation, text='Home')
        navLabel2 = tk.Label(self.navigation, text='History')
        navLabel3 = tk.Label(self.navigation, text='Log Out')
        button1.grid(row=0, column=0, padx=5, pady=20)
        button2.grid(row=0, column=1, padx=5, pady=20)
        button3.grid(row=0, column=2, padx=5, pady=20)
        navLabel1.grid(row=1, column=0, padx=5, sticky='N')
        navLabel2.grid(row=1, column=1, padx=5, sticky='N')
        navLabel3.grid(row=1, column=2, padx=5, sticky='N')
        self.navigation.place(x=0, y=700, height=100, width=480)

        self.index = 1
        print("HSTR: ", self.history)
        for car in self.history:
            scrollable_frame = tk.Frame(self.carsContainer)
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

            label_license = tk.Label(
                scrollable_frame, text=car['licensePlateNumber'], bg=car["bg"], fg=car["fg"], font=(
                    'Helvetica', 12), anchor='w', justify='left')
            label_license.grid(row=0, column=0, sticky='nw',
                               padx=30, pady=62)

            label_date = tk.Label(
                scrollable_frame, text="| "+str(self.format_datetime(car['startTime'])), bg=car["bg"], fg=car["fg"], font=(
                    'Helvetica', 10, 'bold'), anchor='w', justify='left')
            label_date.grid(row=0, column=0, sticky='nw',
                            padx=110, pady=62)

            returnText = ''
            if (car['endTime']):
                returnText = str(car['income'])+'£'
            else:
                returnText = "Return Vehicle"

            label_return = tk.Label(
                scrollable_frame, text=returnText, bg=car["bg"], fg=car["fg"], font=(
                    'Helvetica', 14, 'bold'), anchor='w', justify='left')
            label_return.grid(row=0, column=0, sticky='nw',
                              padx=30, pady=82)

            label_image.bind(
                "<Button-1>", lambda event, car=car, index=self.index: self.handle_click_on_vehicle(self.controller, car, index))
            scrollable_frame.pack()
            self.index += 1

        self.carsContainer.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.update_idletasks()

    def handle_click_on_vehicle(self, controller, car, index):
        # print("Clicked on label..." + str(index), car)
        print("clicked on card")
        print("Car: ", car)
        if car['endTime'] is None:

            controller.set_selected_order(order=car)
            self.controller.change_frame("returnAndPay")

    def format_datetime(self, datetime_str):
        # Convert the datetime string to a datetime object
        dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")

        # Format the datetime as "22 Sep 2023"
        formatted_date = dt.strftime("%d %b %Y")

        return formatted_date
