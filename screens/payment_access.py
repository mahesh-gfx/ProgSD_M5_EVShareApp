from tkinter import *
from tkinter import ttk
# import addcard as ac
# import payment_bill as pb


class pay_access_Screen(ttk.Frame):
    def to_profile_page(self):
        print('to profile page')

    def to_consult_page(self):
        print('to consult page')

    def use_credits(self):
        # choose button image

        if self.have_choose != 1:
            self.button_credit_choose = Button(
                image=self.photoSelect_T, compound=TOP, command=self.use_credits, borderwidth=0, background='#F2F2F2')
            self.button_credit_choose.place(x=393, y=318)
            if self.have_choose == 2:
                self.button_card_choose = Button(
                    image=self.photoSelect_F, compound=TOP, command=self.use_card, borderwidth=0, background='#F2F2F2')
                self.button_card_choose.place(x=393, y=441)
            elif self.have_choose == 3:
                self.button_apple_choose = Button(
                    image=self.photoSelect_F, compound=TOP, command=self.use_apple, borderwidth=0, background='#F2F2F2')
                self.button_apple_choose.place(x=393, y=543)
            else:
                self.button_paypal_choose = Button(
                    image=self.photoSelect_F, compound=TOP, command=self.use_paypal, borderwidth=0, background='#F2F2F2')
                self.button_paypal_choose.place(x=393, y=623)
            self.have_choose = 1

    def use_card(self):
        # choose button image
        if self.have_choose != 2:
            self.button_card_choose = Button(
                image=self.photoSelect_T, compound=TOP, command=self.use_card, borderwidth=0, background='#F2F2F2')
            self.button_card_choose.place(x=393, y=441)
            if self.have_choose == 1:
                self.button_credit_choose = Button(
                    image=self.photoSelect_F, compound=TOP, command=self.use_credits, borderwidth=0, background='#F2F2F2')
                self.button_credit_choose.place(x=393, y=318)
            elif self.have_choose == 3:
                self.button_apple_choose = Button(
                    image=self.photoSelect_F, compound=TOP, command=self.use_apple, borderwidth=0, background='#F2F2F2')
                self.button_apple_choose.place(x=393, y=543)
            else:
                self.button_paypal_choose = Button(
                    image=self.photoSelect_F, compound=TOP, command=self.use_paypal, borderwidth=0, background='#F2F2F2')
                self.button_paypal_choose.place(x=393, y=623)
            self.have_choose = 2

    def use_apple(self):
        if self.have_choose != 3:
            self.button_apple_choose = Button(
                image=self.photoSelect_T, compound=TOP, command=self.use_apple, borderwidth=0, background='#F2F2F2')
            self.button_apple_choose.place(x=393, y=543)
            if self.have_choose == 1:
                self.button_credit_choose = Button(
                    image=self.photoSelect_F, compound=TOP, command=self.use_credits, borderwidth=0, background='#F2F2F2')
                self.button_credit_choose.place(x=393, y=318)
            elif self.have_choose == 2:
                self.button_card_choose = Button(
                    image=self.photoSelect_F, compound=TOP, command=self.use_card, borderwidth=0, background='#F2F2F2')
                self.button_card_choose.place(x=393, y=441)
            else:
                self.button_paypal_choose = Button(
                    image=self.photoSelect_F, compound=TOP, command=self.use_paypal, borderwidth=0, background='#F2F2F2')
                self.button_paypal_choose.place(x=393, y=623)
            self.have_choose = 3

    def use_paypal(self):
        if self.have_choose != 4:
            self.button_paypal_choose = Button(
                image=self.photoSelect_T, compound=TOP, command=self.use_paypal, borderwidth=0, background='#F2F2F2')
            self.button_paypal_choose.place(x=393, y=623)
            if self.have_choose == 1:
                self.button_credit_choose = Button(
                    image=self.photoSelect_F, compound=TOP, command=self.use_credits, borderwidth=0, background='#F2F2F2')
                self.button_credit_choose.place(x=393, y=318)
            elif self.have_choose == 2:
                self.button_card_choose = Button(
                    image=self.photoSelect_F, compound=TOP, command=self.use_card, borderwidth=0, background='#F2F2F2')
                self.button_card_choose.place(x=393, y=441)
            else:
                self.button_apple_choose = Button(
                    image=self.photoSelect_F, compound=TOP, command=self.use_apple, borderwidth=0, background='#F2F2F2')
                self.button_apple_choose.place(x=393, y=543)
            self.have_choose = 4

    def turnto_addcard(self):
        self.destroy()
        # addcard = ac.add_card_Screen()
        # addcard.mainloop()

    def turnto_payresult(self):
        print('to pay ending')

    def to_form_page(self):
        self.destroy()
        # pay_bill = pb.pay_bill_Screen()
        # pay_bill.mainloop()

    def __init__(self, container, controller):
        super().__init__(container)
        # local variable
        font_name = 'Mako'

        # profile button
        self.photoProf = r"./image_components/defect-profile.png"
        self.photoProf = PhotoImage(file=self.photoProf)
        self.buttonProf = Button(self, image=self.photoProf, compound=TOP,
                                 command=self.to_profile_page, borderwidth=0, background='#FFF')
        self.buttonProf.place(x=10, y=20)

        # consult button
        self.photoConsult = r"./image_components/defect-consult.png"
        self.photoConsult = PhotoImage(file=self.photoConsult)
        self.buttonConsult = Button(self, image=self.photoConsult, compound=TOP,
                                    command=self.to_consult_page, borderwidth=0, background='#FFF')
        self.buttonConsult.place(x=440, y=20)

        # show bill
        self.payblock2_file = r"./image_components/payblock2.png"
        self.payblock2 = PhotoImage(file=self.payblock2_file)
        self.topblock = Label(self, image=self.payblock2, background='#FFF')
        self.topblock.place(x=40, y=62)
        # text: bill
        self.bill_left = Label(self, text="amount:\nservice fee:\ndiscount:", font=(
            font_name, 16), background='#F2F2F2', anchor="w")
        self.bill_left.place(x=60, y=83, width=180)
        self.bill_left["justify"] = "left"
        """
        amount = get_amount()
        servicefee=get_service_fee()
        discount=get_discount()
        str_fee=str(a+"\n"+s+"\n"+d)
        """
        str_fee = str("50\n3\n0")
        self.bill_right = Label(self, text=str_fee, font=(
            font_name, 16), background='#F2F2F2', anchor="e")
        self.bill_right.place(x=240, y=83, width=180)
        self.bill_right["justify"] = "right"
        # total
        self.total_left = Label(self, text="Total:", font=(
            font_name, 20, "bold"), background='#F2F2F2', anchor="w")
        self.total_left.place(x=60, y=170, width=180)
        self.total_left["justify"] = "left"
        # total_bill = amount+service_fee-discount
        total_bill = 33.99
        self.total_right = Label(self, text=str(total_bill), font=(
            font_name, 20, "bold"), background='#F2F2F2', anchor="e")
        self.total_right.place(x=240, y=170, width=180)
        self.total_right["justify"] = "right"

        # payment choice
        # bg
        self.payblock3_file = r"./image_components/payblock3.png"
        self.payblock3 = PhotoImage(file=self.payblock3_file)
        self.mainblock = Label(self, image=self.payblock3, background='#FFF')
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
            font_name, 14), background='#F2F2F2', anchor="e")
        self.creditlabel.place(x=75, y=292)
        self.explainlabel = Label(self, text="(100credits=1GBP)", font=(
            2), background='#F2F2F2', anchor="e")
        self.explainlabel.place(x=75, y=315, rely=0)
        '''get current credits from db'''
        self.credit_current = 10000
        self.credit_use = int(100*total_bill)
        self.credit_str = "credits:" + \
            str(self.credit_use)+"/"+str(self.credit_current)
        if self.credit_current >= self.credit_use:
            self.strcreditlabel = Label(self, text=self.credit_str, font=(
                font_name, 14), background='#F2F2F2', anchor="e", fg='#33AF4E')
        else:
            self.strcreditlabel = Label(self, text=self.credit_str+"(Not enough)", font=(
                font_name, 14), background='#F2F2F2', anchor="e", fg='red')
        self.strcreditlabel.place(x=75, y=340)

        self.button_credit_choose = Button(self,
                                           image=self.photoSelect_F, compound=TOP, command=self.use_credits, borderwidth=0, background='#F2F2F2')
        self.button_credit_choose.place(x=393, y=318)

        # use cards
        self.cardlabel = Label(self, text="Use a bank card", font=(
            font_name, 14), background='#F2F2F2', anchor="e")
        self.cardlabel.place(x=75, y=415)
        # add a card
        self.fileaddcard = r"./image_components/pay_addcard.png"
        self.addcard = PhotoImage(file=self.fileaddcard)
        self.addcard_button = Button(self, image=self.addcard, background='#F2F2F2',
                                     borderwidth=0, compound=TOP, command=self.turnto_addcard)
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
        self.option_add("*TCombobox*Listbox*Background", "#F2F2F2")
        self.card_roller.place(x=75, y=450, width=280, height=30)
        combostyle2 = ttk.Style()
        combostyle2.theme_create('combostyle2', parent='alt',
                                 settings={'TCombobox':
                                           {'configure':
                                            {
                                                'foreground': 'black',
                                                'selectforeground': 'black',
                                                'selectbackground': '#F2F2F2',
                                                'fieldbackground': '#F2F2F2',
                                            }}}
                                 )
        combostyle2.theme_use('combostyle2')

        self.button_card_choose = Button(self,
                                         image=self.photoSelect_F, compound=TOP, command=self.use_card, borderwidth=0, background='#F2F2F2')
        self.button_card_choose.place(x=393, y=441)

        # choose apple pay
        self.button_apple_choose = Button(self,
                                          image=self.photoSelect_F, compound=TOP, command=self.use_apple, borderwidth=0, background='#F2F2F2')
        self.button_apple_choose.place(x=393, y=543)

        # choose paypal
        self.button_paypal_choose = Button(self,
                                           image=self.photoSelect_F, compound=TOP, command=self.use_paypal, borderwidth=0, background='#F2F2F2')
        self.button_paypal_choose.place(x=393, y=623)

        # pay button
        self.filepay = r"./image_components/pay_small.png"
        self.photopay = PhotoImage(file=self.filepay)
        self.pay_button = Button(self, image=self.photopay, background='#FFF',
                                 borderwidth=0, compound=TOP, command=self.turnto_payresult)
        self.pay_button.place(x=40, y=720)
        # back
        self.fileback = r"./image_components/pay_back.png"
        self.photoback = PhotoImage(file=self.fileback)
        self.back_button = Button(self, image=self.photoback, background='#FFF',
                                  borderwidth=0, compound=TOP, command=self.to_form_page)
        self.back_button.place(x=279, y=720)
