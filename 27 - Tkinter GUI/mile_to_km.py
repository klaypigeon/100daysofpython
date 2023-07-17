from tkinter import *


def convert():
    if miles_input.get() == "q":
        exit(0)
    kms = float(miles_input.get()) * 1.609344
    km_result.config(text=str(kms))



# Creating a new window and configurations
window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

# Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

km_result = Label(text=0)
km_result.grid(column=1, row=1)

# buttons
calc_button = Button(text="Calculate", command=convert)
calc_button.grid(column=1, row=2)

# Inputs
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

window.mainloop()
