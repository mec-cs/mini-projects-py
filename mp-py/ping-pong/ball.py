from turtle import Turtle
from stick import Stick


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=0.75)
        self.penup()
        self.goto(0, 0)
        self.x = -10
        self.y = -10

    def move(self, stick_l: Stick, stick_r: Stick):
        self.goto(self.xcor() + self.x, self.ycor() + self.y)
        self.wall_collide()
        self.stick_collide(stick_l, stick_r)
        return self.game_over()

    def game_over(self):
        if self.xcor() > 602 or self.xcor() < -610:
            return True

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1

    def wall_collide(self):
        if self.ycor() > 388 or self.ycor() < -378:
            self.bounce_y()

    def stick_collide(self, stick_l: Stick, stick_r: Stick):
        if self.distance(stick_r) < 50 and self.xcor() > 555:
            self.bounce_x()
            stick_r.score += 1
        if self.distance(stick_l) < 50 and self.xcor() < -565:
            self.bounce_x()
            stick_l.score += 1
