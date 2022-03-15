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


# generate circles
tim.speed("fastest")
def draw_circle(gap_size):
    for _ in range(int(360/gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+gap_size)

draw_circle(5)



screen.exitonclick()