import turtle as t
import random

# def get_colors(num_of_colors):
#     colors_extracted = colorgram.extract('200430102527-01-damien-hirst-severed-spots-full-169.jpg',num_of_colors)
#     colors = []
#     for color in colors_extracted:
#         next_color = color.rgb
#         colors.append(next_color)
#     return colors


def switch_colors(tim, new_color):
    tim.pencolor(new_color)


if __name__ == '__main__':

    color_palette = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5),
                     (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165),
                     (229, 17, 121), (73, 9, 31), (60, 14, 8),(224, 141, 211), (10, 97, 61)]

    timmy = t.Turtle()
    t.colormode(255)
    timmy.penup()
    timmy.speed('fastest')
    timmy.sety(-300)
    for y in range(0, 10):
        timmy.setx(-400)
        timmy.left(90)
        timmy.forward(50)
        timmy.right(90)
        for __ in range(0, 100, 10):
            timmy.pencolor(random.choice(color_palette))
            timmy.forward(50)
            timmy.dot(20)



    screen = t.Screen()
    screen.exitonclick()


