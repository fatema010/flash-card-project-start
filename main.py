from tkinter import *
from tkinter import Canvas, PhotoImage
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
new_card = {}
dict_data = {}
try:
    data = pandas.read_csv("data/word_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Untitled spreadsheet - Sheet1.csv")
    dict_data = original_data.to_dict(orient="records")
else:
    dict_data = data.to_dict(orient="records")


def word_collect():
    global new_card, flip_timer
    window.after_cancel(flip_timer)
    new_card = random.choice(dict_data)
    canvas.itemconfig(title_canvas, text="German", fill="black")
    canvas.itemconfig(word_canvas, text=new_card["GERMAN"], fill="black")
    canvas.itemconfig(first_image, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_canvas, text="English", fill="white")
    canvas.itemconfig(word_canvas, text=new_card["ENGLISH"], fill="white")
    canvas.itemconfig(first_image, image=back_image)


def when_clicked():
    dict_data.remove(new_card)
    word = pandas.DataFrame(dict_data)
    word.to_csv("data/word_learn.csv", index=False)
    word_collect()


window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)
canvas = Canvas(width=800, height=526, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
first_image = canvas.create_image(400, 263, image=front_image)
canvas.config(bg=BACKGROUND_COLOR)
title_canvas = canvas.create_text(400, 150, text="", font=("arial", 40, "italic"))
word_canvas = canvas.create_text(400, 263, text="", font=("arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
button_one = Button(image=right_image, highlightthickness=0, command=when_clicked)
button_two = Button(image=wrong_image, highlightthickness=0, command=word_collect)
button_one.grid(row=1, column=1)
button_two.grid(row=1, column=0)

word_collect()

window.mainloop()
