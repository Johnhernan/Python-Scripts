from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

language_text = None
word_text = None
current_image = None
translate_process = None

def next_card():


    canvas.itemconfig(word_text, )


def to_native():
    pass

def to_foreign():
    pass


if __name__ == "__main__":
    window = Tk()
    window.title("Flashcard")
    window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)

    # DataFrames and Lists
    foreign_df = pandas.read_csv("./data/french_words.csv")
    foreign_list = foreign_df["French"].to_list()

    # Images
    front_card = PhotoImage(file="./images/card_front.png")
    back_card = PhotoImage(file="./images/card_back.png")
    right_button_image = PhotoImage(file="./images/right.png")
    wrong_button_image = PhotoImage(file="./images/wrong.png")

    # Canvas Properties
    canvas = Canvas(width=800, height=530, bg=BACKGROUND_COLOR, highlightthickness=0)
    current_image = canvas.create_image(400, 265, image=front_card)
    language_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
    word_text = canvas.create_text(400, 270, text="French", font=("Arial", 60, "bold"))
    canvas.grid(column=0, row=0, columnspan=2)

    # Buttons
    x_button = Button(image=wrong_button_image, highlightthickness=0, bd=0, command=next_card)
    x_button.grid(column=0, row=1)

    check_button = Button(image=right_button_image, highlightthickness=0, bd=0, command=next_card)
    check_button.grid(column=1, row=1)

    window.after(3000, to_native)
    window.mainloop()
