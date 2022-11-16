from car import Car
from turtle import Turtle
import random


class Spawner(Turtle):
    def __init__(self):
        super().__init__()
        self.difficulty = 5
        self.hideturtle()
        self.goto(x=280, y=-230)
        self.setheading(90)
        self.cars = []

    def spawn_car(self):
        if len(self.cars) == 0:
            new_car = Car(self.position())
            self.cars.append(new_car)

        else:
            is_spawning = random.randint(0, 10)
            if is_spawning == 1:
                new_car = Car(self.position())
                self.cars.append(new_car)

    def restart(self):
        self.goto(x=280, y=-230)

    def update_difficulty(self):
        self.difficulty += 2
