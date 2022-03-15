import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()

tim.color("red")
#for _ in range(4):
#    tim.forward(100)
#    tim.right(90)

#import heroes
#print(heroes.gen())


# Write doted lines
#for _ in range(15):
#    tim.penup()
#    tim.forward(10)
#    tim.pendown()
#    tim.forward(10)
side = 3
colors = ["dark slate gray", "green yellow", "orange red", "magenta"]

#My_solution

#for _ in range(10):
#    ang = 360/side
#    tim.color(random.choice(colors))
#    for _ in range(side):
#        tim.forward(100)
#        tim.right(ang)
#    side +=1
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def draw_shape(num_sides):

    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


#for shape_side_n in range(3, 11):

#    tim.color(random.choice(colors))
#    draw_shape(shape_side_n)

#coord = [0, 90, 180, 270]
#tim.pensize(10)
#tim.speed("fastest")
#for _ in range(200):
#    tim.color(random_color())
#    tim.forward(30)
#    tim.seth(random.choice(coord))
tim.speed("fastest")


def draw_circle (gap_size):

    for _ in range (int((360/gap_size))):

        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+gap_size)

draw_circle(5)





screen = Screen()
screen.exitonclick()