from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_numbers + password_symbols + password_letters

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "username": username,
        "password": password
        }
    }
    print(new_data)
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops!', message="Please do not leave any blank information")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
            print("New File getting created")
        else:
            data.update(new_data)

            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("File does not exist")
    else:
        try:
            website = website_entry.get().title()
            username = data[website]["username"]
        except KeyError:
            messagebox.showinfo(title='Oops!', message=f"Data does not exist for {website}")
        else:
            password = data[website]["password"]
            messagebox.showinfo(title=f'{website}', message=f"username: {username}\npassword: {password}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

generate_password_btn = Button(text="Generate Password", command=password_generator)
generate_password_btn.grid(column=2, row=3)

search_button = Button(text="Search", width=12, command=find_password)
search_button.grid(column=2, row=1)

website_entry = Entry(width=18)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, 'mike@mikelossmann.me')

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

add_btn = Button(text="Add", width=33, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
