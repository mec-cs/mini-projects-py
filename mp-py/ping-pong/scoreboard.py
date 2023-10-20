from turtle import Turtle
from stick import Stick

ALIGN = "center"
FONT = ("Times New Roman", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 370)
        self.hideturtle()

    def update_board(self, stick_r: Stick, stick_l: Stick):
        self.clear()
        self.write(f"Left Score: {stick_l.score}, Right Score: {stick_r.score}", align=ALIGN, font=FONT)
