from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_choice = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race?  Enter a color: ")
colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple']
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)


if user_choice:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You Won! {winning_color} WON!")
            else:
                print(f"You lost! {winning_color} WON!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()