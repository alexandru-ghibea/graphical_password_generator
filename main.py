from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

#TODO 1 Password Generator


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_letters + password_numbers
    shuffle(password_list)
    my_password = "".join(password_list)
    password_entry.insert(0, my_password)
    pyperclip.copy(my_password)

#TODO 2 Save Password


def save_password():
    website = entry_website_label.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{email}\nPassword{password}\n Is it ok to save?")
        if is_ok:
            with open("saved_password.txt", "a") as file:
                file.writelines(f'{website}| {email} | {[password]}\n')
                entry_website_label.delete(0, END)
                password_entry.delete(0, END)


#TODO 3 UI Setup

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_user_name_label = Label(text="Email/Username:")
email_user_name_label.grid(column=0, row=2)
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

#Entries
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, string="x@gmail.com")
entry_website_label = Entry(width=35)
entry_website_label.grid(row=1, column=1, columnspan=2)
entry_website_label.focus()
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

#Buttons
add_button = Button(text="Add", width=33, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
window.mainloop()
