from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_level(self):
        self.clear()
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align='Center', font=FONT)