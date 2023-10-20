import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# each meal is 1 point
POINT = 1

# screen settings
wn = Screen()
wn.setup(width=600, height=600)
wn.bgcolor("black")
wn.title("Snake Game with Turtle Library")
wn.tracer(0)  # turn off to move snake smoothly, now .update() must be used to catch the process

snake = Snake()
food = Food()
score = Scoreboard()

wn.listen()
wn.onkey(snake.up, "Up")
wn.onkey(snake.down, "Down")
wn.onkey(snake.left, "Left")
wn.onkey(snake.right, "Right")

game_over = True  # game is active
while game_over:
    wn.update()
    time.sleep(0.1)
    snake.move()
    snake.collision_food(food, score, POINT)

    if snake.collision_wall(score):
        game_over = False

    if snake.collision_byself(score):
        game_over = False



wn.exitonclick()