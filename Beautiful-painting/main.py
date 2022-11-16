import turtle as t
import random


def walk(tim):
    directions = [0, 90, 180, 270]
    tim.forward(20)
    tim.right(random.choice(directions))


def switch_colors(tim, color):
    tim.pencolor(color)


def generate_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color_tuple = (r, g, b)
    return color_tuple


if __name__ == '__main__':
    timmy = t.Turtle()
    t.colormode(255)
    timmy.speed('fastest')
    timmy.pensize(1)

    for _ in range(500):
        next_color = generate_color()
        switch_colors(timmy, next_color)
        timmy.circle(100)
        timmy.left(3)

    # for _ in range(100):
    #     walk(timmy)
    #     next_color = generate_color()
    #     switch_colors(timmy, next_color)

    # circle_degrees = 360
    # side_count = 3
    # for _ in range(8):
    #     for __ in range(side_count):
    #         timmy.forward(100)
    #         timmy.right(circle_degrees/side_count)
    #     side_count += 1

    screen = t.Screen()
    screen.exitonclick()

