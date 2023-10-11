import tkinter as tk


# Create the main window
def open_login_pg():
    win = tk.Tk()
    win.title("Login Page")
    win.geometry("480x800")
    win.configure(bg="white")

    # Image at the top
    image_label = tk.Label(win, width=480, height=320, bg="white")
    image_label.pack()

    # "Login" text
    login_label = tk.Label(win, text="Login", font=("Helvetica", 48), fg="black", bg="white")
    login_label.pack()

    # Email input field
    # email_icon = tk.PhotoImage(file="email_icon.png")  # Replace with your email icon
    email_label = tk.Label(win, bg="white")
    email_label.pack()
    email_entry = tk.Entry(win, width=30)
    email_entry.insert(0, "Email")
    email_entry.pack()

    # Password input field
    # password_icon = tk.PhotoImage(file="password_icon.png")  # Replace with your password icon
    password_label = tk.Label(win, bg="white")
    password_label.pack()
    password_entry = tk.Entry(win, width=30, show="*")
    password_entry.insert(0, "Password")
    password_entry.pack()

    # "Sign up" text
    signup_label = tk.Label(win, text="Sign up", font=("Helvetica", 12), fg="black", bg="white")
    signup_label.pack()

    # Login button
    login_button = tk.Button(win, text="Login", width=40, height=2, bg="red", fg="black")
    login_button.pack()

    # Center the login button in the X-axis
    login_button.place(relx=0.5, rely=0.9, anchor="center")


if __name__ == "__main__":
    open_login_pg()
