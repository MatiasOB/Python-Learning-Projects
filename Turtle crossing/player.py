from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
#FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.speed("fastest")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def move_super_up(self):
        self.forward(MOVE_DISTANCE+10)

    def move_super_down(self):
        self.backward(MOVE_DISTANCE+10)
