from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
# -------READ FILE ------


try:
    data = pandas.read_csv(r"data\words_list.csv")
except FileNotFoundError:
    data = pandas.read_csv(r"data\french_words.csv")
    word_dict = data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")

# ----Button commands---
current_word = {}


def next_image():
    global current_word, timer
    window.after_cancel(timer)
    current_word = random.choice(word_dict)
    current_word['French']
    canvas.itemconfig(language_label, text="French", fill="black")
    canvas.itemconfig(word_label, text=current_word['French'], fill="black")
    canvas.itemconfig(card_image, image=front_image)

    timer = window.after(3000, func=change_card)


def already_know():
    word_dict.remove(current_word)
    next_image()

    data = pandas.DataFrame(word_dict)
    data.to_csv(r"data\words_list.csv", index=False)


def change_card():
    canvas.itemconfig(language_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=current_word['English'], fill="white")
    canvas.itemconfig(card_image, image=back_image)

    # -------UI--------


window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
timer = window.after(3000, func=change_card)

canvas = Canvas(width=800, height=526)

front_image = PhotoImage(file=r"images\card_front.png")
back_image = PhotoImage(file=r"images\card_back.png")

card_image = canvas.create_image(400, 263, image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language_label = canvas.create_text(
    400, 150, text="", font=("Ariel", 40, "italic"))
word_label = canvas.create_text(
    400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

correct_image = PhotoImage(file=r"images\right.png")
correct_button = Button(image=correct_image,
                        highlightthickness=0, bg=BACKGROUND_COLOR, command=already_know)
correct_button.grid(column=1, row=1)

wrong_image = PhotoImage(file=r"images\wrong.png")
wrong_button = Button(
    image=wrong_image, highlightthickness=0, command=next_image)

wrong_button.grid(column=0, row=1)
next_image()

window.mainloop()
