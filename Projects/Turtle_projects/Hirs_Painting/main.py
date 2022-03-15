
#import colorgram

#colors= colorgram.extract('image.jpeg', 20)

#rgb_colors = []

#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)

#print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
tim = Turtle()
tim.color("red")
color_list = [(250, 247, 238), (252, 243, 248), (242, 251, 246), (240, 246, 251), (234, 225, 85), (108, 180, 212), (216, 161, 102), (224, 59, 129), (38, 102, 159), (195, 77, 24), (208, 136, 174), (189, 164, 22), (186, 12, 63), (186, 41, 117), (25, 28, 159), (44, 184, 109), (232, 167, 196), (21, 177, 205), (129, 187, 156), (18, 28, 66)]

tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range (1, number_of_dots +1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = Screen()
screen.exitonclick()


