import turtle
import pandas

IMAGE = "blank_states_img.gif"
data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.setup(width=900, height=600)
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)
screen.tracer(0)



count = 0
while count < 50:

    answer_state = screen.textinput(title=f"{count}/50, Guess the State", prompt="What is a State name:").title()

    if answer_state in data.values:
        state_data = data[data.state == answer_state]
        x_coor, y_coor = int(state_data.x), int(state_data.y)
        state_name = turtle.Turtle()
        state_name.penup()
        state_name.hideturtle()
        state_name.goto(x_coor, y_coor)
        state_name.write(state_data.state.iat[0], font=("Times New Roman", 14, "normal"))
        count += 1






screen.exitonclick()