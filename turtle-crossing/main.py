import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Its the TURTLE GAME!")
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move_fwd, "Up")
car_manager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            print("YOU GOT HIT, SQUISH!!")
            game_is_on = False
            scoreboard.game_over()

    # Detects successful Crossing
    if player.is_at_finish_line():
        scoreboard.update_level()
        player.go_to_start()
        car_manager.level_up()
        print("You hit the top of the game!")


screen.exitonclick()