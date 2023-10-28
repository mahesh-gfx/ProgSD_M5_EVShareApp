import tkinter.messagebox
from tkinter import *

# Create the main window
def open_login_pg():
    win = Tk()
    win.title("Login Page")
    win.geometry("480x800")
    win.configure(bg="white")

    # def handle_input_onclick(event):
    #     print(event)
    #

    def handle_login():
        email = email_entry.get()
        password = password_entry.get()

        if(email == '' or password == ''):
            tkinter.messagebox.showerror("Empty Input", "You should enter email and password")
        else:
            # search by email if not found error message
            # check password(technically it should not be done in that way)
            # if successfull go to main page
            print("email: ", email)
            print("password: ", password)


    # Login Layout
    layout = PhotoImage(file="../image_components/login_layout.png")
    layout_label = Label(image=layout)
    layout_label.place(relx=0, rely=0)

    # Image at the top
    # image_poster = tk.PhotoImage(file="./image_components/poster.png")
    # image_label = tk.Label(win, width=480, height=320, bg="white")
    # image_label.pack()
    # image_label.place(relx=0.5, rely=0)

    # "Login" text
    # login_label = tk.Label(win, text="Login", font=("Helvetica", 48), fg="black", bg="white")
    # login_label.pack()
    # login_label.place(relx=0.5, rely=0.2)

    # Email input field
    # email_icon = tk.PhotoImage(file="../image_components/email_icon.png")  # Replace with your email icon
    # email_label = tk.Label(win, bg="white")
    # email_label.pack()
    # email_label.place(x=0, y=.5)
    email_entry = Entry(win, width=60, font=('Helvetica', 15), highlightthickness=0)
    email_entry.config(borderwidth=0)
    email_entry.insert(0, "Email")
    email_entry.pack()
    email_entry.place(relx=.15, rely=.545)
    # email_entry.bind('<1>', handle_input_onclick)

    # Password input field
    # password_icon = tk.PhotoImage(file="./image_components/email_icon.png")  # Replace with your password icon
    # password_label = tk.Label(win, bg="black")
    # password_label.pack()
    password_entry = Entry(win, width=60, font=('Helvetica', 15), highlightthickness=0, show="*")
    password_entry.config(borderwidth=0)
    # password_entry.insert(0)
    password_entry.pack()
    password_entry.place(relx=.15, rely=.66)

    # "Sign up" text
    # signup_label = tk.Label(win, text="Sign up", font=("Helvetica", 12), fg="black", bg="white")
    # signup_label.pack()
    # signup_label.place(relx=.7, rely=.63)

    # Login button
    LoginBtnPath = r"../image_components/button-grey.png"
    LoginBtnPath = PhotoImage(file=LoginBtnPath)
    buttonLogin = Button(image=LoginBtnPath, compound=TOP, command=handle_login, borderwidth=0,background='white', activebackground="#FFFFFF")
    buttonLogin.place(x=29, y=655)

    win.mainloop()


if __name__ == "__main__":
    open_login_pg()
