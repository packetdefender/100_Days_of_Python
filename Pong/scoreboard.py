from turtle import Turtle
ALIGN = "center"
FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("White")
        self.hideturtle()


    def display_score(self):
        self.goto(-100, 200)
        self.write(arg=f"{self.l_score}", align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(arg=f"{self.r_score}", align=ALIGN, font=FONT)

    def update_l_score(self):
        self.clear()
        self.l_score += 1

    def update_r_score(self):
        self.clear()
        self.r_score += 1

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"Game Over!", align=ALIGN, font=FONT)