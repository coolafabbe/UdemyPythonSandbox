from tkinter import *


def miles_to_km():
    result = float(miles_input.get()) * 1.609
    kilometer_result_label.config(text=str(result))


def func(event):
    miles_to_km()


window = Tk()
window.title("Miles to Kilometer converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)
window.bind('<Return>', func)

miles_input = Entry(width=7)
miles_input.grid(column=1, row= 0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)


kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)


kilometer_label = Label(text="km")
kilometer_label.grid(column=2, row=1)


calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)








window.mainloop()