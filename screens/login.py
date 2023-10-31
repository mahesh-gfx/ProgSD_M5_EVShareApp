import tkinter as tk
from tkinter import *
from tkinter import messagebox
class login_page(tk.Frame):

    def handle_login(self):
        self.email = self.email_entry.get()
        self.password = self.password_entry.get()
        if self.email == '' or self.password == '':
            from tkinter import messagebox
            messagebox.showinfo("Tips", "Please enter your Name and password")
        else:
            controller1.login(username=self.email,secret=self.password)



    def __init__(self, container, controller):
        tk.Frame.__init__(self, container)
        global controller1
        controller1= controller
        # Login Layout
        self.layout = PhotoImage(file=r"./image_components/login_layout.png")
        self.layout_label = Label(self,image=self.layout)
        self.layout_label.place(relx=0, rely=0)

        self.email_entry = Entry(self,font=('Helvetica', 15), highlightthickness=0,background='white')
        self.email_entry.config(borderwidth=0)
        self.email_entry.pack()
        self.email_entry.place(x = 170,y = 440, width=300)
        self.email_entry.focus()

        self.password_entry = Entry(self,width=60, font=('Helvetica', 15), highlightthickness=0, show="*",background='white')
        self.password_entry.config(borderwidth=0)
        # password_entry.insert(0)
        self.password_entry.pack()
        self.password_entry.place(x = 190,y = 530, width=270)

        # Sign up button
        self.SignBtnPath = r"./image_components/login-signup.png"
        self.SignBtnPath = PhotoImage(file=self.SignBtnPath)
        self.buttonSign = Button(self,image=self.SignBtnPath, compound=TOP, command=lambda: controller.change_frame('register'), borderwidth=0,background='white', activebackground="#FFFFFF")
        self.buttonSign.place(x=380, y=570)

        # Login button
        self.LoginBtnPath = r"./image_components/button-grey.png"
        self.LoginBtnPath = PhotoImage(file=self.LoginBtnPath)
        self.buttonLogin = Button(self,image=self.LoginBtnPath, compound=TOP, command=self.handle_login, borderwidth=0,background='white', activebackground="#FFFFFF")
        self.buttonLogin.place(x=79, y=673)

