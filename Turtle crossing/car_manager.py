from turtle import Turtle
import turtle as t
import random
#COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5/2
MOVE_INCREMENT = 5/2


class CarManager:
    def __init__(self):
        self.cars = []
        self.multiple_cars()
        self.starting_move_speed = 5/4
        self.move_increment = 5/4


    def multiple_cars(self):
        for n in range(0,500):
            self.create_car()


    def create_car(self):
        t.colormode(255)
        new_car = Turtle()
        new_car.speed("fastest")
        new_car.shape("square")
        new_car.color(self.random_colour())
        new_car.penup()
        new_car.shapesize(stretch_wid=1, stretch_len=1)
        new_car.setheading(180)
        new_car.goto(random.randrange(0,10000,10),random.randrange(-220,240,10))
        self.cars.append(new_car)

    def move_cars(self):
        for n in self.cars:
            n.forward(self.starting_move_speed)


    def next_level(self):
        self.starting_move_speed += self.move_increment


    def random_colour(self):
        r = random.randint(0, 235)
        g = random.randint(0, 235)
        b = random.randint(0, 235)
        randomcol = (r, g, b)
        return randomcol



