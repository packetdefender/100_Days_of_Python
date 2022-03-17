from tkinter import *


def miles_to_km():
    km['text'] = round(float(input_miles.get()) * 1.609)


window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

label_equalto = Label(text="is equal to")
label_equalto.grid(column=0, row=1)

km = Label(text="0")
km.grid(column=1, row=1)

input_miles = Entry(width=5)
input_miles.grid(column=1, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

km_label = Label(text="KM")
km_label.grid(column=2, row=1)

button_calc = Button(text="Calculate", command=miles_to_km)
button_calc.grid(column=1, row=2)



window.mainloop()