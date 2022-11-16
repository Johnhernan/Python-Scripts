from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=2, stretch_len=.8)
        self.goto(x=position[0], y=position[1])

    def move_up(self):
        if self.ycor() < 240:
            y_increment = self.ycor() + 15
            self.goto(x=self.xcor(), y=y_increment)

    def move_down(self):
        if self.ycor() > -240:
            y_decrement = self.ycor() - 15
            self.goto(x=self.xcor(), y=y_decrement)
