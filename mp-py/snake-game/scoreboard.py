from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)
        self.hideturtle()

    def update_score(self, point):
        self.score += point
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME IS OVER", align=ALIGN, font=FONT)

    def high_score_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0