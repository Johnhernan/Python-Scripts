from turtle import Screen, Turtle
from player import Player
from scoreboard import Scoreboard
from linetracer import LineTracer
from ball import Ball
import time

if __name__ == '__main__':
    screen = Screen()
    screen.title("Pong")
    screen.setup(width=700, height=500)
    screen.bgcolor("black")
    screen.tracer(0)

    STARTING_POSITIONS = [(-300, 0), (300, 0)]
    player1 = Player(STARTING_POSITIONS[0])
    player2 = Player(STARTING_POSITIONS[1])
    scoreboard = Scoreboard()
    line_tracer = LineTracer()
    ball = Ball()

    # Controls for the paddles
    screen.listen()
    screen.onkeypress(player1.move_up, "w")
    screen.onkeypress(player1.move_down, "s")
    screen.onkeypress(player2.move_up, "Up")
    screen.onkeypress(player2.move_down, "Down")

    app_running = True
    while app_running:
        print("run")
        ball.forward(10)

        # Collision detection for paddles
        if player1.distance(ball) < 20 or player2.distance(ball) < 20:
            ball.on_hit()

        if ball.ycor() > 230 or ball.ycor() < -240:
            ball.on_wall_hit()

        # Scores if Goal is reached
        if ball.xcor() > 330:
            ball.home()
            ball.set_starting_heading()
            scoreboard.increment_score("player1")

        elif ball.xcor() < -330:
            ball.home()
            ball.set_starting_heading()
            scoreboard.increment_score("player2")

        # Checks scores to see if game is over
        if scoreboard.is_game_over():
            app_running = False

        time.sleep(.05)
        screen.update()

    screen.exitonclick()
