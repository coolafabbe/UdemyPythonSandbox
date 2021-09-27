import tkinter


def button_clicked():
    my_label.config(text=input.get())


window = tkinter.Tk()
window.title("GUI!")
window.minsize(width=500, height=300)
window.config(padx = 20, pady=20)

# Label
my_label = tkinter.Label(text="I'm a label!", font=("Arial", 24, "bold"))
my_label.grid(column=0, row = 0)
my_label.config(padx=5, pady=5)
# my_label["text"] = "new text"
# my_label.config(text="new text, config")


# Button


button = tkinter.Button(text="click me", command=button_clicked)
button.grid(column=1, row = 1)

# Entry
input = tkinter.Entry()
input.insert("end", string="Example text")
input.focus()
input.grid(column=3, row = 2)

new_button = tkinter.Button(text="new button")
new_button.grid(column=2, row = 0)


window.mainloop()