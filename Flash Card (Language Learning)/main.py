from tkinter import PhotoImage, Button, Label, Tk, Canvas
from pandas import read_csv, errors, DataFrame
from random import choice
from gtts import gTTS
from playsound import playsound
from os import remove

BACKGROUND_COLOR = "#B1DDC6"

with open("data/words_to_learn.csv", "a+"):
    try:
        data = read_csv("data/words_to_learn.csv")
    except (FileNotFoundError, errors.EmptyDataError) as e:
        data = read_csv("data/Korean to spanish.csv")
        data.to_csv("data/words_to_learn.csv", columns=None, sep=",", index=None)

data_dict = data.to_dict(orient="records")
one_word = {}


def grab_word_front():
    global one_word, flip_timer
    window.after_cancel(flip_timer)

    language = 'ko'
    one_word = choice(data_dict)
    first_lang = list(one_word.keys())[0]
    french_word = one_word[first_lang]

    canvas.itemconfig(canvas_image, image=front)
    canvas.itemconfig(title, text=first_lang, fill="black")
    canvas.itemconfig(word, text=french_word, fill="black")

    window.update()

    audio_output = gTTS(text=one_word[first_lang], lang=language)
    audio_output.save("english_word.mp3")
    playsound("english_word.mp3", True)
    remove("english_word.mp3")

    flip_timer = window.after(3000, func=grab_word_back)


def grab_word_back():
    language = 'es'
    second_lang = list(one_word.keys())[1]
    english_word = one_word[second_lang]

    canvas.itemconfig(canvas_image, image=back)
    canvas.itemconfig(title, text=second_lang, fill="white")
    canvas.itemconfig(word, text=english_word, fill="white")

    window.update()

    audio_output = gTTS(text=one_word[second_lang], lang=language)
    audio_output.save("french_word.mp3")
    playsound("french_word.mp3", True)
    remove("french_word.mp3")


def ticket_but():
    try:
        index_to_pop = data_dict.index(one_word)
        data_dict.pop(index_to_pop)
        data = DataFrame(data_dict)
        data.to_csv("data/words_to_learn.csv", columns=None, sep=",", index=False)
        grab_word_front()
    except IndexError:
        canvas.itemconfig(title, text="Congrats, all words finished :)", fill="red", font=("arial", 20, "bold"))
        canvas.itemconfig(word, text="These were the 200 most common words in spanish", fill="red",
                          font=("arial", 20, "bold"))
        right.config(state='disabled')
        wrong.config(state="disabled")
        try:
            remove("english_word.mp3")
            remove("french_word.mp3")
        except:
            pass


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=25, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=grab_word_back)

# Main cards canvas
front = PhotoImage(file="images/card_front.png")
back = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=front)
title = canvas.create_text(400, 150, text="", font=("arial", 40, "italic"))
word = canvas.create_text(400, 265, text="", font=("arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Buttons
right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, highlightthickness=0, background=BACKGROUND_COLOR,
               borderwidth=0, command=ticket_but)
right.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, background=BACKGROUND_COLOR, borderwidth=0,
               command=grab_word_front)
wrong.grid(column=0, row=1)

# Label

my_label = Label(text="Created by Matias", highlightthickness=0, background=BACKGROUND_COLOR)
my_label.place(x=750, y=630)

grab_word_front()
window.mainloop()
