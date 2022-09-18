from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.refresh_scoreboard()

    def l_goal(self):
        self.clear()
        self.l_score += 1
        self.refresh_scoreboard()

    def r_goal(self):
        self.clear()
        self.r_score += 1
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.l_score, move=False, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, move=False, align="center", font=("Courier", 80, "normal"))
