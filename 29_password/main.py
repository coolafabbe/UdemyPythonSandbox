from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

from passwordgenerator.main import Password

FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    password = Password().create_password()
    
    input_password.delete(0,'end')
    input_password.insert('end', password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_website.get()
    user = input_user.get()
    password = input_password.get()

    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the data:\n  user: {user}\n  password:{password}\nIs it ok to save?")

    if is_ok:
        # with open("./data.json", mode="r") as file:
        #     orginial_data = json.load(file)
        #     print(orginial_data)
        with open("./data.txt", mode="a") as file:
            file.writelines(f"{website}\t{user}\t{password}\n")
        
        input_website.delete(0,'end') 
        input_user.delete(0,'end') 
        input_password.delete(0,'end')

        input_user.insert('end', "fabian.fasth@gmail.com")


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
input_password.config(width=21)
input_password.grid(row=3, column=1)

button_generate = Button(text="Generate", command=password_generator)
button_generate.grid(row=3, column= 2)

button_add = Button(text="Add", command=save)
button_add.config(width=35)
button_add.grid(row=4, column = 1, columnspan = 2)


window.mainloop()