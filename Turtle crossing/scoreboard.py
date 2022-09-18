from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.goto(-200, 260)
        self.hideturtle()

    def showboard(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "center", FONT)

    def add_score(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", False, "center", FONT)

    def taking_too_long(self):
        self.clear()
        self.goto(-100, 240)
        self.write("Level has been reset\nYou took to long to cross", False, "center",
                   ("Courier", 16, "normal"))
