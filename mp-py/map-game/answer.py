import turtle


# creates a obj which goes to a loc by using given parameters
class Answer(turtle.Turtle):
    def __init__(self, name, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(f"{name}")
