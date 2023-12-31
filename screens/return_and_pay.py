import math
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox


class ReturnAndPay(ttk.Frame):

    def return_and_pay(self):
        self.controller.set_amount(amount=self.amount)
        print("PAY: ", self.order)
        self.controller.change_frame("paymentAccess")

    def on_select(self, event):
        print("Hey Man: ", self.val.get())
        self.order['returnLocation'] = self.val.get()
        print("Updated Order: ", self.order)
    
    def get_discount(self):
        code = self.disountlabel.get()
        ifdiscount = localController.get_discount(code)
        if ifdiscount == -1:
            messagebox.showerror("Zevo | EV Rental", "Wrong Code")
            localController.discount = 0
        else:
            save_string = "You have a ￡"+str(ifdiscount)+" discount!"
            messagebox.showinfo("Zevo | EV Rental", save_string)
            localController.discount = ifdiscount
            self.total_discount = tk.Label(
            self, text="£" + str(localController.discount), bg="#D9D9D9", font=('Helvetica', 15))
            self.total_discount.place(relx=0.6, rely=0.44)
            localController.discount = ifdiscount
            print('refresh the discount')

    def __init__(self, container, controller):
        super().__init__(container)
        tk.Frame.__init__(self, container)
        global localController
        localController = controller
        global font_name
        font_name = 'Mako'
        self.controller = controller

        self.layout = tk.PhotoImage(
            file=r"./image_components/return_and_pay_layout.png")
        self.layout_label = tk.Label(self, image=self.layout)
        self.layout_label.place(relx=0, rely=0)

        self.backButtonArrow = tk.PhotoImage(
            file="./image_components/arrow_alt_left.png")
        self.backButton = ttk.Button(self,
                                     image=self.backButtonArrow, command=lambda: controller.change_frame('purchaseHistory'))
        self.backButton.place(x=10, y=10)
        self.backButton.lift()
         # report button
        self.photoDefect = r"./image_components/report_defect.png"
        self.photoDefect = tk.PhotoImage(file=self.photoDefect)
        self.buttonDefect = tk.Button(self, image=self.photoDefect, compound=tk.TOP,
                                   command=lambda: controller.change_frame('reportDefect'), borderwidth=0, background='#FFFFFF')
        self.buttonDefect.place(x=440, y=10)
        self.buttonDefect.lift()
        # self.order = self.controller.get_selected_order()
        # self.refresh_data()
        self.payblock1_file = r"./image_components/payblock1.png"
        self.payblock1 = tk.PhotoImage(file=self.payblock1_file)
        self.block_dis = tk.Label(self, image=self.payblock1, background='#FFFFFF')
        self.block_dis.place(x=40, y=435)
        # discount
        self.label4 = tk.Label(self, text="Discount:", font=(
            font_name, 14), background='#D9D9D9', anchor="w")
        self.label4.place(x=60, y=442)
        self.label4["justify"] = "left"
        # enter dicount code
        self.disountlabel = tk.Entry(self, text="", font=(
            font_name, 14), background="#D9D9D9", relief="solid")
        self.disountlabel.place(x=65, y=478, width=280, height=40)
        self.enter_discount_image = r"./image_components/paybill_enter.png"
        self.enter_discount = tk.PhotoImage(file=self.enter_discount_image)
        self.button_enterdiscount = tk.Button(self,
                                           image=self.enter_discount, command=self.get_discount, borderwidth=0, background="#D9D9D9")
        self.button_enterdiscount.place(x=360, y=478)


    def refresh_data(self):

        self.order = self.controller.get_selected_order()
        print("Order: ", self.order)

        self.endTimeStr = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.endTime = datetime.strptime(self.endTimeStr, "%Y-%m-%d %H:%M:%S")
        self.order['endTime'] = self.endTimeStr
        self.controller.set_selected_order(order=self.order)
        self.startTime = datetime.strptime(
            self.order['startTime'], "%Y-%m-%d %H:%M:%S")
        # print("dates: ", type(self.startTime), type(self.endTime))
        # self.dateDifference = (self.endTime - self.startTime)
        self.duration = math.ceil(
            (self.endTime - self.startTime).total_seconds() / 3600)

        # print(self.order["income"], type(self.order["income"]))
        if isinstance(self.order["income"], str):
            self.rateByDay = int(self.order["income"])
            self.amount = self.duration * self.rateByDay
        else:
            tk.messagebox.showerror(
                "SERVER ERROR", "SERVER ERROR OCCURED, PLEASE TRY AGAIN LATER")
            return

        print("Amount: ", self.amount, "Duration: ", self.duration)

        self.time_label = tk.Label(
            self, text="Total Time in hours: ", bg="#D9D9D9", font=('Helvetica', 15))
        self.time_label.place(relx=0.15, rely=0.21)
        self.time = tk.Label(self, text=str(self.duration) +
                             " Hours", bg="#D9D9D9", font=('Helvetica', 15))
        self.time.place(relx=0.6, rely=0.21)

        self.name_label = tk.Label(
            self, text="Vehicle Name: ", bg="#D9D9D9", font=('Helvetica', 15))
        self.name_label.place(relx=0.15, rely=0.26)
        self.name = tk.Label(self, text="Tesla Model S",
                             bg="#D9D9D9", font=('Helvetica', 15))
        self.name.place(relx=0.6, rely=0.26)

        self.locations = ['Havannah St.', 'Bath St.', 'Hannover St.',
                          'Argyle St.', 'Helen St.', 'Govan Road', '5 Morefield Rd']
        self.val = tk.StringVar()
        self.val.set(self.locations[0])
        self.locations_drop_down = ttk.Combobox(self, textvariable=self.val, values=self.locations, state="readonly",
                                                font=('Mako', 15), style="CustomStyles.TCombobox")
        self.locations_drop_down.place(
            relx=0.15, rely=0.32, height=42, width=360)
        self.locations_drop_down.bind("<<ComboboxSelected>>", self.on_select)

        # add default return location
        self.order['returnLocation'] = self.val.get()

        self.total_amount_label = tk.Label(
            self, text="Amount: ", bg="#D9D9D9", font=('Helvetica', 15))
        self.total_amount_label.place(relx=0.15, rely=0.4)
        self.total_amount = tk.Label(
            self, text="£" + str(self.amount), bg="#D9D9D9", font=('Helvetica', 15))
        self.total_amount.place(relx=0.6, rely=0.4)

        self.btnImage = tk.PhotoImage(
            file=r"./image_components/return_and_pay_btn.png")
        self.btn = tk.Button(self, image=self.btnImage, compound=tk.TOP, command=self.return_and_pay, borderwidth=0,
                             background='#D9D9D9', activebackground="#D9D9D9")
        self.btn.place(relx=0.04, rely=0.88)
        self.discount_label = tk.Label(
        self, text="Discount: ", bg="#D9D9D9", font=('Helvetica', 15))
        self.discount_label.place(relx=0.15, rely=0.44)
        self.total_discount = tk.Label(
            self, text="£" + str(localController.discount), bg="#D9D9D9", font=('Helvetica', 15))
        self.total_discount.place(relx=0.6, rely=0.44)


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
#         RAPFram = Return_and_pay(container, controller=self)
#         RAPFram.grid(row=0, column=0, sticky="nsew")

#         RAPFram.tkraise()


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()
