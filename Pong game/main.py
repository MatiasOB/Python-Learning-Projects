from turtle import Screen
import time
# from Paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
from yo_Paddles import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle1 = Paddle([(-380, 40), (-380, 20), (-380, 0), (-380, -20), (-380, -40)])
paddle2 = Paddle([(380, 40), (380, 20), (380, 0), (380, -20), (380, -40)])
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle1.up, "w")
screen.onkey(paddle1.down, "s")
screen.onkey(paddle2.up, "Up")
screen.onkey(paddle2.down, "Down")

game_on = True
while game_on:

    screen.update()
    time.sleep(ball.move_speed)
    paddle1.collisions()
    paddle2.collisions()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to wall_bounce
        ball.wall_bounce()

    # Detect collision with paddle2:
    for n in range(0, 5):
        if ball.distance(paddle2.segments[n]) < 30 and ball.xcor() > 350:
            ball.paddle_bounce()
            break

    # Detect collision with paddle1:
    for n in range(0, 5):
        if ball.distance(paddle1.segments[n]) < 30 and ball.xcor() < -350:
            ball.paddle_bounce()
            break

    # Detect paddle 2 miss:
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.l_goal()

    # Detect paddle 1 miss:
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.r_goal()

screen.exitonclick()
