import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
care_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.go_up, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    care_manager.create_car()
    care_manager.move_car()

    # collision
    for car in care_manager.all_cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False

    # end_game
    if player.ycor() > 280:
        score.increase()
        care_manager.level_up()
        print(care_manager.car_speed)
        player.go_to_start()

screen.exitonclick()
