from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbol = [choice(symbols) for char in range(randint(2, 4))]
    password_number = [choice(numbers) for char in range(randint(2, 4))]

    password_list = password_letters + password_symbol + password_number
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = name_email_entry.get()
    passwrd = password_entry.get()
    new_data = {
        website: {
            "email" : email,
            "password" : passwrd,
        }
    }

    if len(website) == 0 or len(email)==0 or len(passwrd)==0:
        messagebox.showerror(title="Empty Entries", message="Some fields are empty please fill all the fields and try again")
    else:
        try:
            with open("data.json", "r") as data:
                content = json.load(data)
                content.update(new_data)
        except:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            with open("data.json", "w") as data:
                json.dump(content, data, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_entry.delete(0, "end")
            website_entry.focus()

#---------------------------- FIND PASSWORD ----------------------------#
def find_password():
    web = website_entry.get()

    try:
        with open("data.json", "r") as data:
            content = json.load(data)
    except:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        messagebox.showinfo(title=web, message=f"Email: {content[web]['email']}\n Password: {content[web]['password']}")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=50)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website = Label(text="Website:")
website.grid(row=1, column=0)
website_entry = Entry(width=22)
website_entry.grid(row=1, column=1)
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2)
website_entry.focus()

name_email = Label(text="Email/Username:")
name_email.grid(row=2, column=0)
name_email_entry = Entry(width=38)
name_email_entry.grid(row=2, column=1, columnspan=2)
name_email_entry.insert(0, "misterj435@gmail.com")

password = Label(text="Password:")
password.grid(row=3, column=0)
password_entry = Entry(width=22)
password_entry.grid(row=3, column=1)


gen_pass_button = Button(text="Generate Password", width=13, highlightthickness=0, command=generate_password)
gen_pass_button.grid(row=3, column=2)


add_button = Button(text="Add", width=36, highlightthickness=0, command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()