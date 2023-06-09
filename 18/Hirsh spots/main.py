import turtle

import colorgram
from turtle import Turtle, Screen
import random
turtle.colormode(255)
tim = Turtle()
tim.hideturtle()

# color_list generated using colorgram.py to analyze a Damian Hirsh painting
color_list = [(199, 175, 116), (124, 36, 24), (169, 107, 57), (186, 157, 53), (5, 56, 83), (202, 217, 206), (222, 224, 226), (110, 66, 84), (42, 35, 34), (112, 161, 175), (22, 121, 173), (89, 141, 55), (76, 38, 48), (62, 153, 138), (8, 67, 47), (181, 96, 79), (135, 41, 43), (211, 200, 150), (144, 171, 156), (179, 201, 187), (168, 153, 158), (210, 183, 178), (143, 118, 122), (91, 137, 160), (46, 74, 63), (203, 185, 187), (175, 197, 205), (36, 74, 86)]
height = 10
width = 10
start_x = -(width * 50 / 2)
start_y = -(height * 50 / 2)

tim.pu()
tim.sety(start_y)
tim.setx(start_x)
tim.speed(15)


# My solution was more elegant to this exercise
for x in range(1, height+1):
    for y in range(width):
        tim.pd()
        tim.dot(35, random.choice(color_list))
        tim.pu()
        tim.forward(50)
    tim.setx(start_x)
    tim.sety((start_y + (x * 50)))


screen = Screen()
screen.exitonclick()
