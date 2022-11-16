from turtle import Turtle


class Car(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.goto(starting_position)
        self.setheading(180)
        self.showturtle()
        self.shape("square")
        self.shapesize(stretch_wid=1.3, stretch_len=2)
        self.starting_position = starting_position




