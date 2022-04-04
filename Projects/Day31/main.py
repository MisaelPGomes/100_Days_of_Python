from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
window = Tk()
to_learn = []


# ---------------------------- FLIP CARD ------------------------------- #


def flip_card():
    global current_card

    canvas.itemconfig(canvas_image, image=card_flipped)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")


# ---------------------------- CSV DATA FILE ------------------------------- #


def generate_word():
    global word_text, to_learn, current_card, flip_timer

    window.after_cancel(flip_timer)
    canvas.itemconfig(canvas_image, image=card_front)

    try:
        data = pandas.read_csv("data/words_learn.csv")
        to_learn = data.to_dict(orient="records")
        current_card = random.choice(to_learn)
        canvas.itemconfig(language_text, text="French", fill="black")
        canvas.itemconfig(word_text, text=current_card["French"], fill="black")
        flip_timer = window.after(3000, func=flip_card)

    except:

        original_data = pandas.read_csv("data/french_words.csv")

        to_learn = original_data.to_dict(orient="records")
        current_card = random.choice(to_learn)
        print(current_card["French"])

        canvas.itemconfig(language_text, text="French", fill="black")
        canvas.itemconfig(word_text, text=current_card["French"], fill="black")
        flip_timer = window.after(3000, func=flip_card)

# To be continued...
def know_answer():
    global to_learn, current_card
    # This part of the code removes the word that the user already knows
    # and creates a file with the words to keep learning
    to_learn.remove(current_card)
    to_learn_df = pandas.DataFrame(to_learn)
    to_learn_df.to_csv("data/words_learn.csv", index=False)
    generate_word()


def dont_know_answer():
    generate_word()

# ---------------------------- UI SETUP ------------------------------- #


window.title("Flash Card Game")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_flipped = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)

language_text = canvas.create_text(400, 150, text="", font=("Arial", 40))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 40, "bold"))

canvas.grid(column=0, row=0, columnspan=2)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=know_answer)
right_button.grid(column=0, row=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=dont_know_answer)
wrong_button.grid(column=1, row=1)

generate_word()
flip_timer = window.after(3000, func=flip_card)
window.mainloop()
