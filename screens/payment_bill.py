from tkinter import *
from tkinter import ttk
import tkinter.ttk


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

    def get_membership(self):
        global val
        name_membership = val.get()
        print(name_membership)

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

        # profile button
        # self.photoProf = "./image_components/defect-profile.png"
        # self.photoProf = PhotoImage(file=self.photoProf)
        # self.buttonProf = Button(self, image=self.photoProf, compound=TOP,
        #                          command=self.to_profile_page, borderwidth=0, background='#FFF')
        # self.buttonProf.place(x=10, y=20)

        # consult button
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
        self.label1_left = Label(self, text="total time:\ntotal distance:", font=(
            font_name, 14), background='#D9D9D9', anchor="w")
        self.label1_left.place(x=60, y=177, width=180)
        self.label1_left["justify"] = "left"
        '''
        #from database get using time and distance
        clue=str(get_total_time()+"\n"+get_total_distance)
        '''
        clue = str("12:00-3:00(+1)" + "\n" + "9999km")
        self.label1_right = Label(self, text=clue, font=(
            font_name, 14), background='#D9D9D9', anchor="e")
        self.label1_right.place(x=240, y=177, width=180)
        self.label1_right["justify"] = "right"

        # text 2: fee + discount
        self.label2_left = Label(self, text="amount:\nservice fee:\ndiscount:", font=(
            font_name, 14), background='#D9D9D9', anchor="w")
        self.label2_left.place(x=60, y=290, width=180)
        self.label2_left["justify"] = "left"
        """
        amount = get_amount()
        servicefee=get_service_fee()
        discount=get_discount()
        str_fee=str(a+"\n"+s+"\n"+d)
        """
        str_fee = str("50\n3\n0")
        self.label2_right = Label(self, text=str_fee, font=(
            font_name, 14), background='#D9D9D9', anchor="e")
        self.label2_right.place(x=240, y=290, width=180)
        self.label2_right["justify"] = "right"

        # text 3: discount choice
        self.label3 = Label(self, text="Discount:", font=(
            font_name, 14), background='#D9D9D9', anchor="w")
        self.label3.place(x=60, y=410)
        self.label3["justify"] = "left"
        # enter dicount number
        self.disountlabel = Entry(self, text="", font=(
            font_name, 14), background="#D9D9D9", relief="solid")
        self.disountlabel.place(x=65, y=446, width=280, height=40)
        self.enter_discount_image = r"./image_components/paybill_enter.png"
        self.enter_discount = PhotoImage(file=self.enter_discount_image)
        self.button_enterdiscount = Button(self,
                                           image=self.enter_discount, command=self.get_discount, borderwidth=0, background="#D9D9D9")
        self.button_enterdiscount.place(x=360, y=446)

        # text 4: membership
        self.label4 = Label(self, text="Membership:", font=(
            font_name, 14), background='#D9D9D9', anchor="w")
        self.label4.place(x=60, y=542)
        self.label4["justify"] = "left"
        # choose membership
        membership = ["No"]
        # membership append from db
        membership.append("Month for bike")
        membership.append("Year for car")
        self.val = StringVar()
        self.val.set(membership[0])
        self.membership_roller = tkinter.ttk.Combobox(self, textvariable=self.val, values=membership, state="readonly",
                                                      font=(font_name, 14), style="CustomStyles.TCombobox")
        self.option_add("*TCombobox*Listbox*Font", (font_name, 14))
        self.option_add("*TCombobox*Listbox*Background", "white")
        self.membership_roller.place(x=65, y=578, width=280, height=40)
        '''
        self.styled.configure('CustomStyles.TCombobox',
                              foreground='black',
                              selectforeground='black',
                              selectbackground='#D9D9D9',
                              fieldbackground='#D9D9D9')
        '''
        # self.styled.theme_create('combostyle', parent='alt',
        #                         settings={'TCombobox':
        #                                   {'configure':
        #                                    {
        #                                        'foreground': 'black',
        #                                        'selectforeground': 'black',
        #                                        'selectbackground': '#D9D9D9',
        #                                        'fieldbackground': '#D9D9D9',
        #                                    }}}
        #                         )
        # self.styled.theme_use('combostyle')
        # enter membership button

        self.enter_membership_image = r"./image_components/paybill_enter.png"
        self.enter_membership = PhotoImage(file=self.enter_membership_image)
        self.button_entermembership = Button(self,
                                             image=self.enter_membership, command=self.get_membership, borderwidth=0, background="#D9D9D9")
        self.button_entermembership.place(x=360, y=578)
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
