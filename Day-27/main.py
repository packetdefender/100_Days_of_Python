from tkinter import *


def button_clicked():
    my_label['text'] = input.get()


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)



# Button
button = Button(text="Click Me!", command=button_clicked)
button.grid(column=1, row=1)

button1 = Button(text="New Button!")
button1.grid(column=2, row=0)

# Entry

input = Entry(width=10)
input.grid(column=3, row=3)

window.mainloop()
