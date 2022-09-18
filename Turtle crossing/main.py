import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0.05)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_super_up, "w")
screen.onkey(player.move_super_down, "s")




game_is_on = True
while game_is_on:

    time.sleep(0.05)
    screen.update()
    scoreboard.showboard()
    car_manager.move_cars()

    #Detect player collision with cars.
    for n in range(0,len(car_manager.cars) -1):
        if player.distance(car_manager.cars[n]) < 20:
            scoreboard.game_over()
            game_is_on = False
            #Game over

    # Player goes to Finish line and next level starts
    if player.ycor() >= 280:
        player.reset_position()
        for n in car_manager.cars:
            n.hideturtle()
        car_manager.cars = []
        car_manager.multiple_cars()
        car_manager.next_level()
        scoreboard.add_score()

    #Regenerate Cars if player taking too long:
    for n in car_manager.cars:
        if n.xcor() <= -9500:
            player.reset_position()
            for y in car_manager.cars:
                y.hideturtle()
            car_manager.cars = []
            car_manager.multiple_cars()
            scoreboard.taking_too_long()
            time.sleep(3)


screen.exitonclick()
