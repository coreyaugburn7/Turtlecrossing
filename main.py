import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()
    scoreboard.update_level()

    for car in car_manager.all_cars[1:]:
        if player.distance(car) < 15:
            game_is_on = False
            scoreboard.crash()

    if player.ycor() > 280:
        player.player_reset()
        scoreboard.level_up()
        car_manager.increment_cars()
screen.exitonclick()