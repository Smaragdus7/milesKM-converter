from tkinter import *


def convert():
    miles = int(input_miles.get()) * 1.6
    result.config(text=miles)


window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=300, height=350)
window.config(padx=10, pady=10)

input_miles = Entry(width=10)
input_miles.grid(column=1, row=0)

miles_label = Label(text="miles", font=("Candara", 12))
miles_label.grid(column=5, row=0)

eq_label = Label(text="=", font=("Candara", 12))
eq_label.grid(column=6, row=0)

result = Label(text="0", font=("Candara", 12))
result.grid(column=7, row=0)

eq_label = Label(text="Km", font=("Candara", 12))
eq_label.grid(column=8, row=0)

button = Button(text="Convert", command=convert)
button.grid(column=9, row=0)

window.mainloop()
