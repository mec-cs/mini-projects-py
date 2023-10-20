from turtle import Turtle
from food import Food
from scoreboard import Scoreboard

# Snake constants
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
SPEED = 20
COLLISION_DISTANCE = 15

# Directions
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_parts = []
        self.create_snake()
        self.head = self.snake_parts[0]

    def create_snake(self):
        for position in START_POSITION:
            new_part = Turtle("square")
            new_part.color("grey")
            new_part.penup()
            new_part.goto(position)
            self.snake_parts.append(new_part)

    def move(self):
        for order in range(len(self.snake_parts) - 1, 0, -1):
            x = self.snake_parts[order - 1].xcor()
            y = self.snake_parts[order - 1].ycor()
            self.snake_parts[order].goto(x, y)
        self.head.forward(SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def add_part(self):
        x = self.snake_parts[len(self.snake_parts) - 1].xcor()
        y = self.snake_parts[len(self.snake_parts) - 1].ycor()
        new_part = Turtle("square")
        new_part.color("grey")
        new_part.penup()
        new_part.goto(x, y)
        self.snake_parts.append(new_part)

    def collision_food(self, food: Food, sb: Scoreboard, point: int):
        if self.head.distance(food) < COLLISION_DISTANCE:
            food.refresh()
            sb.update_score(point)
            self.add_part()

    def collision_wall(self, sb: Scoreboard):
        if self.head.xcor() > 290 or self.head.xcor() < -300 or self.head.ycor() > 300 or self.head.ycor() < -290:
            sb.game_over()
            return True
        return False

    def collision_byself(self, sb: Scoreboard):
        for part in self.snake_parts[1:]:
            if self.head.distance(part) < 10:
                print("collision by self")
                sb.game_over()
                return True
        return False
