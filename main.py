import turtle
from turtle import Turtle

import pandas

data = pandas.read_csv("50_states.csv")


screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
all_states = data["state"]

guessed_states = []

missed_state = []

def print_state(state_name):
    state_obj = Turtle()
    state_obj.hideturtle()
    state_obj.penup()
    x_location = data[data["state"] == state_name]["x"].iloc[0]
    y_location = data[data["state"] == state_name]["y"].iloc[0]
    state_obj.goto(x_location, y_location)
    state_obj.write(state_name.title())



while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name")
    if answer_state.title() == "Exit":
        for state in all_states:
            if state not in  guessed_states:
                missed_state.append(state)

        df = pandas.DataFrame(missed_state)
        df.to_csv("Missed state")
        break
    for state in all_states:
        if answer_state.lower() == state.lower():
            print_state(state)
            guessed_states.append(answer_state.title())



