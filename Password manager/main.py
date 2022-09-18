from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_entry.delete(0, END)
    password = []

    [password.append(random.choice(letters)) for n in range(random.randint(8, 10))]
    [password.append(random.choice(numbers)) for n in range(random.randint(2, 4))]
    [password.append(random.choice(symbols)) for n in range(random.randint(2, 4))]

    random.shuffle(password)
    password = "".join(password)

    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)

#---------------------------- Search Function -----------------------------#
def search_function():
    try:
        with open("my_passwords.json", mode="r") as file:
            pass
    except FileNotFoundError:
        with open("my_passwords.json", mode="w") as file:
            messagebox.showinfo(title="Opps", message="No Data File Found")

    else:
        searching = website_entry.get().lower()

    with open("my_passwords.json", mode="r") as file:
        try:
            dicts = json.load(file)
            email_info = dicts[searching]["email"]
            password_info = dicts[searching]["password"]
        except KeyError:
            messagebox.showinfo(title="Opps", message="No information Found for that Website")
        except json.decoder.JSONDecodeError:
            messagebox.showinfo(title="Opps", message="Your Password file is empty")

        else:
            messagebox.showinfo(title=f"{searching}", message=f"Email: {email_info}\nPassword: {password_info}")


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_function():
    getting_info = False

    website = website_entry.get().lower()
    username = username_entry.get()
    pass_word = password_entry.get()
    new_data = {
        website: {
            "email": username,
            "password": pass_word
        }
    }

    if username == "" or website == "" or pass_word == "":
        messagebox.showinfo(title="Opps", message="Please don't leave any empty fields")
    else:
        getting_info = True

    if getting_info:

        website_entry.delete(0, END)
        password_entry.delete(0, END)

        is_ok = messagebox.askokcancel(title="Confirmation",
                                       message=f"These are the details entered: \n\nEmail: {username}"
                                               f" \nPassword: {pass_word} \n\nit is ok to save?")
        if is_ok:

            try:
                with open("my_passwords.json", mode="r") as file:
                    pass
            except FileNotFoundError:
                with open("my_passwords.json", mode="w") as file:
                    json.dump({}, file)

            with open("my_passwords.json", mode="r") as file:
                try:
                    data = json.load(file)
                except json.decoder.JSONDecodeError:
                    data = {}



            with open("my_passwords.json", mode="r") as file:
                # Updating old data with new data
                data.update(new_data)

            with open("my_passwords.json", mode="w") as file:
                # Saving the updated data
                json.dump(data, file, indent=4)

                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# website label
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)
# website_label.config(padx=5, pady=5)

# username label
username_label = Label(text="Email/Username:", bg="white")
username_label.grid(column=0, row=2)

# Password label
password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

# Generate password BUTTON.
gen_pass = Button(text="Generate Password", highlightthickness=0, command=gen_pass)
gen_pass.grid(column=2, row=3)

#Generate Search Button
search =  Button(text="Search", highlightthickness=0, bg="yellow", command=search_function,width=14)
search.grid(column=2, row=1)



# add_button
add_button = Button(text="Add", highlightthickness=0, width=44, command=add_function)
add_button.grid(column=1, row=4, columnspan=2)

# website_entry

website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()

# username_entry
username_entry = Entry(width=52)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "matiasobaid11@gmail.com")

# password_entry
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

window.mainloop()
