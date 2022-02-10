import turtle
import pandas

IMAGE = "blank_states_img.gif"
data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.setup(width=900, height=600)
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)





# Repeat with while loop.  Repeat with all states as the variable
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50, States guessed", prompt="What is a State name:").title()
    # Check if answer_state is one of the states in the csv file.
    # if right, how to create turtle to write the name of the state at the state x and y coordinate
    all_states = data.state.to_list()
    if answer_state == "Exit":
        missing_state = []
        for state in all_states:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        # IF you want to use the state data, state_data.state.item()
        guessed_states.append(answer_state)

# states_to_learn.csv
