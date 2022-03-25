import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
game_on = True
count = 0

guessed_states = []

while game_on:

    # Save the typed state and check if it is on the database

    answer_state = (screen.textinput(title=f"Guess a State. {count}/50", prompt="What state do you chose?")).title()
    estados = pd.read_csv("50_states.csv")
    all_states = estados["state"].to_list()

    if answer_state == "Exit":
        # Code rewritten using list comprehension
        study_state = [state for state in all_states if state not in guessed_states]
       
        break

    for state in all_states:

        if state != answer_state:
            pass
        else:
            chosen_state = estados[estados["state"] == answer_state]
            count += 1
            guessed_states.append(state)

            # Consult state location on the map and write it on the map

            x_cord = int(chosen_state["x"])
            y_cord = int(chosen_state["y"])
            t = turtle.Turtle()
            t.penup()
            t.hideturtle()
            t.goto(x_cord, y_cord)
            t.write(answer_state.title())

# Create a List of states that were not guessed and return a csv file
print(study_state)
study_list = pd.DataFrame(study_state)

study_list.to_csv("study_list.csv")

# screen.exitonclick()
