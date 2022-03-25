from turtle import Turtle
import pandas as pd


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

    def store_user_answer(self):
        """Store an answer given by the user"""
        self.answer_state = screen.textinput(title="What state do you chose?", prompt="")

    def search_state(self):
        self.estados = pd.read_csv("50_states.csv")
        self.chosen_state = self.estados[self.estados["state"] == self.answer_state]

    def state_coord(self):
        x_coord = self.chosen_state["x"]
        y_coord = self.chosen_state["y"]

    def new_state(self):
        self.new_state = State()
        self.new_state.penup()



chosen_state = estados[estados["state"] == chosen]
print(chosen_state)

