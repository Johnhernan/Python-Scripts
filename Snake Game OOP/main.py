from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.move_up, "Up")
    screen.onkey(snake.move_down, "Down")
    screen.onkey(snake.move_left, "Left")
    screen.onkey(snake.move_right, "Right")

    app_running = True
    while app_running:
        screen.update()
        time.sleep(.1)
        snake.move_snake()

        if snake.head.distance(food) < 15:
            snake.extend()
            scoreboard.increase_score()
            scoreboard.update_score()
            food.new_location()

        if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -300 or snake.head.ycor() > 300:
            scoreboard.reset()
            snake.reset()

        for seg in snake.segments[1:]:
            if snake.head.distance(seg) < 10:
                scoreboard.reset()
                snake.reset()

    screen.exitonclick()
