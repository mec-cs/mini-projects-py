from turtle import Turtle


class Stick(Turtle):
    def __init__(self, xycor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.score = 0
        self.shapesize(stretch_len=1, stretch_wid=10)
        self.penup()
        self.goto(xycor)

    def go_up(self):
        ycoor = self.ycor() + 40
        self.goto(self.xcor(), ycoor)

    def go_down(self):
        ycoor = self.ycor() - 40
        self.goto(self.xcor(), ycoor)
