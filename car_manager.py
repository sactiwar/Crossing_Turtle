from turtle import Turtle,Screen
import random

COLORS = ["red", "orange", "brown","chocolate","teal","sky blue", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.list_items = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_n = random.randint(1,5)
        if random_n == 1:
            t = Turtle("square")
            t.shapesize(stretch_wid=1, stretch_len=2)
            t.penup()
            t.color(random.choice(COLORS))
            random_cor_y = random.randint(-260, 250)
            t.goto(x=350, y=random_cor_y)
            self.list_items.append(t)

    def obj_move_position(self):
        for i in self.list_items:
            i.backward(self.car_speed)

    def level_up_by_one(self):
            self.car_speed += MOVE_INCREMENT

