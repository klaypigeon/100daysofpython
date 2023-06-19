from turtle import Turtle, Screen
import random


screen = Screen()

screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win? Enter a color: ")

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

all_turtles = []



for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.speed(15)
    loc = -130 + 40 * (turtle_index+1)
    new_turtle.goto(x=-230, y=loc)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 210:
            if turtle.pencolor() == user_bet:
                print(f"{turtle.pencolor()} wins. Your turtle WON!")
            else:
                print(f"{turtle.pencolor()} wins. You are a LOSER!")
            is_race_on = False



screen.exitonclick()
