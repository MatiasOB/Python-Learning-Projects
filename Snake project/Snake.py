
from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTING_POS = [(0,0),(-20,0),(-40,0)]

class Snake:

    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.direction_change = 0


    def create_snake(self):
        for n in STARTING_POS:
            self.add_segment(n)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.direction_change = 0

    def add_segment(self,position):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.segments.append(new_square)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN and self.direction_change < 1:
            self.head.setheading(UP)
            self.direction_change += 1

    def down(self):
        if self.head.heading() != UP and self.direction_change < 1:
            self.head.setheading(DOWN)
            self.direction_change += 1

    def left(self):
        if self.head.heading() != RIGHT and self.direction_change < 1:
            self.head.setheading(LEFT)
            self.direction_change += 1

    def right(self):
        if self.head.heading() != LEFT and self.direction_change < 1:
            self.head.setheading(RIGHT)
            self.direction_change += 1
