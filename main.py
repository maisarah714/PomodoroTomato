import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def time_format(second):
    minute = int(second / 60)
    second = second % 60
    time = f"{minute}:"

    if second < 10:
        time += f"0{second}"
    else:
        time += f"{second}"

    return time


def reset_timer():
    global reps, timer
    window.after_cancel(timer)
    title.config(text="Timer", fg=GREEN)
    reps = 1
    canvas.itemconfig(timer_text, text=time_format(WORK_MIN * 60))
    checkmark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps > 8:
        return
    elif reps == 8:
        countdown(long_break_sec)
        title.config(text="Break", fg=RED)
        print(LONG_BREAK_MIN)
    elif reps % 2 == 1:
        countdown(work_sec)
        title.config(text="Work", fg=GREEN)
        print(WORK_MIN)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title.config(text="Break", fg=PINK)
        print(SHORT_BREAK_MIN)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(time):
    global timer
    canvas.itemconfig(timer_text, text=time_format(time))
    if time > 0:
        timer = window.after(1000, countdown, time - 1)
    else:
        start_timer()
        mark = ""
        # i dont understand this part
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark += "✔"
        checkmark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 18, 'bold'), fill='white')
canvas.grid(row=1, column=1)

title = Label(text="Timer", font=(FONT_NAME, 36, "bold"), bg=YELLOW)
title.config(fg=GREEN)
title.grid(row=0, column=1)

start_btn = Button()
start_btn.config(text="Start", font=(FONT_NAME, 12, "normal"))
start_btn.config(command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = Button()
reset_btn.config(text="Reset", font=(FONT_NAME, 12, "normal"))
reset_btn.config(command=reset_timer)
reset_btn.grid(row=2, column=2)

checkmark = Label()
checkmark.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, "normal"))
checkmark.grid(row=3, column=1)

window.mainloop()
