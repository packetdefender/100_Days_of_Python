from turtle import Turtle
ALIGN = "center"
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("White")
        self.hideturtle()
        self.goto(0, 270)

    def display_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGN, font=FONT)

    def update_score(self):
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game Over!", align=ALIGN, font=FONT)


