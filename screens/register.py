import tkinter.messagebox as messagebox
from tkinter import *

def register_page():
    win = Tk()
    win.title("Register")
    win.geometry("480x800")
    win.configure(bg="white")

    def handle_signup():
        email = email_entry.get()
        name = name_entry.get()
        phone = phone_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()

        # check if password is valid
        if(len(password)<8 or not any(char.isdigit() for char in password)):
            messagebox.showerror("Password should include at least 1 number and should be longer than 8 !")
            return
        # check if passwords are matched
        elif(password != confirm_password):
            messagebox.showerror("Passwords are not matched")
            return
        elif(email=='' or phone=='' or name==''):
            messagebox.showerror("All fields should be filled")
            return

        print("HEY MAN!")
        # check if email, name, phone are valid strings too
        # check if this email or phone is registered in the DB




    # Signup Layout
    # layout = PhotoImage(file=r"../image_components/sign-up-layout.png")
    # layout_label = Label(image=layout)
    # layout_label.place(relx=0, rely=0)

    email_entry = Entry(win, width=60, font=('Helvetica', 15), highlightthickness=0)
    email_entry.config(borderwidth=0)
    # email_entry.insert(0, "Email")
    email_entry.pack()
    email_entry.place(relx=.16, rely=.235)

    phone_entry = Entry(win, width=60, font=('Helvetica', 15), highlightthickness=0)
    phone_entry.config(borderwidth=0)
    # phone_entry.insert(0, "")
    phone_entry.pack()
    phone_entry.place(relx=.16, rely=.345)

    name_entry = Entry(win, width=60, font=('Helvetica', 15), highlightthickness=0)
    name_entry.config(borderwidth=0)
    # email_entry.insert(0, "Email")
    name_entry.pack()
    name_entry.place(relx=.16, rely=.46)

    password_entry = Entry(win, width=60, font=('Helvetica', 15), highlightthickness=0)
    password_entry.config(borderwidth=0)
    # password_entry.insert(0, "Email")
    password_entry.pack()
    password_entry.place(relx=.16, rely=.575)

    confirm_password_entry = Entry(win, width=60, font=('Helvetica', 15), highlightthickness=0)
    confirm_password_entry.config(borderwidth=0)
    # password_entry.insert(0, "Email")
    confirm_password_entry.pack()
    confirm_password_entry.place(relx=.16, rely=.685)

    # SignupBtnPath = r"../image_components/register-btn.png"
    # SignupBtnPath = PhotoImage(file=SignupBtnPath)
    # buttonSignup = Button(image=SignupBtnPath, compound=TOP, command=handle_signup, borderwidth=0, background='white',
    #                      activebackground="#FFFFFF")
    # buttonSignup.place(x=29, y=655)

    win.mainloop()


register_page()