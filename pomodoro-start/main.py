from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
window_timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(window_timer)
    timer.config(text="Timer")
    check_mark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN
    short_break_sec = SHORT_BREAK_MIN
    long_break_sec = LONG_BREAK_MIN
    reps += 1

    #if it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break", font=(FONT_NAME, 50), bg=YELLOW, fg=RED)
    #if it's 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break", font=(FONT_NAME, 50), bg=YELLOW, fg=PINK)

    # if it's the 1st/3rd/5th/7th rep:
    else:
        count_down(work_sec)
        timer.config(text="Work", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    int(count_sec)
    if count > 0:
        global window_timer
        window_timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
            check_mark.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomato")
window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

timer = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
timer.grid(column=1, row=0)

tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(101, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark = Label(bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)

#colorhunt to picking color
window.mainloop()