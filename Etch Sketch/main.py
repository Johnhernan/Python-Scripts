import turtle as t
import random

def create_turtles(colors):
    turtle_collection = []
    for _ in range(0, 6):
        turtle = t.Turtle(shape="turtle")
        turtle.color(colors[_])
        turtle.penup()
        turtle_collection.append(turtle)
    return turtle_collection


def move_to_start(turtles):
    y_increment = -130
    for turtle in turtles:
        turtle.goto(x=-230, y=y_increment)
        y_increment += 50


if __name__ == '__main__':
    screen = t.Screen()
    screen.setup(height=400, width=500)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtles = create_turtles(colors)
    move_to_start(turtles)
    winner = ""
    race_is_on = True

    while race_is_on:
        pace = random.randint(0, 10)
        turtle = random.randint(0, 5)

        turtles[turtle].forward(pace)

        if turtles[turtle].xcor() >= 250.0:
            winner = turtles[turtle].color()[1]
            race_is_on = False

    print(f"The race is over! {winner} is the winner!")
    if user_bet == winner:
        print("You won the bet")
    else:
        print("You lost the bet")



    screen.exitonclick()

