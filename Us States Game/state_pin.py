from turtle import Turtle


class StatePin(Turtle):
    def __init__(self, state, position):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write(f"{state}", align="center")






