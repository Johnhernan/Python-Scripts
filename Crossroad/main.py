from turtle import Screen
from player import Player
from spawner import Spawner
from level_count import LevelCount

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)

    player = Player()
    spawner = Spawner()
    level_count = LevelCount()

    # Player Controls
    screen.listen()
    screen.onkey(player.move_up, "Up")
    screen.onkey(player.move_down, "Down")
    screen.onkey(player.move_left, "Left")
    screen.onkey(player.move_right, "Right")

    difficulty = 5
    app_running = True
    while app_running:
        # Keeps spawner in motion and randomly creates cars
        spawner.forward(10)
        spawner.spawn_car()

        # When level is clear
        if player.ycor() > 230:
            level_count.update_level()
            player.restart()
            difficulty += 2

        # Restarts the spawner loop
        if spawner.ycor() > 230:
            spawner.restart()

        for car in spawner.cars:
            # Boundary to remove car from array
            if car.xcor() < -330:
                car.hideturtle()
                spawner.cars.remove(car)
            # Accelerates cars at the speed of current difficulty
            if car:
                car.forward(difficulty)
            # Collision detection for car
            if player.distance(car) < 30:
                app_running = False

    level_count.game_over()
    screen.exitonclick()
