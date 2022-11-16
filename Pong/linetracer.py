from turtle import Turtle

class LineTracer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=-240)
        for _ in range(0, 9):
            self.pendown()
            self.goto(x=0, y=self.ycor()+30)
            self.penup()
            self.goto(x=0,  y=self.ycor()+30)
