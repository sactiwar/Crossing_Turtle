import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Crossing Turtle")
screen.bgcolor("cornsilk")
screen.setup(width=600, height=650)
screen.tracer(0)

p = Player()
car = CarManager()
car.hideturtle()
score = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.obj_move_position()
    for i in car.list_items:
        if i.distance(p) < 20:
            score.game_over()
            game_is_on = False
    if p.reached_destination():
        p.start_new()
        car.level_up_by_one()
        score.increase_level()

screen.exitonclick()