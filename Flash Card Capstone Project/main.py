from tkinter import *
import pandas as pd
import random as r

BACKGROUND_COLOR = "#B1DDC6"
CURRENT_CARD = {}

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    print("No Progress Found, using Words to learn.csv")
    data = pd.read_csv("./data/french_words.csv")

data_dict = data.to_dict(orient='records')


def next_card():
    global CURRENT_CARD, flip_timer
    window.after_cancel(flip_timer)
    CURRENT_CARD = r.choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{CURRENT_CARD['French']}", fill="black")
    canvas.itemconfig(card_img, image=card_front_img)
    flip_timer = window.after(3000, change_card)


def change_card():
    canvas.itemconfig(card_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{CURRENT_CARD['English']}", fill='white')


def correct_card():
    data_dict.remove(CURRENT_CARD)
    print(len(data_dict))
    data = pd.DataFrame(data_dict)
    data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, change_card)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
card_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(column=0, row=0, columnspan=2)
incorrect_button_image = PhotoImage(file="./images/wrong.png")
incorrect_button = Button(image=incorrect_button_image, highlightthickness=0, command=next_card)
incorrect_button.grid(column=0, row=1)
correct_button_image = PhotoImage(file="./images/right.png")
correct_button = Button(image=correct_button_image, highlightthickness=0, command=correct_card)
correct_button.grid(column=1, row=1)

next_card()

window.mainloop()