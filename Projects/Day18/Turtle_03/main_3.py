import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
# Generate polygons with different random colors

turtle.colormode(255)

def random_color():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range (num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random_color())
    draw_shape(shape_side_n)

screen = Screen()

screen.exitonclick()