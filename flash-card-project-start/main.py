from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_title = ("Arial", 20, "italic")
Font_words = ("Arial", 40, "bold")

#------------------------------ Count -----------------------------#



current_card = {}

#------------------------------- Functions ------------------------#
def french():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(word, text=current_card["French"])
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=bg_image_1)
    canvas.itemconfig(word, fill='black')
    flip_timer = window.after(3000, func=english)

def english():
    global current_card
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=bg_image_2)
    canvas.itemconfig(word, text=current_card["English"])
    canvas.itemconfig(word, fill="white")

def known():
    print(current_card)
    data_dict.remove(current_card)
    print(len(data_dict))
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/Words_to_learn.csv", index=False)

    french()

#-------------------------------- CSV -----------------------------#
try:
    data = pandas.read_csv("./data/Words_to_learn.csv")
except:
    original_data = pandas.read_csv("./data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")





print(data_dict)




#------------------------------- UI ---------------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)


flip_timer = window.after(3000, func=english)



bg_image_1 = PhotoImage(file="./images/card_front.png")
canvas_image = canvas.create_image(400, 268, image=bg_image_1)
title = canvas.create_text(400, 160, font=FONT_title, text="French")
word = canvas.create_text(400, 263, font=Font_words, text="potato")
canvas.grid(row=0, column=0, columnspan=2)
bg_image_2 = PhotoImage(file="./images/card_back.png")




right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, border=0, bg=BACKGROUND_COLOR, command=known)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, border=0, bg=BACKGROUND_COLOR, command=french)
wrong_button.grid(row=1, column=0)

french()






window.mainloop()