from tkinter import *
import tkinter.ttk
import payment_access

def to_profile_page():
    print('to profile page')
def to_consult_page():
    print('to consult page')
def get_discount():
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
def get_membership():
    global val
    name_membership=val.get()
    print(name_membership)
def turnto_payaccess():
    pay_bill_Screen.destroy()
    payment_access.main()

def main():
    global pay_bill_Screen
    # local variable
    font_name = 'Mako'
    pay_bill_Screen = Tk()

    pay_bill_Screen.geometry('480x800')
    pay_bill_Screen.title('Payment Bill')
    pay_bill_Screen.configure(background='#FFF')
    pay_bill_Screen.resizable(False, False)

    # profile button
    photoProf = r"../image_components/defect-profile.png"
    photoProf = PhotoImage(file=photoProf)
    buttonProf = Button(image=photoProf, compound=TOP, command=to_profile_page, borderwidth=0, background='#FFF')
    buttonProf.place(x=10, y=20)

    # consult button
    photoConsult = "../image_components/defect-consult.png"
    photoConsult = PhotoImage(file=photoConsult)
    buttonConsult = Button(image=photoConsult, compound=TOP, command=to_consult_page, borderwidth=0, background='#FFF')
    buttonConsult.place(x=440, y=20)

    # 4 block
    payblock1_file = r"../image_components/payblock1.png"
    payblock1 = PhotoImage(file=payblock1_file)
    block1 = Label(image=payblock1, background='#FFF')
    block1.place(x=40, y=139)
    block2 = Label(image=payblock1, background='#FFF')
    block2.place(x=40, y=271)
    block3 = Label(image=payblock1, background='#FFF')
    block3.place(x=40, y=403)
    block4 = Label(image=payblock1, background='#FFF')
    block4.place(x=40, y=535)

    # text 1: tatal time + distance
    label1_left = Label(text="total time:\ntotal distance:", font=(font_name, 14), background='#D9D9D9', anchor="w")
    label1_left.place(x=60, y=177, width=180)
    label1_left["justify"] = "left"
    '''
    #from database get using time and distance
    clue=str(get_total_time()+"\n"+get_total_distance)
    '''
    clue = str("12:00-3:00(+1)" + "\n" + "9999km")
    label1_right = Label(text=clue, font=(font_name, 14), background='#D9D9D9', anchor="e")
    label1_right.place(x=240, y=177, width=180)
    label1_right["justify"] = "right"

    # text 2: fee + discount
    label2_left = Label(text="amount:\nservice fee:\ndiscount:", font=(font_name, 14), background='#D9D9D9', anchor="w")
    label2_left.place(x=60, y=290, width=180)
    label2_left["justify"] = "left"
    """
    amount = get_amount()
    servicefee=get_service_fee()
    discount=get_discount()
    str_fee=str(a+"\n"+s+"\n"+d)
    """
    str_fee = str("50\n3\n0")
    label2_right = Label(text=str_fee, font=(font_name, 14), background='#D9D9D9', anchor="e")
    label2_right.place(x=240, y=290, width=180)
    label2_right["justify"] = "right"

    # text 3: discount choice
    label3 = Label(text="Dsicount:", font=(font_name, 14), background='#D9D9D9', anchor="w")
    label3.place(x=60, y=410)
    label3["justify"] = "left"
    # enter dicount number
    disountlabel = Entry(text="", font=(font_name, 14), background="#D9D9D9", relief="solid")
    disountlabel.place(x=65, y=446, width=280, height=40)
    enter_discount_image = r"../image_components/paybill_enter.png"
    enter_discount = PhotoImage(file=enter_discount_image)
    button_enterdiscount = Button(image=enter_discount, command=get_discount, borderwidth=0, background="#D9D9D9")
    button_enterdiscount.place(x=360, y=446)

    # text 4: membership
    label4 = Label(text="Membership:", font=(font_name, 14), background='#D9D9D9', anchor="w")
    label4.place(x=60, y=542)
    label4["justify"] = "left"
    # choose membership
    membership = ["No"]
    # membership append from db
    membership.append("Month for bike")
    membership.append("Year for car")
    val = StringVar()
    val.set(membership[0])
    membership_roller = tkinter.ttk.Combobox(textvariable=val, values=membership, state="readonly",
                                             font=(font_name, 14))
    pay_bill_Screen.option_add("*TCombobox*Listbox*Font", (font_name, 14))
    pay_bill_Screen.option_add("*TCombobox*Listbox*Background", "#A3A3A3")
    membership_roller.place(x=65, y=578, width=280, height=40)
    combostyle = tkinter.ttk.Style()
    combostyle.theme_create('combostyle', parent='alt',
                            settings={'TCombobox':
                                {'configure':
                                    {
                                        'foreground': 'black',
                                        'selectforeground': 'black',
                                        'selectbackground': '#D9D9D9',
                                        'fieldbackground': '#D9D9D9',
                                    }}}
                            )
    combostyle.theme_use('combostyle')
    # enter membership button
    enter_membership_image = r"../image_components/paybill_enter.png"
    enter_membership = PhotoImage(file=enter_membership_image)
    button_entermembership = Button(image=enter_membership, command=get_membership, borderwidth=0, background="#D9D9D9")
    button_entermembership.place(x=360, y=578)
    # Ground part
    paybill_groundblock_file = r"../image_components/paybill_groundblock.png"
    paybill_groundblock = PhotoImage(file=paybill_groundblock_file)
    groundblock = Label(image=paybill_groundblock, background='#D9D9D9')
    groundblock.place(y=667)
    # Text for total fee
    label5_left = Label(text="Total:", font=(font_name, 24, "bold"), background='#D9D9D9', anchor="w", fg="#33AF4E")
    label5_left["justify"] = "left"
    label5_left.place(x=20, y=673, width=100)
    '''
    total_fee = amount+service_fee-discount
    '''
    str_total = "29.9"
    label5_right = Label(text=str_total, font=(font_name, 24, "bold"), background='#D9D9D9', anchor="w", fg="#33AF4E")
    label5_right.place(x=130, y=673)
    # pay button
    filepay = r"../image_components/pay_big.png"
    photopay = PhotoImage(file=filepay)
    pay_button = Button(image=photopay, background='#D9D9D9', borderwidth=0, compound=TOP, command=turnto_payaccess)
    pay_button.place(x=20, y=720)

    # top photo
    # select photo according to former page
    # tophoto_file=r"../image_components/pay_car.png"
    tophoto_file = r"../image_components/pay_bike.png"
    tophoto = PhotoImage(file=tophoto_file)
    toplabel = Label(image=tophoto, borderwidth=0)
    # toplabel.place(x=127,y=65,width=227,height=114)
    toplabel.place(x=130, y=57, width=220, height=118)
    pay_bill_Screen.mainloop()
   
if __name__ == '__main__':
    main()