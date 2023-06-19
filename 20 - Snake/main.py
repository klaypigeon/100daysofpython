from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
sb = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.15)
    snake.move()

    # detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        sb.add_point()

    # Detect wall collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        sb.reset()
        snake.reset()

    # detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            sb.reset()
            snake.reset()

screen.exitonclick()
