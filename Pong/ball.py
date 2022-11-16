from turtle import Turtle
import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(.6)
        self.set_starting_heading()

    def set_starting_heading(self):
        direction = random.randint(0, 2)
        if direction == 0:
            self.setheading(0)
        else:
            self.setheading(180)

    def on_hit(self):
        if self.heading() == 0 or self.heading() == 180:
            direction = random.randint(0, 2)
            if direction == 0:
                self.setheading(135)
            else:
                self.setheading(225)

        elif self.xcor() > 1:
            if self.heading() == 45:
                self.setheading(135)
            elif self.heading() == 315:
                self.setheading(225)

        elif self.xcor() < -1:
            if self.heading() == 135:
                self.setheading(45)
            elif self.heading() == 225:
                self.setheading(315)

    def on_wall_hit(self):
        if self.ycor() > 1:
            if self.heading() == 45:
                self.setheading(315)
            elif self.heading() == 135:
                self.setheading(225)

        elif self.ycor() < -1:
            if self.heading() == 225:
                self.setheading(135)
            elif self.heading() == 315:
                self.setheading(45)
