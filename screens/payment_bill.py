from tkinter import *
from tkinter import ttk
import tkinter.ttk
#from classes import vehicleHistory
#from classes import Vehicle

class pay_bill_Screen(ttk.Frame):

    def to_profile_page(self):
        print('to profile page')

    def to_consult_page(self):
        print('to consult page')

    def get_discount(self):
        """
        check dicount lib
        if True:
            global percent = ...
            global discount = amount*percent
            refresh the label2
        if Fales:
            discountlabel["text"]="Please check your discount number"
        """
        print('refresh the discount')

    # def turnto_payaccess(self):
    #     self.destroy()
    #     payment_access = pa.pay_access_Screen()
    #     payment_access.mainloop()

    def __init__(self, container, controller):
        super().__init__(container)
        # local variable
        font_name = 'Mako'
        self.styled = tkinter.ttk.Style()
        self.styled.configure("Custom.TFrame", background="white")
        self.style = "Custom.TFrame"
        self.backButtonArrow = PhotoImage(
            file="./image_components/arrow_alt_left.png")
        self.backButton = ttk.Button(self,
                                     image=self.backButtonArrow, command=lambda: controller.change_frame('vehicleDetails'))
        self.backButton.place(x=10, y=10)

        
        self.photoConsult = "./image_components/defect-consult.png"
        self.photoConsult = PhotoImage(file=self.photoConsult)
        self.buttonConsult = Button(self, image=self.photoConsult, compound=TOP,
                                    command=lambda: controller.change_frame('reportDefect'), borderwidth=0, background='#F0F0F0')
        self.buttonConsult.place(x=440, y=20)

        # 4 block
        self.payblock1_file = r"./image_components/payblock1.png"
        self.payblock1 = PhotoImage(file=self.payblock1_file)
        self.block1 = Label(self, image=self.payblock1, background='#F0F0F0')
        self.block1.place(x=40, y=139)
        self.block2 = Label(self, image=self.payblock1, background='#F0F0F0')
        self.block2.place(x=40, y=271)
        self.block3 = Label(self, image=self.payblock1, background='#F0F0F0')
        self.block3.place(x=40, y=403)
        self.block4 = Label(self, image=self.payblock1, background='#F0F0F0')
        self.block4.place(x=40, y=535)

        # text 1: tatal time + distance
        self.label1_left = Label(self, text="Start Location:\nStart Location:", font=(
            font_name, 14), background='#D9D9D9', anchor="w")
        self.label1_left.place(x=60, y=177, width=180)
        self.label1_left["justify"] = "left"

        #from classes get using time and distance
        loc_str = "G4 0AS\nG10 5ED"
        self.label1_right = Label(self, text=loc_str, font=(
            font_name, 14), background='#D9D9D9', anchor="e")
        self.label1_right.place(x=240, y=177, width=180)
        self.label1_right["justify"] = "right"

        # text 2: usage time
        self.label2_left = Label(self, text="Start Time:\nEnd Time:\nUsage Time:", font=(
            font_name, 14), background='#D9D9D9', anchor="w")
        self.label2_left.place(x=60, y=290, width=180)
        self.label2_left["justify"] = "left"
        #time data
        str_fee = str("11\n16\n5")
        self.label2_right = Label(self, text=str_fee, font=(
            font_name, 14), background='#D9D9D9', anchor="e")
        self.label2_right.place(x=240, y=290, width=180)
        self.label2_right["justify"] = "right"

        # text 3:caculate the vehicle fee
        self.label3_left = Label(self, text="Price(h/day/week):\nVehicle fee:\nDiscount:", font=(
            font_name, 14), background='#D9D9D9', anchor="w")
        self.label3_left.place(x=60, y=422, width=180)
        self.label3_left["justify"] = "left"
        #amount
        str_fee = str("50\n3\n0")
        self.label3_right = Label(self, text=str_fee, font=(
            font_name, 14), background='#D9D9D9', anchor="e")
        self.label3_right.place(x=240, y=422, width=180)
        self.label3_right["justify"] = "right"

        # text 4: discount
        self.label4 = Label(self, text="Discount:", font=(
            font_name, 14), background='#D9D9D9', anchor="w")
        self.label4.place(x=60, y=542)
        self.label4["justify"] = "left"
        #enter dicount code
        self.disountlabel = Entry(self, text="", font=(
            font_name, 14), background="#D9D9D9", relief="solid")
        self.disountlabel.place(x=65, y=578, width=280, height=40)
        self.enter_discount_image = r"./image_components/paybill_enter.png"
        self.enter_discount = PhotoImage(file=self.enter_discount_image)
        self.button_enterdiscount = Button(self,
                                           image=self.enter_discount, command=self.get_discount, borderwidth=0, background="#D9D9D9")
        self.button_enterdiscount.place(x=360, y=578)

        # Ground part
        self.paybill_groundblock_file = r"./image_components/paybill_groundblock.png"
        self.paybill_groundblock = PhotoImage(
            file=self.paybill_groundblock_file)
        self.groundblock = Label(self,
                                 image=self.paybill_groundblock, background='#D9D9D9')
        self.groundblock.place(y=667)
        # Text for total fee
        self.label5_left = Label(self, text="Total:", font=(
            font_name, 24, "bold"), background='#D9D9D9', anchor="w", fg="#33AF4E")
        self.label5_left["justify"] = "left"
        self.label5_left.place(x=20, y=673, width=100)
        '''
        total_fee = amount+service_fee-discount
        '''
        str_total = "29.9"
        self.label5_right = Label(self, text=str_total, font=(
            font_name, 24, "bold"), background='#D9D9D9', anchor="w", fg="#33AF4E")
        self.label5_right.place(x=130, y=673)
        # pay button
        self.filepay = r"./image_components/pay_big.png"
        self.photopay = PhotoImage(file=self.filepay)
        self.pay_button = Button(self, image=self.photopay, background='#D9D9D9',
                                 borderwidth=0, compound=TOP, command=lambda:controller.change_frame('paymentAccess'))
        self.pay_button.place(x=20, y=720)

        # top photo
        # select photo according to former page
        # tophoto_file=r"../image_components/pay_car.png"
        self.tophoto_file = r"./image_components/pay_bike.png"
        self.tophoto = PhotoImage(file=self.tophoto_file)
        self.toplabel = Label(self, image=self.tophoto,
                              borderwidth=0, background='#F0F0F0')
        # toplabel.place(x=127,y=65,width=227,height=114)
        self.toplabel.place(x=130, y=57, width=220, height=118)
        # pay_bill_Screen.mainloop()


# if __name__ == '__main__':
#     app = pay_bill_Screen()
#     app.mainloop()
