from tkinter import *
import tkinter.ttk

def to_profile_page():
    print('to profile page')
def to_consult_page():
    print('to consult page')
def use_credits():
    global have_choose
    if have_choose != 1:
        button_credit_choose = Button(image=photoSelect_T,compound=TOP,command=use_credits,borderwidth=0,background='#F2F2F2')
        button_credit_choose.place(x=393,y=318)
        if have_choose == 2:
            button_card_choose = Button(image=photoSelect_F,compound=TOP,command=use_card,borderwidth=0,background='#F2F2F2')
            button_card_choose.place(x=393,y=441)
        elif have_choose == 3:
            button_apple_choose = Button(image=photoSelect_F,compound=TOP,command=use_apple,borderwidth=0,background='#F2F2F2')
            button_apple_choose.place(x=393,y=543)
        else:
            button_paypal_choose = Button(image=photoSelect_F,compound=TOP,command=use_paypal,borderwidth=0,background='#F2F2F2')
            button_paypal_choose.place(x=393,y=623)
        have_choose =1
def use_card():
    global have_choose
    if have_choose != 2:
        button_card_choose = Button(image=photoSelect_T,compound=TOP,command=use_card,borderwidth=0,background='#F2F2F2')
        button_card_choose.place(x=393,y=441)
        if have_choose == 1:
            button_credit_choose = Button(image=photoSelect_F,compound=TOP,command=use_credits,borderwidth=0,background='#F2F2F2')
            button_credit_choose.place(x=393,y=318)
        elif have_choose == 3:
            button_apple_choose = Button(image=photoSelect_F,compound=TOP,command=use_apple,borderwidth=0,background='#F2F2F2')
            button_apple_choose.place(x=393,y=543)
        else:
            button_paypal_choose = Button(image=photoSelect_F,compound=TOP,command=use_paypal,borderwidth=0,background='#F2F2F2')
            button_paypal_choose.place(x=393,y=623)
        have_choose =2
def use_apple():
    global have_choose
    if have_choose != 3:
        button_apple_choose = Button(image=photoSelect_T,compound=TOP,command=use_apple,borderwidth=0,background='#F2F2F2')
        button_apple_choose.place(x=393,y=543)
        if have_choose == 1:
            button_credit_choose = Button(image=photoSelect_F,compound=TOP,command=use_credits,borderwidth=0,background='#F2F2F2')
            button_credit_choose.place(x=393,y=318)
        elif have_choose == 2:
            button_card_choose = Button(image=photoSelect_F,compound=TOP,command=use_card,borderwidth=0,background='#F2F2F2')
            button_card_choose.place(x=393,y=441)
        else:
            button_paypal_choose = Button(image=photoSelect_F,compound=TOP,command=use_paypal,borderwidth=0,background='#F2F2F2')
            button_paypal_choose.place(x=393,y=623)
        have_choose =3
def use_paypal():
    global have_choose
    if have_choose != 4:
        button_paypal_choose = Button(image=photoSelect_T,compound=TOP,command=use_paypal,borderwidth=0,background='#F2F2F2')
        button_paypal_choose.place(x=393,y=623)
        if have_choose == 1:
            button_credit_choose = Button(image=photoSelect_F,compound=TOP,command=use_credits,borderwidth=0,background='#F2F2F2')
            button_credit_choose.place(x=393,y=318)
        elif have_choose == 2:
            button_card_choose = Button(image=photoSelect_F,compound=TOP,command=use_card,borderwidth=0,background='#F2F2F2')
            button_card_choose.place(x=393,y=441)
        else:
            button_apple_choose = Button(image=photoSelect_F,compound=TOP,command=use_apple,borderwidth=0,background='#F2F2F2')
            button_apple_choose.place(x=393,y=543)
        have_choose =4

def turnto_addcard():
    pay_access_Screen.update()
    pay_access_Screen.decaded()
    import addcard


def turnto_payresult():
    print('to pay ending')

def to_form_page():
    pay_access_Screen.update()
    pay_access_Screen.destroy()
    import payment_bill
    


# local variable
font_name = 'Mako'

pay_access_Screen = Tk()
pay_access_Screen.geometry('480x800')
pay_access_Screen.title('Payment Access')
pay_access_Screen.configure(background='#FFF')
pay_access_Screen.resizable(False,False)

#profile button
photoProf= r"../image_components/defect-profile.png"
photoProf = PhotoImage(file=photoProf)
buttonProf= Button(image=photoProf,compound=TOP,command=to_profile_page,borderwidth=0,background='#FFF')
buttonProf.place(x=10,y=20)

# consult button
photoConsult="../image_components/defect-consult.png"
photoConsult = PhotoImage(file=photoConsult)
buttonConsult= Button(image=photoConsult,compound=TOP,command=to_consult_page,borderwidth=0,background='#FFF')
buttonConsult.place(x=440,y=20)

