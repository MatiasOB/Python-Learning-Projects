from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()

    def showboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, "center", ("Arial", 12, "bold"))

    def add_score(self):
        self.score += 1
        self.showboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as fil:
                fil.write(str(self.score))
        self.score = 0
        self.showboard()

    # def game_over(self):
    #   self.goto(0,0)
    #    self.write("GAME OVER.",False,"center",("Arial",16,"bold"))
