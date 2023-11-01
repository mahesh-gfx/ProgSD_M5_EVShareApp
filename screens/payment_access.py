from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class pay_access_Screen(ttk.Frame):

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

    def __init__(self, container, controller):
        super().__init__(container)
        self.controller = controller
        # local variable
        global font_name
        font_name = 'Mako'
        global localController
        localController = controller
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
        self.isenough = False
        self.creditlabel = Label(self, text="Use your credits", font=(
            font_name, 14), background='#F0F0F0', anchor="e")
        self.creditlabel.place(x=75, y=292)
        self.explainlabel = Label(self, text="(100credits=1GBP)", font=(
            2), background='#F0F0F0', anchor="e")
        self.explainlabel.place(x=75, y=315, rely=0)
        total_bill=1
        credit_use = int(100*total_bill)
        credit_str = "credits:" + \
            str(credit_use)+"/"+str(localController.credits)
        if localController.credits >= credit_use:
            self.strcreditlabel = Label(self, text=credit_str, font=(
                font_name, 14), background='#F0F0F0', anchor="e", fg='#33AF4E')
            self.strcreditlabel.config(anchor="w")
            self.isenough = True
        else:
            self.strcreditlabel = Label(self, text=credit_str+"(Not enough)", font=(
                font_name, 14), background='#F0F0F0', anchor="e", fg='red')
            self.strcreditlabel.config(anchor="w")
        self.strcreditlabel.place(x=75, y=340, width=300)

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
        val = StringVar()
        val.set("choose a card")
        self.card_roller = ttk.Combobox(self,
                                        textvariable=val, values=controller.cards, state="readonly", font=(font_name, 14))
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
            if self.have_choose == 1:
                if self.isenough == False:
                    messagebox.showerror(
                        "Zevo | EV Rental", "No Enough Credits")
                else:
                    messagebox.showinfo("Zevo | EV Rental",
                                        "Pay by Credits Successfully")
                    controller.credits -= total_bill*100
                    controller.change_credit(-total_bill*100)
                    controller.change_frame('vehiclesView')
            if self.have_choose == 2:
                if self.card_roller.get() == "":
                    messagebox.showwarning("Zevo | EV Rental", "Select a card")
                else:
                    messagebox.showinfo("Zevo | EV Rental",
                                        "Pay by card Successfully")
                    controller.credits += total_bill
                    controller.change_credit(total_bill)
                    controller.change_frame('vehiclesView')
            if self.have_choose == 3:
                messagebox.showinfo("Zevo | EV Rental",
                                    "Pay by ApplePay Successfully")
                controller.credits += total_bill
                controller.change_credit(total_bill)
                controller.change_frame('vehiclesView')
            if self.have_choose == 4:
                messagebox.showinfo("Zevo | EV Rental",
                                    "Pay by PayPal Successfully")
                controller.credits += total_bill
                controller.change_credit(total_bill)
                controller.change_frame('vehiclesView')

        self.filepay = r"./image_components/pay_big.png"
        self.photopay = PhotoImage(file=self.filepay)
        self.pay_button = Button(self, image=self.photopay, background='#F0F0F0',
                                 borderwidth=0, compound=TOP, command=turnto_payresult)
        self.pay_button.place(x=20, y=720)

    def refresh_data(self):
                # text: bill
        self.bill_left = Label(self, text="Vehicle fee:\nDiscount:", font=(
            font_name, 16), background='#D9D9D9', anchor="w")
        self.bill_left.place(x=60, y=83, width=180)
        self.bill_left["justify"] = "left"

        str_fee = "£" + str(localController.amount)+"\n£"+str(localController.discount)
        self.bill_right = Label(self, text = str_fee, font=(
            font_name, 16), background='#D9D9D9', anchor="e")
        self.bill_right.place(x=240, y=83, width=180)
        self.bill_right["justify"] = "right"
        # total
        self.total_left = Label(self, text="Total:", font=(
            font_name, 20, "bold"), background='#D9D9D9', anchor="w")
        self.total_left.place(x=60, y=160, width=180)
        self.total_left["justify"] = "left"
        # total_bill = amount+service_fee-discount
        global total_bill
        total_bill = localController.amount - localController.discount
        self.total_right = Label(self, text=str(total_bill), font=(
            font_name, 20, "bold"), background='#D9D9D9', anchor="e")
        self.total_right.place(x=240, y=160, width=180)
        self.total_right["justify"] = "right"
        # gain credits mention
        gain_credits = str(total_bill)+" credits"
        self.credit_mention = Label(self, text="you can gain "+gain_credits, font=(
            font_name, 10, "bold"), background='#D9D9D9', anchor="e")
        self.credit_mention["justify"] = "right"
        self.credit_mention.place(x=65, y=200)
    def refresh_cards(self):
        print("Refreshing data on the payment accsee page..")
        localController.get_card()
        localController.get_credit()
        val = StringVar()
        val.set("choose a card")
        self.card_roller = ttk.Combobox(self,
                                        textvariable=val, values=localController.cards, state="readonly", font=(font_name, 14))
        self.option_add("*TCombobox*Listbox*Font", (font_name, 14))
        self.option_add("*TCombobox*Listbox*Background", "white")
        self.card_roller.place(x=75, y=450, width=280, height=30)

        '''get current credits from db'''
        self.isenough = False
        credit_use = int(100*total_bill)
        credit_str = "credits:" + \
            str(credit_use)+"/"+str(localController.credits)
        if localController.credits >= credit_use:
            self.strcreditlabel = Label(self, text=credit_str, font=(
                font_name, 14), background='#F0F0F0', anchor="e", fg='#33AF4E')
            self.strcreditlabel.config(anchor="w")
            self.isenough = True
        else:
            self.strcreditlabel = Label(self, text=credit_str+"(Not enough)", font=(
                font_name, 14), background='#F0F0F0', anchor="e", fg='red')
            self.strcreditlabel.config(anchor="w")
        self.strcreditlabel.place(x=75, y=340, width=300)
