from tkinter import *
from tkinter import ttk
from tkinter import messagebox




class pay_access_Screen(ttk.Frame):
    def to_profile_page(self):
        print('to profile page')

    def to_consult_page(self):
        print('to consult page')

    def use_credits(self):
        # choose button image

        if self.have_choose != 1:
            self.button_credit_choose = Button(self,
                                               image=self.photoSelect_T, compound=TOP, command=self.use_credits, borderwidth=0, background='#F2F2F2')
            self.button_credit_choose.place(x=393, y=318)
            if self.have_choose == 2:
                self.button_card_choose = Button(self,
                                                 image=self.photoSelect_F, compound=TOP, command=self.use_card, borderwidth=0, background='#F0F0F0')
                self.button_card_choose.place(x=393, y=441)
            elif self.have_choose == 3:
                self.button_apple_choose = Button(self,
                                                  image=self.photoSelect_F, compound=TOP, command=self.use_apple, borderwidth=0, background='#F0F0F0')
                self.button_apple_choose.place(x=393, y=543)
            else:
                self.button_paypal_choose = Button(self,
                                                   image=self.photoSelect_F, compound=TOP, command=self.use_paypal, borderwidth=0, background='#F0F0F0')
                self.button_paypal_choose.place(x=393, y=623)
            self.have_choose = 1

    def use_card(self):
        # choose button image
        if self.have_choose != 2:
            self.button_card_choose = Button(self,
                                             image=self.photoSelect_T, compound=TOP, command=self.use_card, borderwidth=0, background='#F0F0F0')
            self.button_card_choose.place(x=393, y=441)
            if self.have_choose == 1:
                self.button_credit_choose = Button(self,
                                                   image=self.photoSelect_F, compound=TOP, command=self.use_credits, borderwidth=0, background='#F0F0F0')
                self.button_credit_choose.place(x=393, y=318)
            elif self.have_choose == 3:
                self.button_apple_choose = Button(self,
                                                  image=self.photoSelect_F, compound=TOP, command=self.use_apple, borderwidth=0, background='#F0F0F0')
                self.button_apple_choose.place(x=393, y=543)
            else:
                self.button_paypal_choose = Button(self,
                                                   image=self.photoSelect_F, compound=TOP, command=self.use_paypal, borderwidth=0, background='#F0F0F0')
                self.button_paypal_choose.place(x=393, y=623)
            self.have_choose = 2

    def use_apple(self):
        if self.have_choose != 3:
            self.button_apple_choose = Button(self,
                                              image=self.photoSelect_T, compound=TOP, command=self.use_apple, borderwidth=0, background='#F0F0F0')
            self.button_apple_choose.place(x=393, y=543)
            if self.have_choose == 1:
                self.button_credit_choose = Button(self,
                                                   image=self.photoSelect_F, compound=TOP, command=self.use_credits, borderwidth=0, background='#F0F0F0')
                self.button_credit_choose.place(x=393, y=318)
            elif self.have_choose == 2:
                self.button_card_choose = Button(self,
                                                 image=self.photoSelect_F, compound=TOP, command=self.use_card, borderwidth=0, background='#F0F0F0')
                self.button_card_choose.place(x=393, y=441)
            else:
                self.button_paypal_choose = Button(self,
                                                   image=self.photoSelect_F, compound=TOP, command=self.use_paypal, borderwidth=0, background='#F0F0F0')
                self.button_paypal_choose.place(x=393, y=623)
            self.have_choose = 3

    def use_paypal(self):
        if self.have_choose != 4:
            self.button_paypal_choose = Button(self,
                                               image=self.photoSelect_T, compound=TOP, command=self.use_paypal, borderwidth=0, background='#F0F0F0')
            self.button_paypal_choose.place(x=393, y=623)
            if self.have_choose == 1:
                self.button_credit_choose = Button(self,
                                                   image=self.photoSelect_F, compound=TOP, command=self.use_credits, borderwidth=0, background='#F0F0F0')
                self.button_credit_choose.place(x=393, y=318)
            elif self.have_choose == 2:
                self.button_card_choose = Button(self,
                                                 image=self.photoSelect_F, compound=TOP, command=self.use_card, borderwidth=0, background='#F0F0F0')
                self.button_card_choose.place(x=393, y=441)
            else:
                self.button_apple_choose = Button(self,
                                                  image=self.photoSelect_F, compound=TOP, command=self.use_apple, borderwidth=0, background='#F0F0F0')
                self.button_apple_choose.place(x=393, y=543)
            self.have_choose = 4

    def turnto_addcard(self):
        self.destroy()
        # addcard = ac.add_card_Screen()
        # addcard.mainloop()

    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller
        # local variable
        font_name = 'Mako'

        # back button
        self.backButtonArrow = PhotoImage(
            file="./image_components/arrow_alt_left.png")
        self.backButton = ttk.Button(self,
                                     image=self.backButtonArrow,
                                     command=lambda: controller.change_frame('returnAndPay'))
        self.backButton.place(x=10, y=10)

        # report button
        self.photoDefect = r"./image_components/report_defect.png"
        self.photoDefect = PhotoImage(file=self.photoDefect)
        self.buttonDefect = Button(self, image=self.photoDefect, compound=TOP,
                                    command=lambda: controller.change_frame('reportDefect'), borderwidth=0, background='#F0F0F0')
        self.buttonDefect.place(x=440, y=20)

        # show bill
        self.payblock2_file = r"./image_components/payblock2.png"
        self.payblock2 = PhotoImage(file=self.payblock2_file)
        self.topblock = Label(self, image=self.payblock2, background='#F0F0F0')
        self.topblock.place(x=40, y=62)
        # text: bill
        self.bill_left = Label(self, text="Vehicle fee:\nDiscount:", font=(
            font_name, 16), background='#D9D9D9', anchor="w")
        self.bill_left.place(x=60, y=83, width=180)
        self.bill_left["justify"] = "left"
        """
        amount = get_amount()
        servicefee=get_service_fee()
        discount=get_discount()
        str_fee=str(a+"\n"+s+"\n"+d)
        """
        str_fee = str("50\n3")
        self.bill_right = Label(self, text=str_fee, font=(
            font_name, 16), background='#D9D9D9', anchor="e")
        self.bill_right.place(x=240, y=83, width=180)
        self.bill_right["justify"] = "right"
        # total
        self.total_left = Label(self, text="Total:", font=(
            font_name, 20, "bold"), background='#D9D9D9', anchor="w")
        self.total_left.place(x=60, y=160, width=180)
        self.total_left["justify"] = "left"
        # total_bill = amount+service_fee-discount
        self.total_bill = 47
        self.total_right = Label(self, text=str(self.total_bill), font=(
            font_name, 20, "bold"), background='#D9D9D9', anchor="e")
        self.total_right.place(x=240, y=160, width=180)
        self.total_right["justify"] = "right"
        #gain credits mention
        gain_credits = str(self.total_bill)+" credits"
        self.credit_mention = Label(self, text = "you can gain "+gain_credits, font=(
        font_name, 10, "bold"),background='#D9D9D9', anchor="e")
        self.credit_mention["justify"] = "right"
        self.credit_mention.place(x=65, y=200)

        # payment choice
        # bg
        self.payblock3_file = r"./image_components/payblock3.png"
        self.payblock3 = PhotoImage(file=self.payblock3_file)
        self.mainblock = Label(
            self, image=self.payblock3, background='#F0F0F0')
        self.mainblock.place(x=40, y=256)
        # choose button image
        self.photoSelect_T = r"./image_components/defect-choise-T.png"
        self.photoSelect_T = PhotoImage(file=self.photoSelect_T)
        self.photoSelect_F = r"./image_components/defect-choise-F.png"
        self.photoSelect_F = PhotoImage(file=self.photoSelect_F)
        self.photoSelect_T = r"./image_components/defect-choise-T.png"
        self.photoSelect_T = PhotoImage(file=self.photoSelect_T)
        self.have_choose = 0
        # use credits
        self.creditlabel = Label(self, text="Use your credits", font=(
            font_name, 14), background='#F0F0F0', anchor="e")
        self.creditlabel.place(x=75, y=292)
        self.explainlabel = Label(self, text="(100credits=1GBP)", font=(
            2), background='#F0F0F0', anchor="e")
        self.explainlabel.place(x=75, y=315, rely=0)
        '''get current credits from db'''
        self.credit_current = 10000
        self.credit_use = int(100*self.total_bill)
        self.credit_str = "credits:" + \
            str(self.credit_use)+"/"+str(self.credit_current)
        if self.credit_current >= self.credit_use:
            self.strcreditlabel = Label(self, text=self.credit_str, font=(
                font_name, 14), background='#F0F0F0', anchor="e", fg='#33AF4E')
        else:
            self.strcreditlabel = Label(self, text=self.credit_str+"(Not enough)", font=(
                font_name, 14), background='#F0F0F0', anchor="e", fg='red')
        self.strcreditlabel.place(x=75, y=340)

        self.button_credit_choose = Button(self,
                                           image=self.photoSelect_F, compound=TOP, command=self.use_credits, borderwidth=0, background='#F0F0F0')
        self.button_credit_choose.place(x=393, y=318)

        # use cards
        self.cardlabel = Label(self, text="Use a bank card", font=(
            font_name, 14), background='#F0F0F0', anchor="e")
        self.cardlabel.place(x=75, y=415)
        # add a card
        self.fileaddcard = r"./image_components/pay_addcard.png"
        self.addcard = PhotoImage(file=self.fileaddcard)
        self.addcard_button = Button(self, image=self.addcard, background='#F0F0F0',
                                     borderwidth=0, compound=TOP, command=lambda: controller.change_frame('addCard'))
        self.addcard_button.place(x=235, y=417)

        # choose card
        card = []
        # card append from db
        card.append("1111 1111 1111")
        card.append("2222 2222 2222")
        val = StringVar()
        val.set("choose a card")
        self.card_roller = ttk.Combobox(self,
                                        textvariable=val, values=card, state="readonly", font=(font_name, 14))
        self.option_add("*TCombobox*Listbox*Font", (font_name, 14))
        self.option_add("*TCombobox*Listbox*Background", "white")
        self.card_roller.place(x=75, y=450, width=280, height=30)
        

        self.button_card_choose = Button(self,
                                         image=self.photoSelect_F, compound=TOP, command=self.use_card, borderwidth=0, background='#F0F0F0')
        self.button_card_choose.place(x=393, y=441)

        # choose apple pay
        self.button_apple_choose = Button(self,
                                          image=self.photoSelect_F, compound=TOP, command=self.use_apple, borderwidth=0, background='#F0F0F0')
        self.button_apple_choose.place(x=393, y=543)

        # choose paypal
        self.button_paypal_choose = Button(self,
                                           image=self.photoSelect_F, compound=TOP, command=self.use_paypal, borderwidth=0, background='#F0F0F0')
        self.button_paypal_choose.place(x=393, y=623)

        def turnto_payresult():
            messagebox.showinfo("Zevo | EV Rental", "Pay Successfully")
            controller.return_vehicle()
            controller.change_frame('vehiclesView')

        self.filepay = r"./image_components/pay_big.png"
        self.photopay = PhotoImage(file=self.filepay)
        self.pay_button = Button(self, image=self.photopay, background='#F0F0F0',
                                 borderwidth=0, compound=TOP, command=turnto_payresult)
        self.pay_button.place(x=20, y=720)

    def refresh_data(self):
        self.amount = self.controller.get_amount()
        self.total_right.config(text=self.amount)
        self.bill_right.config(text=self.amount)
        self.credit_mention.config(text=self.amount)

