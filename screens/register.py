import tkinter.messagebox as messagebox
import tkinter as tk
from tkinter import *
class register_page(tk.Frame):

    def handle_signup(self):
        self.email = self.email_entry.get()
        self.name = self.name_entry.get()
        self.phone = self.phone_entry.get()
        self.password = self.password_entry.get()
        self.confirm_password = self.confirm_password_entry.get()

        # check if password is valid
        if(len(self.password)<8 or not any(char.isdigit() for char in self.password)):
            messagebox.showerror("Password should include at least 1 number and should be longer than 8 !")
            return
        # check if passwords are matched
        elif(self.password != self.confirm_password):
            messagebox.showerror("Passwords are not matched")
            return
        elif(self.email=='' or self.phone=='' or self.name==''):
            messagebox.showerror("All fields should be filled")
            return

        print("HEY MAN!")

    def __init__(self, container, controller):
        tk.Frame.__init__(self, container)
        # Signup Layout
        self.layout = PhotoImage(file=r"./image_components/sign-up-layout.png")
        self.layout_label = Label(self,image=self.layout)
        self.layout_label.place(relx=0, rely=0)

        self.email_entry = Entry(self,width=60, font=('Helvetica', 15), highlightthickness=0)
        self.email_entry.config(borderwidth=0)
        self.email_entry.place(relx=.16, rely=.235)

        self.phone_entry = Entry(self,width=60, font=('Helvetica', 15), highlightthickness=0)
        self.phone_entry.config(borderwidth=0)
        # phone_entry.insert(0, "")
        self.phone_entry.pack()
        self. phone_entry.place(relx=.16, rely=.345)

        self.name_entry = Entry(self,width=60, font=('Helvetica', 15), highlightthickness=0)
        self.name_entry.config(borderwidth=0)
        # email_entry.insert(0, "Email")
        self.name_entry.pack()
        self.name_entry.place(relx=.16, rely=.46)

        self.password_entry = Entry(self,width=60, font=('Helvetica', 15), highlightthickness=0)
        self.password_entry.config(borderwidth=0)
        # password_entry.insert(0, "Email")
        self.password_entry.pack()
        self.password_entry.place(relx=.16, rely=.575)

        self.confirm_password_entry = Entry( self,width=60, font=('Helvetica', 15), highlightthickness=0)
        self.confirm_password_entry.config(borderwidth=0)
        # password_entry.insert(0, "Email")
        self.confirm_password_entry.pack()
        self.confirm_password_entry.place(relx=.16, rely=.685)

        self.SignupBtnPath = r"./image_components/register-btn.png"
        self.SignupBtnPath = PhotoImage(file=self.SignupBtnPath)
        self.buttonSignup = Button(self,image=self.SignupBtnPath, compound=TOP, command=lambda: controller.change_frame('login'), borderwidth=0, background='white',
                             activebackground="#FFFFFF")
        self.buttonSignup.place(x=81, y=654)