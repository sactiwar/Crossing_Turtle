from turtle import Turtle,Screen
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.LEVEL = 1
        self.penup()
        self.goto(x=0, y=280)
        self.color("BLACK")
        self.write(f"LEVEL {self.LEVEL}", align="center", font=FONT)
        self.hideturtle()

    def increase_level(self):
        self.LEVEL += 1
        self.clear()
        self.write(f"LEVEL {self.LEVEL}", align="center", font=FONT)

    def game_over(self):
        self.penup()
        self.goto(x=0, y=120)
        self.color("black")
        self.write(f"Your final score is: {self.LEVEL}", align="center", font=FONT)
        self.goto(x=0, y=80)
        self.color("black")
        self.write(f" {'GAME OVER'}", align="center", font=FONT)
        self.hideturtle()


