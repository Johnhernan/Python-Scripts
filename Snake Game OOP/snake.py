from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

STARTING_POSITIONS = [(0, 0), (-25, 0), (-45, 0)]
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.create_segment(position)

    def create_segment(self, position):
        segment = Turtle()
        segment.color("white")
        segment.shape("square")
        segment.speed("fast")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.create_segment(self.segments[-1].position())

    def move_snake(self):
        snake_index = len(self.segments) - 1
        for seg in range(snake_index, -1, -1):
            if self.segments[seg] == self.segments[0]:
                self.segments[seg].forward(21)
            else:
                self.segments[seg].goto(self.segments[seg - 1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move_up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(90)

    def move_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)

    def move_left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)

    def move_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)
