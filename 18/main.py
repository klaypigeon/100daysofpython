from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")
tim.color("black")
"""x = 1
while x < 5:
    tim.forward(150)
    tim.right(90)
    x += 1

for _ in range(15):
    tim.forward(10)
    tim.pu()
    tim.forward(10)
    tim.pd()"""
screen = Screen()
angles = [0, 90, 180, 270]
def randomy():
    return random.randint(0, 255)

def angle():
    return random.choice(angles)


screen.colormode(255)

"""for x in range(3,25):
    d = 360/x
    tim.color(randomy(), randomy(), randomy())
    for _ in range(x):
        tim.forward(100)
        tim.right(d)
x = True
tim.width(10)
tim.speed(15)
for _ in range(200):
    tim.color(randomy(), randomy(), randomy())
    tim.forward(30)
    tim.setheading(angle())
"""
tim.speed(15)
tim.width(3)
for x in range(0, 360, 5):
    tim.color(randomy(), randomy(), randomy())
    tim.setheading(x)
    tim.circle(150)



screen.exitonclick()
