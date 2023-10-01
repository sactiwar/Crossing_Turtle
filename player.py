from turtle import Turtle,Screen
STARTING_POSITION = (0, -300)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start_new()
        self.setheading(90)
        self.color("black")
        self.listen()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reached_destination(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False

    def start_new(self):
        self.goto(STARTING_POSITION)

    def listen(self):
        screen = Screen()
        screen.listen()
        screen.onkey(key="Up",fun=self.move)