#show bill
payblock2_file = r"../image_components/payblock2.png"
payblock2 = PhotoImage(file=payblock2_file)
topblock=Label(image=payblock2,background='#FFF')
topblock.place(x=40,y=62)
#text: bill
bill_left = Label(text="amount:\nservice fee:\ndiscount:",font=(font_name,16),background='#F2F2F2',anchor="w")
bill_left.place(x=60,y=83,width=180)
bill_left["justify"]="left"
"""
amount = get_amount()
servicefee=get_service_fee()
discount=get_discount()
str_fee=str(a+"\n"+s+"\n"+d)
"""
str_fee = str("50\n3\n0")
bill_right = Label(text=str_fee,font=(font_name,16),background='#F2F2F2',anchor="e")
bill_right.place(x=240,y=83,width=180)
bill_right["justify"]="right"
#total
total_left = Label(text="Total:",font=(font_name,20,"bold"),background='#F2F2F2',anchor="w")
total_left.place(x=60,y=170,width=180)
total_left["justify"]="left"
#total_bill = amount+service_fee-discount
total_bill = 33.99
total_right = Label(text=str(total_bill),font=(font_name,20,"bold"),background='#F2F2F2',anchor="e")
total_right.place(x=240,y=170,width=180)
total_right["justify"]="right"

#payment choice
#bg
payblock3_file = r"../image_components/payblock3.png"
payblock3 = PhotoImage(file=payblock3_file)
mainblock=Label(image=payblock3,background='#FFF')
mainblock.place(x=40,y=256)
#choose button image
photoSelect_T="../image_components/defect-choise-T.png"
photoSelect_T = PhotoImage(file=photoSelect_T)
photoSelect_F="../image_components/defect-choise-F.png"
photoSelect_F = PhotoImage(file=photoSelect_F)
global have_choose
have_choose = 0
#use credits
creditlabel = Label(text="Use your credits",font=(font_name,14),background='#F2F2F2',anchor="e")
creditlabel.place(x=75,y=292)
explainlabel = Label(text="(100credits=1GBP)",font=(2),background='#F2F2F2',anchor="e")
explainlabel.place(x=75,y=315,rely=0)
'''get current credits from db'''
credit_current = 10000
credit_use= int(100*total_bill)
credit_str ="credits:"+str(credit_use)+"/"+str(credit_current)
if credit_current>=credit_use:
    strcreditlabel = Label(text=credit_str,font=(font_name,14),background='#F2F2F2',anchor="e",fg='#33AF4E')
else:
    strcreditlabel = Label(text=credit_str+"(Not enough)",font=(font_name,14),background='#F2F2F2',anchor="e",fg='red')
strcreditlabel.place(x=75,y=340)

button_credit_choose = Button(image=photoSelect_F,compound=TOP,command=use_credits,borderwidth=0,background='#F2F2F2')
button_credit_choose.place(x=393,y=318)

#use cards
cardlabel = Label(text="Use a bank card",font=(font_name,14),background='#F2F2F2',anchor="e")
cardlabel.place(x=75,y=415)
#add a card
fileaddcard=r"../image_components/pay_addcard.png"
addcard = PhotoImage(file=fileaddcard)
addcard_button = Button(image=addcard,background='#F2F2F2',borderwidth=0,compound=TOP,command=turnto_addcard)
addcard_button.place(x=235,y=417)

#choose card
card=[]
#card append from db
card.append("1111 1111 1111")
card.append("2222 2222 2222")
val = StringVar()
val.set("choose a card")
card_roller = tkinter.ttk.Combobox(textvariable=val,values=card,state="readonly",font=(font_name,14))
pay_access_Screen.option_add("*TCombobox*Listbox*Font", (font_name,14))
pay_access_Screen.option_add("*TCombobox*Listbox*Background","#F2F2F2")
card_roller.place(x=75,y=450,width=280,height=30)
combostyle2 = tkinter.ttk.Style()
combostyle2.theme_create('combostyle2', parent='alt',
                        settings={'TCombobox':
                                      {'configure':
                                           {
                                            'foreground': 'black',
                                            'selectforeground':'black',
                                            'selectbackground': '#F2F2F2',
                                            'fieldbackground': '#F2F2F2',             
                                            }}}
                        )
combostyle2.theme_use('combostyle2')

button_card_choose = Button(image=photoSelect_F,compound=TOP,command=use_card,borderwidth=0,background='#F2F2F2')
button_card_choose.place(x=393,y=441)

#choose apple pay
button_apple_choose = Button(image=photoSelect_F,compound=TOP,command=use_apple,borderwidth=0,background='#F2F2F2')
button_apple_choose.place(x=393,y=543)

#choose paypal
button_paypal_choose = Button(image=photoSelect_F,compound=TOP,command=use_paypal,borderwidth=0,background='#F2F2F2')
button_paypal_choose.place(x=393,y=623)


#pay button
filepay=r"../image_components/pay_small.png"
photopay = PhotoImage(file=filepay)
pay_button = Button(image=photopay,background='#FFF',borderwidth=0,compound=TOP,command=turnto_payresult)
pay_button.place(x=40,y=720)
#back
fileback=r"../image_components/pay_back.png"
photoback = PhotoImage(file=fileback)
back_button = Button(image=photoback,background='#FFF',borderwidth=0,compound=TOP,command=to_form_page)
back_button.place(x=279,y=720)

pay_access_Screen.mainloop()

