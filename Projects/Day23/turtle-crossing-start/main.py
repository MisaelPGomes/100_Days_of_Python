import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title("Cross Road Game")
wall = (0, 290)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.move, key="Up")

    # Generate Car
    car_manager.create_car()
    car_manager.move_car()

    if player.distance(wall) < 20:
        scoreboard.pointmaker()
        player.restart()
        car_manager.level_up()


    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
