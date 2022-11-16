from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player1_score = 0
        self.player2_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=-5, y=200)
        self.write(f" {self.player1_score}  {self.player2_score}", move=False, align="center",
                   font=("Arial", 35, "normal"))

    def increment_score(self, scorer):
        if scorer == "player1":
            self.player1_score += 1

        elif scorer == "player2":
            self.player2_score += 1

        self.clear()
        self.write(f" {self.player1_score}  {self.player2_score}", move=False, align="center",
                   font=("Arial", 35, "normal"))

    def is_game_over(self):
        if self.player1_score == 5:
            self.home()
            self.write("Game over Player 1 won")
            return True
        elif self.player2_score == 5:
            self.home()
            self.write("Game over Player 2 won")
            return True
        else:
            return False
