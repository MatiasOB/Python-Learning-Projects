from turtle import Turtle

paddle2_POS = [(380, 40), (380, 20), (380, 0), (380, -20), (380, -40)]
paddle1_POS = [(-380, 40), (-380, 20), (-380, 0), (-380, -20), (-380, -40)]


class Paddle:

    def __init__(self, paddle_cords):
        self.paddle_cords = paddle_cords
        self.segments = []
        self.create_paddle()
        self.head = self.segments[0]
        self.head.setheading(90)
        self.tail = self.segments[-1]
        self.move_speed = 50

    def create_paddle(self):
        for n in self.paddle_cords:
            self.create_segment(n)

    def create_segment(self, position):
        new_square = Turtle(shape="square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.segments.append(new_square)

    def up(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor() + abs(self.move_speed - 20)
            self.segments[seg_num].goto(new_x, new_y)
        self.head.setheading(90)
        self.tail.setheading(90)
        self.head.forward(self.move_speed)

    def down(self):
        for seg_num in range(0, len(self.segments) - 1, 1):
            new_x = self.segments[seg_num + 1].xcor()
            new_y = self.segments[seg_num + 1].ycor() - abs(self.move_speed - 20)
            self.segments[seg_num].goto(new_x, new_y)
        self.head.setheading(270)
        self.tail.setheading(270)
        self.tail.forward(self.move_speed)

    def collisions(self):
        if self.head.ycor() >= 300:
            self.down()
        elif self.tail.ycor() <= -300:
            self.up()
