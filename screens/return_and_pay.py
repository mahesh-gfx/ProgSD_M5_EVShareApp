import tkinter as tk
from tkinter import ttk

class Return_and_pay(ttk.Frame):

    def return_and_pay(self):
        print("pay")

    def __init__(self, container, controller):
        tk.Frame.__init__(self, container)

        self.layout = tk.PhotoImage(file=r"../image_components/return_and_pay_layout.png")
        self.layout_label = tk.Label(self,image=self.layout)
        self.layout_label.place(relx=0, rely=0)

        self.time_label = tk.Label(self, text="Total Time in hours: ", bg="#D9D9D9", font=('Helvetica', 15))
        self.time_label.place(relx=0.15, rely=0.21)
        self.time = tk.Label(self, text="4 Hours", bg="#D9D9D9", font=('Helvetica', 15))
        self.time.place(relx=0.6, rely=0.21)

        self.name_label = tk.Label(self, text="Vehicle Name: ", bg="#D9D9D9", font=('Helvetica', 15))
        self.name_label.place(relx=0.15, rely=0.26)
        self.name = tk.Label(self, text="Tesla Model S", bg="#D9D9D9", font=('Helvetica', 15))
        self.name.place(relx=0.6, rely=0.26)

        self.locations = ["Bath St.", "Havannah St.", "Hannover St."]
        self.val = tk.StringVar()
        self.val.set(self.locations[0])
        self.locations_drop_down = ttk.Combobox(self, textvariable=self.val, values=self.locations, state="readonly",
                                                      font=('Mako', 15), style="CustomStyles.TCombobox")
        self.locations_drop_down.place(relx=0.15, rely=0.32, height=42, width=360)

        self.amount_label = tk.Label(self, text="Amount: ", bg="#D9D9D9", font=('Helvetica', 15))
        self.amount_label.place(relx=0.15, rely=0.4)
        self.amount = tk.Label(self, text="£400", bg="#D9D9D9", font=('Helvetica', 15))
        self.amount.place(relx=0.6, rely=0.4)

        self.btnImage = tk.PhotoImage(file=r"../image_components/return_and_pay_btn.png")
        self.btn = tk.Button(self, image=self.btnImage, compound=tk.TOP, command=self.return_and_pay, borderwidth=0,
                                  background='#D9D9D9', activebackground="#D9D9D9")
        self.btn.place(relx=0.04, rely=0.88)


class App(tk.Tk):
    # Attributes
    vehicles = []
    db_name = 'zevo-dev.db'
    # Constructors

    def __init__(self):
        super().__init__()
        self.geometry("480x800")
        self.title("Zevo | EV Rental")
        self.resizable(False, True)
        print("Constructing App...")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        RAPFram = Return_and_pay(container, controller=self)
        RAPFram.grid(row=0, column=0, sticky="nsew")

        RAPFram.tkraise()


if __name__ == "__main__":
    app = App()
    app.mainloop()