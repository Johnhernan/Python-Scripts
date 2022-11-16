from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0

        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("red")
        self.goto(200,200)
        self.write(f"{self.score}/50", align='left', font=('Arial', 20, 'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}/50", align='left', font=('Arial', 20, 'normal'))