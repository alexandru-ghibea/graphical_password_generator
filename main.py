from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

#TODO 1 Password Generator


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    new_data = {website: {
        "email": email,
        "password": password,
    }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOPS", message="Please don't leave any fields empty")
    else:
        try:
            with open("saved_password.json", "r") as data_file:
                #reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("saved_password.json", 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            #update date with new data
            data.update(new_data)

            with open("saved_password.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            entry_website_label.delete(0, END)
            password_entry.delete(0, END)


#TODO 3 Search if Website/password exists
def check_if_saved():
    try:
        with open("saved_password.json", "r") as data_file:
            # reading data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=" Website not found")
    else:
        if entry_website_label.get() in data:
            messagebox.showwarning(title=entry_website_label.get(),
                                   message=f"Email: {data[entry_website_label.get()]['email']},"
                                           f"\nPassword:{data[entry_website_label.get()]['password']} ")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {entry_website_label.get()} ")


#TODO 4 UI Setup

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
entry_website_label = Entry(width=21)
entry_website_label.grid(row=1, column=1)
entry_website_label.focus()
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

#Buttons
add_button = Button(text="Add", width=33, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)
generate_password_button = Button(text="Generate Password", width=11,  command=generate_password)
generate_password_button.grid(column=2, row=3)
search_button = Button(text="Search", width=11, command=check_if_saved)
search_button.grid(row=1, column=2)
window.mainloop()
