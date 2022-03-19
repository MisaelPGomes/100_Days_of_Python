from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

scoreboard = Scoreboard()

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Ping Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_movement()

    # Detect Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 340:
            ball.bounce_x()


    # Detect collision with r_paddle
    if ball.distance(l_paddle) < 60 and ball.xcor() < - 340:
            ball.bounce_x()


    # R Paddle misses ball
    if ball.xcor() > 380:
        ball.restart_position()
        ball.bounce_x()
        scoreboard.l_point()


    # R Paddle misses ball
    if ball.xcor() < -380:
        ball.restart_position()
        ball.bounce_x()
        scoreboard.r_point()









screen.exitonclick()