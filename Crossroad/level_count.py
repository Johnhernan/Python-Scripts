from turtle import Turtle


class LevelCount(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.write(f"Level: {self.level}")


    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}")

    def game_over(self):
        self.home()
        self.write(f"Game Over")