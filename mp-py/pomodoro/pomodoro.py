from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer = None
reps = 0


def start_pomodoro():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title.config(text="Short Break", fg=RED)
        count_down(short_break_sec)
    else:
        title.config(text="Work Time", fg=RED)
        count_down(work_sec)


def count_down(count):

    count_min = count // 60
    count_sec = count % 60

    if count_sec > 9:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    else:
        canvas.itemconfig(timer_text, text=f"{count_min}:0{count_sec}")

    if count > 0:
        global timer
        timer = wn.after(1000, count_down, count - 1)
    else:
        start_pomodoro()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "+"
        check_marks.config(text=marks)


def reset_pomodoro():
    wn.after_cancel(timer)
    title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")
    global reps
    reps = 0


# Window Create
wn = Tk()
wn.title("Pomodoro App")
wn.config(width=500, height=400, padx=100, pady=100, bg=YELLOW)

# Title Label
title = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, border=0.0, font=(FONT_NAME, 24, "bold"))
title.grid(column=1, row=0)

# Tomato and Time Show by using Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, border=0.0, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(102, 112, image=tomato)
timer_text = canvas.create_text(103, 132, text="00:00", fill="white", font=(FONT_NAME, 16, "bold italic"))
canvas.grid(column=1, row=1)


# Buttons (start & reset)
start = Button(text="Start", bg=YELLOW, font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=start_pomodoro)
start.grid(column=0, row=2)
reset = Button(text="Reset", bg=YELLOW, font=(FONT_NAME, 12, "bold"), highlightthickness=0, command=reset_pomodoro)
reset.grid(column=2, row=2)


# Check marks
check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

wn.mainloop()
