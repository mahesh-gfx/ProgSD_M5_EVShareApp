import tkinter as tk
# from tkinter import  *


# Create the main window
def open_login_pg():
    win = tk.Tk()
    win.title("Login Page")
    win.geometry("480x800")
    win.configure(bg="white")

    # Image at the top
    image_poster = tk.PhotoImage(file="./image_components/poster.png")
    image_label = tk.Label(win, width=480, height=320, bg="white")
    image_label.pack()
    image_label.place(relx=0.5, rely=0)

    # "Login" text
    login_label = tk.Label(win, text="Login", font=("Helvetica", 48), fg="black", bg="white")
    login_label.pack()
    login_label.place(relx=0.5, rely=0.2)

    # Email input field
    email_icon = tk.PhotoImage(file="./image_components/email_icon.png")  # Replace with your email icon
    email_label = tk.Label(win, bg="black")
    email_label.pack()
    email_entry = tk.Entry(win, width=60)
    email_entry.insert(0, "Email")
    email_entry.pack()
    email_entry.place(relx=.1, rely=.5)

    # Password input field
    password_icon = tk.PhotoImage(file="./image_components/email_icon.png")  # Replace with your password icon
    password_label = tk.Label(win, bg="black")
    password_label.pack()
    password_entry = tk.Entry(win, width=60, show="*")
    password_entry.insert(0, "Password")
    password_entry.pack()
    password_entry.place(relx=.1, rely=.6)

    # "Sign up" text
    signup_label = tk.Label(win, text="Sign up", font=("Helvetica", 12), fg="black", bg="white")
    signup_label.pack()
    signup_label.place(relx=.7, rely=.63)

    # Login button
    login_button = tk.Button(win, text="Login", width=40, height=2, borderwidth=0, bg="#33AF4E", fg="white")
    login_button.pack()

    # Center the login button in the X-axis
    login_button.place(relx=0.5, rely=0.9, anchor="center")


if __name__ == "__main__":
    open_login_pg()
