import time
from turtle import Screen, Turtle
from stick import Stick
from ball import Ball
from scoreboard import Scoreboard

wn = Screen()
wn.bgcolor("black")
wn.setup(width=1200, height=800)
wn.title("Ping Pong")
wn.tracer(0)

stick_right = Stick((580, 0))
stick_left = Stick((-590, 0))
ball = Ball()
sb = Scoreboard()

wn.listen()
wn.onkey(stick_right.go_up, "Up")
wn.onkey(stick_right.go_down, "Down")
wn.onkey(stick_left.go_up, "w")
wn.onkey(stick_left.go_down, "s")

game_run = True
while game_run:
    time.sleep(0.05)
    wn.update()
    sb.update_board(stick_right, stick_left)
    if ball.move(stick_left, stick_right):
        game_run = False

wn.exitonclick()
