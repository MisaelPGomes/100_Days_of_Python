import random
import turtle
from turtle import Turtle, Screen
screen = Screen()
tim = Turtle()
# Generate polygons with different random colors

turtle.colormode(255)

def random_color():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# generate random movements and random colors

directions = [0, 90, 180, 270]
tim.pensize(20)
tim.speed("fastest")
for _ in range(200):
    tim.color(random_color())
    tim.forward(100)
    tim.seth(random.choice(directions))






screen.exitonclick()