from sys import argv
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

from passwordgenerator.main import PasswordGeneration
from encryption import PasswordEncryption

FONT_NAME = "Courier"


def clear_input_fields(prefill_user=False):
    input_website.delete(0,'end') 
    input_user.delete(0,'end') 
    input_password.delete(0,'end')

    if prefill_user:
        input_user.insert('end', "fabian.fasth@gmail.com")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password = PasswordGeneration().create_password()
    
    input_password.delete(0,'end')
    input_password.insert('end', password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_website.get()
    user = input_user.get()
    password = input_password.get()
    encrypted_password = encryption.encrypt(input_password.get()).decode()

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        return

    new_data = { website : {"user" : user, "password": encrypted_password}}
    print(new_data)
    try:
        with open("./data.json", mode="r") as file:
            data = json.load(file)
            print(data)
    except FileNotFoundError:
        with open("./data.json", mode="w") as file:
            json.dump(new_data, file, indent=2)
    else:
        with open("./data.json", mode="w") as file:
            data.update(new_data)
            json.dump(data, file, indent=2)
    
    clear_input_fields(True)

def search():
    website = input_website.get()

    if len(website) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave website field empty!")
        return

    try:
        with open("./data.json", mode="r") as file:
            data = json.load(file)

        user = data[website]["user"]
        encrypted = data[website]["password"]
        decrypted = encryption.decrypt(encrypted.encode()).decode()

        clear_input_fields(False)
        input_website.insert('end', website)
        input_user.insert('end', user)
        input_password.insert('end', decrypted)

        pyperclip.copy(decrypted)
    except FileNotFoundError:
        messagebox.showwarning(title="Oops", message="Database not found!")
        clear_input_fields()
    except KeyError:
        messagebox.showwarning(title="Oops", message=f"Entry ({website}) not found!")
        clear_input_fields()


# ------------------------ Encryption SETUP --------------------------- #
key = "1234".encode()
salt = 'SALT'.encode()
encryption = PasswordEncryption(key, salt)
#print(encryption._key)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=20, pady=20)
#window.minsize(width=240, height=240)

logo_img = PhotoImage(file="./logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100,100, image=logo_img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column = 0)

label_user = Label(text="Username/Email:")
label_user.grid(row=2, column = 0)

label_password = Label(text="Password:")
label_password.grid(row=3, column = 0)

input_website = Entry()
input_website.focus()
input_website.config(width=35)
input_website.grid(row=1, column=1, columnspan=2)

input_user = Entry()
input_user.config(width=35)
input_user.insert(END, "fabian.fasth@gmail.com")
input_user.grid(row=2, column=1, columnspan=2)

input_password = Entry()
input_password.config(width=35)
input_password.grid(row=3, column=1, columnspan=2)

button_generate = Button(text="Generate", command=password_generator)
button_generate.grid(row=3, column= 3)

button_add = Button(text="Add", command=save)
button_add.config(width=15)
button_add.grid(row=4, column = 1, columnspan = 1)

button_search = Button(text="Search", command=search)
button_search.config(width=15)
button_search.grid(row=4, column = 2, columnspan = 1)

button_clear = Button(text="Clear", command=clear_input_fields)
button_clear.config(width=15)
button_clear.grid(row=4, column = 3, columnspan = 1)

window.mainloop()
print("good bye!")