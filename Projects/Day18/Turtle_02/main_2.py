import random
from turtle import Turtle, Screen
tim = Turtle()
tim.color("green")

# Draw a doted line
for _ in range (15):
    tim.penup()
    tim.forward(10)
    tim.pendown()
    tim.forward(10)
