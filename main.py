from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import csv
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
BACKGROUND_COLOR = "#B1DDC6"
game_is_on = True
timer = None
reps = 0
my_images = []
my_image_number = 0
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(counter=3):
    global timer
    if counter > 0:
        timer = window.after(1000, count_down, counter - 1)
    else:
        window.after_cancel(timer)
        english_word_show()


# ---------------------------- DATA FUNCTIONS ------------------------------- #


# with open("./data/french_words.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
data = pandas.read_csv("./data/french_words.csv")
game_dictionary = {row.French: row.English for (index, row) in data.iterrows()}
# while game_is_on:
keys_list = list(game_dictionary)

french_word = str(keys_list[randint(0, len(keys_list) - 1)])
english_word = game_dictionary[f"{french_word}"]


def french_word_show():
    global french_word
    global english_word
    french_word = str(keys_list[randint(0, len(keys_list) - 1)])
    english_word = game_dictionary[f"{french_word}"]
    canvas.itemconfig(image_on_canvas, image=my_images[0])
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")

    count_down()


def english_word_show():
    global english_word
    canvas.itemconfig(image_on_canvas, image=my_images[1])
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=english_word, fill="white")



def answer_right():
    global french_word
    global english_word
    keys_list.remove(french_word)
    french_word_show()

def answer_wrong():
    french_word_show()





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
#images append to list
card_front_img = my_images.append(PhotoImage(file="./images/card_front.png"))
card_back_img = my_images.append(PhotoImage(file="./images/card_back.png"))
print(len(my_images))
# set first image on canvas
image_on_canvas = canvas.create_image(400, 263, image=my_images[0])



language_text = canvas.create_text(400, 150, text="language", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, command=answer_wrong, bg=BACKGROUND_COLOR, fg=BACKGROUND_COLOR, highlightthickness=0, bd=0)
wrong_button.grid(column=0, row=1)

right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, command=answer_right, bg=BACKGROUND_COLOR, highlightthickness=0, bd=0)
right_button.grid(column=1, row=1)

french_word_show()

mainloop()
