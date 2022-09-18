from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos):
        super().__init__()
        self.x_pos = x_pos
        self.penup()
        self.speed("fastest")
        self.setpos(self.x_pos, 0)
        self.setheading(90)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)

    def up(self):
        self.setheading(90)
        # self.forward(20)

    def down(self):
        self.setheading(270)
        # self.forward(20)

    def move(self):
        self.forward(20)
        self.collisions()

    def collisions(self):
        if self.ycor() >= 260:
            self.setheading(270)
        elif self.ycor() <= -260:
            self.setheading(90)
