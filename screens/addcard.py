from tkinter import *
import tkinter.ttk
import payment_access


def to_consult_page():
    print('to consult page')


def to_form_page():
    add_card_Screen.destroy()
    payment_access.main()


def save():
    add_card_Screen.destroy()
    payment_access.main()


def numclear(event):
    global enternumber, entername, enterend, entercvv
    if enternumber.get() == "card number":
        enternumber.delete(0, END)
    if entername.get() == "":
        entername.insert(0, "name on card")
    if enterend.get() == "":
        enterend.insert(0, "expires end: DD/MM/YYYY")
    if entercvv.get() == "":
        entercvv.insert(0, "cvv")


def nameclear(event):
    global enternumber, entername, enterend, entercvv
    if entername.get() == "name on card":
        entername.delete(0, END)
    if enternumber.get() == "":
        enternumber.insert(0, "card number")
    if enterend.get() == "":
        enterend.insert(0, "expires end: DD/MM/YYYY")
    if entercvv.get() == "":
        entercvv.insert(0, "cvv")


def endclear(event):
    global enternumber, entername, enterend, entercvv
    if enterend.get() == "expires end: DD/MM/YYYY":
        enterend.delete(0, END)
    if enternumber.get() == "":
        enternumber.insert(0, "card number")
    if entername.get() == "":
        entername.insert(0, "name on card")
    if entercvv.get() == "":
        entercvv.insert(0, "cvv")


def cvvclear(event):
    global enternumber, entername, enterend, entercvv
    if entercvv.get() == "CVV":
        entercvv.delete(0, END)
    if enternumber.get() == "":
        enternumber.insert(0, "card number")
    if entername.get() == "":
        entername.insert(0, "name on card")
    if enterend.get() == "":
        enterend.insert(0, "expires end: DD/MM/YYYY")


def main():

    global add_card_Screen
    font_name = 'Mako'

    add_card_Screen = Tk()
    add_card_Screen.geometry('480x800')
    add_card_Screen.title('Add Card')
    add_card_Screen.configure(background='#FFF')
    add_card_Screen.resizable(False, False)

    # consult button
    photoConsult = "../image_components/defect-consult.png"
    photoConsult = PhotoImage(file=photoConsult)
    buttonConsult = Button(image=photoConsult, compound=TOP,
                           command=to_consult_page, borderwidth=0, background='#FFF')
    buttonConsult.place(x=440, y=20)
    # back button
    photoForm = r"../image_components/pay_backarrow.png"
    photoForm = PhotoImage(file=photoForm)
    buttonForm = Button(image=photoForm, compound=TOP,
                        command=to_form_page, borderwidth=0, background='#FFF')
    buttonForm.place(x=8, y=20)
    # Tittle
    tittlefile = r"../image_components/Your Card Details.png"
    tittlephoto = PhotoImage(file=tittlefile)
    tittle = Label(image=tittlephoto, borderwidth=0, background="#FFF")
    tittle.place(x=38, y=102)
    # mainblock
    mainblockfile = r"../image_components/addcard_main.png"
    mainblock = PhotoImage(file=mainblockfile)
    mainlabel = Label(image=mainblock, borderwidth=0, background="#FFF")
    mainlabel.place(x=40, y=210)
    # 4 text for details
    # card number
    enternumber = Entry(font=(font_name, 14),
                        background="#E8E9E7", borderwidth=0)
    enternumber.place(x=129, y=286, width=270)
    enternumber.insert(0, "card number")
    numclick = enternumber.bind('<Button-1>', numclear)
    # host name
    entername = Entry(font=(font_name, 14),
                      background="#E8E9E7", borderwidth=0)
    entername.place(x=129, y=350, width=270)
    entername.insert(0, "name on card")
    nameclick = entername.bind('<Button-1>', nameclear)
    # expires end
    enterend = Entry(font=(font_name, 14), background="#E8E9E7", borderwidth=0)
    enterend.place(x=129, y=414, width=270)
    enterend.insert(0, "expires end: DD/MM/YYYY")
    endclick = enterend.bind('<Button-1>', endclear)
    # cvv
    entercvv = Entry(font=(font_name, 14), background="#E8E9E7", borderwidth=0)
    entercvv.place(x=129, y=486, width=270)
    entercvv.insert(0, "CVV")
    cvvclick = entercvv.bind('<Button-1>', cvvclear)

    # save button
    filesave = r"../image_components/cardsave.png"
    photosave = PhotoImage(file=filesave)
    save_button = Button(image=photosave, background='#FFF',
                         borderwidth=0, compound=TOP, command=save)
    save_button.place(x=20, y=720)

    add_card_Screen.mainloop()


if __name__ == '__main__':
    main()
