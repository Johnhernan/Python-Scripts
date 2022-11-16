from tkinter import *
from tkinter import messagebox
from random import randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_entry.delete(0, END)
    password_list = [letters[char] for char in range(randint(8, 10))]
    password_list += [symbols[char] for char in range(randint(2, 4))]
    password_list += [numbers[char] for char in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if website == "" or email == "" or password == "":
        messagebox.showerror(title="ERROR", message="Please do not leave any fields empty")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Are these Details Correct?\n\n Website: {website}\n "
                                                              f"Email:{email}\n Password:{password} ")
        if is_ok:
            try:
                with open("pass.json", "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError as error:
                print(f"Password File not found. Creating... ")
                with open("pass.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)

            else:
                with open("pass.json", mode="w") as file:
                    data.update(new_data)
                    json.dump(data, file, indent=4)

            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)
                pyperclip.copy(password)
                website_entry.focus()


# ---------------------------- Website Search ------------------------------- #
def search():
    query = website_entry.get()

    try:
        with open("pass.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError as error:
        print(f"Password file not found. Make an entry to create")

    else:
        try:
            data[query]

        except KeyError:

            messagebox.showinfo(title="Not found", message=f"{query} was not found")

        else:
            messagebox.showinfo(title=query, message=f"Your {query} details are:\n "
                                                        f"\tEmail: {data[query]['email']}\n" 
                                                        f"\tPassword: {data[query]['password']}\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0 )
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# ---- LABELS ----
website_label = Label(text="Website")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)

# ---- ENTRIES ----
website_entry = Entry()
website_entry.focus()
website_entry.grid(column=1, row=1,  sticky="nsew")
email_entry = Entry()
email_entry.grid(column=1, columnspan=2, row=2,  sticky="nsew")
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="nsew")

# ---- BUTTONS ----
generate_password_button = Button(text="Generate Password", command=generate_password,width=25, highlightthickness=0)
generate_password_button.grid(column=2, row=3)

search_button = Button(text="Search",width=25, command=search)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", command=save_password,  highlightthickness=0)
add_button.grid(column=1, row=4, columnspan=3, sticky="nsew", pady=6)

window.mainloop()
