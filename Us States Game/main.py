import turtle as t
import pandas

from scoreboard import Scoreboard
from state_pin import StatePin


if __name__ == "__main__":
    image = "blank_states_img.gif"

    screen = t.Screen()
    screen.title("US Guess ")
    screen.addshape(image)

    t.shape(image)

    states_df = pandas.read_csv("50_states.csv")
    states = states_df["state"]
    scoreboard = Scoreboard()

    app_running = True
    while app_running:

        answer_state = screen.textinput(title="Guess A State", prompt="What's another state's name? ").capitalize()

        if answer_state == "Exit":
            break

        if answer_state in set(states):
            state_found = states_df[states_df["state"] == answer_state]

            state = state_found.state.item()
            x = state_found.x.item()
            y = state_found.y.item()
            position = (x, y)

            state_to_pin = StatePin(state=state, position=position)
            scoreboard.update_score()

            if scoreboard.score == 50:
                app_running = False

        else:
            print("Not found ")

    t.mainloop()
