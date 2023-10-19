from tkinter import *
import tkinter.ttk
import payment_access as pa

class add_card_Screen(Tk):
    def to_consult_page(self):
        print('to consult page')
    def to_form_page(self):
        self.destroy()
        payment_access = pa.pay_access_Screen()
        payment_access.mainloop()

    def save(self):
        self.destroy()
        payment_access = pa.pay_access_Screen()
        payment_access.mainloop()

    def numclear(self,event):
        if self.enternumber.get() == "card number":
            self.enternumber.delete(0,END)
        if self.entername.get() == "":
            self.entername.insert(0,"name on card")
        if self.enterend.get() == "":
            self.enterend.insert(0,"expires end: DD/MM/YYYY")
        if self.entercvv.get() == "":
            self.entercvv.insert(0,"cvv") 
    def nameclear(self,event):
        if self.entername.get() == "name on card":
            self.entername.delete(0,END)
        if self.enternumber.get() == "":
            self.enternumber.insert(0,"card number")
        if self.enterend.get() == "":
            self.enterend.insert(0,"expires end: DD/MM/YYYY")
        if self.entercvv.get() == "":
            self.entercvv.insert(0,"cvv") 
    def endclear(self,event):
        if self.enterend.get() == "expires end: DD/MM/YYYY":
            self.enterend.delete(0,END)
        if self.enternumber.get() == "":
            self.enternumber.insert(0,"card number")
        if self.entername.get() == "":
            self.entername.insert(0,"name on card")
        if self.entercvv.get() == "":
            self.entercvv.insert(0,"cvv") 
    def cvvclear(self,event):
        if self.entercvv.get() == "CVV":
            self.entercvv.delete(0,END)
        if self.enternumber.get() == "":
            self.enternumber.insert(0,"card number")
        if self.entername.get() == "":
            self.entername.insert(0,"name on card")
        if self.enterend.get() == "":
            self.enterend.insert(0,"expires end: DD/MM/YYYY")

    def __init__(self):
        super().__init__()
        font_name = 'Mako'
        self.geometry('480x800')
        self.title('Add Card')
        self.configure(background='#FFF')
        self.resizable(False,False)

        # consult button
        self.photoConsult="../image_components/defect-consult.png"
        self.photoConsult = PhotoImage(file=self.photoConsult)
        self.buttonConsult= Button(image=self.photoConsult,compound=TOP,command=self.to_consult_page,borderwidth=0,background='#FFF')
        self.buttonConsult.place(x=440,y=20)
        # back button
        self.photoForm= r"../image_components/pay_backarrow.png"
        self.photoForm = PhotoImage(file=self.photoForm)
        self.buttonForm= Button(image=self.photoForm,compound=TOP,command=self.to_form_page,borderwidth=0,background='#FFF')
        self.buttonForm.place(x=8,y=20)
        #Tittle
        self.tittlefile = r"../image_components/Your Card Details.png"
        self.tittlephoto = PhotoImage(file=self.tittlefile)
        self.tittle = Label(image=self.tittlephoto,borderwidth=0,background="#FFF")
        self.tittle.place(x=38,y=102)
        #mainblock
        self.mainblockfile = r"../image_components/addcard_main.png"
        self.mainblock = PhotoImage(file=self.mainblockfile)
        self.mainlabel =Label(image=self.mainblock,borderwidth=0,background="#FFF")
        self.mainlabel.place(x=40,y=210)
        #4 text for details
        #card number
        self.enternumber=Entry(font=(font_name,14),background="#E8E9E7",borderwidth=0)
        self.enternumber.place(x=129,y=286,width=270)
        self.enternumber.insert(0,"card number")
        numclick =self.enternumber.bind('<Button-1>',self.numclear)
        #host name
        self.entername=Entry(font=(font_name,14),background="#E8E9E7",borderwidth=0)
        self.entername.place(x=129,y=350,width=270)
        self.entername.insert(0,"name on card")
        nameclick =self.entername.bind('<Button-1>',self.nameclear)
        #expires end
        self.enterend=Entry(font=(font_name,14),background="#E8E9E7",borderwidth=0)
        self.enterend.place(x=129,y=414,width=270)
        self.enterend.insert(0,"expires end: DD/MM/YYYY")
        endclick =self.enterend.bind('<Button-1>',self.endclear)
        #cvv
        self.entercvv=Entry(font=(font_name,14),background="#E8E9E7",borderwidth=0)
        self.entercvv.place(x=129,y=486,width=270)
        self.entercvv.insert(0,"CVV")
        cvvclick =self.entercvv.bind('<Button-1>',self.cvvclear)

        # save button
        self.filesave=r"../image_components/cardsave.png"
        self.photosave = PhotoImage(file=self.filesave)
        self.save_button = Button(image=self.photosave,background='#FFF',borderwidth=0,compound=TOP,command=self.save)
        self.save_button.place(x=20,y=720)



if __name__ == '__main__':
    page = add_card_Screen()
    page.mainloop()